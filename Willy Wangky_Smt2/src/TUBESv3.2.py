import csv
#KAMUS UTAMA

#Nmax:integer
#data: array of string [1..Nmax]
#type datafile: <array [1..10] of data>
#du,dw,dp,dk,dks,dg,dr,dth: datafile
#constant mark: "."
#isOn,isLogin,isSave,isValid: boolean
#choice: integer
#role,uName:string
#agree, retry: character

#FUNGSI ANTARA YANG DIGUNAKAN
#----------------------------------------------------------------------------------
#fungsi is17
#Mengembalikan nilai true jika umur >=17

#KAMUS LOKAL
#dd1,mm1,yyyy1,dd2,mm2,yyyy2: integer
def is17(dd1,mm1,yyyy1,dd2,mm2,yyyy2):
    if(yyyy2-yyyy1<17):
        return False
    elif(yyyy2-yyyy1>17):
        return True
    else:
        if(mm2-mm1>0):
            return True
        elif(mm2-mm1<0):
            return False
        else:
            if(dd2-dd1<0):
                return False
            else:
                return True

#fungsi locate
#mengembalikan indeks kolom ketika parameter pencarian ditemukan di kolom tertentu

#KAMUS LOKAL
#df: datafile
#idx,count: integer
#param: string
#isTersedia: boolean

def locate(df,idx,param):
    count=0
    isTersedia=False
    while(not isTersedia and (count<10)):
        if(df[count][idx]==param):
            isTersedia=True
        else:
            count+=1
    if(not isTersedia):
        return 999
    return count

#fungsi inputdata
# mencari row kosong dan menginput data baru ke row tersebut

#KAMUS LOKAL
#df: datafile
#jmlcol,i: integer
#newdata: array of string
#function rowkosong(df: datafile)
def inputdata(df,jmlcol,newdata):
    row=rowkosong(df)
    for i in range (jmlcol):
        df[row][i]=newdata[i]
    return df

#fungsi rowkosng
# mencari row kosong yang tersedia pada filedata df

#KAMUS LOKAL
#df: datafile
#rownum: integer
def rowkosong(df):
    rownum=0
    while (df[rownum][0]!='0' and rownum<10):
        rownum+=1
    
    if(rownum<10):
        return rownum
    else:
        print("Data penuh")
        return 999

#fungsi isTersedia
#output=False jika ditemukan data yang sama pada kolom tertentu dan True jika tidak ditemukan

#KAMUS LOKAL
#df: datafile
#param: string
#idx,k,i:integer
def isTersedia(df,param,idxcol): 
    k=idxcol
    for i in range (10):
        if(df[i][k]==param):
            return False
    return True

#fungsi tglTrue
# memeriksa apakah format tanggal sudah benar

#KAMUS LOKAL
#tl: string
#dd,mm,yyyy: integer
def tglTrue(tl):#cek format tanggal
    if(tl[2]=="/" and tl[5]=="/"):
        dd=int(tl[0]+tl[1])
        mm=int(tl[3]+tl[4])
        yyyy=int(tl[6]+tl[7]+tl[8]+tl[9])
        if((mm>0) and (mm<=12)):
            if((mm==2) and (yyyy%4==0)):#kabisat februari
                if ((dd<=29) and (dd>0)):
                    return True
                else:
                    return False
            elif((mm==2) and (yyyy%4 !=0)):#tidak kabisat februari
                if ((dd<=28) and (dd>0)):
                    return True
                else:
                    return False
            elif(((mm%2==0) and (mm<7) and (mm!=2)) or ((mm%2==1) and (mm>7))): #setiap bulan yg ada 30 hari
                if((dd<=30) and (dd>0)):
                    return True
                else:
                    return False
            else: #tiap bulan yg 31 hari
                if((dd<=31) and (dd>0)):
                    return True
                else:
                    return False
        else:
            return False
                   
    else:
        return False

#fungsi isAda
#output= True jika data terdapat pada kolom ke-idxcol

#KAMUS LOKAL
#df:datafile
#param:string
#idxcol,i,k: integer
def isAda(df,param,idxcol): #ngecek apakah username udah terdaftar atau belum
    k=idxcol
    for i in range (10):
        if(df[i][k]==param):
            return True
    return False

#fungsi EOP
#output= True jika row yang dibaca sama seperti mark

#KAMUS LOKAL
#row: array of string
#mark:"."
def EOP(row,mark):
    if(row==mark):
        return True
    else:
        return False
#------------------------------------------------------------------------------------------------
#FUNGSI UTAMA
#Fungsi load
#Membaca data yang tertulis pada file dan disimpan dalam array bernama df

