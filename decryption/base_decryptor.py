from abstract_decryptor import AbstractDecryptor


class BaseDecryptor(AbstractDecryptor):

    def convert_to_string(self, base64_bytes):
        message_bytes = super().convert_from_base64(base64_bytes)
        message = ""
        try:
            # converts bytes to string assuming ascii representation
            message = message_bytes.decode('ascii')
        except:
            pass
        return message

    def convert_from_base64(self, input_bytes):
        return input_bytes.decode('ascii')
