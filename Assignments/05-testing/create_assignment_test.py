import Professor
import pytest
import json
import System

def test_createAssign(grading_system):
    username = 'goggins'
    password =  'augurrox'
    
    grading_system.login(username,password)
    grading_system.usr.create_assignment('assignment3', '04/01/20', 'databases')    
    grading_system.reload_data()

    with open('Data/courses.json') as f:
        courses2 = json.load(f)
    assert courses2['databases']['assignments']['assignment3']['due_date'] == '04/01/20'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem