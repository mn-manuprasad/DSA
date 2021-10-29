# linear search in strings

class findString():
    def findchar(self,string,char):
        for i in range(0,len(string)):
            if char == string[i]:
                return i
        else:
            return False

string = 'manuu'
char = 'k'
c = findString().findchar(string,char)
print(f'{char} is found at index {c}') if c else print(f'{char} Not Found')