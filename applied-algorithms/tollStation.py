# A) Design an Design a O(N) time algorithm that computes the cost of going 
# between any two stations i and j using only an array of the stretch costs.

def tollStationCostA(i,j):
    costs = [0, 5 , 7, 4, 9]
    finalCost = 0
    
    for k in range(i,j):
        finalCost += costs[k]

    return finalCost

## Toggle Comments to see print test cases for part A
# print(tollStationCostA(1,2))
# print(tollStationCostA(1,3))
# print(tollStationCostA(1,4))
# print(tollStationCostA(1,5))
# print(tollStationCostA(2,3))
# print(tollStationCostA(2,4))
# print(tollStationCostA(2,5))
# print(tollStationCostA(3,4))
# print(tollStationCostA(3,5))
# print(tollStationCostA(4,5))



# B) Design a O(1) time algorithm that computes the cost of going between any 
# two stations i and j using a pre-computed table with O(N^2) entries.

def tollStationCostB(i,j):
    costsDict = {
        '1,2':5,
        '1,3':12,
        '1,4':16,
        '1,5':25,
        '2,3':7,
        '2,4':11,
        '2,5':20,
        '3,4':4,
        '3,5':13,
        '4,5':9
    }
    
    key = str(i) + ',' + str(j)
    
    return costsDict[key]

## Toggle Comments to see print test cases for part B
# print(tollStationCostB(1,2))
# print(tollStationCostB(1,3))
# print(tollStationCostB(1,4))
# print(tollStationCostB(1,5))
# print(tollStationCostB(2,3))
# print(tollStationCostB(2,4))
# print(tollStationCostB(2,5))
# print(tollStationCostB(3,4))
# print(tollStationCostB(3,5))
# print(tollStationCostB(4,5))




# C) Design a O(1) time algorithm that computes the cost of going between any 
# two stations i and j using a pre-computed array of size O(N).

def tollStationCostC(i,j):
    costs = [0, 5, 12, 16, 25]    
    
    return costs[j-1] - costs[i-1]
    


## Toggle Comments to see print test cases for part B
# print(tollStationCostC(1,2))
# print(tollStationCostC(1,3))
# print(tollStationCostC(1,4))
# print(tollStationCostC(1,5))
# print(tollStationCostC(2,3))
# print(tollStationCostC(2,4))
# print(tollStationCostC(2,5))
# print(tollStationCostC(3,4))
# print(tollStationCostC(3,5))
# print(tollStationCostC(4,5))