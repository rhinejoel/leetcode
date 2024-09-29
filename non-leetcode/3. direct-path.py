grid = [[0, 0, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 0, 0]]

# Need to find number of unique paths from [0, 0] to [n, n]
# Assuming the arrays are a stacked physically and "0" means open while "1" means blocked
# First get all possible way locations and store them in valid[]
# if [n, n] not in valid[] return p_exist=0 -> no possible paths
# Start is [0, 0]
# propogation is possible if neighbours exist at [-i, j], [+i, j], [i, -j], [i, +j] if they are each not None and if they exist in valid[]
# eg if -i is not None and -i is in valid[]
# add all valid propogations to pos[]
# if len(pos)>1 that means there are more then 1 possible ways to move forward
# set current node to xway and run propogation on each pos[] node
# if [n,n] in pos[], the set p_exist=1

start = [0, 0]
end = [3, 3]
path = [start] #Path has at least start node
valid = [] #All valid nodes

def goForward(node, p_exist):
    pos = [] # possible movement nodes for node

    i = node[0]
    j = node[1]

    left = [i, j-1]
    right = [i, j+1]
    up = [i-1, j]
    down = [i+1, j]

    dirs = [down, up, left, right] # directions

    for d in dirs:
        if d != None and d in valid:
            if d not in path:   # check if d is already in path
                pos.append(d)   # pos will constain all possible valid cells to move forward
    
    if end in pos:
        path.append(end)
        p_exist += 1
        print(path, p_exist)
        return path

    if len(pos) > 1:
        # for p in pos:
        #     branch = p
        #     branch.append(goForward(p, p_exist))
        pass
    elif len(pos) == 1:
        path.append(pos[0])
        cur_node = pos[0]
        goForward(cur_node, p_exist)
    


def getValidNodes():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                valid.append([i, j])

    p_exist = 0 #All current valid paths
    
    if start in valid and end in valid:
        goForward(start, p_exist)
    else:
        print(p_exist)

getValidNodes()