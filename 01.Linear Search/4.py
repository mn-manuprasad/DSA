# Finding the minimum number

class min_In_List():
    def Min(self,ls):
        min = ls[0]
        for i in ls:
            if i < min:
                min = i
        else:
            return min

ls = [4,8,9,-54,68,34]

print(min_In_List().Min(ls))
