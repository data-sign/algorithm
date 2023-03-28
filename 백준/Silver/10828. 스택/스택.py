import sys
N = int(sys.stdin.readline())

lst = []

for i in range(N): 
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push': 
        lst.append(cmd[1])
    elif cmd[0] == 'pop': 
        if len(lst): 
            print(lst[-1])
            lst.pop()
        else: print(-1)
    elif cmd[0] == 'size': 
        print(len(lst))
    elif cmd[0] == 'empty': 
        if len(lst): print(0)
        else: print(1) 
    elif cmd[0] == 'top': 
        if len(lst): print(lst[-1])
        else: print(-1) 