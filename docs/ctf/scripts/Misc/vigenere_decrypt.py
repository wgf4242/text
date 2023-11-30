
def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ""

    key_index = 0
    for char in ciphertext:
        if char.upper() in alphabet:
            shift = alphabet.find(key[key_index % len(key)].upper())
            decrypted_char_index = (alphabet.find(char.upper()) - shift) % len(alphabet)
            decrypted_text += alphabet[decrypted_char_index]

            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

def main():
    with open("a.txt", "r") as file:
        ciphertext = file.read()

    with open("b.txt", "r") as file:
        keys = file.readlines()

    with open("c.txt", "w") as output_file:
        for key in keys:
            decrypted_text = vigenere_decrypt(ciphertext, key.strip())
            #output_file.write(f"Key: {key.strip()}\n")
            output_file.write(f"{decrypted_text}\n")
            output_file.write("\n")

if __name__ == "__main__":
    main()


# b = vigenere_decrypt('rla xymijgpf ppsoto wq u nncwel ff tfqlgnxwzz sgnlwduzmy vcyg ib bhfbe u tnaxua ff satzmpibf vszqen eyvlatq cnzhk dk hfy mnciuzj ou s yygusfp bl dq e okcvpa hmsz vi wdimyfqqjqubzc hmpmbgxifbgi qs lciyaktb jf clntkspy drywuz wucfm', 'YEWCQGEWCYBNHDHPXOYUBJJPQIRAPSOUIYEOMTSV')
# print(b)
