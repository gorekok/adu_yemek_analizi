import pandas as pd
import os

def veri_analizi_ve_temizleme():
    dosya_yolu = "data/raw/gunluk_menu.csv"
    
    if not os.path.exists(dosya_yolu):
        print(f"Hata: {dosya_yolu} bulunamadı! Lütfen önce veri kazıma adımını çalıştırın.")
        return
        
    print("Ham veri dosyası okunuyor...")
    df = pd.read_csv(dosya_yolu)
    
    print(f"\n--- Orijinal Veri Boyutu ve Bilgileri ---")
    print(f"Toplam Satır/Sütun: {df.shape}")
    print(df.head())
    
    # 1. Veri Temizleme: Yinelenen (tekrar eden) satırları temizleme
    print("\n[Temizlik] Tekrar eden (duplicate) satırlar temizleniyor...")
    temiz_df = df.drop_duplicates().copy()
    print(f"Temizleme sonrası satır/sütun: {temiz_df.shape}")
    
    # 2. Keşifsel Veri Analizi (EDA) Temelleri
    print("\n--- Keşifsel Veri Analizi (EDA) ---")
    print(f"Mevcut Tarihler: {temiz_df['Tarih'].unique()}")
    print(f"Öğün Dağılımı:\n{temiz_df['Ogun'].value_counts()}")
    
    # İşlenmiş temiz veriyi outputs klasörüne kaydedelim
    os.makedirs("outputs", exist_ok=True)
    cikti_yolu = "outputs/temizlenmis_menu.csv"
    temiz_df.to_csv(cikti_yolu, index=False)
    print(f"\nTemizlenmiş veri başarıyla {cikti_yolu} konumuna kaydedildi!")

if __name__ == "__main__":
    veri_analizi_ve_temizleme()