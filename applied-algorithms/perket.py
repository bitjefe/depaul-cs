# number of ingredients
m = int(input())

# create an object for sour and bitter ingredients
sourObj = {}
bitterObj = {}

# fill the sourness and bitterness objects for each ingredient
for i in range(m):
    n = input().split()
    
    sourObj[i] = int(n[0])
    bitterObj[i] = int(n[1])

#set smallest difference to 2,000,000,000 since sour and bitter will be both less than 1,000,000,000
smallest = 2000000000;
newSmallestCandidate = 2000000000;
sourProduct = 1
bitterSum = 0


# start bitwise ops for ingredients
for i in range(1, (1<<m)):
    for j in range(0, m):
        if(j == 0 and (i & 1<<j)):
            sourProduct = sourProduct * sourObj[0]
            bitterSum = bitterSum + bitterObj[0]
        else:
            if(i & 1<<j):
                sourProduct = sourProduct * sourObj[j]
                bitterSum = bitterSum + bitterObj[j]  
                
    newSmallestCandidate = abs(sourProduct-bitterSum)
    # update the smallest difference between sour and bitter ingredients
    if (newSmallestCandidate < smallest):
        smallest = newSmallestCandidate      

    # reset sourProduct = 1 and bitterSum = 0 for next combination
    sourProduct = 1
    bitterSum = 0

print(smallest)    