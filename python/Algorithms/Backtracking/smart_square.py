smart_squares = []

def is_valid(a):
    if (a[0]+a[1]+a[2])%5 != 0 or (a[3]+a[4]+a[5])%5 != 0 or (a[6]+a[7]+a[8])%5 != 0:
        return False
    if (a[0]+a[3]+a[6])%5 != 0 or (a[1]+a[4]+a[7])%5 != 0 or (a[2]+a[5]+a[8])%5 != 0:
        return False
    if (a[0]+a[4]+a[8])%5 != 0 or (a[2]+a[4]+a[6])%5 != 0:
        return False
    return True
    
def generate_squares(temp, vis, idx):
    if idx == 9:
        if is_valid(temp):
            smart_squares.append(temp[:])
        return

    for i in range(1, 10):
        if not vis[i]:
            temp[idx] = i
            vis[i] = True
            generate_squares(temp, vis, idx+1)
            vis[i] = False

temp = [0]*9
v = [False]*(10)
generate_squares(temp, v, 0)

tests = int(input())
for _ in range(tests):
    a = []
    for _ in range(3):
        a.extend(list(map(int, input().split())))
    mncost = float("inf")
    for mat in smart_squares:
        cost = 0
        for i in range(9):
            cost+= abs(a[i]-mat[i])
        mncost = min(mncost, cost)
    print(mncost)