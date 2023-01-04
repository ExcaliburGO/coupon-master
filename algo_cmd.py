P, K=map(int, input().split())
C=[int(i) for i in input().split()]
R=[]
W=[]
M=[]
N=[]
for i in range(K):
    inp=input().split()
    R.append(inp[0])
    W.append(float(inp[1]))
    M.append(float(inp[2]))
    L=int(inp[3])
    N.append([int(i)-1 for i in inp[4:]])
print(C, R, W, M, N)
jakiprodukt=[-1 for i in range(K)]
minprice=9999999999
mindist=jakiprodukt
def calcprice():
    price=0
    for kupon, produkt in enumerate(jakiprodukt):
        if produkt>=0:
            if R[kupon]=="P":
                price-=C[produkt]*W[kupon]/100
            else:
                price-=W[kupon]
    return price
def solve(kupon):
    global minprice, mindist
    if kupon==K:
        if calcprice()<=minprice:
            minprice=calcprice()
            mindist=jakiprodukt[:]
            print(jakiprodukt)
        return
    solve(kupon+1)
    for produkt in N[kupon]:
        if produkt not in jakiprodukt:
            print("jakiprodukt[", kupon, "]=", produkt)
            jakiprodukt[kupon]=produkt
        solve(kupon+1)
    jakiprodukt[kupon]=-1
solve(0)
print(minprice, mindist)