import base64
from abc import ABC


class AbstractDecryptor(ABC):

    def decrypt_message(self, encrypted_message: str):

        base64_bytes = self.convert_to_bytes(encrypted_message)

        res = self.convert_and_decreas_char(base64_bytes)

        return res

    def convert_and_decreas_char(self, base64_bytes):
        message = self.convert_to_string(base64_bytes)
        res = self.decrease_char_value(message)
        return res

    def decrease_char_value(self, message):
        res = ""
        for c in message:
            res += chr(ord(c) - 1)
        return res

    def convert_to_string(self, base64_bytes):

        message = self.convert_from_base64(base64_bytes)

        return message

    def convert_from_base64(self, input_bytes):
        """
        Converts the input base64 representation to bytes
        :return: Byte represntation of the input.
        """
        message_bytes = base64.b64decode(input_bytes)
        return message_bytes

    def convert_to_bytes(self, message):
        """
        Converts string to bytes
        :return: Byte representation of the input.
        """
        my_bytes = message.encode('ascii')
        return my_bytes
