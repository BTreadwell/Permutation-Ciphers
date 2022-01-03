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
Key: a permutation of the digits 0,1,2,3. Default key can be changed by modifying DEFAULT_KEY in permutationciphers.py
Acceptable examples: 1032, 1230, 0123, 3210
Unacceptable examples: 0000, 0112, 0 1 2 3, zero one two three, abcd, 2578

***Future improvements:
*Add GUI using pyqt
*Modify Message class to take advantage of property that each permutation cipher
has a reverse key that will decipher an encrypted message. Therefore we only need
one encryption method that uses either the key or the inverse key
*Create functionality to customize the length of the key used.
