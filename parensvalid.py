def parensvalid(stringInput):
    opencount = 0
    closedcount = 0

    for i in range(0, len(stringInput), 1):
        if stringInput[i] == "(":
            opencount += 1

        elif stringInput[i] == ")":
            closedcount += 1
        
        if closedcount > opencount:
            return False
    
        if opencount != closedcount:
            return False

        else:
            return True

print(parensvalid(")(()"))



def parenvalid2(stringInput):
    # your code here 
    count = 0
    # closedcount = 0
    for i in range(0, len(stringInput), 1):
        if stringInput[i] == "(":
            count += 1
        elif stringInput[i] == ")":
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False

print(parenvalid2(")(()"))