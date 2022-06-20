import logging

import pytest

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.functional
def test_status(too_old_female):
    logger.info('\nTEST START')
    human = too_old_female
    assert human.status == 'alive', f'\nStatus is not as expected\nActual: {human.status}\nExpected: alive'


@pytest.mark.smoke
@pytest.mark.parametrize('age_number', [0, 99, 105])
def test_age(create_custom_human, age_number):
    """
    Description:
    This test was created to testing the function "age".

    Pre-conditions:
    1. Create Fixture with ability to set parameters according to the "Human" class.
    2. Create parametrize fixture with several variables of parameter "age_number".

    Steps:
    1. Pass Fixture and parameter "age_number" to created test function.
    2. Set some variables in Fixture according to the "Human" class.
    3. Call method "age" on Fixture and set parameter "age_number" as a variable of age.

    Expected:
    1. Three tests will be performed with different age settings.
    """
    logger.info('\nTEST START:')
    human = create_custom_human(name='Shon', age=age_number, gender='male')
    assert human.age == age_number, f'\nAge is not as expected\nActual: {human.age}\nExpected: {age_number}'


@pytest.mark.regression
def test_grow_plus(old_female):
    logger.info('\nTEST START')
    human = old_female
    human.grow()
    assert human.age == 105, f'\nAge is not as expected\nActual: {human.age}\nExpected: 105'


@pytest.mark.smoke
def test_grow_dead(too_old_female):
    logger.info('\nTEST START')
    human = too_old_female
    human.grow()
    assert human.status == 'dead', f'\nStatus is not as expected\nActual: {human.status}\nExpected: dead'


@pytest.mark.functional
def test_name(old_female):
    logger.info('\nTEST START')
    human = old_female
    assert human.name == 'Lara', f'\nName is not as expected\nActual: {human.name}\nExpected: Lara'


@pytest.mark.regression
def test_change_name_1(old_female):
    logger.info('\nTEST START')
    human = old_female
    human.change_name('Ria')
    assert human.name == 'Ria', f'\nName is not as expected\nActual: {human.name}\nExpected: Ria'


@pytest.mark.regression
def test_change_name_2(old_female):
    logger.info('\nTEST START')
    human = old_female
    human.change_name('riiiiiiiia')
    assert human.name == 'riiiiiiiia', f'\nName is not as expected\nActual: {human.name}\nExpected: riiiiiiiia'


@pytest.mark.regression
def test_change_name_3(old_female):
    logger.info('\nTEST START')
    human = old_female
    with pytest.raises(SyntaxError):
        human.change_name('ria')
    logger.info('\nSyntax Error Raises')


@pytest.mark.regression
def test_gender(young_male):
    logger.info('\nTEST START')
    human = young_male
    assert human.gender == 'male', f'\nGender is not as expected\nActual: {human.gender}\nExpected: male'


@pytest.mark.functional
def test_gender_setter_1(young_male):
    logger.info('\nTEST START')
    human = young_male
    with pytest.raises(Exception):
        human.gender = 'people'
    logger.info('\nException Error Raises')


@pytest.mark.smoke
def test_gender_setter_2(young_male):
    logger.info('\nTEST START')
    human = young_male
    human.gender = 'female'
    assert human.gender == 'female', f'\nGender is not as expected\nActual: {human.gender}\nExpected: female'


@pytest.mark.smoke
def test_is_alive(too_old_female):
    logger.info('\nTEST START')
    human = too_old_female
    human.grow()
    with pytest.raises(Exception):
        human.grow()
        logger.info('\nException Error Raises')


@pytest.mark.functional
def test_get_friends(old_female):
    logger.info('\nTEST START')
    human = old_female
    human.get_friends()
    assert human.friends == [], f'Friends list should be empty'


@pytest.mark.smoke
def test_make_friends(young_male, old_female):
    """
    Description:
    This test was created to testing the function "make_friends".

    Pre-conditions:
    1. Create Fixture #1 with the given parameters according to the Human class.
    2. Create another Fixture #2 with the given parameters according to the Human class.

    Steps:
    1. Pass both created fixtures as variables to the created test function.
    2. Call method "make_friends" on Fixture #1 and pass Fixture #2 into it as a variable.

    Expected:
    1. Fixture #2 will be added to Fixture #1 friends list.
    """
    logger.info('\nTEST START')
    human = young_male
    human.make_friends(old_female)
    assert human.friends == [old_female], f'Friends list should contain {old_female}'
