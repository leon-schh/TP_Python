Tab =[5,2,4,8,1,3]

for i in range(len(Tab)):
    plus_petit = Tab[i]
    for x in range(i,len(Tab)):
        if plus_petit > Tab[x]:
            plus_petit = Tab[x]
            pos_plus_petit = x
    if plus_petit != Tab[i]:
        element = Tab[i]
        Tab[i] = plus_petit
        Tab[pos_plus_petit] = element
    print(Tab)

Tab =[5,2,4,8,1,3]

print("Sorted Tab : ",sorted(Tab))
Tab =[5,2,4,8,1,3]
Tab.sort()
print("Tab.sort : ",Tab)
