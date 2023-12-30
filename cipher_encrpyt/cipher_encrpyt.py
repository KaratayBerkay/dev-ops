from numpy import mean
from time import perf_counter


class KayCipherEncrypter:
    """
    <TextEncrypt>(<ext_level><ext_shift>)*90<reserved_text_length-5>
    level =90
    reserved_text_length=<,,,$&>

    """

    def __init__(self, plain_text: str, encrypt_level: int = 1, encrypt: bool = True, debug=False):

        if not len(plain_text) > 0:
            raise Exception('Text length can not be less than 0...')

        self.debug = debug
        self.string_bank = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', '!',
            ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '}', '~', ' ', 'ı',
            'ü', 'ö', 'ç', 'ğ', 'ş', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '|'
        ]
        self.string_bank_shuffled = [
            '7', ',', 'j', 'I', 'ö', 'W', 'V', 'B', ':', 'E', 'b', 'v', '@', '1', '(', '~', 'D', 'Y', 'U', 'm', '*',
            '}', 'l', 'h', 's', 'o', 'c', '+', 'g', '-', '9', '>', 'w', 'f', '_', ';', ')', 'ü', 'x', 'R', 'q', '[',
            '8', 'k', 'S', '$', '0', '.', '6', '&', 'u', 'r', 'A', '^', '?', '/', 'ç', ']', 'Z', 'T', '{', '=', 'N',
            'Q', 'ı', 'K', '`', '!', 'X', 'F', '4', 'H', 'C', 'L', '#', 'i', '"', '2', 'n', '<', 'ğ', 'd', "'", 'z',
            'J', 'G', 'y', '3', '%', 'ş', 'e', 'a', 'M', 'p', '5', 'P', 'O', 't', '|', ' '
        ]
        self.text = plain_text
        self.text_list = list(plain_text)
        self.levels = encrypt_level
        self.greet()
        self.encryption = encrypt
        self.text_length = None
        self.text_body = self.text
        self.encrypt_ext = ''
        self.output = None
        self.active_level = 0
        self.process_plain_string()

    def process_plain_string(self):
        convert_length = []
        if self.encryption:  # If a decryption
            text_length_base = self.string_bank_shuffled[0] * 5
            for index, number in enumerate(''.join(list(reversed(list(str(len(self.text_list))))))):
                text_length_base = list(text_length_base)
                text_length_base[4 - index] = self.string_bank_shuffled[int(number)]
            self.text_length = ''.join(text_length_base)
            self.text_body = self.text
            if self.debug:
                print(self.get_text_info())
            self.output = self.encrypt_text()
        else:
            decrypt_convert_reserved = str(self.text_list[len(self.text_list) - 5])
            for letter in decrypt_convert_reserved:
                convert_length.append(str(self.string_bank_shuffled.index(letter)))
            self.text_length = int(''.join(convert_length))
            self.text_body = self.text[self.text_length:]
            self.encrypt_ext = self.text[self.text_length:len(self.text) - 5]
            self.output = self.decrypt_text()

    def get_text_info(self):
        return {
            "text_length": self.text_length, "text_body": self.text_body, "encrypt_ext": self.encrypt_ext,
            "active_level": self.active_level
        }

    def shift_list_negative_by_digit(self, n):
        new_list = []
        for x in range(n):
            new_list = [self.string_bank_shuffled[-1]] + self.string_bank_shuffled[:-1]
        return new_list

    def shift_list_positive_by_digit(self, n):
        new_list = []
        for x in range(n):
            new_list = [self.string_bank_shuffled[-1]] + self.string_bank_shuffled[:-1]
        return new_list

    def decrypt_text(self):

        return ""

    def encrypt_text(self):
        for level_itr in range(0, self.levels):
            output_encrypt, index_map = [], []
            for index, input_string in enumerate(self.text_body):
                cip_index = self.string_bank.index(str(input_string))
                index_map.append(cip_index)
                if level_itr == 0:
                    corresponding_letter = self.string_bank_shuffled[cip_index]
                else:
                    new_shuffled_list = self.shift_list_negative_by_digit(
                        self.string_bank_shuffled.index(self.encrypt_ext[:1])
                    )
                    corresponding_letter = new_shuffled_list[cip_index]
                output_encrypt.append(str(corresponding_letter))
            self.text_body = ''.join(output_encrypt)
            self.encrypt_ext += str(self.string_bank_shuffled[int(mean(index_map))])
            self.active_level = level_itr + 1
            if self.debug:
                print('Step ', self.get_text_info())
        self.active_level = self.levels
        return self.text_body.replace(' ', '\\') + self.encrypt_ext + self.text_length

    def greet(self):
        if self.debug:
            print('input_text', self.text)
            print('input_text length', len(self.text))
            print('input_text max level', self.levels)

iter_ = 1
print('processing....')
start_time = perf_counter()

while True:
    input_strings_ = ("Yazıyı kript enkript ederek son halinde, tekrar ilk haline getireceğim.! "
                      "Sonra da ciprx okuyacağız. Yazıyı kript enkript ederek son halinde, tekrar ilk haline getireceğim.! "
                      "Sonra da ciprx okuyacağız. Yazıyı kript enkript opğşöçxcpqpçpçq, tekrar ilk haline getireceğim.! "
                      "Sonra da ciprx okuyacağız. Yazıyı kript aklşsjkdlşaks  aklşklşka şlk ilk haline getireceğim.! "
                      "Sonra da ciprx okuyacağız. Yazıyı kript enkript ederek son halinde, tekrar ilk haline getireceğim.! "
                      "Sonra da ciprx okuyacağız.")
    new_encryption = KayCipherEncrypter(plain_text=input_strings_, encrypt_level=iter_, encrypt=True, debug=False)
    iter_ += 1

    if len(new_encryption.output) > 600:
        print(f'end_time {perf_counter() - start_time} ms')
        print(f'output level {iter_} | output {new_encryption.output}')
        # print(f'to bytes {str(new_encryption.output).encode()}')
        break

