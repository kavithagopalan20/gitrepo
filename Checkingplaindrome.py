def is_palindrome(text):
    # usually palindromes ignore case/spaces
    clean_text = "".join(char.lower() for char in text if char.isalnum())
    
    left = 0
    right = len(clean_text) - 1
    
    while left < right:
        if clean_text[left] != clean_text[right]:
            return False
        left += 1
        right -= 1
        
    return True

test_input = input("Enter a string to check for palindrome: ")
print(is_palindrome(test_input))
