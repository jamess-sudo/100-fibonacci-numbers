fibonacciListi=[]
fibonacciListi.append(1)
fibonacciListi.append(1)

for i in range (2,100):
    fibonacciListi.append(fibonacciListi[i-2]+fibonacciListi[i-1])

print(fibonacciListi)
