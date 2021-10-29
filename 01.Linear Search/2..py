# Simple Linear Search In Interger array

class LinearSearch():
    def Search(self,ls,target):
        for i in range(0,len(ls)):
            if ls[i] == target:
                return i
        else:
            return -1


ls = [89,99,76,54,67,82]
target = 121

'''
# We can Call The fucntion in a class like this
index = LinearSearch().Search(ls,target)
             OR
# We can create an object of the class and using that we can access the class
liner = LinearSearch()
index = liner.Search(ls, target)

'''

liner = LinearSearch()
index = liner.Search(ls, target)
if not(index==-1):
    print(f'{target} is found at index {index}')
else:
    print(f'{target} is not found in the list')