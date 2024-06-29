class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def process_text(self, text, shift, is_encrypt):
        text_lower = str.lower(text)
        changed_text = ''
        if is_encrypt:
            for symbol in text_lower:
                if symbol in self.alphabet:
                    if str.find(self.alphabet, symbol) + shift <= len(self.alphabet) - 1:
                        changed_text += self.alphabet[str.find(self.alphabet, symbol) + shift]
                    else:
                        changed_text += self.alphabet[str.find(self.alphabet, symbol) + shift - len(self.alphabet)]
                else:
                    changed_text += symbol
        else:
            for symbol in text_lower:
                if symbol in self.alphabet and shift > 0:
                    if str.find(self.alphabet, symbol) - shift >= 0:
                        changed_text += self.alphabet[str.find(self.alphabet, symbol) - shift]
                    else:
                        changed_text += self.alphabet[str.find(self.alphabet, symbol) - shift + len(self.alphabet)]
                elif symbol in self.alphabet and shift < 0:
                    module_shift = shift * (-1)
                    if str.find(self.alphabet, symbol) + module_shift <= len(self.alphabet) - 1:
                        changed_text += self.alphabet[str.find(self.alphabet, symbol) + module_shift]
                    else:
                        changed_text += self.alphabet[str.find(self.alphabet, symbol) + module_shift - len(self.alphabet)]
                else:
                    changed_text += symbol
        return changed_text


# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))