class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст 
        # с учетом переданного смещения shift.
        text_lower = str.lower(original_text)
        changed_text = ''
        for symbol in text_lower:
            if symbol in self.alphabet:
                if str.find(self.alphabet, symbol) + shift <= len(self.alphabet) - 1:
                    changed_text += self.alphabet[str.find(self.alphabet, symbol) + shift]
                else:
                    changed_text += self.alphabet[str.find(self.alphabet, symbol) + shift - len(self.alphabet)]
            else:
                changed_text += symbol
        return changed_text
    
    
    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        text_lower = str.lower(cipher_text)
        changed_text = ''
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



cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))

print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))