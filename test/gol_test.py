import pytest
from gol.gol import * #folder is called "gol" as well, so we have to do the gol.gol thing :D


class TestUnderpop():
    def test_underpop_positive(self):
        '''
        Positive case to determine an underpopulation event
        '''
        testArray = [[0,1,0],[0,1,0],[0,0,0]]
        assert underpop(testArray,1,1) == True
    
    def test_underpop_negative(self):
        '''
        Negative case to test underpopulation
        '''
        #This one im not doing right
        testArray = [[0,1,0],[1,1,0],[0,0,0]]
        assert underpop(testArray,1,1) == False

class TestOverpop():
    def test_overpop_positive(self):
        '''
        Testing if we are detecting the overpopulation right
        '''
        #This one doesnt work
        testArray = [[1,1,0],[1,1,0],[0,0,0]]
        assert overpop(testArray,1,1) == True

    def test_overpop_negative(self):
        '''
        Testing if we can detect if theres no overpopulation
        '''
        testArray = [[0,1,0],[0,1,0],[0,0,0]]
        assert overpop(testArray,1,1) == False

class TestRepro():
    def test_repro_positive(self):
        '''
        expect True if reproduction is expected
        '''
        #not working
        testArray = [[0, 1, 0],
                     [1, 0, 1],
                     [0, 1, 0]]
        assert repro(testArray, 1, 1) == True
    

    def test_repo_negative(self):
        '''
        expect False if reproduction is not expected
        '''
        testArray = [[0, 1, 0],
                     [1, 0, 0],
                     [0, 1, 0]]
        assert repro(testArray, 1, 1) == False

class TestNeighbours():
    def test_check_neighbours_none(self):
        '''
        No neighbours, should return 0
        '''
        testArray = [[0,0,0],[0,1,0],[0,0,0]]
        assert checkNeighbours(testArray,1,1) == 0

if __name__ == '__main__':
    '''
    '''