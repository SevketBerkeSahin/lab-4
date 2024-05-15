import random

# Rastgele sayılar içeren bir liste oluştur
lst = []
for i in range(10):
    number = random.randint(0, 101)
    lst.append(number)
print("lst = ", lst)

# Listeyi dosyaya yaz
with open('file.txt', 'w') as f:
    f.write(str(len(lst)) + '\n')
    for i in lst:
        f.write(str(i) + ' ')
    f.write('\n')

# Dosyayı okuyarak tek sayıları bul ve 2 katına çıkar
with open('file.txt', 'r') as f:
    s = f.readline()
    lst2 = []
    for line in f:
        strs = line.split(' ')
        print('strs =', strs)
        for s in strs:
            if s.strip():  # Boş stringleri atla
                lst2.append(int(s))
print('lst2 =', lst2)

# Tek sayıları 2 katına çıkar ve yeni listeye ekle
odd_numbers_doubled = []
for x in lst2:
    if x % 2 != 0:
        odd_numbers_doubled.append(x * 2)
print('Tek sayıların 2 katı:', odd_numbers_doubled)

# 2 katına çıkarılmış tek sayıların toplamını hesapla
sum_of_doubled_odds = sum(odd_numbers_doubled)

# Yeni dosyaya yaz
with open('new_file.txt', 'w') as f:
    f.write(str(len(odd_numbers_doubled)) + '\n')
    for i in odd_numbers_doubled:
        f.write(str(i) + ' ')
    f.write('\nCem: ' + str(sum_of_doubled_odds))

# Sonuçları yazdır
print("Tek sayıların 2 katına çıkarılmış halleri:", odd_numbers_doubled)
print("Tek sayıların 2 katına çıkarılmış hallerinin cemi:", sum_of_doubled_odds)
