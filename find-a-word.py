#This is the Python Essentials 2 LAB 2.5.1.10 Find a word!


def input_line(ordinal):
    # This function prompts the user and validates the input
    # Parameter 'ordinal' is to enumerte inputs
    # It returns a string in lower case without spaces
    # It checks user input for alphanumeric characters and spaces
    # Blank lines are not allowed
    while True:
        text = input("Enter " + ordinal + " line of text to check (Roman alphabet only): ")
        if not text.isalpha():        # only alphabetic characters are allowed
            print("Invalid input. Only alphabetic characters and spaces are allowed.")
        elif len(text) == 0:          # blank lines are not allowed
            print("Invalid input. Blank lines are not allowed.")
        else:
            break
    return text

def user_input():
    # This function sequentially prompts the user for two strings
    # Returns tuple with two strings.
    while True:
        text1 = input_line("first")               # first line to check 
        text2 = input_line("second")              # second line to check
        return text1, text2

def find_a_word(what, where):
    # This function accepts two strings.
    # where - where to find.
    # what - what to find.
    # It returns True if the characters comprising the first string
    # are hidden inside the second string.
    # E.g., first string is "dog", the second is "vcxzxduybfdsobywuefgas"
    # The answer is Yes
    if not where.isalpha() \               # check input for alphabetic characters
       or len(where) == 0 \                # check input for empty strings
       or not what.isalpha() \             #
       or len(what) == 0:                  #
        return False                       # if checks failed -> exit function
                                           # index - is for last found char.
    index = -1                             # initialize it with 'not found'
                                           # next search will start from prev. found index
    for char in what:                      # iterating over characters in first string
        index = where.find(char, index+1)  # search current character in second string
        if index == -1:                    # if we found nothing
            return False                   # exit the function because answer is 'No'
    return True                            # if we got here, than answer is 'Yes'
        

def tests():
    # typical function that tries test cases
    print("Self-test ...")
    test_texts1 = ("donor",
                   "donut")
    test_texts2 = ("Nabucodonosor",
                   "Nabucodonosor")
    test_results = (True,
                    False)
    for i in range(len(test_texts1)):
        txt1 = test_texts1[i]
        txt2 = test_texts2[i]
        result = find_a_word(txt1, txt2)
        print(txt1 + ",", txt2, "->", result, end=" ")
        if result == test_results[i]:
                print("OK")
        else:
                print("Failed")


# Main
if __name__ == "__main__":
    text1, text2 = user_input()
    if find_a_word(text1, text2):
        print("Yes")
    else:
        print("No")

##tests() # uncomment to perform self-test
