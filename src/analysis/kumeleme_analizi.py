import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

def besin_dengesi_kumeleme():
    dosya_yolu = "outputs/temizlenmis_menu.csv"
    
    if not os.path.exists(dosya_yolu):
        print(f"Hata: {dosya_yolu} bulunamadı!")
        return
        
    df = pd.read_csv(dosya_yolu)
    
    besin_veritabani = {
        "Mercimek Çorbası": {"Kalori": 150, "Protein": 8, "Karbonhidrat": 20},
        "Ezogelin Çorbası": {"Kalori": 160, "Protein": 7, "Karbonhidrat": 22},
        "Yayla Çorbası": {"Kalori": 140, "Protein": 5, "Karbonhidrat": 18},
        "Domates Çorbası": {"Kalori": 120, "Protein": 3, "Karbonhidrat": 15},
        "Tarhana Çorbası": {"Kalori": 170, "Protein": 6, "Karbonhidrat": 25},
        "Etli Patetes": {"Kalori": 320, "Protein": 18, "Karbonhidrat": 30},
        "İzmir Köfte": {"Kalori": 380, "Protein": 22, "Karbonhidrat": 15},
        "Tavuk Sote": {"Kalori": 290, "Protein": 28, "Karbonhidrat": 10},
        "Kuru Fasulye": {"Kalori": 340, "Protein": 16, "Karbonhidrat": 45},
        "Orman Kebabı": {"Kalori": 310, "Protein": 19, "Karbonhidrat": 20},
        "Fırın Tavuk": {"Kalori": 270, "Protein": 30, "Karbonhidrat": 5},
        "Kıymalı Nohut": {"Kalori": 350, "Protein": 17, "Karbonhidrat": 40},
        "Şehriyeli Bulgur Pilavı": {"Kalori": 250, "Protein": 6, "Karbonhidrat": 45},
        "Pirinç Pilavı": {"Kalori": 260, "Protein": 5, "Karbonhidrat": 50},
        "Makarna": {"Kalori": 280, "Protein": 7, "Karbonhidrat": 52},
        "Erişte": {"Kalori": 270, "Protein": 6, "Karbonhidrat": 48},
        "Bulgur Pilavı": {"Kalori": 240, "Protein": 6, "Karbonhidrat": 42},
        "Mandalina": {"Kalori": 50, "Protein": 1, "Karbonhidrat": 12},
        "Elma": {"Kalori": 60, "Protein": 0, "Karbonhidrat": 15},
        "Muz": {"Kalori": 105, "Protein": 1, "Karbonhidrat": 27},
        "Sütlaç": {"Kalori": 220, "Protein": 5, "Karbonhidrat": 35},
        "Baklava": {"Kalori": 400, "Protein": 4, "Karbonhidrat": 55},
        "Meyve Suyu": {"Kalori": 110, "Protein": 0, "Karbonhidrat": 26},
        "Revani": {"Kalori": 320, "Protein": 4, "Karbonhidrat": 50}
    }
    
    toplam_kalori = []
    toplam_protein = []
    toplam_karbonhidrat = []
    
    yemek_sutunlari = [col for col in df.columns if 'Yemek' in col]
    
    for _, row in df.iterrows():
        kalori, protein, karbonhidrat = 0, 0, 0
        for col in yemek_sutunlari:
            yemek = str(row[col]).strip()
            if yemek in besin_veritabani:
                kalori += besin_veritabani[yemek]["Kalori"]
                protein += besin_veritabani[yemek]["Protein"]
                karbonhidrat += besin_veritabani[yemek]["Karbonhidrat"]
        toplam_kalori.append(kalori)
        toplam_protein.append(protein)
        toplam_karbonhidrat.append(karbonhidrat)
        
    df['Toplam_Kalori'] = toplam_kalori
    df['Toplam_Protein'] = toplam_protein
    df['Toplam_Karbonhidrat'] = toplam_karbonhidrat
    
    X = df[['Toplam_Kalori', 'Toplam_Protein', 'Toplam_Karbonhidrat']]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Besin_Kumesi'] = kmeans.fit_predict(X_scaled)
    
    cikti_yolu = "outputs/kumeleme_sonuclari.csv"
    df.to_csv(cikti_yolu, index=False, encoding="utf-8-sig")
    print(f"Kümeleme analizi tamamlandı ve {cikti_yolu} dosyasına kaydedildi!")
    print(df['Besin_Kumesi'].value_counts())

if __name__ == "__main__":
    besin_dengesi_kumeleme()