#KAMUS LOKAL
#nama,mark,namafile: string
#f: SEQFILE of datafile
#reader = hasil pembacaan data csv
#row,df=array of string
#function EOP (row:array, mark:".")
#count: integer
def load(nama,mark):#harus pakai array default biar jumlah datanya sama
    namafile=str(input("Masukkan nama File "+str(nama)+" : "))
    df=['+' for i in range (10)]
    f=open(namafile,'r',encoding="utf-8")
    reader=csv.reader(f,delimiter=',')
    row=next(reader)
    count=0
    if(EOP(row,mark)):
        return mark
        f.close()
    else:
        while(not EOP(row,mark)):
            df[count]=row
            count+=1
            if(count<10):
                row=next(reader)
            else:
                break
        f.close()
        return df


#fungsi login    
#menerima input berupa username dan password dan mencocokkan data tersebut dengan data yang tertulis pada file csv

#KAMUS LOKAL
#du: datafile
#function dec(epass:string)

def login(du):
    uName=str(input("Masukkan username: "))
    passw=str(input("Masukkan password: "))
    for i in range (10):
        if(du[i][3]==uName):
            if(dec(du[i][4])==passw):
                print("Selamat bersenang-senang, "+str(du[i][0])+"!")
                return True,uName
            else:
                break
    print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
    return False,0

#fungsi save
#Menyimpan data terbaru ke file csv

#KAMUS LOKAL
#nama,namafile: string
#data: datafile
#newdata: array of string
#writer = fungsi penulisan data ke file csv
#f: SEQFILE of datafile
#mark: "."
def save(nama,data,mark):
    namafile=str(input("Masukkan nama File "+str(nama)+" : "))
    f=open(namafile,'w',newline='',encoding="utf-8")
    writer=csv.writer(f,delimiter=',')
    i=0
    newdata=data[i]
    while(not(EOP(newdata,mark))):
        writer.writerow(newdata)
        i+=1
        if(i<10):
            newdata=data[i]
        else:
            break
    writer.writerow(mark)    
    f.close()

#fungsi signup
#Menyimpan data yang dimasukkan oleh user ke file user.csv
#jika menemukan username yang sama pada file user, akan dilakukan pengulangan terhadap masukan username user
#hanya bisa mendaftarkan pemain baru

#KAMUS LOKAL
#constant Nmax: integer = 8
#du,newarr: datafile
#name,tb,tl,uName,passw,epass: string
#newacc: array of string
#function tglTrue(tl:string)
#function isTersedia(df: datafile, param: string, idx: integer)
#function enc(decpass: string)
#function locate(df: datafile, idx: integer, param: string)
def signup(du):
    name=str(input("Masukkan nama pemain: "))
    tb=str(input("Masukkan tinggi badan (cm): "))
    tl=str(input("Masukkan tanggal lahir pemain (DD/MM/YYYY): "))
    while (not tglTrue(tl)):
        tl=str(input("Format tanggal salah, ulangi input tanggal (DD/MM/YYYY): "))
    uName=str(input("Masukkan username pemain: "))
    while(isTersedia(du,uName,3)==False):
        uName=str(input("Username telah terdaftar! Masukkan username pemain: "))
    passw=str(input("Masukkan password pemain: "))
    epass=enc(passw)
    newacc=[name,tl,tb,uName,epass,"Pemain","0","No"]
    newarr=inputdata(du,8,newacc)
    print("Selamat menjadi pemain, "+str(du[locate(newarr,3,uName)][0])+". Selamat bermain.")
    return newarr

#fungsi cariPemain
#menerima inputan user berupa username player yang akan dicari
#mengeluarkan hasil berupa data diri pemain yang dicari
#hanya bisa diakses oleh admin

#KAMUS LOKAL
#du: datafile
#uName: string
#row: integer
#function locate(df: datafile, idx: integer, param: string)
def cariPemain(du):#BERGANTUNG PADA FILE USER
    uName=str(input("Masukkan username: "))
    row=locate(du,3,uName)
    if(row!=999):
        print("Nama Pemain: "+str(du[row][0]))
        print("Tinggi Pemain (cm): "+str(du[row][2]))
        print("Tanggal Lahir Pemain: "+str(du[row][1]))
    else:
        print("Data pemain tidak ditemukan")

#fungsi cari wahana
#input= batasan umur dan batasan tinggi badan suatu wahana
#output= id, nama, dan harga dari wahana yang memiliki batasan yang telah diinput oleh pengguna
#dapat diakses oleh admin dan pemain

