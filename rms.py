#RUMAH SAKIT
listPasien = [
{   'kode' : 'PS001',
    'nama' : 'Taufik',
    'ruangan' : 'RM001',
    'alamat' : 'Pater',
    'umur' : 30,
    'status' : 'Dirawat'
},

{  'kode' : 'PS002',
    'nama' : 'Risang',
    'ruangan' : 'RM002',
    'alamat' : 'Cengek',
    'umur' : 31,
    'status' : 'Dirawat'
},

{  'kode' : 'PS003',
    'nama' : 'Dono',
    'ruangan' : 'RM003',
    'alamat' : 'Ambar',
    'umur' : 32,
    'status' : 'Dirawat'
}
]

trash = []

def keputusan(data,aksi,pesan):
    checker = input(f"Mau {pesan} Y jika tidak N ? (Y/N) =").upper()
    
    if(checker == 'N'):
        print(f"Data tidak Jadi di {pesan}")
        return 0
    if(aksi == 'input' and checker == 'Y'):
        print("======       Data Tersimpan      ======")
        listPasien.append(data)
        return 1
    if aksi == 'update' and checker == 'Y':
        print("===========      Data Pasien Terupdate      ==============")
        listPasien.pop(data['index'])
        listPasien.insert(data['index'],data['data'])
        return 1

    keputusan(data,aksi,pesan)

def cariIndex(dataBaru):
    for i in range(len(listPasien)):
        if listPasien[i]['kode'] == dataBaru:
            return i
    return -1

def printsampah(data2):
    print("Daftar Pasien Pulang\n")
    print("Kode\t\t|Nama\t\t|Ruangan\t|Alamat\t\t|Umur\t\t|Status")
    for i in range(len(data2)):
        print("{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}".format(  data2[i]['kode'], data2[i]['nama'], data2[i]['ruangan'], data2[i]['alamat'], data2[i]['umur'], data2[i]['status']))

def printing(data1):
    print("Kode\t\t|Nama\t\t|Ruangan\t|Alamat\t\t|Umur\t\t|Status")
    print("{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}".format( data1['kode'], data1['nama'], data1['ruangan'], data1['alamat'], data1['umur'], data1['status']))

def tampilan(pasien = listPasien):
    print("Daftar Pasien\n")
    print("Index\t\t|Kode\t\t|Nama\t\t|Ruangan\t|Alamat\t\t|Umur\t\t|Status")
    for i in range(len(pasien)):
        print("{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}".format(i+1, pasien[i]['kode'], pasien[i]['nama'], pasien[i]['ruangan'], pasien[i]['alamat'], pasien[i]['umur'], pasien[i]['status']))

def menampilkanDaftarPasien():
    while True:
        print('''
                1. Melihat Daftar Seluruh Pasien
                2. Melihat Nama Pasien Melalui Kode
                3. Kembali ke Menu Utama
                ''')
        a = input("Masukan angka 1 sampe  3: ")
        if(a == '1'):
            tampilan()
        if(a == '2'):
            cariKode = input('Masukkan Kode Pasien :').upper()
            index = cariIndex(cariKode)
            if index != -1:
                data = listPasien[index]
                printing(data)
        if(a == '3'):
            break

def menambahPasien():
    tampilan()
    while True:
        print('''
                1. Pasien Check IN
                2. Kembali ke Menu Utama
                ''')
        a = input("Masukan angka 1 atau 2: ")
        if(a == '1'):
            tambah_kode = input('Masukkan Kode Pasien :').upper()
            index = cariIndex(tambah_kode)
            # print(index)
            if index != -1:
                print('=============== Pasien Yang Ingin Di tambah Sudah ada =================')
                continue
            tambah_nama = (input('Masukkan Nama Pasien :')).capitalize()
            tambah_ruangan = (input('Masukkan Ruangan :')).upper() 
            tambah_alamat = (input('Masukkan Alamat :')).capitalize() 
            tambah_umur = int(input('Masukkan Umur :'))
            tambah_status = input('Masukkan Status Pasien :').capitalize()
            temporary_table = {
                    'kode' : tambah_kode,
                    'nama' : tambah_nama,
                    'ruangan' :tambah_ruangan,
                    'alamat' : tambah_alamat,
                    'umur' : tambah_umur,\
                    'status' : tambah_status}
            res = keputusan(temporary_table,'input','tambah')
            if  res :
                break
        if(a == '2'):
            break

def mengeditPasien():
    
    while True:
        tampilan() 
        print('''
                1. Edit Nama
                2. Edit Ruangan
                3. Edit Alamat
                4. Edit Umur
                5. Edit Status
                6. KELUAR
                ''')
        a = input("Piliha 1 - 6: ")
        pilihan = {
            '1' : 'nama',
            '2' : 'ruangan',
            '3' : 'alamat',
            '4' : 'umur',
            '5' : 'status'
        }
        if a == '6':
            break
        dataBaru = str(input('Masukkan Kode Pasien :')).upper()
        index = cariIndex(dataBaru)
        if index == -1 :
            print("Data Yang Di Cari tidak ada")
            continue
        ubahke = input(f"Ubah {pilihan[a]} Menjadi: ").capitalize()
        temp = {
            'index' : index,
            'data'  : listPasien[index].copy()

        }
        temp['data'][pilihan[a]] = ubahke
        res = keputusan(temp,'update','perbarui')
        # if res:
        #     tampilan()
        #     break

def mengHapusPasien():
    while True:
        tampilan()
        print('''
                1. Hapus Data Pasien
                2. Kembali ke Menu Utama
                ''')
        a = input("Masukan angka 1 atau 2: ")
        if(a == '1'):
            tambah_kode = input('Masukkan Kode Pasien :').upper()
            index = cariIndex(tambah_kode)
            if index == -1:
                print('=============== Pasien Yang Ingin Di Check Out Tidak Ada Sudah ada =================')
                continue
            # hapus_index = int(input("Masukkan Index yang ingin di Hapus : "))
            while True:  
                checker = str(input("Yakin Di HAPUS Y/N : ")).upper()
                if(checker == 'Y'):
                    print("Data Pasien Telah Terhapus")
                    print("=====================================")
                    trash.append(listPasien.pop(index))
                    
                    break
                    
                if(checker == 'N'):
                    print("Gak jadi di hapus")
                    print("=====================================")
                    
                    break
                
        elif('2' == a):
            break
def cekHistoryPasien():
    print('''
        Pasien yang telah pulang dan Sehat
       ''')
    sampah =  trash
    for i in range(len(sampah)):
        sampah[-1*i]['status'] = 'Pulang'
        
    printsampah(sampah)

while True:
    pilihanmenu = input('''
        Selamat Datang RSM ( RUMAH SAKIT MARKENJI )

        list Menu :
        1. Melihat Daftar Pasien
        2. Pasien Check IN
        3. Mengedit Data Pasien
        4. Pasien Check OUT
        5. Cek History Kunjungan Pasien
        6. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')
    if(pilihanmenu == '1'):
        menampilkanDaftarPasien()
    elif(pilihanmenu == '2'):
        menambahPasien()
    elif(pilihanmenu == '3'):
        mengeditPasien()
    elif(pilihanmenu == '4'):
        mengHapusPasien()
    elif(pilihanmenu == '5'):
        cekHistoryPasien()
    elif(pilihanmenu == '6'):
        break