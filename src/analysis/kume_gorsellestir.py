import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def kume_gorsellestir():
    dosya_yolu = "outputs/kume_sonuclari.csv" # Alternatif kontrol
    if not os.path.exists("outputs/kumeleme_sonuclari.csv"):
        print("Hata: kumeleme_sonuclari.csv bulunamadı!")
        return
        
    df = pd.read_csv("outputs/kumeleme_sonuclari.csv")
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df, 
        x='Toplam_Kalori', 
        y='Toplam_Protein', 
        hue='Besin_Kumesi', 
        palette='viridis', 
        s=100, 
        alpha=0.8
    )
    
    plt.title('ADÜ Menüleri Besin Dengesi Kümeleme Analizi (Kalori vs Protein)', fontsize=12)
    plt.xlabel('Toplam Kalori (kcal)', fontsize=10)
    plt.ylabel('Toplam Protein (g)', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title='Besin Kümesi')
    
    os.makedirs("outputs/figures", exist_ok=True)
    cikti_resim = "outputs/figures/kumeleme_dagilimi.png"
    plt.savefig(cikti_resim, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Kümeleme görseli başarıyla {cikti_resim} konumuna kaydedildi!")

if __name__ == "__main__":
    kume_gorsellestir()