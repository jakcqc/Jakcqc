import Student
import pytest
import json
import System

def test_checkTime(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    
    grading_system.login(username,password)
    assignments = grading_system.usr.view_assignments('databases')
    
    assert assignments[0] == ['assignment1', '1/6/20']
    assert assignments[1] == ['assignment2', '2/6/20']
    
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem