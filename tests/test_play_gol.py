from gol.play_gol import *


class TestGOL():
    def equals_helper(self, ar1, ar2):
        try:
            for x in range(len(ar1)):
                for y in range(len(ar1)):
                    if ar1[x][y] != ar2[x][y]:
                        return False
            return True
        except:
            return False

    def test_repro(self):
        '''
        .**      .**
        ..*  ->  .** 
        ...      ...
        '''
        testArray = [['.','*','*'],
                     ['.','.','*'],
                     ['.','.','.']]
        
        # each tick all the cells will check for the neighbours, then they will do the events

        expectedArray = [['.','*','*'],
                         ['.','*','*'],
                         ['.','.','.']]
        game = Gol(testArray)
        assert self.equals_helper(expectedArray,game.tick()) == True

    def test_underpopulation(self):
        testArray = [['*','.','.'],
                     ['.','.','.'],
                     ['.','.','.']]
        
        

        expectedArray = [['.','.','.'],
                         ['.','.','.'],
                         ['.','.','.']]
        game = Gol(testArray)
        assert self.equals_helper(expectedArray,game.tick()) == True

    def test_overpopulation(self):
        """
        * * *    * . *
        * * * -> . . .
        * * *    * . *
        """
        testArray = [['*','*','*'],
                ['*','*','*'],
                ['*','*','*']]
        
        

        expectedArray = [['*','.','*'],
                         ['.','.','.'],
                         ['*','.','*']]
        game = Gol(testArray)
        
        assert self.equals_helper(expectedArray,game.tick()) == True
