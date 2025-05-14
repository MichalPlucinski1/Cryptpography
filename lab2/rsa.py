import random 

from sympy import isprime 

from math import gcd 

 

def generate_prime(min, max): 

    while True: 

        # Generuj losową 4-cyfrową liczbę 

        num = random.randint(min, max) 

        # Sprawdź, czy liczba jest pierwsza 

        if isprime(num): 

            return num 


def generate_e(phi): 

    while True: 

        # Generuj losową liczbę mniejszą od phi 

        e = random.randint(2, phi - 1) 

        # Sprawdź, czy gcd(e, phi) == 1 i czy e jest liczbą pierwszą 

        if gcd(e, phi) == 1 and isprime(e): 

            return e 

def generate_d(e, phi): 

    # Znajdź d jako odwrotność modularną e względem phi 

    d = pow(e, -1, phi)  # Funkcja pow z trzema argumentami oblicza odwrotność modularną 

    return d 


def encrypt_message(m, e, n): 

    """ 

    Szyfrowanie wiadomości. 

    :param m: Wiadomość jawna (liczba całkowita) 

    :param e: Klucz publiczny (eksponent) 

    :param n: Klucz publiczny (moduł) 

    :return: Zaszyfrowana wiadomość (liczba całkowita) 

    """ 

    c = pow(m, e, n)  # c = m^e mod n 

    return c 


def decrypt_message(c, d, n): 

    """ 

    Deszyfrowanie wiadomości. 

    :param c: Zaszyfrowana wiadomość (liczba całkowita) 

    :param d: Klucz prywatny (eksponent) 

    :param n: Klucz prywatny (moduł) 

    :return: Odszyfrowana wiadomość (liczba całkowita) 

    """ 

    m = pow(c, d, n)  # m = c^d mod n 

    return m 

def generate_keys(p, q): 

    """ 

    Generuje klucz publiczny i klucz prywatny. 

    :return: Słownik zawierający klucz publiczny i klucz prywatny. 

    """ 

    # Obliczanie modułu n i funkcji Eulera phi 

    n = p * q 

    phi = (p - 1) * (q - 1) 

 
 

    # Generowanie eksponenta klucza publicznego e 

    e = generate_e(phi) 

 
 

    # Generowanie eksponenta klucza prywatnego d 

    d = generate_d(e, phi) 

 
 

    # Klucz publiczny: (e, n), klucz prywatny: (d, n) 

    public_key = (e, n) 

    private_key = (d, n) 

 
 

    return {"public_key": public_key, "private_key": private_key} 

 
 
 
p = generate_prime() 

q = generate_prime() 



keys = generate_keys(p, q) 

print("Klucz publiczny:", keys["public_key"]) 

print("Klucz prywatny:", keys["private_key"]) 


# message = "To jest przykładowa wiadomość o długości 50 znaków.".ljust(50)  # Dopasowanie długości do 50 znaków
message = 'Tojestprzykladowa'
message_as_int = int.from_bytes(message.encode('utf-8'), byteorder='big')
print("Wiadomość jako liczba całkowita:", message_as_int)
encrypt_message = encrypt_message(message_as_int, keys["public_key"][0], keys["public_key"][1])
print("Zaszyfrowana wiadomość:", encrypt_message)

decrypt_message = decrypt_message(encrypt_message, keys["private_key"][0], keys["private_key"][1])
print("Odszyfrowana wiadomość:", decrypt_message)

message_decoded = decrypt_message.to_bytes((decrypt_message.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
 
print("Odszyfrowana wiadomość jako tekst:", message_decoded)

# # Szyfrowanie wiadomości
# encrypted_message = encrypt_message(message_as_int, keys["public_key"][0], keys["public_key"][1])
# print("Zaszyfrowana wiadomość:", encrypted_message)

# # Deszyfrowanie wiadomości
# decrypted_message_as_int = decrypt_message(encrypted_message, keys["private_key"][0], keys["private_key"][1])

# # Zamiana odszyfrowanej liczby całkowitej z powrotem na tekst
# decrypted_message = decrypted_message_as_int.to_bytes((decrypted_message_as_int.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
# print("Odszyfrowana wiadomość:", decrypted_message)

# p = 31 

# q = 19 

# Generowanie dwóch 4-cyfrowych liczb pierwszych 

# p = generate_prime() 

# q = generate_prime() 

 
 
 

# n = p * q # klucz publiczny moduł 

 
 

# phi = (p - 1) * (q - 1) # 540 

 
 

# e=generate_e(phi) # eksponent klucza publicznego 

 
 

# d = generate_d(e, phi) 

 
 
 
 
 
 
 

# # Przykład użycia 

# m = 8  # Wiadomość jawna 

# e = 7  # Klucz publiczny (eksponent) 

# n = 589  # Klucz publiczny (moduł) 

# d = 463  # Klucz prywatny (eksponent) 

 
 

# # Szyfrowanie 

# c = encrypt_message(m, e, n) 

# print("Zaszyfrowana wiadomość:", c) 

 
 

# # Deszyfrowanie 

# decoded_m = decrypt_message(c, d, n) 

# print("Odszyfrowana wiadomość:", decoded_m) 

 