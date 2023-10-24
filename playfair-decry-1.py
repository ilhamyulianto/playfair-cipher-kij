import string

def key_generation(key):
    # Inisialisasi main matrix tanpa huruf 'j'
    main = string.ascii_lowercase.replace('j', '.')
    key = key.lower()
    
    # Inisialisasi matriks kunci
    key_matrix = ['' for i in range(5)]
    i = 0
    j = 0
    
    for c in key:
        if c in main:
            key_matrix[i] += c
            main = main.replace(c, '.')
            j += 1

            if j > 4:
                i += 1
                j = 0

    for c in main:
        if c != '.':
            key_matrix[i] += c

            j += 1
            if j > 4:
                i += 1
                j = 0
                
    return key_matrix

def conversion(cipher_text):
    plain_text_pairs = []
    cipher_text_pairs = []

    cipher_text = cipher_text.lower()

    i = 0
    while i < len(cipher_text):
        a = cipher_text[i]
        b = cipher_text[i+1]

        cipher_text_pairs.append(a + b)

        i += 2
            
    print("Pasangan Teks Sandi: ", cipher_text_pairs)

    for pair in cipher_text_pairs:
        flag = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                plain_text_pair = row[(j0+4)%5] + row[(j1+4)%5]
                plain_text_pairs.append(plain_text_pair)
                flag = True
        if flag:
            continue
        
        for j in range(5):
            col = "".join([key_matrix[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])
                plain_text_pair = col[(i0+4)%5] + col[(i1+4)%5]
                plain_text_pairs.append(plain_text_pair)
                flag = True
        if flag:
            continue
        
        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0

        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])
        plain_text_pair = key_matrix[i0][j1] + key_matrix[i1][j0]
        plain_text_pairs.append(plain_text_pair)
        
    print("Pasangan Teks Biasa: ", plain_text_pairs)
    
    print('Teks Sandi: ', "".join(cipher_text_pairs))
    print('Teks Biasa (pesan): ', "".join(plain_text_pairs))

# Input dari pengguna untuk kunci dan teks terenkripsi
key = input("Masukan kata kunci: ")

# Menghasilkan matriks kunci
key_matrix = key_generation(key)
print("Matriks Kunci untuk enkripsi:")
print(key_matrix)

cipher_text = input("Masukan pesan terenkripsi: ")

# Memanggil fungsi konversi dengan teks terenkripsi
conversion(cipher_text)
