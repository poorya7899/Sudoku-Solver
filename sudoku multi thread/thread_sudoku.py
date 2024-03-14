import threading 

# make global variables
# map array for game
current_map = [[0 for i in range(9) ] for j in range(9)]
# start map for checking free
check_map = [[0 for i in range(9) ] for j in range(9)]
# player row
player_row = 0
# player column
player_col = 0 
# player value
value = -1

# read map
def readMap(mp):
    # open file
    with open("map.txt") as f:
        # read 9 line
        for i in range(9):
            line = f.readline()
            # read 9 column
            for j in range(9):
                mp[i][j] = int(line[j])

# rows thread
class row(threading.Thread): 
    def __init__(self, row): 
        threading.Thread.__init__(self) 
        self.row = row

    def run(self): 
        for j in range(9):
            if(j != player_col and value == current_map[self.row][j]):
                return False
        return True

# columns thread
class col(threading.Thread): 
    def __init__(self, col): 
        threading.Thread.__init__(self) 
        self.col = col

    def run(self): 
        for i in range(9):
            if(i != player_row and value == current_map[i][self.col]):
                return False
        return True

# boxs threads
class box(threading.Thread):
    def __init__(self, num): 
        threading.Thread.__init__(self) 
        self.num = num
        self.st_r = int(num/3)*3
        self.st_c = (int(num%3))*3

    def run(self): 
        for i in range(3):
            for j in range(3):
                if((i+self.st_r != player_row or j+self.st_c != player_col ) and value == current_map[i+self.st_r][j+self.st_c]):
                    return False
        return True

# print game board function
def printMap():
    for i in range(9):
        for j in range(9):
            if(current_map[i][j]==0):
                print(' ',end='|')
            else:
                print(current_map[i][j],end='|')
        print("\n------------------",end='\n')

""" _________________________________________________________________"""

def can_continue(mp):
    for i in range(9):
        for j in range(9):
            if(mp[i][j] == 0):
                return True
    return False

# start game
# read map
#game map
readMap(current_map)
# start map
readMap(check_map)

# rows thread array
rows = []
# columns thread array
cols = []
# boxs thread array
boxs = []

# make threads
for i in range(9):
	# row_i
    rows.append(row(i))
	# column _i
    cols.append(col(i))
	# box_i
    boxs.append(box(i))
	# start them
    rows[i].start()
    cols[i].start()
    boxs[i].start()

# play game 
while(can_continue(current_map)):
    # print map
    printMap()
    # get user input
	# row
    player_row = int(input("row 1 to 9 : "))-1
	# column
    player_col = int(input("col 1 tp 9 : "))-1
	# value
    value = int(input("value : "))
    print("___________________________________________")
    # can write in player cell?
    if(check_map[player_row][player_col] == 0):
        # check row , column , box
		# row
        flag1 = rows[player_row].run()
		# column
        flag2 = cols[player_col].run()
		# box
        flag3 = boxs[int(player_row/3)*3 + int(player_col/3)].run()
		# wait to complete
        rows[player_row].join()
        cols[player_col].join()
        boxs[int(player_row/3)*3 + int(player_col/3)].join()
        # can write ?
        if(flag1 and flag2 and flag3):
			# yes
            current_map[player_row][player_col] = value
        else:
			# no
            print("Invalid input\n")
    else:
		# cell is full
        print("cell is full")