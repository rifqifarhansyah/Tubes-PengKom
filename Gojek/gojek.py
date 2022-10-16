# Import Library
import numpy as np
# !pip install numpy
# import random

# User interface awal app

choose = int(input("""Selamat datang di Go-Jek\n
1. Go-Ride
2. Go-Tix
3. Top Up Gopay
4. Go-Send
"""))



# Go-Ride

if choose == 1:
    
    # Set current location ('Jalan Bangbayang No.23, Dago, Bandung')
    location = input('Masukkan posisi anda saat ini ')
    
    # Set destination
    destination = input('Masukkan alamat yang ingin dituju ')
    
    if len(destination.split())>0:
        
        # Set random number for KM 
        random_km = round(np.random.choice(np.arange(start=1, stop=10, step=0.1)),1)
        
        # Set ETA (Time Estimation), V average = 30 km/jam
        eta = np.round(random_km / 30 * 60, 1) # dalam menit
        
        # Set harga, per KM biaya yang diperlukan Rp 2600 (Go-Ride)
        harga = int(random_km * 2600)
        
        # Lanjutkan pembayaran 
        lanjutkan_pembayaran = (input(f"""
        Current Location : {location}
        Destination : {destination}
        {random_km} KM
        ETA : {eta} minutes
        Rp {harga}\n
        Lanjutkan pembayaran (y or n)
        """)).lower()
        
        if lanjutkan_pembayaran == 'y':
           # Set random number (waktu yang diperlukan oleh untuk menunggu ojek online)
            random_number = np.random.randint(low=3, high=15)
            input(f'Terima kasih, silahkan tunggu {random_number} menit')
        else:
            input('Pesanan anda dibatalkan')
            

            
            
# Go-Tix

if choose == 2:
    
    # Set lokasi anda
    lokasi = input('Masukkan lokasi anda saat ini')
    
    # Set lokasi bioskop
    lokasi_bioskop = int(input("""
    Selamat datang di Go-Tix, nikmati nonton seru tanpa terkendala biaya\n
    Pilih lokasi bioskop
    1. Empire XXI BIP Bandung
    2. BTC XXI
    3. Jatos Cinema XXI
    4. Braga XXI
    5. Ciwalk Premiere
    6. Lokasi lainnya
    """))
    
    # Jika lokasi lainnya
    if lokasi_bioskop == 6:
        nama_bioskop = input('Masukkan nama bioskop')
        
        # Set list film
        list_film = int(input(f"""
        Bioskop {nama_bioskop}\n

        Popular movies
        1. No Time to Die 
        2. Ali & Ratu Ratu Queens
        3. A World Without
        4. Venom : Let There Be Carnage

        Pilih film..
        5. Film lainnya
        """))
    
    # Jika lokasi ada dalam list
    else:
        # Set dictionary lokasi bioskop
        loc = {1: 'Empire XXI BIP Bandung', 2: 'BTC XXI', 3: 'Jatos Cinema XXI',
              4: 'Braga XXI', 5: 'Ciwalk Premiere'}
    
        # Set list film
        list_film = int(input(f"""
        Bioskop {loc[lokasi_bioskop]}\n

        Popular movies
        1. No Time to Die 
        2. Ali & Ratu Ratu Queens
        3. A World Without
        4. Venom : Let There Be Carnage

        Pilih film..
        5. Film lainnya
        """))
    
    # Set dictionary films
    film = {1: 'No Time to Die', 2: 'Ali & Ratu Ratu Queens',
            3: 'A World Without', 4: 'Venom : Let There Be Carnage'}
    
    # Set durasi film dan harga tiket
    random_jam = np.random.randint(low=1, high=3) # Pilih antara 1 atau 2 jam
    random_menit = np.random.randint(low=0, high=61) # Pilih diantara 0 dan 60 menit
    random_harga_tiket = np.random.choice(np.arange(start=30000, stop=55000, step=5000))
    
    
    
    # Jika dipilih judul film lainnya (selain di list)
    if list_film == 5:
        
        # Input nama film
        nama_film = input('Masukkan judul film')
        
        # Set keterangan film & opsi lanjutkan pembayaran
        lanjutkan_pembayaran = (input(f"""
        Judul film : {nama_film}
        Durasi : {random_jam} jam {random_menit} menit
        Harga : Rp {random_harga_tiket}\n
        Lanjutkan pembayaran (y or n)
        """)).lower()

        if lanjutkan_pembayaran == 'y':
            # Set jumlah tiket
            jumlah_tiket = int(input("""
            Masukkan jumlah tiket
            """))

            input(f"""
            Pembelian tiket {nama_film}
            sebanyak {jumlah_tiket} buah
            seharga {random_harga_tiket * jumlah_tiket}
            berhasil dilakukan
            """)
        else:
            input('Pembayaran anda dibatalkan')

    # Jika nama film ada dalam list        
    else:
        
        # Set keterangan film & opsi lanjutkan pembayaran
        lanjutkan_pembayaran = (input(f"""
        Judul film : {film[list_film]}
        Durasi : {random_jam} jam {random_menit} menit
        Harga : Rp {random_harga_tiket}\n
        Lanjutkan pembayaran (y or n)
        """)).lower()

        if lanjutkan_pembayaran == 'y':
            # Set jumlah tiket
            jumlah_tiket = int(input("""
            Masukkan jumlah tiket
            """))

            input(f"""
            Pembelian tiket {film[list_film]}
            sebanyak {jumlah_tiket} buah
            seharga {random_harga_tiket * jumlah_tiket}
            berhasil dilakukan
            """)
        else:
            input('Pembayaran anda dibatalkan')
        
    
    


