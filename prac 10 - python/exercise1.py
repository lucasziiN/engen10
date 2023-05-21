prices = [ 11.35, 11.15, 12.11, 13.01, 10.99 ]
min = prices[0]
for price in prices:
    if price < min:
        min = price
print("Lowest price =", min)

for x in range(1,11): #line 1
    for y in range(1,11): #line 2
        print(x, "+", y, "=", x + y) #line 3
    print("") #line 4
    
