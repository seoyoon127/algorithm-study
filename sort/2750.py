n = int(input())
inputList=[]
for i in range(n):
    x = int(input())
    inputList.append(x)

#버블정렬
for i in range(n-1):
    for j in range(i+1,n):
        if inputList[i] > inputList[j]:
            temp = inputList[i]
            inputList[i] = inputList[j]
            inputList[j] = temp

for i in inputList:
    print(i)