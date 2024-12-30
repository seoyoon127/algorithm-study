n = input()
numList = list(n.split('-'))

for i in range (len(numList)):
    if i == 0:
        answer = sum(map(int, numList[i].split('+')))
    else:
        answer -= sum(map(int, numList[i].split('+')))
print(answer)
