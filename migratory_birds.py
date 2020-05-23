""" 
You have been asked to help study the population of birds migrating across the continent. 
Each type of bird you are interested in will be identified by an integer value. 
Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. 
You would like to be able to find out which type of bird is most common given a list of sightings. 
Your task is to print the type number of that bird and if two or more types of birds are equally common,
 choose the type with the smallest ID number.
"""

def migratoryBirds(arr):
    pairs = {}
    arr1 = set(arr)    
    for i in arr1:
        count = 0
        for k in arr:
            if k == i:
                count += 1 
        pairs[i] = count           
    ky = [x for x in pairs if pairs[x]==(max(list(pairs.values())))]
    return min(ky)

print(migratoryBirds([1, 4, 4, 4, 5, 3]))
print(migratoryBirds([1,1,2,2,3]))