def check_yesno(answer):
    if answer.lower()=="y":
        return True
    else:
        return False
    
def int_input(input_string, max_number):
    while True:
        try:
            value=int(input(input_string))
            if value>=0 and value<max_number:
                break
            else:
                print("Please insert a valid number.")                
        except:
            print("Please insert a valid number.")
    return value