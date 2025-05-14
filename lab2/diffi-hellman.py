import random

def diffie_hellman(n, g):
    """
    Implementacja algorytmu Diffiego-Hellmana.
    :param n: Liczba pierwsza (modulo)
    :param g: Pierwiastek pierwotny modulo n
    :return: Klucz sesji k
    """
    # Krok 2: A wybiera losową liczbę x (klucz prywatny A)
    x = random.randint(2, n - 2)
    X = pow(g, x, n)  # X = g^x mod n

    # Krok 3: B wybiera losową liczbę y (klucz prywatny B)
    y = random.randint(2, n - 2)
    Y = pow(g, y, n)  # Y = g^y mod n

    # Krok 4: Wymiana kluczy publicznych (X i Y)
    # Krok 5: A oblicza klucz sesji k = Y^x mod n
    k_A = pow(Y, x, n)

    # Krok 6: B oblicza klucz sesji k = X^y mod n
    k_B = pow(X, y, n)

    # Klucze k_A i k_B powinny być identyczne
    assert k_A == k_B, "Klucze sesji nie są zgodne!"

    return k_A

if __name__ == "__main__":
    # Duża liczba pierwsza n i pierwiastek pierwotny g
    n = 23  # Przykładowa liczba pierwsza
    g = 5   # Przykładowy pierwiastek pierwotny modulo n

    klucz_sesji = diffie_hellman(n, g)
    print(f"Uzgodniony klucz sesji: {klucz_sesji}")


#     2. Ograniczenia dla użytych parametrów
# Liczba pierwsza n: Powinna być wystarczająco duża, aby zapewnić bezpieczeństwo. W praktyce stosuje się liczby pierwsze o długości co najmniej 2048 bitów.
# Pierwiastek pierwotny g: Musi być pierwiastkiem pierwotnym modulo n, co oznacza, że generuje wszystkie liczby od 1 do n-1 w grupie multiplikatywnej modulo n. Wybór niewłaściwego g może osłabić bezpieczeństwo.
# Losowe liczby prywatne x i y: Powinny być wystarczająco duże i generowane w sposób kryptograficznie bezpieczny. Użycie funkcji random.randint może być niewystarczające, ponieważ nie jest to generator kryptograficznie bezpieczny.

# 3. Dane, które można podsłuchać i potencjalny schemat ataku
# Dane możliwe do podsłuchania:

# Liczby publiczne X = g^x mod n i Y = g^y mod n, które są wymieniane między stronami.
# Parametry n i g, które są uzgadniane jawnie.
# Schemat ataku:
# Atak man in the middle: Atakujący może przechwycić komunikację między stronami A i B, a następnie podszyć się pod każdą z nich. Atakujący generuje własne klucze publiczne i prywatne, a następnie negocjuje dwa różne klucze sesji z A i B. W ten sposób atakujący może odszyfrować i zmodyfikować przesyłane dane.


# Atak bruteforce: Jeśli n jest małe, atakujący może próbować odgadnąć x lub y poprzez obliczenie dyskretnego logarytmu X = g^x mod n lub Y = g^y mod n. Dla małych wartości n jest to wykonalne.
# Oraz jeśli g nie jest pierwiastkiem pierwotnym lub n nie jest liczbą pierwszą, może to prowadzić do osłabienia bezpieczeństwa i umożliwić atakującemu odgadnięcie klucza sesji.

# Wnioski:
# Diffie-Hellman sam w sobie nie zapewnia uwierzytelnienia, co czyni go podatnym na ataki MITM.
# Algorytm wymaga bezpiecznego wyboru parametrów i implementacji, aby był odporny na ataki.