strList = []
while True:
    s = input()
    strList.append(s)
    if s == ".":
        break

for str in strList:
    if str == ".":
        break
    stack = []
    for i in str:
        if i == "[" or i == "(" :
            stack.append(i)
        elif i == "]" or i == ")" :
            p = stack[-1] if stack else ""
            if (i =="]" and p == "[") or (i ==")" and p == "(") :
                stack.pop()
            else:
                print("no")
                break
    else:
        if not stack:
            print("yes")
        else:
            print("no")