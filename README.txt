QUICKSTART
Create a text file containing the message you want to decipher/encipher. Run
permutationciphers.py in command line and follow prompts. Output will be saved to
text file with a user specified name.

***Intro
A permutation cipher is a method of encrypting data by rearranging the sequence
of characters according to a permutation. The goal of using a permutation cipher
is to secure sensitive information.

Project goals: Develop software that can encrypt and then decrypt data using a
permutation cipher; Explore and implement any preexisting code or algorithms
relating to permutation ciphers; Gain familiarity with GitHub through publishing,
updating, and maintaining project code

***Usage
Key: a permutation of the digits 0:len(key)-1. Default key can be changed by modifying DEFAULT_KEY in permutationciphers.py
Acceptable examples: 1032, 1230, 0123, 540312
Unacceptable examples: 0000, 0112, 0 1 2 3, zero one two three, abcd, 2578, 1234, 32415

***Future improvements:
*Add GUI using pyqt

***Completed Improvements
*Modify Message class to take advantage of property that each permutation cipher
has a reverse key that will decipher an encrypted message. Therefore we only need
one encryption method that uses either the key or the inverse key
--Created message.py to hold Message class and improvement readability of code.
--removed encrypt() and decrypt() methods from Message class
--added permutate() method to Message class which permutates message using a specified key
--added get_inverse() method to find the inverse key of the given key
*Create functionality to customize the length of the key used.
--User can input a key of any length as long as it follows the guidelines outline in README Usage section
--Default key is still only 4 digits long but can easily be modified by user to any length without impacting code
