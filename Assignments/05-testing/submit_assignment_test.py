import Student
import pytest
import json
import System

def test_checkSubmit(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    grading_system.login(username,password)
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')
    
    with open('Data/users.json') as f:
        users2 = json.load(f)
    
    assert users2['hdjsr7']['courses']['cloud_computing']['assignment1']['submission_date'] == '03/01/20'
    assert users2['hdjsr7']['courses']['cloud_computing']['assignment1']['submission'] == 'Blahhhhh'

     
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem