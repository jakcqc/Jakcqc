import pytest
import System

#Tests if the program can check passwords even with weird format
def test_checkPassword():
        assert System.System().check_password('saab','boomr345') == True
        assert System.System().check_password('saab','BOOMR345') == False
        assert System.System().check_password('goggins','augurrox') == True

    



	
