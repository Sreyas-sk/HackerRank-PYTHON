if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    A=list(arr)
    A.sort()
    m=max(A)
    i=n-1
    while(A[i]==m):
        i-=1
    print(A[i])    
  
