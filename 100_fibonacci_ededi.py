#ilk 100 fibonacci ededini ekrana yazdiran proqram

#1,1,2,3,5,8,13,21,34...

fibonacci_list=[]
fibonacci_list.append(1)
fibonacci_list.append(1)
index=2

while True:
    fibonacci_list.append(fibonacci_list[index-2]+ fibonacci_list[index-1])
    index+=1

    if len(fibonacci_list)==100:
        break

print(fibonacci_list)
