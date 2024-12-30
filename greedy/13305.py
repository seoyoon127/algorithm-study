N= int(input())
dist = list(map(int,input().split()))
cost = list(map(int,input().split()))

min_value = cost[0]
answer = 0
for i in range(len(dist)):
    total = min_value * dist[i]
    answer += total
    print('i',i,total)

    min_value = min(min_value, cost[i+1])
print(answer)


# n = int(input())
# need = list(map(int, input().split()))
# price = list(map(int, input().split()))
# i,answer=0,0
# while i < n-1:
#     answer += price[i] * need[i]
#     for j in range(i+1,n-1):
#         if price[i] < price[j]:
#             answer += price[i] * need[j]
#             if j == n-2:
#                 i = j
#                 break
#         else: 
#             i = j-1
#             break
#     i+=1

# print(answer) 