#KAMUS LOKAL
#dw: datafile
#bu,btb: string
#count,i : integer
def cariWahana(dw):
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur","\n")
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170cm")
    print("2. Tanpa batasan","\n")
    bu=str(input("Batasan umur pemain: "))
    while (not(bu=="1" or bu=="2" or bu=="3")):
        print("Batasan umur tidak valid!")
        bu=str(input("Batasan umur pemain: "))
    btb=str(input("Batasan tinggi badan: "))
    while (not(btb=="1" or btb=="2")):
        print("Batasan tinggi badan tidak valid")
        btb=str(input("Batasan tinggi badan: "))

    if(bu=="1"):
        bu="anak-anak"
    elif(bu=="2"):
        bu="dewasa"
    else:
        bu="semua umur"

    if(btb=="1"):
        btb=">=170"
    else:
        btb="tanpa batasan"

    print("Hasil pencarian:")
    count=0
    for i in range (10):
        if(dw[i][3]==bu):
            if(dw[i][4]==btb):
                print(str(dw[i][0])+" | "+str(dw[i][1])+" | "+str(dw[i][2]))#id | nama | harga
                count+=1

    if(count==0):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu")
        
#fungsi beliTiket
#fungsi untuk membeli tiket wahana yang memiliki id tertentu dan bergantung pada saldo user
#hanya dapat diakses oleh pemain

#KAMUS LOKAL
#du,dw,dk,newrowDK,dp,newrowDP: datafile
#uName, id, tgl, tl, gold,btb, bu, harga, nama: string
#tb, saldo, dd1,mm1,yyyy1,dd2,mm2,yyyy2,total,i: integer
#mK,mP: array of string
#isFound: boolean
#function locate(df:datafile, idx:integer, param: string)
#function isAda(df:datafile,param:string,idxcol:integer)
#function tglTrue(tl:string)
#function is17(dd1,mm1,yyyy1,dd2,mm2,yyyy2:integer)
#function inputdata(df:datafile,jmlcol:integer,newdata:array of string)

def beliTiket(uName,du,dw,dk,dp):#BERGANTUNG PADA FILE KEPEMILIKAN,WAHANA, USER
    id=str(input("Masukkan ID wahana: "))
    while(not isAda(dw,id,0)):
        id=str(input("ID wahana tidak ditemukan. Masukkan ID wahana: "))
    tgl=str(input("Masukkan tanggal hari ini (DD/MM/YYYY): "))
    while(not tglTrue(tgl)):
        tgl=str(input("Tanggal invalid. Masukkan tanggal hari ini (DD/MM/YYYY): "))
    jml=int(input("Jumlah tiket yang dibeli: "))

    #DATA USER
    tb=du[locate(du,3,uName)][2]
    tl=du[locate(du,3,uName)][1]
    saldo=du[locate(du,3,uName)][6]
    gold=du[locate(du,3,uName)][7]
    
    #DATA WAHANA
    btb=dw[locate(dw,0,id)][4]#kategori
    bu=dw[locate(dw,0,id)][3]#kategori
    harga=dw[locate(dw,0,id)][2]#int
    nama=dw[locate(dw,0,id)][1]
    
    #PEngolahan data user
    tb=int(tb[0]+tb[1]+tb[2])
    dd1=int(tl[0]+tl[1])
    mm1=int(tl[3]+tl[4])
    yyyy1=int(tl[6]+tl[7]+tl[8]+tl[9])
    saldo=int(saldo)
    
    #Pengolahan data wahana
    if(gold=="Gold"):
        harga=int(int(harga)*0.5)
    else:
        harga=int(harga)
    
    #Pengolahan data input
    dd2=int(tgl[0]+tgl[1])
    mm2=int(tgl[3]+tgl[4])
    yyyy2=int(tgl[6]+tgl[7]+tgl[8]+tgl[9])
    
    
    #Algoritma
    if(bu=="anak-anak"):
        if(is17(dd1,mm1,yyyy1,dd2,mm2,yyyy2)):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini")
            print("Silakan menggunakan wahana lain yang tersedia.")
            return du,dk,dp

    elif(bu=="dewasa"):
        if(not is17(dd1,mm1,yyyy1,dd2,mm2,yyyy2)):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini")
            print("Silakan menggunakan wahana lain yang tersedia.")
            return du,dk,dp
    #bu=semua umur sudah pasti True
    
    if(btb==">=170"):
        if(tb<170):
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini")
            print("Silakan menggunakan wahana lain yang tersedia.")
            return du,dk,dp
    
    total=jml*harga
    if(saldo<total):
        print("Saldo Anda tidak cukup")
        print("Silakan mengisi saldo Anda")
        return du,dk,dp
    
    saldo-=total
    du[locate(du,3,uName)][6]=str(saldo)
    
    print("Selamat bersenang-senang di "+str(nama)+".")
    mK=[uName,id,jml]
    mP=[uName,tgl,id,jml]
    
    newrowDP=inputdata(dp,4,mP)
    i=0
    isFound=False
    while (i<10 and (not isFound)):
        if (dk[i][0]==uName):
            if(dk[i][1]==id):
                dk[i][2]=str(jml+int(dk[i][2]))
                isFound=True
            else:
                i+=1
        else:
            i+=1
    if(isFound):
        return du,dk,newrowDP
    else:
        newrowDK=inputdata(dk,3,mK)
        return du,newrowDK,newrowDP

