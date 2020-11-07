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
        testArray = [['*','*','*'],
                     ['.','.','.'],
                     ['.','.','.']]
        
        game = Gol(testArray)

        expectedArray = [['.','*','.'],
                         ['.','*','.'],
                         ['.','.','.']]
        
        assert self.equals_helper(expectedArray,game.tick()) == True

        
        

