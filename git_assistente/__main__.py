#!/usr/bin/python

from sys import exit
from git_assistente.core.cmd import cmd
from git_assistente.core.get_repository_name import get_repository_name
from git_assistente.core.typewriter import typewriter
from git_assistente.core.check_response import check_response
from git_assistente.core.clear import clear
from git_assistente.utils.banner import banner
from colorama import Fore, Style
from os import system
import requests 

red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
dim = Style.DIM
reset_all = Style.RESET_ALL

class git_assistente:
    def __init__(self):
        system("clear")
        banner()
        git_config = {}

        self.first = ""
        
        try:
            result_cmd = str(cmd("git config --list").stdout, encoding="utf-8").split()
            for line in result_cmd:
                line = line.split("=")
                git_config[line[0]] = line[1]
            self.git_config = git_config
        except:
            pass

        try:
            self.name = git_config['user.name']
            self.email = git_config['user.email']
        except:
            self.first = True
    
        cmd("git config --global credential.helper store")
        cmd("git config --global pull.rebase true")
        print(f"{green}[+] Configuraçãoes de ajuda feitas{reset}")



    # verifica se é primeira vez usando o assistente
    def verify_first(self):
        if self.first:
            typewriter("Olá, sou seu novo assistente do Git. \ncomo parece ser sua primeira vez usando o Git preciso saber quem é você.\n")
            name = str(input("Me diga seu Username usado no GitHub: "))
            cmd(f"git config --global user.name \"{name}\"")
            print(f"{green}[+] Username cadastrado com sucesso{reset}")
            clear()
            typewriter(f"Prazer em te conhecer, {name}")
            clear()
            email = str(input("Agora Digite seu Email: "))
            cmd(f"git config --global user.email \"{email}\"")
            print(f"{green}[+] Email cadastrado com sucesso{reset}")
            clear()
            self.name = name



    # verifica conexão com repositório
    def verify_repository_connect(self):
        try: 
            result_cmd = str(cmd("git remote -v").stdout, encoding="utf-8")
            if "not a git repository" in result_cmd:
                typewriter("Seu projeto ainda não foi conectado à um repositório no GitHub.\n")
                return True
        except: 
            exit("Erro ao verificar conexão com repositório.")
        

    
    # verifica se o repositório existe no GitHub
    def vefify_exists_repository(self):
        try:
            repositories = requests.get(f"https://api.github.com/users/{self.name}/repos").json()
            repository_name = [repo["name"] for repo in repositories]
            repository = get_repository_name()
            if repository in repository_name:
                return True
            
            typewriter(f"Para fazermos a ligação da pasta com o GitHub é preciso que já exista um repósitorio VÁZIO com o nome {repository}\n no seu GitHub.")
            typewriter("Faça a criação do repositório e me chame novamente.")
            exit()
        except:
            exit("Não foi possivel listar os repositorios. \nVerifique a conexão com a sua internet.")



    # faz a conexão com o repositório no GitHub
    def repository_connect(self):
        typewriter("Vamos fazer a conexão agora\n")
        repository = get_repository_name()
        try:
            cmd("git init")
            cmd(f"git remote add origin https://github.com/{self.name}/{repository}.git")
            cmd("git branch -M main")
            print(f"{green}[+] Conexão feita com sucesso.{reset}")
        except:
            exit("Erro ao fazer conexão com repositório.")



    # verifica se tem alguma coisa para dar commit no seu projeto
    def verify_commit(self):
        try:
            cmd_result = str(cmd("git status").stdout, encoding="utf-8")
            if "nothing to commit" in cmd_result:
                return print("Seu projeto não tem nenhuma atualização para dar commit.")
            return True
        except:
            exit("Erro ao verificar se tem alguma coisa para dar commit.")



    # adiciona commit no projeto
    def commit(self):
        try: 
            cmd("git add .")
            print("Commit é um breve resumo das atualizações feitas no repositório. \nExemplo: [editei o arquivo.py, excluir o arquivo teste.py, refatoração, alteração no estilo]\nCaso escolha não passar um commit sera utilizado um commit padrão.\n")
            if check_response("Deseja adicionar um commit?"):
                commit = str(input("Digite seu commit: "))
                return cmd(f"git commit -m \"{commit}\"") 
            cmd("git commit -m \"Add files via GitAssistente\"")
        except:
            exit("Erro ao dar commit no projeto.")



    # verifica se o repositório tem alguma atualização pedente
    def verify_pull(self):
        try:
            cmd("git fetch")
            cmd_result = str(cmd("git status").stdout, encoding="utf-8")
            if "git pull" in cmd_result:
                print("O projeto tem atualizaçãoes mais recentes no GitHub que devemos trazer para a sua máquina.")
                print("Isso pode fazer com que algumas coisas possam ser sobreescritas.\n")
                if check_response("Deseja trazer as atualizações para sua máquina?"):
                    return True
                exit("Não é possivel subir as atualizações para o GitHub sem antes trazer as modificações.")
        except:
            exit("Erro ao verificar atualização no GitHub.")



    # puxa as coisas do repositório do GitHub para sua máquina
    def pull(self):
        try:
            cmd_result = str(cmd("git pull origin main").stdout, encoding="utf-8")
            if "Already up to date." in cmd_result:
                return print("Nada para atualizar.")
            if "Successfully rebased and updated" in cmd_result:
                print(f"{green}[+] Modificações do GitHub puxadas para a sua maquina.{reset}")
        except:
            exit("Erro ao trazer atualizaçãoes do GitHub para o sua máquina.")
    
    
    
    # sobe o projeto
    def push(self):
        try:
            if self.first:
                print("[INFO]: Faça a criação do seu token em https://github.com/settings/tokens\n")
                print(f"""{dim}[DICA]: Você pode seguir as etapas abaixo: 
                0 - Abra o link acima
                1 - Clique em \"Generate new token\"
                2 - Escolha a opção classic
                3 - Marque todas as caixinhas
                4 - Gere seu token.
                5 - Guarde o token. O git vai pedir nestante.{reset_all}\n
                """)
                print("[OBS]: o token sera salvo e não sera pedido novamente.\n")
                clear()

            cmd_result = str(cmd("git push origin main").stdout, encoding="utf-8")
            if "main -> main" in cmd_result:
                return print(f"{green}[+] Projeto subiu no GitHub com sucesso!{reset}")
            if "Everything up-to-date" in cmd_result:
                return print("Seu projeto não tem nenhuma atualização para subir.")
            print("Nâo foi possivel subir o projeto no GitHub.")
        except:
            exit("Erro ao subir o projeto no GitHub.")
    
    

    # executa a ferramenta na ordem certa
    def run(self):
        self.verify_first()
        
        if self.verify_repository_connect():
            if self.vefify_exists_repository():
                self.repository_connect()

        if self.verify_commit():
            self.commit()

            if self.verify_pull():
                self.pull()
            
        self.push()      

def main():
    git_assistente().run()  

if __name__ == "__main__":
    main()

typewriter("\nAté a próxima.\n")