#fungsi useTiket
#menggunakan tiket milik player untuk main di wahana tertentu
#hanya dapat diakses oleh pemain

#KAMUS LOKAL
#dk,dg,newdg: datafile
#uName,tgl,id: string
#jml, i,sisa,tiket: integer
#isFound: boolean
#arrdg: array of string
#function inputdata(df: datafile, jmlcol: integer,newdata: array of string)
#function isAda(df:datafile,param:string,idxcol:integer)
#function tglTrue(tl:string)
def useTiket(uName,dk,dg,dw):#Bergantung kepemilikan tiket, penggunaan tiket
    id=str(input("Masukkan ID wahana: "))
    while(not isAda(dw,id,0)):
        id=str(input("ID wahana tidak ditemukan. Masukkan ID wahana: "))
    tgl=str(input("Masukkan tanggal hari ini (DD/MM/YYYY): "))
    while(not tglTrue(tgl)):
        tgl=str(input("Tanggal invalid. Masukkan tanggal hari ini (DD/MM/YYYY): "))
    jml=int(input("Jumlah tiket yang digunakan: "))

    i=0
    isFound=False
    while (i<10 and(not isFound)):
        if (dk[i][0]==uName):
            if(dk[i][1]==id):
                tiket=int(dk[i][2])
                isFound=True
            else:
                i+=1
        else:
            i+=1
    
    if(isFound):
        if(tiket>=jml):
            sisa=tiket-jml
            dk[i][2]=sisa
            arrdg=[uName,tgl,id,jml]
            newdg=inputdata(dg,4,arrdg)
            print("Terima kasih telah bermain")
            return dk,newdg
        else:
            print("Tiket Anda tidak valid dalam sistem kami")
    else:
        print("Tiket Anda tidak valid dalam sistem kami")

    return dk,dg


#fungsi refund
#Menukar tiket menjadi uang dengan jumlah 80% dari harga awal tiket
#hanya dapat diakses oleh pemain

#KAMUS LOKAL
#du,dw,dr,dk,newdr:filedata
#uName,id,tgl: string
#harga,total,uang,jml,i: integer
#isFound: boolean
#refarr: array of string
#function inputdata(df:datafile, jmlcol: integer, newdata: array of string)
def refund(uName,du,dw,dk,dr):#80%
    id=str(input("Masukkan ID wahana: "))
    while(not isAda(dw,id,0)):
        id=str(input("ID wahana tidak ditemukan. Masukkan ID wahana: "))
    tgl=str(input("Masukkan tanggal refund (DD/MM/YYYY): "))
    while(not tglTrue(tgl)):
        tgl=str(input("Tanggal invalid. Masukkan tanggal refund (DD/MM/YYYY): "))
    jml=int(input("Jumlah tiket yang di-refund: "))

    rowdw=locate(dw,0,id)
    rowdu=locate(du,3,uName)
    harga=int(dw[rowdw][2])
    total=harga*jml
    uang=int(0.8*total)

    i=0
    isFound=False
    while (i<10 and(not isFound)):
        if (dk[i][0]==uName):
            if(dk[i][1]==id):
                isFound=True
            else:
                i+=1
        else:
            i+=1
    
    if(isFound):
        if(int(dk[i][2])>=jml):
            dk[i][2]=str(int(dk[i][2])-jml)
            du[rowdu][6]=int(du[rowdu][6])+uang
        else:
            print("Anda tidak memiliki tiket terkait")
            return du,dk,dr
    else:
        print("Anda tidak memiliki tiket terkait")
        return du,dk,dr
    
    print("Uang refund sudah kami berikan pada akun Anda")
    refarr=[uName,tgl,id,jml]
    newdr=inputdata(dr,4,refarr)
    return du,dk,newdr


#fungsi saran
#memfasilitasi player untuk memberikan kritik saran pada wahana
#hanya dapat diakses oleh pemain

