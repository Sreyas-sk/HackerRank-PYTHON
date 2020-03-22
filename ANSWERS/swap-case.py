def swap_case(s):
  i=0
  b=""
  for i in range(0,len(s)):
    if(s[i].islower()):
        b=b+s[i].upper()
    elif(s[i].isupper()):
        b=b+s[i].lower()
    else:
        b=b+s[i]        
  return(b)

