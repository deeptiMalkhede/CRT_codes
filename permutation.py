from itertools import permutations
# def get_permutation(n):
#     arr=permutations(n)
#     print(arr)

n=int(input("enter no"))
val=int(input("enter value "))
perm_list=[]
num=str(n)
arr=permutations(num)
list=[''.join(p) for p in arr]
print(list)
for i in list:
    if int(i) >= val:
        perm_list.append(i)
        
print(perm_list)
print(min(perm_list))







