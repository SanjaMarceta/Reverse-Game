# reverse

def print_board(board):
    print('   1  2  3  4  5  6  7  8' )
    br = 1
    for i in board:
        print(br, end='  ')
        br+=1
        for j in i:
            print(j, end='  ')
        print('')

def applay_to_board_bottom(board,player,i,j):
    br = 0
    i+=1
    k = i
    while k < (len(board)) and board[k][j] != player and board[k][j] != '~':
        k+=1
    if  k < (len(board)) and board[k][j] == player:
        while i < (len(board)) and board[i][j] != player and board[i][j] != '~':
            board[i][j] = player
            i += 1
            br += 1      
    return br

def applay_to_board_left(board,player,i,j):
    br = 0
    j-=1
    m = j
    while m>=0 and board[i][m] != player and board[i][m] != '~':
        m-=1
    if m >= 0 and board[i][m] == player:
        while j>=0 and board[i][j] != player and board[i][j] != '~':
            board[i][j] = player
            j-= 1
            br += 1    
    return br

def applay_to_board_top(board,player,i,j):
    br = 0
    i-=1
    k = i
    while k>=0 and board[k][j] != player and board[k][j] != '~':
        k-=1
    if k>=0  and board[k][j] == player:
        while i>=0 and board[i][j] != player and board[i][j] != '~':
            board[i][j] = player
            i -= 1 
            br += 1   
    return br
def applay_to_board_right(board,player,i,j):
    br = 0
    j+=1
    m = j
    while m < (len(board)) and board[i][m] != player and board[i][m] != '~':
        m +=1
    if m < (len(board)) and  board[i][m] == player:
        while j < (len(board)) and board[i][j] != player and board[i][j] != '~':
            board[i][j] = player
            j += 1
            br += 1  
    return br
def applay_to_board_left_to_bottom(board,player,i,j):
    br = 0
    i +=1
    j -=1
    k = i
    m = j
    while k < (len(board)) and m>=0 and board[k][m] != player and board[k][m] != '~':
        k += 1
        m -= 1
    if k < (len(board)) and m>=0 and  board[k][m] == player:
        while i < (len(board)) and j>=0 and board[i][j] != player and board[i][j] != '~':
            board[i][j] = player
            i += 1
            j-=1
            br += 1    
    return br
def applay_to_board_right_to_bottom(board,player,i,j):
    br = 0
    i += 1
    j+=1
    k = i
    m = j
    while k < (len(board))and m < (len(board)) and board[k][m] != player and board[k][m] != '~':
        k +=1
        m += 1
    if k < (len(board))and m < (len(board)) and board[k][m] == player:
        while i < (len(board))and j < (len(board)) and board[i][j] != player and board[i][j] != '~':
            board[i][j] = player
            i += 1
            j+=1
            br += 1
    return br
def applay_to_board_right_to_top(board,player,i,j):
    br = 0
    i -= 1
    j+=1
    k = i
    m = j
    while k>= 0 and m < (len(board)) and board[k][m] != player and board[k][m] != '~':
        k-=1
        m+=1
    if  k>= 0 and m < (len(board)) and  board[k][m] == player:
        while i>= 0 and j < (len(board)) and board[i][j] != player and board[i][j] != '~':
            board[i][j] = player
            i -= 1
            j+=1
            br += 1
    return br
def applay_to_board_left_to_top(board,player,i,j):
    br = 0
    i-= 1
    j-=1
    k = i
    m = j
    while k>=0 and m>=0 and board[k][m] != player and board[k][m] != '~':
        k-=1
        m-=1
    if k>=0 and m>=0 and  board[k][m] == player:
        while i>=0 and j>=0 and board[i][j] != player and board[i][j] != '~':
            board[i][j] = player
            i-= 1
            j-=1
            br += 1
    return br

def applay_to_board(board, player, field):
    i = int(field[0])-1
    j = int(field[1])-1
    br = 0
    
    board[i][j] = player
    br+=1
    br += applay_to_board_bottom(board,player,i,j)  
    br += applay_to_board_left(board,player,i,j)
    br += applay_to_board_top(board,player,i,j)
    br += applay_to_board_right(board,player,i,j)
    br += applay_to_board_left_to_bottom(board,player,i,j)
    br += applay_to_board_right_to_bottom(board,player,i,j)
    br += applay_to_board_right_to_top(board,player,i,j)
    br += applay_to_board_left_to_top(board,player,i,j)
    
    return br
    

def show_possibilities_left(board,player,i,j):
    j -=1
    br = 0
    while j >=0 and board[i][j] != player and board[i][j] != '*' and board[i][j] != '~':
        j -= 1
        br += 1
        if j >=0 and  board[i][j] == '~' and br != 0:
            board[i][j] = '*'
            br = 0
