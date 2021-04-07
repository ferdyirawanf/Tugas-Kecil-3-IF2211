import pythonfile.BacaSqlite as BS
import pythonfile.TucilAstar as TA
import pythonfile.JarakEulidean as JE
import pythonfile.MakeHTML as MH
import pythonfile.MakeSqlite as MS
import os

def Tampilan_Awal():
    print(
    """
===================================================================
   Implementasi Algoritma A* untuk Menentukan Lintasan Terpendek
             Tugas Kecil 2 IF2211 Strategi Algoritma
                   Semester II tahun 2020/2021
===================================================================\n""" 
            )

def List_file_test ():
    #membaca list file yang ada di file test
    print("\nDaftar file test :\n")
    path = "../test"
    Dir_test = os.listdir(path)
    for namefile in Dir_test:
        print(namefile)

def input_file ():
    nfile = input("\nMasukkan Nama File\n:> ")
    try:
        path = "../test/"+str(nfile)
        MS.FiletoSql(path)
    except:
        print("\n================= ============================== =================\n")
        print("Maaf Nama File salah")
        print("\n================= ============================== =================\n")

def Daftar_Simpul():
    count = 1
    print("\nDaftar Lokasi : ")
    for text in BS.getSimpulAll():
        print(str(count) + str("."),text)
        count += 1

def Input_Asal_Tujuan():
    print("\n")
    NameSimpulAsal = input("Masukkan Nama Lokai Awal: > ")
    NameSimpulTujuan = input("Masukkan Nama Lokai Tujuan: > ")
    MH.ExportHTML(NameSimpulAsal, NameSimpulTujuan)
    print("Silahkan Buka file 'index.html' untuk melihat visualisasi hasil.")


        



#MAIN PROGRAM
Tampilan_Awal()
List_file_test ()
input_file ()
Daftar_Simpul()
Input_Asal_Tujuan()



