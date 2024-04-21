import random
# if number == 1:  #sci
# elif number == 2:  #stone
# elif number == 3:  #paper

def game_proccess():
    while True:
        number = random.randint(1, 3)
        try:
            answer = int(input('U go'))
            if answer > 3 or answer < 0:
                print('Hmmm, It\'s a big or too little')
                print('Let\'s try again!')
                continue
        except ValueError:
            print("Sorry, but we use only numbers!")
            print('Let\'s try again!')
            continue

        if answer == number:
            print(f"AI has chosen {number}")
            print('Draw ;)')
            break

        elif ((answer == 1 and number == 3) or
              (answer == 2 and number == 1) or
              (answer == 3 and number == 2)):
            print(f"AI has chosen {number} \nU win!!")
            break

        else:
            print(f"AI has chosen {number} \nAI win!")
            break
