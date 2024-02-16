
def findLeastNumOfUniqueInts( arr: list[int], k: int):
    #least number of uniques so
    # 1. remove singles
    # 2. remove least frequent integers
    # 3. randomly select if frequency matches
    # freq = ([(1,2),(2,5),(num,count)])
    #frequency=dict.fromkeys(range(10), 0)
    frequency={}
    index={}
    for i,j in enumerate(arr):
        frequency[j] = frequency.setdefault(j,0)+1
        val = index.setdefault(j,[])
        val.append(i)

    while k>0:
        try:
            minimum = min(frequency,key=frequency.get)
            print(minimum)
        except ValueError:
            return 0
        if frequency[minimum]<k:
            # removes the least frequent element where k is more than frequency
            k-=frequency[minimum]
            frequency.pop(minimum)
            continue
        # now k is lower than the least frequent element, and no more singles.
        frequency[minimum] = frequency[minimum]- k
        print(frequency)
        break
    return len(frequency)





test=[2,3,3,3,4,4,5,5]
print(findLeastNumOfUniqueInts(test,4))