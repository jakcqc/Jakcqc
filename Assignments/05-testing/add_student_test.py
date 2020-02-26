import pytest
import json
import System
import Professor

def test_checkAdd(grading_system):
    username = 'goggins'
    password =  'augurrox'
    grading_system.login(username,password)
    grading_system.usr.add_student('yted91', 'databases')
    grading_system.reload_data()
    with open('Data/users.json') as f:
        users2 = json.load(f)

    assert users2['yted91']['courses']['databases'] != ""
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem