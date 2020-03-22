# Complete the solve function below.
def solve(s):
    b=s.split(" ")
    s=""
    for i in range(0,len(b)):
        b[i]=b[i].capitalize()
        print(b[i])
        s=s+b[i]+" "
    return(s)        



