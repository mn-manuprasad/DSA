# Search in 2D array


class searchIn2dArray():
    def search(self,ls,target):
        for i in range(0,len(ls)):
            for j in range(0,len(ls[i])):
                if target == ls[i][j]:
                    return (i,j)
        else:
            return False


ls=[[4,6,78,9,4],
    [45,7,8],
    [76,34,32,67]
    ]
target =  34

c = searchIn2dArray().search(ls, target)
if c:
    print(f'{target} found at index {c[0]},{c[1]}')
else:
    print(f'{target} not found')

print(c[0])