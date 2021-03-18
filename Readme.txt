Instructions:

Fix the code in order to decrypt your encrypted message.
Your message is found in the file named encrypted_<YOUR_SERIAL_NUMBER>.txt .
Check your changes by running main.py - the decrypted message should be a valid english sentence.

You cannot delete methods or change the method signatures ( function name and input parameters ) and class names.
Pay attention that the class AbstractEncryptor is an abstract class and cant be changed to a regular class.

The encryption algorithm that was used to encrypt your original message is:

1. Increase by one the ordinal of each character in the input message.
2. Convert the string to bytes according to the ascii value of each character.
3. Convert the bytes to base64
4. Convert the base64 bytes to string according to the ascii value of each character.

