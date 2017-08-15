import core


def Gladiator_start():
    print('Gladiator 1: 100 HP ||| 0 rage.. Low damage: 12, High damage: 20')
    print('gladiator 2: 100 HP ||| 0 rage.. Low damage: 5, High damage: 30')


def Gladiators1_details(gladiator_one):
    print('Gladiator 1:', gladiator_one['health'], 'HP |||',
          gladiator_one['rage'], 'Rage')


def Gladiators2_details(gladiator_two):
    print('Gladiator 2:', gladiator_two['health'], 'HP |||',
          gladiator_two['rage'], 'Rage')


def gladiator_choice(n):
    s = '''Gladiator {}... What would you like to do?\n
    \t- attack\n
    \t- pass\n
    \t- quit\n
    \t- heal\n
    '''.format(n)
    return input(s)


def main():
    Gladiator_start()
    gladiator_one = core.new_gladiator(100, 0, 12, 20)
    gladiator_two = core.new_gladiator(100, 0, 5, 30)
    while True:
        choice = gladiator_choice('1')
        if choice.lower() == 'attack':
            core.attack(gladiator_one, gladiator_two)
            if core.is_dead(gladiator_two):
                print('Gladiator 1 wins')
                print('Gladiator 2 looses')
                break
        elif choice.lower() == 'quit':
            print('Gladiator 1 looses')
            print('Gladiator 2 wins')
            exit()
        elif choice.lower() == 'heal':
            core.heal(gladiator_one)
        elif choice.lower() == 'pass':
            print('gladiator 1 pass')
        else:
            print('Invalid choice.')
        Gladiators1_details(gladiator_one)
        Gladiators2_details(gladiator_two)
        choice = gladiator_choice('2')
        if choice.lower() == 'quit':
            print('Gladiator 2 looses')
            print('Gladiator 1 wins')
            exit()
        elif choice.lower() == 'attack':
            core.attack(gladiator_two, gladiator_one)
            if core.is_dead(gladiator_one):
                print('Gladiator 1 looses')
                print('Gladiator 2 wins')
                break
        elif choice.lower() == 'heal':
            core.heal(gladiator_two)
        else:
            print('Invalid choice.')
        Gladiators1_details(gladiator_one)
        Gladiators2_details(gladiator_two)


if __name__ == '__main__':
    main()