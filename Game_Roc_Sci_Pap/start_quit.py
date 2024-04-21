from gfunc import game_proccess


def start():
    while True:
        try:
            ask = int(input('Do u want to play? 1 - Yes, 2 - No'))
            if ask not in range(1, 3):
                print('Oh, I don\'t understand')
                print('Try again please')
                continue

        except ValueError:
            print('Sorry, but we use only numbers! :(')
            continue

        if ask == 1:
            print('Ok, Just do it!')
            game_proccess()
            continue

        else:
            print('Well, goodbye and have a nice day!;)')
            input("Click 'Enter' to close")
            break

