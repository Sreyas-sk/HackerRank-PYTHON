import itertools
elements=input()
A=list(map(int,elements.strip().split()))
elements=input()
B=list(map(int,elements.strip().split()))
for i in itertools.product(A,B):
          print(i,end=" ")
