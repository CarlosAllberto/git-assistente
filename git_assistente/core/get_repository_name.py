import os

def get_repository_name():
  return os.path.basename(os.getcwd())
    
if __name__ == "__main__":
  get_repository_name()