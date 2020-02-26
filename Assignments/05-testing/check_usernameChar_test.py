import pytest
import System

#test if username allows caps for username which fails 
def test_login(grading_system):
    username = 'SAAB'
    password =  'boomr345'
    grading_system.login(username,password)
    assert username == 'saab' and password == 'boomr345'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
    
