import pytest
import System


def test_login(grading_system):
    username = 'saab'
    password =  'BOOMR345'
    grading_system.login(username,password)
    assert username == 'saab' and password == 'boomr345'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
    