#KAMUS LOKAL
#dks,dw,newdks: datafile
#uName,id,tgl,laporan: string
#newarr: array of string
#function isAda(df:datafile, param:string, idxcol: integer)
#function tglTrue(tl:string)
#function inputdata(df:datafile, jmlcol: integer, newdata: array of string)
def saran(uName,dks,dw):
    id=str(input("Masukkan ID wahana: "))
    while(not isAda(dw,id,0)):
        id=str(input("ID wahana tidak ditemukan. Masukkan ID wahana: "))
    tgl=str(input("Masukkan tanggal pelaporan (DD/MM/YYYY): "))
    while(not tglTrue(tgl)):
        tgl=str(input("Tanggal invalid. Masukkan tanggal pelaporan (DD/MM/YYYY): "))
    laporan=str(input("Kritik/saran Anda: "))

    newarr=[uName,tgl,id,laporan]
    newdks=inputdata(dks,4,newarr)
    print("Kritik dan saran Anda kami terima.")
    return newdks

#fungsi review
#menampilkan data kritik dan saran yang telah diisi oleh pemain
#hanya dapat diakses oleh admin
#diurutkan secara alfabetis
#hanya dapat diakses oleh admin

#dks:datafile
#i,j,loc:integer
#min:string
#bigger:array of string
def review(dks):#id | tgl | uname | laporan
    print("Kritik dan saran:")
    i=0
    while (i<10 and dks[i][2]!="0"):
        min=dks[i][2]
        for j in range (i,10,1):
            if (dks[j][2]!="0"):
                if(dks[j][2]<min):
                    min=dks[j][2]
                    loc=j
        bigger=dks[i]
        dks[i]=dks[loc]
        dks[loc]=bigger
        i+=1

    for i in range (10):
        if(str(dks[i][0])!="0"):
            print(str(dks[i][2])+" | "+str(dks[i][1])+" | "+str(dks[i][0])+" | "+str(dks[i][3]))
    
#fungsi addWahana
#menambahkan wahana baru ke daftar wahana
#hanya dapat diakses oleh admin

#KAMUS LOKAL
#dw,newarr: datafile
#id,nama,harga,age,btb: string
#newwahana: array of string
#function isTersedia(df:datafile, param: string, idxcol: integer )
#function inputdata(df:datafile, jmlcol: integer, newdata: array of string)
def addWahana(dw):#BERGANTUNG PADA FILE WAHANA
    id=str(input("Masukkan ID Wahana: "))
    nama=str(input("Masukkan Nama Wahana: "))
    while(isTersedia(dw,nama,1)==False):
        nama=str(input("Nama telah digunakan. Coba nama lain: "))
    harga=str(input("Masukkan Harga Tiket (Rp): "))
    age=str(input("Batasan umur (dewasa/anak-anak/semua umur): "))
    btb=str(input("Batasan tinggi badan ('>=170' atau 'tanpa batasan'): "))
    
    newwahana=[id,nama,harga,age,btb]
    newarr=inputdata(dw,5,newwahana)
    print("Info wahana telah ditambahkan!")
    return newarr


#fungsi topup
#menambahkan saldo user
#dapat diakses oleh admin

#KAMUS LOKAL
#du: datafile
#uName: string
#jumlah, total: integer
#function isAda(df:datafile, param:string, idxcol: integer)
def topup(du):
    uName=input(str("Masukkan username: "))
    jumlah=int(input("Masukkan saldo yang di-top up: "))
    if(not isAda(du,uName,3)):
        print("Username tidak terdaftar, kembali ke menu utama")
    else:
        total=int(du[locate(du,3,uName)][6])+jumlah
        du[locate(du,3,uName)][6]=str(total)
        print("Top up berhasil. Saldo "+str(du[locate(du,3,uName)][0]+" bertambah menjadi "+str(du[locate(du,3,uName)][6])))
    return du


#fungsi riwayat
#melihat riwayat penggunaan wahana
#diakses oleh admin

#KAMUS LOKAL
#dg,dw: datafile
#id:string
#count,i:integer
#function isAda(df:datafile, param:string, idxcol:integer)
def riwayat(dg,dw):#tgl | uname | jml
    id=str(input("Masukkan ID wahana: "))
    while(not isAda(dw,id,0)):
        id=str(input("ID wahana tidak ditemukan. Masukkan ID wahana: "))
    print("Riwayat:")
    count=0
    for i in range(10):
        if(dg[i][2]==id):
            print(str(dg[i][1])+" | "+str(dg[i][0])+" | "+str(dg[i][3]))
            count+=1
    
    if(count==0):
        print("Tidak ada riwayat penggunaan tiket wahana tersebut")

#fungsi jumlah
#melihat jumlah tiket milik pemain
#diakses oleh admin

