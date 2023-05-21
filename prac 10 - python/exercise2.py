# Request user input for minimum number, convert to integer
min = int(input("Enter minimum number: "))
# Request user input for maximum number, convert to integer
max = int(input("Enter maximum number: "))

# Check if maximum number is greater than or equal to minimum number
if (max >= min):
    # Loop through each number in the range from min to max (inclusive)
    for i in range(min,max+1):
        # For each number i, loop through numbers 1 to 9 (inclusive)
        for j in range(1,10):
            # Print multiplication statement and result
            print(j, "*", i, "=", j * i)
        # Print a blank line after each set of multiplication results for a given i
        print("")
    
