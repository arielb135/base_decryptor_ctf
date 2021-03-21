Instructions:

Fix the small bug in the code in order to decrypt your encrypted message.
Your message is found in the bit.ly link you got.
Check your changes by running main.py - the decrypted message should be a valid English sentence.

You cannot delete or change the classes and methods signatures ( names and input parameters ).
Pay attention that the class AbstractEncryptor is an abstract class and can't be changed to a regular class.

The encryption algorithm that was used to encrypt your original message is:

1. Increase by one the ordinal of each character in the input message.
2. Convert the string to bytes according to the ascii value of each character.
3. Convert the bytes to base64
4. Convert the base64 bytes to string according to the ascii value of each character.
