from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import time

def encrypt_decrypt(mode, key, iv, data, operation):
    cipher = Cipher(algorithms.AES(key), mode, backend=default_backend())
    if operation == "encrypt":
        encryptor = cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize()
    elif operation == "decrypt":
        decryptor = cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()

def measure_time(mode, key, iv, data):
    start = time.time()
    encrypted = encrypt_decrypt(mode, key, iv, data, "encrypt")
    encryption_time = time.time() - start

    start = time.time()
    decrypted = encrypt_decrypt(mode, key, iv, encrypted, "decrypt")  # Fixed function call
    decryption_time = time.time() - start

    return encryption_time, decryption_time

file_sizes = [64, 256, 512, 1024, 2048 ,10240, 102400, 1024000, 1024*10000]  # Sizes in bytes (1 KB, 10 KB, 100 KB)
test_files = []

for size in file_sizes:
    test_files.append(os.urandom(size))



key = os.urandom(32)  # 256-bit key
iv = os.urandom(16)   # 128-bit IV

modes_list = [
    modes.ECB(),
    modes.CBC(iv),
    modes.OFB(iv),
    modes.CFB(iv),
    modes.CTR(iv)
]
n = 5  # Number of repetitions for each test

results = {}

for mode in modes_list:
    mode_name = mode.__class__.__name__
    results[mode_name] = []
    for data in test_files:
        total_enc_time = 0
        total_dec_time = 0
        for _ in range(n):  # Repeat the test n times
            enc_time, dec_time = measure_time(mode, key, iv, data)
            total_enc_time += enc_time
            total_dec_time += dec_time
        # Calculate average times
        avg_enc_time = total_enc_time / n
        avg_dec_time = total_dec_time / n
        results[mode_name].append((avg_enc_time, avg_dec_time))
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(16, 6))  # Create two subplots side by side

# Wykres dla szyfrowania (Encryption)
axes[0].set_title("Average Encryption Times for Block Cipher Modes")
for mode_name, times in results.items():
    enc_times, _ = zip(*times)
    axes[0].plot(file_sizes, enc_times, label=f"{mode_name} Encryption")
axes[0].set_xlabel("File Size (bytes)")
axes[0].set_ylabel("Time (seconds)")
axes[0].set_xscale("log")  # Opcjonalnie: skala logarytmiczna dla osi X
axes[0].legend()
axes[0].grid(True)

# Wykres dla deszyfrowania (Decryption)
axes[1].set_title("Average Decryption Times for Block Cipher Modes")
for mode_name, times in results.items():
    _, dec_times = zip(*times)
    axes[1].plot(file_sizes, dec_times, label=f"{mode_name} Decryption")
axes[1].set_xlabel("File Size (bytes)")
axes[1].set_ylabel("Time (seconds)")
axes[1].set_xscale("log")  # Opcjonalnie: skala logarytmiczna dla osi X
axes[1].legend()
axes[1].grid(True)



plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()