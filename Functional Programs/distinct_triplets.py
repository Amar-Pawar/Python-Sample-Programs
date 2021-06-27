'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-27
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-27
@Title : To find distinct triplet whoes addition is zero
/**********************************************************************************
'''

def dist_triples():
    """
    Description:
        This function takes array elements as input and returns distinct triplets if sum of
        triplets is 0.     
    """
    arr = [int(x) for x in input("enter list elements: ").split()]
    print(arr)
    n = len(arr)
    count = 0  # count for number of distinct triples
    for i in range(0, n - 2):  # take arr[0], arr[1], arr[2] to compare
        for j in range(i + 1, n - 1):  # i,j,k represents respective numbers to be compare
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:  # this is required condition to find distinct triples
                    print("triplets are", arr[i], " ", arr[j], " ", arr[k])
                    count += 1  # when triples are found increment count by 1
    print(count, "number of triplets")

dist_triples()