def show_possibilities_right(board,player,i,j):
    j+=1
    br = 0
    while j < (len(board)) and board[i][j] != player and board[i][j] != '*' and board[i][j] != '~':
        j += 1
        br += 1
        if j < (len(board)) and board[i][j] == '~' and br != 0:
            board[i][j] = '*'
            br = 0
def show_possibilities_top(board,player,i,j):
    i-=1
    br = 0
    while i >= 0 and board[i][j] != player and board[i][j] != '*' and board[i][j] != '~':
        i -= 1
        br += 1
        if i >= 0 and board[i][j] == '~' and br != 0:
            board[i][j] = '*'
            br = 0
def show_possibilities_bottom(board,player,i,j):
    i+=1
    br = 0
    while i < (len(board)) and board[i][j] != player and board[i][j] != '*' and board[i][j] != '~':
        i += 1
        br += 1
        if i < (len(board)) and  board[i][j] == '~' and br != 0:
            board[i][j] = '*'
            br = 0
def show_possibilities_left_to_bottom(board,player,i,j):
    i+=1
    j-=1
    br = 0
    while i < (len(board)) and j>= 0 and board[i][j] != player and board[i][j] != '*' and board[i][j] != '~':
        i+=1
        j-=1
        br += 1
        if i < (len(board)) and j>= 0 and board[i][j] == '~' and br != 0:
            board[i][j] = '*'
            br = 0
def show_possibilities_right_to_bottom(board,player,i,j):
    i+=1
    j+=1
    br = 0
    while i < (len(board)) and j < len(board) and board[i][j] != player and board[i][j] != '*' and board[i][j] != '~':
        i += 1
        j += 1
        br += 1
        if  i < (len(board)) and j < len(board) and board[i][j] == '~' and br != 0:
            board[i][j] = '*'
            br = 0
def show_possibilities_left_to_top(board,player,i,j):
    i-=1
    j-=1
    br = 0
    while i >= 0 and j >= 0 and board[i][j] != player and board[i][j] != '*' and board[i][j] != '~':
        i -= 1
        j -= 1
        br += 1
        if i >= 0 and j >= 0 and board[i][j] == '~' and br != 0:
            board[i][j] = '*'
            br = 0
def show_possibilities_right_to_top(board,player,i,j):
    i-=1
    j+=1
    br = 0
    while i >=0 and j < len(board) and board[i][j] != player and board[i][j] != '*' and board[i][j] != '~':
        i -= 1
        j += 1
        br += 1
        if i >=0 and j < len(board) and  board[i][j] == '~' and br != 0:
            board[i][j] = '*'
            br = 0
def show_possibilities(board, player):

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == player:
                show_possibilities_bottom(board,player,i,j)
                show_possibilities_left(board,player,i,j)
                show_possibilities_top(board,player,i,j)
                show_possibilities_right(board,player,i,j)
                show_possibilities_left_to_bottom(board,player,i,j)
                show_possibilities_right_to_bottom(board,player,i,j)
                show_possibilities_right_to_top(board,player,i,j)
                show_possibilities_left_to_top(board,player,i,j)

    for i in range(0, len(board)):
        if board[i].count('*'):
            return True
    return False
def remove_possibilities(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == '*':
                board[i][j] = '~'              
            
def is_valid(field):
    i = int(field[0]) -1
    j = int(field[1]) -1
    if board[i][j] == '*':
        return True
    else:
        return False

def input_field(player):
    res = input(f"Unesite polje za {player} igraca: ")
    while is_valid(res) == False:
        print("Greska!")
        res = input(f"Unesite polje za {player} igraca: ")
    return res

board = [
    ['~','~','~','~','~','~','~','~'],
    ['~','~','~','~','~','~','~','~'],
    ['~','~','~','~','~','~','~','~'],
    ['~','~','~','▣','◍','~','~','~'],
    ['~','~','~','◍','▣','~','~','~'],
    ['~','~','~','~','~','~','~','~'],
    ['~','~','~','~','~','~','~','~'],
    ['~','~','~','~','~','~','~','~'],
]

black_br = 2
white_br = 2
black = ''
white = ''
pom = 0
end = 0
while black_br != 0 and white_br != 0 and end<2: 
    end = 0
    if show_possibilities(board,'▣'):
        print_board(board)
        crni = input_field('crnog')
        remove_possibilities(board)
        pom += applay_to_board(board, '▣', crni)
        black_br += pom
        white_br -= pom-1
        print_board(board)
        pom = 0
    else: 
        end += 1

    if show_possibilities(board,'◍'):
        print_board(board)
        bijeli = input_field('bijelog')
        remove_possibilities(board)
        pom += applay_to_board(board, '◍', bijeli)
        white_br += pom
        black_br -= pom-1
        print_board(board)
        pom = 0
    else:
        end += 1
    print(f'Crni: {black_br},Bijeli: {white_br}')
