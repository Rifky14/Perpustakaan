# database
import sqlite3
conn = sqlite3.connect('database.db')	


tb_line ='~'*100
h_line='='*100
q_line='_'*100
br="\n"

# def
def create_db(db_name,t_h):
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS \
                "{}"({})'''.format(db_name,t_h))
        c.close()

def tambah(t_name,o):
        c = conn.cursor()
        c.execute('''INSERT INTO "{}" VALUES('{}')'''.format(t_name,o))
        conn.commit()
        c.close()

def next():
	print(br*100)

def main_header():
	print(tb_line+br)
	print("{:^100}".format('Perpustakaan'))
	print("{:^100}".format(l_n))
	print(br+tb_line)

def header (name_header):
	print(tb_line+br)
	print("{:^100}".format(name_header))
	print(br+tb_line)

def body (menu):
	print(menu+br+q_line)

def nothing():
	print("Pilihan Tidak tersedia")

def answer():
	answer = input("Jawab : ")
	return answer
def cs():
	print("Coming Soon")


# create database if not exists
create_db("lock","activation INTEGER, password TEXT")
create_db("nama_perpus","nama TEXT")
create_db("daftar_buku","title TEXT,writer TEXT, genre TEXT, width INTEGER, qty INTEGER, location TEXT" )


# Set default LOck
c = conn.cursor()
c.execute('''SELECT * FROM "lock"''')
lock=c.fetchall()
if lock == []:
	c.execute("INSERT INTO 'lock' VALUES(0,NULL)")
	conn.commit()
	print ("Anda dapat mengatur sandi di pengaturan")
c.close()


# mengatur nama default jika belum ada
c = conn.cursor()
c.execute('''SELECT * FROM "nama_perpus"''')
l=c.fetchall()
if l == []:
	tambah("nama_perpus",'X')
c.close()

# Home
# lock
c = conn.cursor()
c.execute('''SELECT * FROM "lock"''')
lock=c.fetchall()
c.close()
if lock[0][0] == 0 :
	pilihan = "0"
else :
	sandi = False
	while sandi == False :
		in_pw = input("Masukkan Sandi untuk masuk : ")

		if in_pw != lock[0][1]:
			print("{:^100}".format("Sandi salah"))
			print(br)

		else :
			sandi = True
			pilihan = '0'

pilihan ="0"
while pilihan == '0':

	# membuka database nama perpus
	c = conn.cursor()
	c.execute('''SELECT * FROM "nama_perpus"''')
	l=c.fetchall()
	l_n=l[0][0]
	c.close()
	# home
	next()	
	main_header()
	body("Menu |"+br+"1.Katalog"+br+"2.Anggota(Comming Soon)"+br+"3.Peminjaman Buku(Comming Soon)"+br+"4.Pengembalian buku(Comming Soon)"+br+"5.Pengaturan"+br+"6.Keluar"+br+"0.Refresh")
	pilihan = 'ulang'
	while pilihan == 'ulang':
		pilihan = answer()

		# Menu-1 Katalog
		while pilihan == '1' :
			next()
			header("Katalog")
			# load book
			c = conn.cursor()
			c.execute('''SELECT * FROM "daftar_buku" ORDER BY "title" DESC''')
			l=c.fetchall()
			c.close()

			if l == []:
				print("Buku Belum Ada")
			else :
				# create terminal header table
				print("No.|"+"{:^20}|{:^15}|{:^11}|{:^7}|{:^6}|{:^15}".format('Judul','Penulis','jenis','tebal','jumlah','letak'),br+h_line)
				# create content of table
				row = len(l)-1
				no=1
				while row  >= 0:
					print (no," |"+"{:<20}|{:<15}|{:<11}|{:>7}|{:>6}|{:<15}".format(l[row ][0], l[row][1], l[row][2], l[row][3], l[row][4], l[row][5]))
					no = no+1
					row = row-1
			print(q_line+br)
			body("Pilihan |"+br+"1.Tambah"+br+"2.Temukan Buku"+br+"4.Hapus Buku"+br+"5.Kosongkan katalog"+br+"0.Kembali")
			pilihan = 'ulang'
			while pilihan == 'ulang':
				pilihan=answer()

				if pilihan == '0':
					continue
				
				elif pilihan == '1' :
					header("Tambah Buku")
					nama_buku = input ("Judul buku         : ")
					pengarang = input ("Pengarang          : ")
					genre_buku = input("Jenis              : ")
					w_buku     = int(input("Tebal Buku(lembar) : "))
					q_buku = int(input    ("Jumlah             : "))
					letak_buku = input("Letak              : ")
					c = conn.cursor()
					c.execute("INSERT INTO daftar_buku VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(nama_buku, pengarang, genre_buku, w_buku, q_buku, letak_buku))
					conn.commit()
					c.close()
					pilihan = '1'

				elif pilihan == '2' :
					filter = input ("Masukan kata kunci judul yang dicari : ")
					c = conn.cursor()
					c.execute('''SELECT "_rowid_",* FROM "main"."daftar_buku" WHERE "title" LIKE '%{}%' ORDER by title DESC'''.format(filter))
					l=c.fetchall()
					c.close()

					if l == []:
						print("Tidak ada hasil yang ditemukan")
					else :
						# create terminal header table
						print("No.|"+"{:^20}|{:^15}|{:^11}|{:^7}|{:^6}|{:^15}".format('Judul','Penulis','jenis','tebal','jumlah','letak'),br+h_line)
						# create content of table
						row = len(l)-1
						no=1
						while row  >= 0:
							print (no," |"+"{:<20}|{:<15}|{:<11}|{:>7}|{:>6}|{:<15}".format(l[row ][1], l[row][2], l[row][3], l[row][5], l[row][5], l[row][6]))
							no = no+1
							row = row-1

					pilihan = 'ulang'
					while pilihan == 'ulang':
						pilihan = answer()
						if pilihan == '0':
							pilihan ='1'

					

				elif pilihan == '5' :
					print(c.rowcount, "judul buku terhapus")
					c = conn.cursor()
					c.execute('''DELETE FROM "daftar_buku"''')
					conn.commit()
					c.close()
					pilihan = '1'


				else :
					nothing()
					pilihan = 'ulang'

		# Menu-2 Member
		while pilihan == '2' :
			next()
			header("Keanggotaan")
			body("Pilihan |"+br+"1.Daftar Anggota"+br+"2.Tambah Anggota"+br+"0.back")
			pilihan = 'ulang'
			while pilihan == 'ulang':
				pilihan = answer()
				
				if pilihan == '0':
					next()
					continue
				else :
					nothing()
					pilihan = 'ulang'

		# Menu-3 Borrow
		while pilihan == '3' :
			next()
			header("Peminjaman Buku")
			k_b=input("Masukkan kode buku    : ")

			
			k_m=input("Masukkan kode anggota : ")
	
		# Menu-4 Return
		while pilihan == '4' :
			next()
			header("Pengembalian Buku")
			body("Pilihan |"+br+"1.View Member"+br+"2.Add Member"+br+"0.back")
			pilihan = 'ulang'
			while pilihan == 'ulang':
				pilihan = answer()
				
				if pilihan == '0':
					next()
					continue
				else :
					nothing()
					pilihan = 'ulang'
		
		# Menu-5 Option
		while pilihan == '5' :
			next()
			header("Pengaturan")
			body("Pilihan |"+br+"1.Profil Perpustakaan"+br+"2.Gembok"+br+"0.back")
			pilihan = 'ulang'
			while pilihan == 'ulang':
				pilihan = answer()
				

				while pilihan == '1':
					c = conn.cursor()
					c.execute('''SELECT * FROM "nama_perpus"''')
					l=c.fetchall()
					l_n=l[0][0]
					c.close()
					next()
					header("Profil Perpustakaan")
					body("Nama Perpustakaan : "+l_n+br+"Pilihan |"+br+"1.Ganti Nama"+br+"2.Reset Nama"+br+"0.back")
					pilihan = 'ulang'
					while pilihan == 'ulang':
						pilihan=answer()

						if pilihan == '0':
							next()
							pilihan = '5'

						# pilihan-1 mengatur nama
						elif pilihan == '1':
							i_l_n = input("Masukkan Nama Perpustakaan : ")
							c = conn.cursor()
							c.execute('''DELETE FROM "main"."nama_perpus" WHERE _rowid_ IN ('1')''')
							conn.commit()
							c.close
							tambah('nama_perpus',i_l_n)
							continue
						# REset nama
						elif pilihan == '2':
							c = conn.cursor()
							c.execute('''DELETE FROM "main"."nama_perpus" WHERE _rowid_ IN ('1')''')
							conn.commit()
							c.close
							tambah("nama_perpus",'X')
							pilihan = '1'

						else :
							nothing()
							pilihan = 'ulang'
				while pilihan == '2':
					c = conn.cursor()
					c.execute('''SELECT * FROM "lock"''')
					lock=c.fetchall()
					c.close()
					s_c = lock[0][0]
					pw = lock[0][1]
					next()
					header("Pergembokan")
					if s_c == 0 :
						status = 'off'
					else :
						status = 'on'
					body("status gembok : {}".format(status)+br+"Pilihan |"+br+"1.On/off"+br+"2.Ubah Sandi(Cooming Soon)"+br+"0.back")	
					pilihan = 'ulang'
					while pilihan == 'ulang':
						pilihan=answer()
						if pilihan == '1' :
							if status == 'off' :

								i_pw = input("Atur sandi :")
								conn.execute("UPDATE lock SET password = '%s' WHERE activation = 0"%(i_pw))
								conn.execute('''UPDATE "main"."lock" SET "activation"='1' WHERE "_rowid_"="1"''')
								conn.commit()
								c.close()
								pilihan = '2'
							
							else :
								conn.execute('''UPDATE "main"."lock" SET "activation"='0' WHERE "_rowid_"="1"''')
								conn.commit()
								c.close()
								pilihan = '2'


				
				if pilihan == '0':
					next()
					continue
				elif pilihan =='5':
					continue

				else :
					nothing()
					pilihan = 'ulang'

		# Exit
		if pilihan == '6' :
			# tutup database
			conn.close() 
			break

		# Refresh
		elif pilihan == '0' :
			continue
		else :
			nothing()
			pilihan = 'ulang'
	else :
		continue

	
		
