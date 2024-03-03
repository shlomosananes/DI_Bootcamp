"""
Exercise 1 : Use The Terminal
Instructions
Run this command in the terminal to open a python console:
$ python3
Hint: Replace python3 with python for Windows

Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory.
PATH explanation can be found here.
"""

# When we write a command in the terminal it is like a program is being executed.
# Usually we must specify the directory of the program by specifying its full path.
# However, there is an alternative to avoid having to write the full path.
# The way to do it is adding directories to the PATH function.
# Everytime we write a command to execute a program without specifying the full path,
# the system will scan all the directories saved on the PATH function.
# If the program is located in one of the pre-saved paths (on the PATH function),
# the system will execute the program successfully.
# THAT IS THE REASON WE CAN EXECUTE PYTHON WITHOUT SPECIFYING ITS FULL PATH ONCE WE PREVIOUSLY ADDED THE PATH TO THE PATH FUNCTION.


"""
Exercise 2 : Alias
Instructions
Read about alias, and try to open a python console with the command:
$ py
"""

# py is an alias to see the installed versions of python


"""
Exercise 3 : Outputs
Instructions
Predict the output of the following code snippets:
    >>> 3 <= 3 < 9
    >>> 3 == 3 == 3
    >>> bool(0)
    >>> bool(5 == "5")
    >>> bool(4 == 4) == bool("4" == "4")
    >>> bool(bool(None))
    x = (1 == True)
    y = (1 == False)
    a = True + 4
    b = False + 10

    print("x is", x)
    print("y is", y)
    print("a:", a)
    print("b:", b)
"""

# True
# True
# False
# False
# True
# False

# x is True
# y is False
# a: 5
# b: 10


"""
Exercise 4 : How Many Characters In A Sentence ?
Instructions
Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

my_text_len = len("Lorem ipsum dolor sit amet, consectetur adipiscing elit,  \n           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  \n           Ut enim ad minim veniam, quis nostrud exercitation ullamco  \n           laboris nisi ut aliquip ex ea commodo consequat.  \n           Duis aute irure dolor in reprehenderit in voluptate velit  \n           esse cillum dolore eu fugiat nulla pariatur.  \n           Excepteur sint occaecat cupidatat non proident,  \n           sunt in culpa qui officia deserunt mollit anim id est laborum. ")
print(my_text_len)


"""
Exercise 5: Longest Word Without A Specific Character
Instructions
Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message.
"""

a = 1
current_sentence = ""
current_len = 0
while (a == 1):
    new_sentence = input("\nWrite the longest sentence you can without using the character A: ")
    new_len = len(new_sentence)
    if new_sentence.count("A") > 0:
        print("You failed. This sentence has the character A.")
        print("The longest sentence is still: '{}'. The sentence has {} characteres.".format(current_sentence,current_len))
        b = input("Do you want to stop? (Y/N)")
    elif new_len < current_len:
        print("The sentence is not longer than the current record")
        print("The longest sentence is still: '{}'. The sentence has {} characteres.".format(current_sentence,current_len))
        b = input("Do you want to stop? (Y/N)")
    else:
        current_sentence = new_sentence
        current_len = new_len
        print("Well done! The longest sentence was updated to: '{}'. The sentence has {} characteres.".format(current_sentence,current_len))
        b = input("Do you want to stop? (Y/N)")

    if b == "Y":
        a = 2



