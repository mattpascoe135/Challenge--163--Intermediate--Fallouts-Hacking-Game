import random

""" Generates random words from a dictionary, depending on the selected
difficulty (increasing from 1 to 5). Give the player 4 chances to select
the correct password, otherwise they lose the game.
"""
def falloutHacking():
    #
    # Recieve the input data, determine length of string
    #
    number = raw_input("Difficulty (1-5)? ");
    length = 0
    if(number == '1'):
        length = 4
    elif(number == "2"):
        length = 5
    elif(number == "3"):
        length = 6
    elif(number == "4"):
        length = 7
    elif(number == "5"):
        length = 8
    else:
        print "Invalid input"
        return
        
    #
    # Go through the dictionary and compile all words which are the same length as given input
    #
    words = list()
    dic = open("dictionary.txt", "r")
    for line in dic:
        if(len(line.strip()) == length):
            words.append(line)
    dic.close()


    #
    # Find 8 random words and select one to be the password
    #
    password = "foo"
    possible = list()
    while (len(possible) != 8):
        for word in words:
            if(random.randint(0, 699) == 400):
                if(len(possible) != 8):
                    possible.append(word.strip())
                    
    while(password == "foo"):
        for word in possible:
            if(random.randint(0, 999) == 70):
                password = word

    for word in possible:
        print word


    #
    # Loop around counting the number of faliures checking for the correct password
    #
    successful = 0
    for x in range (0, 4):
        correct = 0
        outStr = 'Guess (' + str(4-x) + ' left)? '
        guess = raw_input (outStr);
        for x in range(0, length):
            if(x < len(guess)):
                if(guess[x] == password[x]):
                    correct += 1
        if(guess == password):
            print correct, "/", length, " correct"
            print "You win!"
            successful = 1
            break
        else:
            print correct, "/", length, " correct"

    if(successful == 0):
        print "FALIURE: You have been locked out, the password was: ", password


#
# Run the game
#
falloutHacking()
