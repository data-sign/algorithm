def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    
    tmp = set()
    while True:
        
        for i in range(m-1) :
            for j in range(n-1):
                t = board[i][j]
                if ( t == [] ) :
                    continue
                else :
                    if( board[i][j+1] == t and board[i+1][j] == t and board[i+1][j+1] == t) :
                        tmp.add((i,j))
                        tmp.add((i,j+1))
                        tmp.add((i+1,j))
                        tmp.add((i+1,j+1))
                        
        if ( tmp ) :
            answer += len(tmp)
            for i,j in tmp :
                board[i][j] = []
            tmp = set()
        else :
            break
        
        while True :
            moved = 0
            for i in range(m-1) :
                for j in range(n) :
                    if( board[i][j] and board[i+1][j] == [] ) :
                        board[i][j],board[i+1][j] = board[i+1][j],board[i][j]
                        moved = 1
            if ( moved == 0 ):
                break
    
    return answer