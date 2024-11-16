from prettytable import PrettyTable

data_barang = [{'nama barang': 'aqua 500ml', 'jenis': 'minuman', 'harga': 5000},
               {'nama barang': 'milo drink', 'jenis': 'minuman', 'harga': 5650},
               {'nama barang': 'le-minerale', 'jenis': 'minuman', 'harga': 4800},
               {'nama barang': '1000 vit c', 'jenis': 'minuman', 'harga': 10000},
               {'nama barang': 'teh pucuk', 'jenis': 'minuman', 'harga': 6300},
               {'nama barang': 'roti awok', 'jenis': 'makanan', 'harga': 2300},
               {'nama barang': 'snack boncabe', 'jenis': 'makanan', 'harga': 4900},
               {'nama barang': 'mie gelas', 'jenis': 'makanan', 'harga': 3000},
               {'nama barang': 'indomie', 'jenis': 'makanan', 'harga': 3500},
               {'nama barang': 'ice cream', 'jenis': 'makanan', 'harga': 8300},
               {'nama barang': 'buku', 'jenis': 'alat tulis', 'harga': 4300},
               {'nama barang': 'pulpen', 'jenis': 'alat tulis', 'harga': 3200},
               {'nama barang': 'pensil', 'jenis': 'alat tulis', 'harga': 3300},
               {'nama barang': 'penggaris', 'jenis': 'alat tulis', 'harga': 2900},
               {'nama barang': 'penghapus', 'jenis': 'alat tulis', 'harga': 2000}
               ]


def mengecek_barang():
    while True:
        pilihan = input('masukkan nama barang(jika sudah selesai ketik "selesai"): ').lower()
        if pilihan == 'selesai':
            return
        for barang in data_barang:
            if pilihan == barang['nama barang']:
                print('informasi barang:')
                print(f"nama Barang: {barang['nama barang']} ")
                print(f"Jenis Barang: {barang['jenis']} ")
                print(f"Harga Barang: {barang['harga']} ")
                barang_ditemukan = True
                break
        if not barang_ditemukan:
            print('Barang tidak ditemukan')


def memasukkan_belanjaan():
    global barang_belanjaan
    barang_belanjaan = []
    while True:
        pilihan = input('masukkan nama barang(jika sudah selesai ketik "selesai"): ').lower()
        barang_ditemukan = False
        if pilihan == 'selesai':
            return

        for barang in data_barang:
            if pilihan == barang['nama barang']:
                print(f'{barang["nama barang"]} telah ditambahka kedalam daftar belanjaan')
                barang_belanjaan.append(barang)
                barang_ditemukan = True
        if not barang_ditemukan:
            print('barang tidak ditemukan')


def cetak_struk():
    uang_kembalian = 0
    print('Struk Belanjaan Anda:')
    barang_belanjaan1 = PrettyTable()
    barang_belanjaan1.field_names = ['nama barang', 'jenis', 'harga']
    if barang_belanjaan:
        for barang in barang_belanjaan:
            barang_belanjaan1.add_row([barang['nama barang'], barang['jenis'], barang['harga']])
        print(barang_belanjaan1)
        total_harga = sum(barang['harga'] for barang in barang_belanjaan)
        print(f'total harga belanjaan anda adalah Rp. {total_harga}')
        uang_pelanggan = int(input('masukkan uang anda : '))
        if uang_pelanggan >= total_harga:
            uang_kembalian = uang_pelanggan - total_harga
            print(f'uang kembalian anda adalah Rp. {uang_kembalian}')


while True:
    print('---------------------------------')
    print('| Selamat Datang Di Haikal Mart |')
    print('---------------------------------')
    print('|1. Mengecek Harga Barang       |')
    print('|2. Memasukkan Belanjaan        |')
    print('|3. Mencetak Struk Belanjaan    |')
    print('|4. Keluar dari Program Kasir   |')
    print('---------------------------------')
    pilihan = input('masukkan pilihan di atas (1,2,3 atau 4) : ')
    if pilihan == '1':
        mengecek_barang()
    elif pilihan == '2':
        memasukkan_belanjaan()
    elif pilihan == '3':
        cetak_struk()
    elif pilihan == '4':
        print('TERIMA KASIH TELAH BERBELANJA DI PUTRA MART')
        break
    else:
        print('pilihan yang anda masukkan tidak ada')
        break










