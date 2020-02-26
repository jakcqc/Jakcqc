import Student
import pytest
import json
import System

def test_checkTime(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    grading_system.login(username,password)
    submission_date = '06/09/42'
    due_date = '06/09/40'
    result = grading_system.usr.check_ontime(submission_date,due_date)
    
    assert result == False
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem