import hashlib
import time
import matplotlib.pyplot as plt

# Funkcja generująca hash
def generate_hash(input_text, algorithm):
    hash_object = hashlib.new(algorithm)
    hash_object.update(input_text.encode('utf-8'))
    return hash_object.hexdigest()

# Funkcja mierząca czas generowania hash
def measure_time_avg(input_text, algorithm, repetitions):
    total_time = 0
    for _ in range(repetitions):
        start_time = time.time()
        generate_hash(input_text, algorithm)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / repetitions  # Zwraca średni czas


# Generowanie danych
inputs = {}


# Zakres 100-1500 co 100
for i in range(1000, 30000, 1000):
    inputs[str(i)] = "a" * i

# Lista algorytmów
algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']


# Wyniki czasów
results = {alg: [] for alg in algorithms}

# Mierzenie czasów dla każdego algorytmu i długości wejścia
for length, text in inputs.items():
    for alg in algorithms:
        avg_time = measure_time_avg(text, alg, 30) 
        results[alg].append(avg_time)

# Generowanie wykresów
plt.figure(figsize=(12, 8))
input_lengths = [int(length) for length in inputs.keys()]  # Konwersja kluczy na liczby

# Definicja stylów linii i znaczników
styles = ['-', '--', '-.', ':']
markers = ['o', 's', 'D', '^', 'v', 'p', '*', 'h', 'x', '+']
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

# Iteracja po algorytmach i przypisanie stylów
for idx, (alg, times) in enumerate(results.items()):
    style = styles[idx % len(styles)]  # Styl linii (cyklicznie)
    marker = markers[idx % len(markers)]  # Znacznik (cyklicznie)
    color = colors[idx % len(colors)]  # Kolor (cyklicznie)
    plt.plot(input_lengths, times, label=alg, linestyle=style, marker=marker, color=color)

plt.title("Porównanie szybkości funkcji skrótu (średnia z 10 pomiarów)")
plt.xlabel("Długość wejścia")
plt.ylabel("Średni czas (s)")
plt.legend(title="Algorytmy", loc="upper left", bbox_to_anchor=(1, 1))  # Legenda poza wykresem
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()  # Automatyczne dopasowanie elementów
plt.xlim(min(input_lengths), max(input_lengths))  # Zakres osi X
plt.savefig("e:\\studia\\krypto\\lab3\\hash_performance_avg.png")
plt.show()