#KAMUS LOKAL
#dk,dw:datafile
#uName:string
#count,i,j:integer
#isFound: boolean
def jumlah(dk,dw):#id | namawahana | jml
    uName=str(input("Masukkan username: "))
    print("Riwayat:")
    count=0
    for i in range (10):
        if(dk[i][0]==uName):
            count+=1
            isFound=False
            j=0
            while(not isFound):
                if(dk[i][1]==dw[j][0]):
                    print(str(dk[i][1])+" | "+str(dw[j][1])+" | "+str(dk[i][2]))
                    isFound=True
                else:
                    j+=1
            
    if(count==0):
        print("Pengguna tidak memiliki tiket")

#fungsi exit
#user memilih ingin menyimpan data atau tidak saat fungsi ini dijalankan
#diakses oleh pemain dan admin

#KAMUS LOKAL
#du,dw,dp,dg,dk,dr,dks,dth:datafile
#choice:string
#constant mark: "."
#function save(nama: string, data:datafile, mark)
def exit(du,dw,dp,dg,dk,dr,dks,dth,mark):
    choice=str(input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)?: "))
    if(choice=="y" or choice=="Y"):
        save("User",du,mark)         
        save("Daftar Wahana",dw,mark)
        save("Pembelian Tiket",dp,mark)
        save("Penggunaan Tiket",dg,mark)
        save("Kepemilikan Tiket",dk,mark)
        save("Refund Tiket",dr,mark)
        save("Kritik dan Saran",dks,mark)
        save("Kehilangan Tiket",dth,mark)
        print("Data berhasil disimpan")
    elif(choice=="N" or choice=="n"):
        print("Keluar tanpa menyimpan")
    else:
        print("Input invalid") 

#fungsi penyimpanan password
#terdiri dari enc(decpass: string) dan dec(epass: string)
#enkripsi dekripsi pass

#fungsi enc(decpass: string)
#passw: array of character
#new: array of integer
#fin: string
#i: integer
#temp: character
def enc(decpass):
    passw=[]
    for i in range(len(decpass)):
        passw+=[decpass[i]]

    for i in range(len(passw)):
        temp=passw[i]
        passw[i]=passw[i-3]
        passw[i-3]=temp

    
    new=[]
    for i in range(len(passw)):
        new+=[ord(passw[i])]

    for i in range(len(new)):
        if(int(new[i])%2==0):
            new[i]=new[i]//2
            if(int(new[i])<10):
                new[i]+=1000
            elif(int(new[i])<20):
                new[i]+=2000
            elif(int(new[i])<30):
                new[i]+=3000
        else:
            new[i]+=5000
            if(new[i]>5070):
                new[i]-=330

    fin=""
    for i in range(len(new)):
        new[i]=chr(new[i])
        fin+=new[i]

    return fin

#fungsi dec(epass: string)
#passw: array of integer
#i: integer
#init: string
def dec(epass):
    #pass sudah tersedia
    passw=[]
    for i in range(len(epass)):
        passw+=[ord(epass[i])]

    for i in range(len(passw)):
        if(passw[i]>5000):
            passw[i]-=5000
        elif(passw[i]>=4740):
            passw[i]-=4670
        elif(passw[i]>3000):
            passw[i]-=3000
            passw[i]=passw[i]*2
        elif(passw[i]>2000):
            passw[i]-=2000
            passw[i]=passw[i]*2
        elif(passw[i]>1000):
            passw[i]-=1000
            passw[i]=passw[i]*2
        else:
            passw[i]=passw[i]*2

    for i in range(len(passw)-1,-1,-1):
        temp=passw[i]
        passw[i]=passw[i-3]
        passw[i-3]=temp

    init=""
    for i in range(len(passw)):
        passw[i]=chr(passw[i])
        init+=passw[i]
    
    return init


#fungsi goldacc
#mengupgrade akun player ke gold 
#diakses oleh admin

#KAMUS LOKAL
#du: datafile
#uName: string
#harga: integer
#function isAda(df: datafile, param: string, idxcol: integer)
def goldacc(du):#Harga goldacc 999999
    uName=str(input("Masukkan username yang ingin di-upgrade: "))
    harga=999999
    if(isAda(du,uName,3)):
        if(int(du[locate(du,3,uName)][6])<harga):
            print("Saldo kurang, silakan topup terlebih dahulu")
        else:
            du[locate(du,3,uName)][6]=int(du[locate(du,3,uName)][6])-harga
            du[locate(du,3,uName)][7]="Gold"
            print("Akun Anda telah diupgrade")
            return du
    else:
        print("Username tidak terdaftar")
    
    return du

