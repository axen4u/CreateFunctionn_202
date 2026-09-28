import math

# Fungsi konversi suhu Celsius <-> Fahrenheit
def konversi_suhu(nilai, satuan):
    # Validasi satuan input
    if satuan not in ['C', 'F']:
        return "Error: Satuan harus 'C' atau 'F'"
    
    # Jika satuan C, konversi ke Fahrenheit
    if satuan == 'C':
        hasil = (nilai * 9/5) + 32
        return hasil
    
    # Jika satuan F, konversi ke Celsius
    else:
        hasil = (nilai - 32) * 5/9
        return hasil


# Fungsi hitung luas lingkaran menggunakan lambda
hitung_luas_lingkaran = lambda r: math.pi * r * r


# === TUGAS 1: Konversi Suhu ===
print("=== KONVERSI SUHU ===")
try:
    # Minta input dari user
    suhu_input = input("Masukkan nilai suhu: ")
    nilai_suhu = float(suhu_input)
    
    satuan_input = input("Masukkan satuan (C/F): ")
    satuan = satuan_input.upper()  # Ubah ke huruf besar
    
    # Panggil fungsi konversi
    hasil = konversi_suhu(nilai_suhu, satuan)
    
    # Tampilkan hasil
    if isinstance(hasil, str):  # Jika hasilnya string error
        print(hasil)
    else:
        if satuan == 'C':
            print(f"{nilai_suhu}°C = {hasil:.2f}°F")
        else:
            print(f"{nilai_suhu}°F = {hasil:.2f}°C")

except ValueError:
    print("Error: Input nilai suhu harus berupa angka!")


# === TUGAS 2: Luas Lingkaran ===
print("\n=== LUAS LINGKARAN ===")
try:
    # Minta input jari-jari dari user
    jari_jari_input = input("Masukkan jari-jari lingkaran: ")
    jari_jari = float(jari_jari_input)
    
    # Panggil fungsi lambda
    luas = hitung_luas_lingkaran(jari_jari)
    
    # Tampilkan hasil
    print(f"Jari-jari: {jari_jari} cm")
    print(f"Luas lingkaran: {luas:.2f} cm²")

except ValueError:
    print("Error: Input jari-jari harus berupa angka!")
