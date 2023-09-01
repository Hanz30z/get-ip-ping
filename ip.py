import os
import colorama
from colorama import Fore,Back,Style

print("Tools Search ip dan ping")
print("1.Cari IP")
print("2.Ping IP")
print("3.Exit")

while True:
    select = int(input("Pilih Fitur:"))

    if select == 1:
        os.system('cmd /c "ipconfig /all"')
        print("Tools Search ip dan ping")
        print("1.Cari IP")
        print("2.Ping IP")
        print("3.Exit")
    elif select == 2:
        ip = str(input("Masukan Ip:"))
        Byte = str(input('Masukan Jumlah Byte:'))
        print(Fore.GREEN + "Berhasil melakukan ping "+ip+"")
        os.system('cmd /c "ping -l '+Byte+' '+ip+' -t"')
    elif select == 3:
        break

