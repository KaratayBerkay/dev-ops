import random
from random import choice
from time import perf_counter


class KayCipherEncrypter:

    def __init__(self, plain_text: str, encrypt_level: int = 1, encrypt: bool = True, debug=False):

        if not len(plain_text) > 0:
            raise Exception('Text length can not be less than 0...')

        self.debug = debug
        self.string_bank = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', '!',
            ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '}', '~', ' ', 'ı',
            'ü', 'ö', 'ç', 'ğ', 'ş', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '|', '’', '“', '”', '–'
        ]
        self.string_bank_shuffled = [
            '7', ',', 'j', 'I', 'ö', 'W', 'V', 'B', ':', 'E', 'b', 'v', '@', '1', '(', '~', 'D', 'Y', 'U', 'm', '*',
            '}', 'l', '“', 'h', 's', 'o', 'c', '+', 'g', '-', '9', '>', 'w', 'f', '_', ';', ')', 'ü', 'x', 'R', 'q',
            '[', '8', 'k', 'S', '$', '0', '.', '6', '&', 'u', 'r', 'A', '^', '?', '/', 'ç', ']', '’', 'Z', 'T', '{',
            '=', 'N', 'Q', 'ı', 'K', '`', '!', 'X', 'F', '4', 'H', 'C', 'L', '#', 'i', '"', '2', 'n', '<', 'ğ', 'd',
            "'", 'z', 'J', 'G', 'y', '3', '%', 'ş', 'e', 'a', 'M', 'p', '5', 'P', 'O', 't', '|', ' ', '”', '–'
        ]
        self.text = plain_text
        self.text_list = list(plain_text)
        self.levels = encrypt_level
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
            text_length_base = self.string_bank_shuffled[random.randrange(
                start=0, stop=len(self.string_bank_shuffled), step=10
            )] * 5
            for index, number in enumerate(''.join(list(reversed(list(str(len(self.text_list))))))):
                text_length_base = list(text_length_base)
                text_length_base[4 - index] = self.string_bank_shuffled[self.generate_random(int(number))]
            self.text_length = ''.join(text_length_base)
            self.text_body = self.text
            if self.debug:
                self.get_text_info()
            self.output = self.encrypt_text()
        else:
            decrypt_convert_reserved = self.text_list[len(self.text_list) - 5:]
            for letter in decrypt_convert_reserved:
                convert_length.append(str(self.read_random_number(self.string_bank_shuffled.index(letter))))
            self.text_length = int(''.join(convert_length))
            self.text_body = self.text[:self.text_length]
            self.encrypt_ext = self.text[self.text_length:len(self.text) - 5]
            self.output = self.decrypt_text()

    def get_text_info(self):
        print("active_level -> ", self.active_level, "output", self.text_body)

    def generate_random(self, st: int = 0):
        return random.randrange(start=st, stop=len(self.string_bank_shuffled), step=10)

    @staticmethod
    def read_random_number(st: int):
        return st % 10

    def shift_list_negative_by_digit(self, n):
        new_list = self.string_bank_shuffled
        for x in range(n):
            new_list = [new_list[-1]] + new_list[:-1]
        return new_list

    def decrypt_text(self):
        shift_number_list, index_map, layer, self.active_level = [], [], len(self.encrypt_ext), len(self.encrypt_ext)
        self.text_body = self.text_body.replace('\\', ' ')
        reversed_list = list(str(self.encrypt_ext[:-1]))
        for letter_ in reversed(reversed_list):
            shift_number_list.append(self.string_bank_shuffled.index(letter_))
        shift_number_list += [0]
        for index_shuffler, shuffler in enumerate(shift_number_list):
            output_encrypt = []
            new_shuffled_list = self.shift_list_negative_by_digit(shuffler)
            for index, input_string in enumerate(self.text_body):
                cip_index = new_shuffled_list.index(str(input_string))
                corresponding_letter = self.string_bank[cip_index]
                output_encrypt.append(str(corresponding_letter))
            self.text_body = ''.join(output_encrypt)
            self.active_level = self.active_level - 1
            if self.debug:
                self.get_text_info()
        self.active_level = self.levels
        return self.text_body

    def encrypt_text(self):
        for level_itr in range(0, self.levels):
            output_encrypt, index_map, corresponding_letter, new_shuffled_list = [], [], '', []
            if level_itr == 0:
                new_shuffled_list = self.string_bank_shuffled
            else:
                shuffled_index = self.string_bank_shuffled.index(self.encrypt_ext[-1])
                new_shuffled_list = self.shift_list_negative_by_digit(shuffled_index)

            for index, input_string in enumerate(self.text_body):
                cip_index = self.string_bank.index(str(input_string))
                index_map.append(cip_index)
                corresponding_letter = new_shuffled_list[cip_index]
                output_encrypt.append(str(corresponding_letter))
            self.text_body = ''.join(output_encrypt)
            # print('text_body', self.text_body)
            if int(choice(index_map)) < len(self.string_bank_shuffled):
                random_key = int(choice(index_map))
            else:
                random_key = random.randint(1, int(len(self.string_bank_shuffled) / 2))

            self.encrypt_ext += str(self.string_bank_shuffled[random_key])
            self.active_level = level_itr + 1
            if self.debug:
                self.get_text_info()
        self.active_level = self.levels
        return self.text_body.replace(' ', '\\') + self.encrypt_ext + self.text_length


