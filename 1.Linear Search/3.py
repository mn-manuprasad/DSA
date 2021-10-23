#  Linear Search Within a given Range

class rangeSearch():
    def rangeSearch(self,ls,ele,start,end):
        for i in range(start,end+1):
            if ls[i]==ele:
                return i
        else:
            return False

c = rangeSearch().rangeSearch([1,2,3,4,5,6,7], 6, 2, 6)
if c:
    print(f'Element found at index {c}')
else:
    print("Element Not Found")
