import logging

import pytest

from code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.fixture()
def old_female():
    logger.info(msg='\nFixture start')
    yield Human(name='Lara', age=104, gender='female')
    logger.info(msg='\nFixture finished')


@pytest.fixture()
def too_old_female():
    logger.info(msg='\nFixture start')
    yield Human(name='Dora', age=105, gender='female')
    logger.info(msg='\nFixture finished')


@pytest.fixture()
def young_male():
    logger.info(msg='\nFixture start')
    yield Human(name='Fred', age=18, gender='male')
    logger.info(msg='\nFixture finished')


@pytest.fixture()
def create_custom_human():
    def human_factory(name, age, gender):
        return Human(name=name, age=age, gender=gender)
    yield human_factory


@pytest.fixture()
def to_old_female():
    logger.info(msg='\nFixture start')
    yield Human(name='Dora', age=108, gender='female')
    logger.info(msg='\nFixture finished')