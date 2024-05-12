import subprocess
from subprocess import PIPE, STDOUT
from colorama import Style

def cmd_print(command): 
  result_cmd = subprocess.run(command, stdout=PIPE, stderr=STDOUT, shell=True)
  print(f"{Style.DIM}[COMANDO USADO]: {result_cmd.args}{Style.RESET_ALL}\n")
  return result_cmd

def cmd(command): 
  result_cmd = subprocess.run(command, stdout=PIPE, stderr=STDOUT, shell=True)
  return result_cmd

if __name__ == "__main__":
  print(cmd("pwd").stdout)