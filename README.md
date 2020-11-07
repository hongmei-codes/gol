# gol
an implementation of game of life

## rules
* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction


## New Design
* Alive: *
* Dead: .


## my earlier design is have cell

cell (position [x,y], state)
[ list of cellss ]

checkNeighbour (cell)
    return num_of_neighbours

```python
class Cell:
    pos=()
    state=0


```
