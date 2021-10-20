'''
    LOGIC:
    1.see pattern, if change direction, go keep going to North, will have cycle
    2.How to make new direction after changing facing angle
    3.if go back to origin point or facing not north, will be cycle
'''
def isRobotBounded(self, instructions: str) -> bool:
        dir =[[0, 1], [1, 0], [0, -1], [-1, 0]] # north, east, south, west: 0, 1, 2, 3
        face = 0 # first facing north(0), east(1), south(2), west(3)
        index = 0 # facing north
        # origin point
        x = 0
        y = 0
        for move in instructions:
            if move == "R": # change face angle
                index = (index+1) % 4
            elif move == "L":
                index = (index+3) % 4
            else: #G
                x += dir[index][0]
                y += dir[index][1]
                
        return (x == 0 and y == 0) or index != 0