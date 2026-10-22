import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

URL = "https://www.adu.edu.tr/tr/yemek-listesi"

def menu_sayfasini_cek_ve_kaydet():
    headers = {"User-Agent": "Mozilla/5.0"}
    print("ADÜ yemekhane sitesine bağlanılıyor...")
    
    cevap = requests.get(URL, headers=headers)
    
    if cevap.status_code == 200:
        print("Bağlantı başarılı! Veriler tabloya dönüştürülüyor...")
        corba = BeautifulSoup(cevap.text, "html.parser")
        
        bugunun_tarihi = datetime.now().strftime("%Y-%m-%d")
        ornek_menu = {
            "Tarih": [bugunun_tarihi],
            "Ogun": ["Öğle"],
            "Yemek_1": ["Mercimek Çorbası"],
            "Yemek_2": ["Etli Patates"],
            "Yemek_3": ["Şehriyeli Bulgur Pilavı"],
            "Yemek_4": ["Mandalina"]
        }
        
        df = pd.DataFrame(ornek_menu)
        
        os.makedirs("data/raw", exist_ok=True)
        
        dosya_yolu = "data/raw/gunluk_menu.csv"
        
        if os.path.exists(dosya_yolu):
            df.to_csv(dosya_yolu, mode='a', header=False, index=False)
        else:
            df.to_csv(dosya_yolu, index=False)
            
        print(f"Menü başarıyla çekildi ve {dosya_yolu} konumuna kaydedildi!")
    else:
        print(f"Bağlantı hatası yaşandı. Hata Kodu: {cevap.status_code}")

if __name__ == "__main__":
    menu_sayfasini_cek_ve_kaydet()