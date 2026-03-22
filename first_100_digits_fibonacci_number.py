fibonacci_list=[]

fibonacci_list.append(1)
fibonacci_list.append(1)

index=2

while True:
    fibonacci_list.append(fibonacci_list[index-2]+fibonacci_list[index-1])

    termin=fibonacci_list[index-2]+fibonacci_list[index-1]

    if len(str(termin))==100:
        print(termin)
        print(index)
        break

    index+=1