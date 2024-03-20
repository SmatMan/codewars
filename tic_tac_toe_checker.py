def checkAdj(board, x, y, direction):
    try:
        if direction == "u":
            p = board[y-1][x]
            return p if p != 0 else None
        if direction == "d":
            p = board[y+1][x]
            return p if p != 0 else None
        if direction == "l":
            p = board[y][x-1]
            return p if p != 0 else None
        if direction == "r":
            p = board[y][x+1]
            return p if p != 0 else None
        if direction == "ul":
            p = board[y-1][x-1]
            return p if p != 0 else None
        if direction == "ur":
            p = board[y-1][x+1]
            return p if p != 0 else None
        if direction == "dl":
            p = board[y+1][y-1]
            return p if p != 0 else None
        if direction == "dr":
            p = board[y+1][y+1]   
            return p if p != 0 else None
    except:
        return None

def is_solved(board):      
    piece = board[1][1] # centrepiece diagonals check
    if checkAdj(board, 1, 1, "ul") == piece and checkAdj(board, 1, 1, "dr") == piece:
        return piece
    if checkAdj(board, 1, 1, "dl") == piece and checkAdj(board, 1, 1, "ur") == piece:
        return piece
    
    for idx, spot in enumerate(board): # vertical centre tree stemming left and right
        piece = spot[1]
        if checkAdj(board, 1, idx, "l") == piece and checkAdj(board, 1, idx, "r") == piece:
            return piece

    for idx in range(len(board)): # horizontal centre tree stemming up and down
        piece = board[1][idx]
        if checkAdj(board, idx, 1, "u") == piece and checkAdj(board, idx, 1, "d") == piece:
            return piece

    for i in board: # if any space is free
        for j in i:
            if j == 0:
                return -1
    return 0