#fungsi bestWahana
#menampilkan 3 wahana terbaik berdasarkan pembelian tiket

#KAMUS LOKAL
#dw,dp: datafile
#jmlwhn,i,j,no1,no2,no3,total: integer
#mtemp,ranks: array of array of string
#idx1,idx2,idx3,nama1,nama2,nama3,rank1,rank2,rank3: string
#function inputdata(df:datafile, jmlcol: integer, newdata:array of string)
def bestWahana(dw,dp):
    jmlwhn=0
    i=0
    while(str(dw[i][0])!="0"):
        jmlwhn+=1
        i+=1
    
    mtemp=[]#[[idx,nama,jml]]
    for i in range(jmlwhn):
        total=0
        for j in range (10):
            if(dw[i][0]==dp[j][2]):
                total+=int(dp[j][3])
        mtemp+=[[dw[i][0],dw[i][1],str(total)]]

    
    ranks=[["0" for i in range(4)] for j in range (10)]
    no1=0
    no2=0
    no3=0
    for i in range(jmlwhn):
        if(int(mtemp[i][2])>no1):
            no1=int(mtemp[i][2])
            idx1=mtemp[i][0]
            nama1=mtemp[i][1]
    rank1=["1",idx1,nama1,no1]
    ranks=inputdata(ranks,4,rank1)

    for i in range(jmlwhn):
        if(int(mtemp[i][2])>no2 and mtemp[i][0]!=idx1):
            no2=int(mtemp[i][2])
            idx2=mtemp[i][0]
            nama2=mtemp[i][1]
    rank2=["2",idx2,nama2,no2]
    ranks=inputdata(ranks,4,rank2)

    for i in range(jmlwhn):
        if(int(mtemp[i][2])>no3 and (mtemp[i][0]!=idx1 and mtemp[i][0]!=idx2)):
            no3=int(mtemp[i][2])
            idx3=mtemp[i][0]
            nama3=mtemp[i][1]
    rank3=["3",idx3,nama3,no3]
    ranks=inputdata(ranks,4,rank3)

    for i in range (3):
        print(str(ranks[i][0])+" | "+str(ranks[i][1])+" | "+str(ranks[i][2])+" | "+str(ranks[i][3]))

#fungsi tikethilang
#mencatat keluhan pemain yang mengalami kehilangan tiket

#KAMUS LOKAL
#dk,dth,dw,du, newdth: datafile
#uName,tgl, id:string
#i, jml: integer
#isFound: boolean
#arr: array of string
#function isAda(df: datafile, param: string, idxcol: integer)
#function tglTrue(tl: string)
#function inputdata(df: datafile, jmlcol:integer, newdata:array of string)
def tikethilang(dk,dth,dw,du):
    uName=str(input("Masukkan username: "))
    tgl=str(input("Tanggal kehilangan tiket (DD/MM/YYYY): "))
    if(not tglTrue(tgl)):
        tgl=str(input("Tanggal invalid. Tanggal kehilangan tiket (DD/MM/YYYY): "))
    id=str(input("ID wahana: "))
    if(not isAda(dw,id,0)):
        id=str(input("ID wahana tidak ditemukan. ID wahana: "))
    jml=int(input("Jumlah tiket yang dihilangkan: "))

    isFound=False
    if(isAda(du,uName,3)):
        for i in range(10):
            if(dk[i][0]==uName):
                if(dk[i][1]==id):
                    if(int(dk[i][2])>=jml):
                        dk[i][2]=str(int(dk[i][2])-jml)
                        isFound=True
                    else:
                        print("Jumlah tiket anda kurang dari tiket yang hilang")
    else:
        print("Username tidak terdaftar")
        return dk,dth

    if(isFound):
        arr=[uName,tgl,id,jml]
        newdth=inputdata(dth,4,arr)
        print("Laporan kehilangan tiket Anda telah direkam.")
        return dk,newdth
    else:
        print("Username tidak memiliki tiket wahana tersebut")


#PROGRAM
mark="."

du=load("User",mark)
dw=load("File Wahana",mark)
dp=load("Pembelian Tiket",mark)
dg=load("Penggunaan Tiket",mark)
dk=load("Kepemilikan Tiket",mark)
dr=load("Refund Tiket",mark)
dks=load("Kritik dan Saran",mark)
dth=load("Kehilangan Tiket",mark)
print("File perusahaan Willy Wangky's Chocolate Factory telah di-load")

