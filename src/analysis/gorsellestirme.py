import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def veri_gorsellestir():
    dosya_yolu = "outputs/temizlenmis_menu.csv"
    
    if not os.path.exists(dosya_yolu):
        print(f"Hata: {dosya_yolu} bulunamadı! Lütfen önce veri temizleme adımını çalıştırın.")
        return
        
    print("Temizlenmiş veri okunuyor ve görselleştirme hazırlanıyor...")
    df = pd.read_csv(dosya_yolu)
    
    # Görsel tema ayarları (Seaborn estetiği)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    
    # Öğün dağılımını sütun grafiği ile görselleştirme
    ogun_sayilari = df['Ogun'].value_counts()
    
    ax = sns.barplot(x=ogun_sayilari.index, y=ogun_sayilari.values, palette="Purples")
    plt.title("ADÜ Yemekhane - Öğün Dağılım Grafiği", fontsize=12, fontweight='bold')
    plt.xlabel("Öğün", fontsize=10)
    plt.ylabel("Kayıt / Menü Sayısı", fontsize=10)
    
    # Çıktı klasörünü oluştur ve grafiği kaydet
    os.makedirs("outputs/figures", exist_ok=True)
    cikti_resim = "outputs/figures/ogun_dagilimi.png"
    plt.savefig(cikti_resim, bbox_inches='tight')
    print(f"\nGrafik başarıyla kaydedildi: {cikti_resim}")
    
    plt.close()

if __name__ == "__main__":
    veri_gorsellestir()