def count_substring(string, sub_string):
  a=len(sub_string)
  b=[]
  for i in range(0,len(string)):
    b.append(string[i:i+a])
  a=0
  for i in range(0,len(b)):
    if(b[i]==sub_string):
        a+=1
  return a 


