def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")




def longest_palindrome(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    longest = ""
    for i in range(len(s)):
        odd = expand(i, i)  
        even = expand(i, i + 1) 
        longest = max(longest, odd, even, key=len)

    return longest

string = input("Enter a string: ")
print(f"Longest palindromic substring is: {longest_palindrome(string)}")



from collections import Counter

def can_form_palindrome(s):
    count = Counter(s)  #յուրաքանչյուր տառի հաճախականությունը
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)  #թե քանի տառ ունի անհավասար հաճախականություն
    return odd_count <= 1  

string = input("Enter a string: ")
if can_form_palindrome(string):
    print(f"{string} Can be a palindrome")
else:
    print(f"{string} Can't be a palindrome.")

