
def check_response(texto):
    try:
        while True:
            response = input(f"{texto} [Y/n]: ")
            if response == "":
                break
            response = str(response)[0].upper()
            if response == "Y" or response == "N":
                break
            
        if response == "":
            return True
        elif response == "Y":
            return True
        elif response == "N":
            return False
        
    except Exception as err:
        print(err)

if __name__ == "__main__":
    check_response("Tudo bem?")