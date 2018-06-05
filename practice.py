"""
Implement here!
"""
def main():
    x = [ 3,4,-1,1,8,2]
    firstpos(x)

def firstpos(data):
    if not data:
        return 1

    print ("Initial state:\n{}".format(" ".join(map(str,data))))

    for i in range(len(data)):
        print ("FOR LOOP".center(30,"-"))
        print ("{} [{}] {}".format(data[0:i],data[i],data[i+1:]))
        while 0 < data[i] <= len(data) and data[i] != (i + 1):
            val = data[i]
            data[i], data[val-1] = data[val-1],data[i]
            print ("{} [{}] {}".format(data[0:i],data[i],data[i+1:]))
            
            if data[i] == data[val-1]:
                break
    
    
if __name__ == "__main__":
    main()
