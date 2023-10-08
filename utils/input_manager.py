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

def parse_value(max_value, value):
    parsed=[]
    if "-" in value:
        value=value.split("-")
        try:
            minpl=int(value[0])
            maxpl=int(value[1])+1
            for playlist in range(minpl, maxpl):
                if playlist in range(max_value):
                    parsed.append(playlist)
                else:
                    return None
        except:
            return None
    else:
        try:
            if (int(value)) in range(max_value):
                parsed.append(int(value))
            else:
                return None
        except:
            return None
    return parsed

def playlist_choice_parser(max_value):
    while True:
        choices=[]
        input_choice=input("Insert your choices: ")
        input_choice=input_choice.replace(" ", "").split(",")
        if len(input_choice)==1:
            if input_choice[0]=="!":
                exit("GOODBYE!")
            if input_choice[0]==".":
                print("Preparing all the playlists for you! :D")
                for v in range(max_value):
                    choices.append(v)
                break
            else:
                parsed=parse_value(max_value, input_choice[0])
                if not parsed:
                    print("Please insert a valid input!\n")
                    continue
                else:
                    for value in parsed:
                        choices.append(value)
                    break
        else:
            valid=True
            for v in input_choice:
                parsed=parse_value(max_value, v)
                if not parsed:
                    print("Please insert a valid input!\n")
                    valid=False
                    break
                else:
                    for value in parsed:
                        choices.append(value)
            if valid:
                break
    return choices   