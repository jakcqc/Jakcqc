import Student
import pytest
import json
import System

def test_checkTime(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    
    grading_system.login(username,password)
    grades = grading_system.usr.check_grades('software_engineering')
    
    assert grades[0] == ['assignment1', 100]
    assert grades[1] == ['assignment2', 100]
    
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem