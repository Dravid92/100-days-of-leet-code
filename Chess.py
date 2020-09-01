board = [[".",".",".",".",".",".",".","."],
[".","p","p","p","p","p",".","."],
[".","p","p","B","p","p",".","."],
[".","p","B","R","B","p",".","."],
[".","p","p","B","p","p",".","."],
[".","p","p","p","p","p",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."]]

# pawns in the same index as the rook is in every list
# pawns in the same list as the rook is
# no white bishops inbetween the rook and the pawn both index wise and row wise
rookindex = 0
rookrow = 0
elemc = []
pidx = 0
bidx = 0
fin1 = 0
fin2 = 0
for k,i in enumerate(board):
    for n,j in enumerate(i):
        if j == 'R':
            rookindex += n
            rookrow += k
elemr = board[rookrow]
for i in board:
    elemc.append(i[rookindex])
for m,i in enumerate(elemc[:elemc.index('R')]):
    pidx = 0
    bidx = 0
    if i == 'p':
        pidx += m
        fin1 += 1
        if bidx > pidx:
            fin1 = 0
    elif i == 'B':
        bidx += m
        if bidx > pidx:
            fin1 = 0
if fin1 > 1:
    fin1 = 1

for y,i in enumerate(elemc[elemc.index('R'):]):
    pidx = 0
    bidx = 0
    if i == 'p' and pidx == 0 :
        pidx += y
        fin2 += 1
        if bidx > pidx:#0:
            fin2 = 0
        break
    elif i == 'B':
        bidx += y
        if bidx > pidx:
            fin2 = 0
            if pidx == 0:
                break
if fin2 > 1:
    fin2 = 1        
fin3 = 0
fin4 = 0
for x,i in enumerate(elemr[:elemr.index('R')]):
    pidx = 0
    bidx = 0# first half of column
    if i == 'p':
        pidx += x
        fin3 += 1
        if bidx > pidx:
            fin3 = 0
    elif i == 'B':
        bidx += x
        if bidx > pidx:
            fin3 = 0

if fin3 > 1:
    fin3 = 1
for w,i in enumerate(elemr[elemr.index('R'):]):
    pidx = 0
    bidx = 0# Second half of column
    if i == 'p' and pidx == 0 :
        pidx += w
        fin4 += 1
        if bidx > pidx:#0:
            fin4 = 0
        break
    elif i == 'B':
        bidx += w
        if bidx > pidx:
            fin4 = 0
            if pidx == 0:
                break
if fin4 > 1:
    fin4 = 1
print(fin1+fin2+fin3+fin4)