isOn=True
isLogin=False
isSave=False
while(isOn):
    print("---------------------------------------------------------")
    print("Pilih untuk masuk: ")
    print("1.Sign up")
    print("2.Log in")
    print("3.Close Program")
    choice=int(input())
    while(not(choice==1 or choice==2 or choice==3)):
        print("Pilihan Invalid")
        print("Pilih untuk masuk: ")
        print("1.Sign up")
        print("2.Log in")
        print("3.Close Program")
        choice=int(input())
    if(choice==1):
        du=signup(du)
    elif(choice==2):
        isValid,uName=login(du)
        while ((not isValid) and (uName==0)):
            retry=str(input("Ingin mengulangi proses login (Y/N)?: "))
            while(not (retry=="Y" or retry=="y" or retry=="n" or retry=="N")):
                print("Input Invalid")
                retry=str(input("Ingin mengulangi proses login (Y/N)?: "))
            if(retry=="N" or retry=="n"):
                isValid=True
                uName="1"
            else:
                isValid, uName=login(du)
        if(uName!="1"):
            input("----------------- press enter -----------------")
            isLogin=True
            while(isLogin):
                role=du[locate(du,3,uName)][5]
                if(role=="Admin"):
                    print("Pilih layanan: ")
                    print("1. Pencarian Pemain")
                    print("2. Pencarian Wahana")
                    print("3. Top-up")
                    print("4. Menambahkan Wahana Baru")
                    print("5. Kritik dan Saran Pemain")
                    print("6. Riwayat Penggunaan Wahana")
                    print("7. Jumlah Tiket Pemain")
                    print("8. Golden Account")
                    print("9. Wahana Terpopuler")
                    print("10. Logout")
                    choice=int(input())
                    if (choice==1):
                        cariPemain(du)
                        input("----------------- press enter -----------------")
                    elif (choice==2):
                        cariWahana(dw)
                        input("----------------- press enter -----------------")
                    elif (choice==3):
                        du=topup(du)
                        input("----------------- press enter -----------------")
                    elif (choice==4):
                        dw=addWahana(dw)
                        input("----------------- press enter -----------------")
                    elif(choice==5):
                        review(dks)
                        input("----------------- press enter -----------------")
                    elif(choice==6):
                        riwayat(dg,dw)
                        input("----------------- press enter -----------------")
                    elif(choice==7):
                        jumlah(dk,dw)
                        input("----------------- press enter -----------------")
                    elif(choice==8):
                        du=goldacc(du)
                        input("----------------- press enter -----------------")
                    elif(choice==9):
                        bestWahana(dw,dp)
                        input("----------------- press enter -----------------")
                    elif(choice==10):
                        exit(du,dw,dp,dg,dk,dr,dks,dth,mark)
                        isLogin=False
                        isSave=True
                        print("Kembali ke halaman login")
                    else:
                        print("Pilihan invalid")
                        input("----------------- press enter -----------------")
                else:
                    print("Pilih layanan: ")
                    print("1. Bermain di wahana")
                    print("2. Beli Tiket")
                    print("3. Refund Tiket")
                    print("4. Beri Kritik dan Saran")
                    print("5. Kehilangan Tiket")
                    print("6. Cari Wahana")
                    print("7. Logout")
                    choice=int(input())
                    if (choice==1):
                        dk,dg=useTiket(uName,dk,dg,dw)
                        input("----------------- press enter -----------------")
                    elif (choice==2):
                        du,dk,dp=beliTiket(uName,du,dw,dk,dp)
                        input("----------------- press enter -----------------")
                    elif (choice==3):
                        du,dk,dr=refund(uName,du,dw,dk,dr)
                        input("----------------- press enter -----------------")
                    elif (choice==4):
                        dks=saran(uName,dks,dw)
                        input("----------------- press enter -----------------")
                    elif(choice==5):
                        dk,dth=tikethilang(dk,dth,dw,du)
                        input("----------------- press enter -----------------")
                    elif(choice==6):
                        cariWahana(dw)
                        input("----------------- press enter -----------------")
                    elif(choice==7):
                        exit(du,dw,dp,dg,dk,dr,dks,dth,mark)
                        isLogin=False
                        isSave=True
                        print("Kembali ke halaman login")
                    else:
                        print("Pilihan Invalid")
                        input("----------------- press enter -----------------")
        else:
            print("Kembali ke halaman login")    
    else:
        if(not isSave):
            exit(du,dw,dp,dg,dk,dr,dks,dth,mark)
        agree=str(input("Akan menutup program, Anda yakin (Y/N)?: "))
        while(not (agree=="Y" or agree=="y" or agree=="n" or agree=="N")):
            print("Input Invalid")
            agree=str(input("Akan menutup program, Anda yakin (Y/N)?: "))
        if(agree=="Y" or agree=="y"):
            isOn=False

