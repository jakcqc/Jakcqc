import Professor
import pytest
import json
import System

def test_changeGrade(grading_system):
    username = 'goggins'
    password =  'augurrox'
    
    grading_system.login(username,password)
    grading_system.usr.add_student('akend3', 'databases')
    grading_system.reload_data()

    with open('Data/users.json') as f:
        users2 = json.load(f)

    assert len(users2['akend3']['courses']) == 2

    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem