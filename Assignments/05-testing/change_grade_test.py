import Staff
import pytest
import json
import System

def test_changeGrade(grading_system):
    username = 'goggins'
    password =  'augurrox'
    
    grading_system.login(username,password)
    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', 100)
    
    grading_system.reload_data()

    with open('Data/users.json') as f:
        users2 = json.load(f)
		
    assert users2['yted91']['courses']['software_engineering']['assignment1'] == 100

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem