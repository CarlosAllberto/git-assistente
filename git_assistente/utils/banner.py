from colorama import Fore
from dankware import align

art = """
⠀⠀⠀⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣦⣀⣀⣤⣤⣤⣤⣤⣤⣄⣠⣶⣿⣿⣿⣿⡇⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀
⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
⢠⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⡟⠁⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠈⢻⣿⣿⣿⡇
⠘⣿⣿⣿⡇⠀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡄⠀⢸⣿⣿⣿⠃
⠀⢿⣿⣿⡇⠀⠀⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠻⠛⠀⠀⢸⣿⣿⡟⠀
⠀⠀⠻⣿⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠀⠀
⠀⠀⠀⠀⠙⠛⠿⣷⣶⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⠿⠛⠋⠀⠀⠀⠀
"""

def banner():
    print(f"{Fore.GREEN}{art}{Fore.RESET}\n")
    # print(align(f"{Fore.YELLOW}[-]              Version: 0.1.8              [-]{Fore.RESET}"))
    # print(align(f"{Fore.YELLOW}[-]          Author: CarlosAllberto          [-]{Fore.RESET}"))
    # print(align(f"{Fore.YELLOW}[-]   GitHub: www.github.com/CarlosAllberto  [-]{Fore.RESET}"))
    # print(align(f"[*]            *****************             [*]"))
    # print(align(f"Projeto criado com o a intuito de ajudar\n iniciantes e profissionais a subir projetos \nno GitHub de forma super rápida.\n"))
  
if __name__ == "__main__":
    banner()
