import Student
import pytest
import json
import System

def test_changeGrade(grading_system):
    username = 'yted91'
    password =  'imoutofpasswordnames'
    
    grading_system.login(username,password)

    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', 100)
    
    grading_system.reload_data()

    grades = grading_system.usr.check_grades('software_engineering')

    assert grades[0] == ["assignment1",0]

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem