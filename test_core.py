import core


def test_new_gladiator():
    assert core.new_gladiator(20, 30, 3, 12) == {
        'health': 20,
        'rage': 30,
        'damage_low': 3,
        'damage_high': 12
    }


def test_is_dead():
    choice = {'health': -1, 'rage': 30, 'damage_low': 3, 'damage_high': 12}
    assert core.is_dead(choice) == True
    choice = {'health': 10, 'rage': 30, 'damage_low': 3, 'damage_high': 12}
    assert core.is_dead(choice) == False


def test_heal():
    choice = {'health': 100, 'rage': 15, 'damage_low': 10, 'damage_high': 20}
    assert core.heal(choice) == None


def test_attack():
    attacker = {'health': 75, 'rage': 0, 'damage_low': 10, 'damage_high': 10}
    defender = {'health': 75, 'rage': 0, 'damage_low': 10, 'damage_high': 10}
    core.attack(attacker, defender)
    assert attacker['rage'] == 15
    assert defender['health'] == 65
    attacker = {'health': 75, 'rage': 100, 'damage_low': 10, 'damage_high': 10}
    defender = {'health': 65, 'rage': 100, 'damage_low': 10, 'damage_high': 10}
    core.attack(attacker, defender)
    assert attacker['rage'] == 0
    assert defender['health'] == 20


def test_pass_rage():
    gladiator = {'rage': 0, 'health': 60}
    assert core.pass_rage(gladiator) == None
