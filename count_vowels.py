a = "This is a sample string to count vowels"
s = 0
for i in range(len(a)):
    if a[i] in "aeiouAEIOU":
        print(a[i])
        s = s+1
print("Total number of vowels in the given string is:", s)
