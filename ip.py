import os
import requests
import json
import colorama
import getpass
from colorama import Fore,Back,Style

colorama.init()
os.system('CLS')
while True:
    print(Fore.RED +"="*35)
    print("     TOOLS PING DAN TRACKING IP")
    print("         Created BY HANZ30Z")
    print("="*35)
    Style.RESET_ALL
    print(Fore.YELLOW +"[+]1.Search DNS Server")
    print("[+]2.PING DNS Server")
    print("[+]3.Find My IP")
    print("[+]4.IP Tracker")
    print("[+]5.Exit")
    print("="*18)
    select = int(input("[<>]Pilih Fitur:"))

    if select == 1:
        print(Fore.GREEN)
        os.system('cmd /c "ipconfig /all"')
        print(Style.RESET_ALL)
    elif select == 2:
        print(Fore.YELLOW)
        ip = str(input("Masukan Ip:"))
        Byte = str(input('Masukan Jumlah Byte:'))
        print(Fore.GREEN + "Berhasil melakukan ping "+ip+"")
        os.system('cmd /c "ping -l '+Byte+' '+ip+' -t"')
        print(Style.RESET_ALL)
    elif select == 3:
        ipreq = requests.get(f"http://ip-api.com/json/")
        if ipreq.status_code == 200:
            data = json.loads(ipreq.text)
            if data["status"] == "success":
                print(Fore.GREEN)
                print("="*11)
                print("[v]Berhasil Mendapatkan Data!")
                print("IP Address Anda :", data["query"])
                print("ISP :", data["isp"])
                print("="*11)
                Style.RESET_ALL
    elif select == 4:
        print(Fore.YELLOW)
        print("="*18)
        print(" Traking IP")
        print("="*18)
        ip = input("[+]Masukan IP Address :")
        Style.RESET_ALL
        ipreq = requests.get(f"http://ip-api.com/json/{ip}")
        if ipreq.status_code == 200:
            data = json.loads(ipreq.text)
            if data["status"] == "success":
                print(Fore.GREEN)
                print("="*18)
                print("[v]Berhasil Mendapatkan Data!")
                print("="*18)
                print("Negara :", data["country"])
                print("Provinsi :", data["regionName"])
                print("Kota :", data["city"])
                print("kode Pos :", data["zip"])
                lat = data["lat"]
                lon = data["lon"]
                map = f"https://www.google.com/maps/@{lat},{lon},4z?entry=ttu"
                print("Lokasi :", lat,",",lon)
                print("Zona Waktu :", data["timezone"])
                print("Jaringan :", data["isp"])
                print("="*18)
            print(Style.RESET_ALL)

    elif select == 5:
        break


