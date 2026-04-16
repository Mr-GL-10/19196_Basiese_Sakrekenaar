'''
Basiese sak rekenaar wat kan maal, deel, optel en aftrek.
'''

running = True

num1 = None
num2 = None
operator = None

final_answer = ''

# funksies
def multiply(num1, num2):
    return num1 * num2


def devide(num1, num2):
    if num2 == 0:
        return "Kan nie deur 0 deel nie"
    return  num1 / num2

def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2


while running:
    user_input = input("Basiese Sakrekenaar:\n'help" \
    " - vir help.'\n>> ")

    #Kry die nommers en operators van die gebruiker af.
    try:
        num = float(user_input)
        if num1 == None:
            num1 = num
        elif num1 != None:
            num2 = num
    except ValueError:
        pass

    if user_input == 'help':
        print("\nVoeg in 'n nommer, dan 'n operator, en nog 'n nommer.\n" \
                "'!' - Vee uit vorige poging.\n" \
                "'=' - Gee antwoord.\n" \
                "'#' - Maak program toe.\n")
    elif user_input == "!":
        num1 = None
        num2 = None
    elif user_input == '#':
        running = False
    
    elif user_input in ['*','/','+','-']:
        if num1 == None:
            print("\nVoeg eers 'n nommer in.\n")
        else:
            operator = user_input


    #Vat die gebruiker se insette en bewerk die som.
    if user_input == "=":
        if num1 == None or num2 == None or operator == None:
            print("\nOnvoledige berekening.\n")
        else:
            if operator == "*":
                final_answer = multiply(num1,num2)
            elif operator == "/":
                final_answer = devide(num1,num2)
            elif operator == "+":
                final_answer = plus(num1,num2)
            elif operator == "-":
                final_answer = minus(num1,num2)

        #Toets die antwoord    
        if final_answer == None:
            pass
        else:
            print(f"\n{final_answer}\n")

        num1 = None
        num2 = None
        operator = None
        final_answer = None