# Top Up Gopay

if choose == 3:
    
    # Definisikan saldo awal
    saldo = 100000
    
    # Opsi nominal saldo
    topup_balance = int(input(f"""
    Saldo anda saat ini Rp {saldo}\n
    Masukkan nominal yang ingin anda tambahkan ke saldo Gopay
    1. 10000
    2. 20000
    3. 50000
    4. 100000
    5. nominal lainnya
    """))
    
    # Nominal saldo 10 ribu
    if topup_balance == 1:
        
        # Masukkan opsi pembayaran
        opsi_pembayaran = int(input("""
        Pilih opsi pembayaran
        1. BCA
        2. BNI
        3. Indomaret/Alfamart
        """))
        if opsi_pembayaran in range(1, 4):
            saldo += 10000
            input(f'Saldo anda sekarang Rp {saldo}')
    
    # Nominal saldo 20 ribu
    elif topup_balance == 2:
        
        # Masukkan opsi pembayaran
        opsi_pembayaran = int(input("""
        Pilih opsi pembayaran
        1. BCA
        2. BNI
        3. Indomaret/Alfamart
        """))
        if opsi_pembayaran in range(1, 4):
            saldo += 20000
            input(f'Saldo anda sekarang Rp {saldo}')
    
    # Nominal saldo 50 ribu
    elif topup_balance == 3:
        
        # Masukkan opsi pembayaran
        opsi_pembayaran = int(input("""
        Pilih opsi pembayaran
        1. BCA
        2. BNI
        3. Indomaret/Alfamart
        """))
        if opsi_pembayaran in range(1, 4):
            saldo += 50000
            input(f'Saldo anda sekarang Rp {saldo}')
    
    # Nominal saldo 100 ribu
    elif topup_balance == 4:
        
        # Masukkan opsi pembayaran
        opsi_pembayaran = int(input("""
        Pilih opsi pembayaran
        1. BCA
        2. BNI
        3. Indomaret/Alfamart
        """))
        if opsi_pembayaran in range(1, 4):
            saldo += 100000
            input(f'Saldo anda sekarang Rp {saldo}')
   
    # Nominal saldo lainnya
    else:
        
        # Masukkan opsi pembayaran
        opsi_pembayaran = int(input("""
        Pilih opsi pembayaran
        1. BCA
        2. BNI
        3. Indomaret/Alfamart
        """))
        if opsi_pembayaran in range(1, 4):
            saldo_tambahan = int(input(""""
            Masukkan nominal yang ingin anda tambahkan ke saldo Gopay\n
            """))
            saldo += saldo_tambahan
            input(f'Saldo anda sekarang Rp {saldo}')
            
           
        
        
        
        
# Go-Send

if choose == 4:
    
    # Set current location ('Jalan Bangbayang No.23, Dago, Bandung')
    location = input('Masukkan posisi anda saat ini ')
    
    # Set destination
    destination = input('Masukkan alamat yang ingin dituju ')
    
    if len(destination.split())>0:
        
        # Set random number for KM 
        import numpy as np
        random_km = round(np.random.choice(np.arange(start=1, stop=10, step=0.1)),1)
        
        # Set ETA (Time Estimation), V average = 30 km/jam
        eta = np.round(random_km / 30 * 60, 1) # dalam menit
        
        # Set harga, per KM biaya yang diperlukan Rp 3000 (Go-Send)
        harga = int(random_km * 3000)
        
        # Set berat barang 
        berat_barang = input('Masukkan perkiraan berat barang')
        
        # Set apabila berat barang kurang dari 1 kg maka menggunakan harga normal
        if float(berat_barang) > 1:
            # Penambahan biaya 5000/kg
            harga += ((float(berat_barang)-1) * 5000)
        else: 
            # Harga normal
            harga = harga
        
        # Lanjutkan pembayaran 
        lanjutkan_pembayaran = (input(f"""
        Current Location : {location}
        Destination : {destination}
        {random_km} KM
        ETA : {eta} minutes
        Weights : {berat_barang} Kg
        Rp {harga}\n
        Lanjutkan pembayaran (y or n)
        """)).lower()
        
        if lanjutkan_pembayaran == 'y':
            # Set random number (waktu yang diperlukan oleh untuk menunggu ojek online)
            random_number = np.random.randint(low=3, high=15)
            input(f'Terima kasih, silahkan tunggu {random_number} menit')
        else:
            input('Pesanan anda dibatalkan')