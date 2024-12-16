def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x != 0 and x % 10 == 0:
        return False
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    return x == reversed_half or x == reversed_half // 10
x = 121
print(isPalindrome(x)) 
x = -121
print(isPalindrome(x))  
x = 10
print(isPalindrome(x))  
