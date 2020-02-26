import Professor
import pytest
import json
import System
import Student

def test_changeGrade(grading_system):
    username = 'goggins'
    password =  'augurrox'
    
    grading_system.login(username,password)
    grading_system.usr.drop_student('goggins', 'databases')
    #should fail here because of type error or keyError
    grading_system.reload_data()

    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem