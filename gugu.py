import sys

def gugu(end = 9):
    data =''
    for j in range(2,end + 1):
        print(f"{str(j)+'단':=^10}")
        for i in range(1,10):
            data += (f'{j} x {i} = {j*i}')+'\n'
    return data
print(gugu(2))

result = int() + int()
print(result)