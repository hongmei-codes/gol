import time
import random


class Gol():
    '''
    Instance of a Game of Life
    
    Attributes:
        array:  representation of the board in a nxn array
    '''
    def __init__(self, array):
        self.array = array
        self.actions = [[None for _ in range(len(array))] for _ in range(len(array))]


    def check_neighbours(self, coordinates):
        '''
        Given a tuple of coordinates, checks how many live neighbours

        :param: coordinates(tuple): (x, y) coordinates
        
        :returns: alive_sum(integer): sum of all living neighbour cells
        '''
        current_row, current_col = coordinates

        possible_rows = [current_row]
        for num in range(-1, 2):
            neighbour_row = current_row + num
            if 0 <= neighbour_row < len(self.array) and neighbour_row != current_row:
                possible_rows.append(neighbour_row)

        possible_cols = [current_col]
        for num in range(-1, 2):
            neighbour_col = current_col + num
            if 0 <= neighbour_col < len(self.array) and neighbour_col != current_col:
                possible_cols.append(neighbour_col)

        neighbours = []
        for row in possible_rows:
            for col in possible_cols:
                if (row, col) != coordinates:
                    neighbours.append((row, col))
        
        living_neighbours = 0

        for c in neighbours:
            x, y = c
            if self.array[x][y] == '*':
                living_neighbours += 1

        return living_neighbours


    def determine_rule(self,coordinates):
        '''
        Given a tuple of coordinates, determine which rule to apply

        
        '''
        no_of_neighbours = self.check_neighbours(coordinates)
        x,y = coordinates[0],coordinates[1]
        def reprod(array,coordinates):
            array[coordinates[0]][coordinates[1]] = '*'
        def kill(array,coordinates):
            array[coordinates[0]][coordinates[1]] = '.'
        if self.array[x][y] == '.' and no_of_neighbours == 3:
            self.actions[x][y] = reprod
        elif no_of_neighbours < 2 or no_of_neighbours>3:
            self.actions[x][y] = kill
        

    def tick(self):
        """
        For each cell in array, check neighbour cells.
        According to neighbour cells, apply reproduction/...
        Apply the rule to create next generation

        Returns:
            next_gen: a list to represent the next generation
        """
        for row in range(len(self.array)):
            for col in range(len(self.array[0])):
                self.determine_rule((row,col))
        for row in range(len(self.array)):
            for col in range(len(self.array[0])):
                action = self.actions[row][col]
                if action is not None:
                    action(self.array,(row,col))
        return self.array


if __name__ == '__main__':

    n = 10
    a = ['*','*','.']
    array = [[ random.choice(a) for _ in range(n) ] for _ in range(n)]
    
    for x in array:
        print(x)

    gol = Gol(array)
    while True:
        gol.tick()
        time.sleep(1)
        print('='*10)
        for x in gol.array:
            print(x)
