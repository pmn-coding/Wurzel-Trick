# ::::::::::::::::::::::SUB::::::::::::::::::::::

def isprim(a):
    x = 2
    if a == 0 or a == 1: 
        return False                   
    elif a == 2: 
        return True                    
    else:
        while x < a:                    
            if a % x == 0: 
                return False            
            x += 1                      
    return True

# :::::::::::::::::::::MAIN::::::::::::::::::::::

n = int(input(">>> n: "))
nn = n**0.5
nn = int(nn)
q = 0
p = 0
q = nn

while not p * q == n:
    p = n / q
    if isprim(q):
        break
    else:
        q += 1               
print(q, p)
