angka= int(input('Masukkan angka: '))

listAngka = ['Bulat']

def bilangan():
    if angka < 0: 
        listAngka.append('Negatif')
    elif angka >= 0:
        listAngka.append('Cacah')
        if angka == 0:
            listAngka.append('Nol')
        elif angka >= 1:
            listAngka.append('Asli')
            if angka % 2 == 0:
                listAngka.append('Genap')
            elif angka % 2 != 0:
                listAngka.append('Ganjil')
            if angka > 1:
                for i in range(2, angka):
                    if (angka % i) == 0:
                        listAngka.append ('Komposit')
                        break
                else:
                    return listAngka.append ('Prima')
            else:
                return listAngka.append ('Komposit')    
        print('Termasuk bilangan : ' , listAngka)

bilangan()
            


