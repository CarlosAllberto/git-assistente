from git_assistente.utils.banner import banner
from os import system
from time import sleep

def clear():
  print("\npress enter", end=" ")
  for ponto in "...":
    print(ponto, flush=True, end="")
    sleep(0.5)
  input()
  system("clear")
  banner()