start_time = perf_counter()
encryption_strings = """
Wondering what to do with your new Viking name?
Well, wonder no more! With our Viking Name Generator, you’re just a click away from discovering your epic Norse alter ego. What comes next, now that you’ve generated a name you’re proud of? Fear not! We’ve crafted a delightful list of amusing and slightly mischievous ways you can use your newfound Viking name in everyday life. From jazzing up your coffee runs to conquering the digital realms, these ideas are sure to add a splash of Viking fun to your day. Read on and let the adventures of “you-the-Viking” begin!

Conquer Your Coffee: Demand your local barista write your Viking name on your morning cup. Who needs “Bob” when you can be “Erik Bloodaxe”?
Redefine Your Wi-Fi: Rename your Wi-Fi network to something like “ValhallaNet” or “Odin’s Online Oasis” – neighbors will think twice before trying to connect!
Alter Ego for Gaming: Dominate online games with a name that screams Viking warrior. Other players will know “Thor Thunderfist” means business.
Spice Up Book Club: Suggest a Norse saga for your next read and introduce yourself with your Viking name. Watch as Mildred becomes “Mildred the Merciless”.
Revamp Social Media: Update your profiles with your Viking name for a day. Watch as friends try to pronounce “Gunnar Gobletbreaker”.
Mighty Grocery Shopping: Tackle the grocery store aisles as “Helga Honey-Mead” or “Sven Sword-Seeker”. May the odds of finding good deals be ever in your favor.
Work Email Signature: Sign off your emails with your Viking name for a day. “Best regards, Astrid Axewielder, Regional Manager”.
Theme Dinner Nights: Host a Viking-themed dinner where everyone must address each other by their Viking names. “Pass the salt, Bjorn Battleborn!”
Viking Holiday Cards: Send out your holiday greetings from “The Erikson Clan: Leif, Lara, and little Loki Lightfoot”.
Craft Beer Critic: Rate and review craft beers under your Viking pseudonym. “Gorm Grog-Guzzler gives this IPA four horned helmets out of five”.
Unleashed your inner Viking and found a clever way to use your new Norse name? Share your most creative exploits with us – we’d love to hear how you’re channeling your inner Viking! Leave us a comment below.

Wondering what to do with your new Viking name?
Well, wonder no more! With our Viking Name Generator, you’re just a click away from discovering your epic Norse alter ego. What comes next, now that you’ve generated a name you’re proud of? Fear not! We’ve crafted a delightful list of amusing and slightly mischievous ways you can use your newfound Viking name in everyday life. From jazzing up your coffee runs to conquering the digital realms, these ideas are sure to add a splash of Viking fun to your day. Read on and let the adventures of “you-the-Viking” begin!

Conquer Your Coffee: Demand your local barista write your Viking name on your morning cup. Who needs “Bob” when you can be “Erik Bloodaxe”?
Redefine Your Wi-Fi: Rename your Wi-Fi network to something like “ValhallaNet” or “Odin’s Online Oasis” – neighbors will think twice before trying to connect!
Alter Ego for Gaming: Dominate online games with a name that screams Viking warrior. Other players will know “Thor Thunderfist” means business.
Spice Up Book Club: Suggest a Norse saga for your next read and introduce yourself with your Viking name. Watch as Mildred becomes “Mildred the Merciless”.
Revamp Social Media: Update your profiles with your Viking name for a day. Watch as friends try to pronounce “Gunnar Gobletbreaker”.
Mighty Grocery Shopping: Tackle the grocery store aisles as “Helga Honey-Mead” or “Sven Sword-Seeker”. May the odds of finding good deals be ever in your favor.
Work Email Signature: Sign off your emails with your Viking name for a day. “Best regards, Astrid Axewielder, Regional Manager”.
Theme Dinner Nights: Host a Viking-themed dinner where everyone must address each other by their Viking names. “Pass the salt, Bjorn Battleborn!”
Viking Holiday Cards: Send out your holiday greetings from “The Erikson Clan: Leif, Lara, and little Loki Lightfoot”.
Craft Beer Critic: Rate and review craft beers under your Viking pseudonym. “Gorm Grog-Guzzler gives this IPA four horned helmets out of five”.

Wondering what to do with your new Viking name?
Well, wonder no more! With our Viking Name Generator, you’re just a click away from discovering your epic Norse alter ego. What comes next, now that you’ve generated a name you’re proud of? Fear not! We’ve crafted a delightful list of amusing and slightly mischievous ways you can use your newfound Viking name in everyday life. From jazzing up your coffee runs to conquering the digital realms, these ideas are sure to add a splash of Viking fun to your day. Read on and let the adventures of “you-the-Viking” begin!

Conquer Your Coffee: Demand your local barista write your Viking name on your morning cup. Who needs “Bob” when you can be “Erik Bloodaxe”?
Redefine Your Wi-Fi: Rename your Wi-Fi network to something like “ValhallaNet” or “Odin’s Online Oasis” – neighbors will think twice before trying to connect!
Alter Ego for Gaming: Dominate online games with a name that screams Viking warrior. Other players will know “Thor Thunderfist” means business.
Spice Up Book Club: Suggest a Norse saga for your next read and introduce yourself with your Viking name. Watch as Mildred becomes “Mildred the Merciless”.
Revamp Social Media: Update your profiles with your Viking name for a day. Watch as friends try to pronounce “Gunnar Gobletbreaker”.
Mighty Grocery Shopping: Tackle the grocery store aisles as “Helga Honey-Mead” or “Sven Sword-Seeker”. May the odds of finding good deals be ever in your favor.
Work Email Signature: Sign off your emails with your Viking name for a day. “Best regards, Astrid Axewielder, Regional Manager”.
Theme Dinner Nights: Host a Viking-themed dinner where everyone must address each other by their Viking names. “Pass the salt, Bjorn Battleborn!”
Viking Holiday Cards: Send out your holiday greetings from “The Erikson Clan: Leif, Lara, and little Loki Lightfoot”.
Craft Beer Critic: Rate and review craft beers under your Viking pseudonym. “Gorm Grog-Guzzler gives this IPA four horned helmets out of five”.

Wondering what to do with your new Viking name?
Well, wonder no more! With our Viking Name Generator, you’re just a click away from discovering your epic Norse alter ego. What comes next, now that you’ve generated a name you’re proud of? Fear not! We’ve crafted a delightful list of amusing and slightly mischievous ways you can use your newfound Viking name in everyday life. From jazzing up your coffee runs to conquering the digital realms, these ideas are sure to add a splash of Viking fun to your day. Read on and let the adventures of “you-the-Viking” begin!

Conquer Your Coffee: Demand your local barista write your Viking name on your morning cup. Who needs “Bob” when you can be “Erik Bloodaxe”?
Redefine Your Wi-Fi: Rename your Wi-Fi network to something like “ValhallaNet” or “Odin’s Online Oasis” – neighbors will think twice before trying to connect!
Alter Ego for Gaming: Dominate online games with a name that screams Viking warrior. Other players will know “Thor Thunderfist” means business.
Spice Up Book Club: Suggest a Norse saga for your next read and introduce yourself with your Viking name. Watch as Mildred becomes “Mildred the Merciless”.
Revamp Social Media: Update your profiles with your Viking name for a day. Watch as friends try to pronounce “Gunnar Gobletbreaker”.
Mighty Grocery Shopping: Tackle the grocery store aisles as “Helga Honey-Mead” or “Sven Sword-Seeker”. May the odds of finding good deals be ever in your favor.
Work Email Signature: Sign off your emails with your Viking name for a day. “Best regards, Astrid Axewielder, Regional Manager”.
Theme Dinner Nights: Host a Viking-themed dinner where everyone must address each other by their Viking names. “Pass the salt, Bjorn Battleborn!”
Viking Holiday Cards: Send out your holiday greetings from “The Erikson Clan: Leif, Lara, and little Loki Lightfoot”.
Craft Beer Critic: Rate and review craft beers under your Viking pseudonym. “Gorm Grog-Guzzler gives this IPA four horned helmets out of five”.
"""
print('encryption_strings')
# print(encryption_strings)
print(len(encryption_strings))
encryption_strings = encryption_strings.replace("\n", "")
encryption_strings = encryption_strings.replace('\\', "")

print('input', encryption_strings)
new_encryption = KayCipherEncrypter(plain_text=encryption_strings, encrypt_level=447, encrypt=True, debug=False)
new_decryption = KayCipherEncrypter(plain_text=new_encryption.output, encrypt_level=447, encrypt=False, debug=False)
print('output', new_decryption.output)

print('Total time : ', perf_counter() - start_time)
