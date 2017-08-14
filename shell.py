import core


def Gladiator_start():
    print('Gladiator 1: 100 HP ||| 0 rage.. Low damage: 10, High damage: 17')
    print('gladiator 2: 100 HP ||| 0 rage.. Low damage: 5, High damage: 30')


def Gladiators1_details(gladiator):
    print('Gladiator 1:',gladiator['health'],'HP |||',gladiator['rage'],'Rage')

def Gladiators2_details(gladiator):
    print('Gladiator 2:',gladiator['health'],'HP |||',gladiator['rage'],'Rage')


def gladiator_1():
    return input('''Gladiator 1... What would you like to do?\n
    \t- attack\n
    \t- pass\n
    \t- quit\n
    \t- heal\n
    ''')


def gladiator_2():
    return input('''Gladiator 2... What would you like to do?\n
    \t- attack\n
    \t- pass\n
    \t- quit\n
    \t- heal\n
    ''')


def main():
    Gladiator_start()
    while True:
        gladiator = core.new_gladiator(health, rage, damage_low, damage_high)
        choice = gladiator_1()
        if choice.lower == 'attack':

        elif choice.lower == 'pass':

        elif choice.lower == 'quit':
            print('Gladiator 1 looses')
            print('Gladiator 2 wins')
            exit()
        elif choice.lower == 'heal':
            core.heal(gladiator)
        else:
            print('Invalid choice.')
        Gladiators1_details(gladiator)
        Gladiators2_details(gladiator)
        choice = gladiator_2
        if choice.lower == 'attack':

        elif choice.lower() == 'pass':
        
        elif choice.lower() == 'quit':
            print('Gladiator 2 looses')
            print('Gladiator 1 wins')
            exit()
        elif choice.lower() == 'heal':
            core.heal(gladiator)
        else: 
            print('Invalid choice.')

if __name__ == '__main__':
    main()