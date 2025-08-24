tweet = input("Input: ")
tweet = tweet.strip()
vowels = "aeiouAEIOU"

for t in tweet:
    if t not in vowels:
        print(t,end="")
print("\n")
