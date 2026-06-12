def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input("Enter a string: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")