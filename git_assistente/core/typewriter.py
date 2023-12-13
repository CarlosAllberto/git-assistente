from time import sleep

def typewriter(texto):
  for letra in texto:
    print(letra, flush=True, end="")
    sleep(0.05)
  print()

if __name__ == "__main__":
  texto = "testando 123"
  typewriter(texto)
