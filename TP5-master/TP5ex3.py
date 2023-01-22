def Palindromes():
    user_input = input("Entrez un mot ou une phrase : ")
    cleaned_input = ""
    for char in user_input:
        if char.isalpha():
            cleaned_input += char.lower()
    if cleaned_input == cleaned_input[::-1]:
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

Palindromes()
