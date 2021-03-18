from base_decryptor import BaseDecryptor

YOUR_SERIAL_NUMBER = 12
with open(f'encrypted_{YOUR_SERIAL_NUMBER}.txt', 'r') as file:
    data = file.read().replace('\n', '')
base64_message = data

# DECRYPT
result = BaseDecryptor().decrypt_message(base64_message)
print("The encrypted message is: " + result)
