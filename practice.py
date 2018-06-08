"""
Implement here!
"""
def main():
    data = [3,4,-1,1] #2
    data2 = [1,2,3] # 4
    data3 = [1]
    data1 = [0,-1,5,6]
    print(firstMissingPosInt(data1))
    

def firstMissingPosInt(data):
    """
    data = [3,4,-1,1] #2
    data = [1,2,3] # 4
    """
    if not data:
        return 1

    for i in range(len(data)):
        while(data[i] != i + 1 and 0 < data[i] <= len(data)):
            val = data[i]
            data[i], data[val - 1] = data[val -1], data[i]

            if data[i] == data[val-1]:
                break

    for i,j in enumerate(data,1):
        if i != j:
            return i

    return len(data) + 1
            
            

def maxIsland(data):
    """
    practice of maxisland
    g = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    g2 = [[0,0,0,0,0]]
    g3 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    g4 = [[1]]

    6,0,4,1
    """
    vis = set()
    def recurse(i,j):
        #all the conditions that have to be met 'not' 
        if not(0 <= i < len(data) and
               0 <= j < len(data[0]) and
               data[i][j] == 1 and
               (i,j) not in vis):
            return 0

        vis.add((i,j))
        return 1 + recurse(i-1,j) + recurse(i+1,j) \
            +recurse(i,j-1) + recurse(i,j+1)

    return max(recurse(i,j)
               for i in range(len(data))
               for j in range(len(data[0])))
               
    
    
if __name__ == "__main__":
    main()
