from anagram_checker import AnagramChecker

print("*****************************************")
print("*                                       *")
print("*          THE ANAGRAM CHECKER          *")
print("*                                       *")
print("*****************************************")

print("\n> Do you wanna play?")
response = input("> Input a word or write exit: ").lower().strip()

# while response != "exit":

while response != 'exit':
    check = "".join(response.split())

    try:
        if response != check:
            raise ValueError("You typed more than one word.")
        else:

            if response.isalpha() == False:
                raise ValueError("Your words must contain only alphabetical characters!")
            else:
                testing = AnagramChecker('sowpods.txt')

                if testing.is_valid_word(response) == False:
                    raise ValueError("This is not a valid english word!")
                else:

                    print(f"\nYOUR WORD: '{response}'")
                    print("This is a valid English word.")
                    print(f"Anagrams for your word: {", ".join(testing.anagrams(response))}.")

    except ValueError as e:
        print(f"\nERROR! {e}")

    finally:
        print("\n> Do you wanna keep playing?")
        response = input("> Input a word or write exit: ").lower().strip()

print("\nWe are done for today. Thanks for playing THE ANAGRAM CHECKER!")
