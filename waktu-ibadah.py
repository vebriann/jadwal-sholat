import os,sys,time,json,requests,datetime


# Author By VebrianDev

# list API

# https://jadwal-shalat-api.herokuapp.com/daily?date=tahun-bulan-hari&cityId=id kota
# https://jadwal-shalat-api.herokuapp.com/cities

# simpan sini ae lah
nama_kota, total_kota, waktu = [], [], []

# API server tahun - bulan - hari
url = "https://raw.githubusercontent.com/vebriann/database-server/main/data-waktu.json"

# API cek id kota
urll = "https://jadwal-shalat-api.herokuapp.com/cities"


timer = datetime.date.today()


def main():
    waktu.append(timer)
    try:
        response = requests.get(urll).json()
        for i in response["data"]:
            nama_kota.append(i["cityName"])
        for x in range(len(nama_kota)):
            total_kota.append(str(x+1))
            print(x+1,nama_kota[x])
        pilih = input(" ! pilih angka sesuai kota anda\n ? piih: ")
        if int(pilih) <= len(total_kota):
            hasil(pilih)
        elif int(pilih) <= int(0):
            print(f" ! maaf kota pada nomor {pilih} tidak tersedia")
            exit()
        else:
            print(f" ! maaf kota pada nomor {pilih} tidak tersedia")
            exit()
    except (KeyError,IOError):
        print(f" ! maaf response {response}")
        exit()

def hasil(pilihan):
    try:
        response = requests.get(f"https://jadwal-shalat-api.herokuapp.com/daily?date={str(waktu[0])}&cityId={pilihan}").json()
        if response["status"] == True:
            for i in response["data"]["data"]:
                print(f" Waktu {i['name']} : {i['time']}")
        else:
            print(" ! maaf data tidak ada ")
    except (KeyError,IOError):
        print(f" ! maaf response {response}")
        exit()

def service():
    print(" ! maaf program masih dalam pengembangan dan perbaikan bug")
    exit()

if __name__=="__main__":
    #service()
    main()