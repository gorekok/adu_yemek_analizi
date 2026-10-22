import requests
from bs4 import BeautifulSoup

URL = "https://www.adu.edu.tr/tr/yemek-listesi" 

def menu_sayfasini_cek():
    headers = {"User-Agent": "Mozilla/5.0"}
    print("ADÜ yemekhane sitesine bağlanılıyor...")
    
    cevap = requests.get(URL, headers=headers)
    
    if cevap.status_code == 200:
        print("Bağlantı başarılı! Sayfa verisi alındı.")
        corba = BeautifulSoup(cevap.text, "html.parser")
        print("Sitenin Başlığı:", corba.title.text)
    else:
        print(f"Bağlantı hatası yaşandı. Hata Kodu: {cevap.status_code}")

if __name__ == "__main__":
    menu_sayfasini_cek()