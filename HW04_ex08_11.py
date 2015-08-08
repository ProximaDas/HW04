#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """This works.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """This checks for a constant character 'c'. Doesn't process
    the user input at all.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """This works.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """This works.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """This actually checks if a character is not in lowercase.
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print any_lowercase2('THISDOESNTWORK')
    print any_lowercase5('BoOHOO')
    

if __name__ == '__main__':
    main()