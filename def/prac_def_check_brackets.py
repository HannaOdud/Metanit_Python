print("Створи функцію: ")

def check_brackets(text):
    l_bracket = 0
    r_bracket = 0
    for i in text:
        if i == "(":
            l_bracket = l_bracket + 1
        if i == ")":
            r_bracket = r_bracket + 1    
    #return l_bracket == r_bracket
    if l_bracket == r_bracket:
        return True
    else: 
        return False

print(check_brackets("nxjskdhck(())"))
print(check_brackets("nxjskdhck(()))"))
