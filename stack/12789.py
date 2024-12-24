n = int(input())
array = list(map(int, input().split())) 
recieved = 1
stack = []

for i in range (n):
    while stack and stack[-1] == recieved:
        recieved += 1
        stack.pop()
    if array[i] == recieved:
        recieved+=1
    elif not stack or stack[-1] > array[i]:
        stack.append(array[i])
    elif stack and array[i]>stack[-1]:
            print("Sad")
            break
else:
    print("Nice")