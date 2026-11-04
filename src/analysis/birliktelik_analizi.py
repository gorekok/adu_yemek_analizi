import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import os

def menu_birliktelik_analizi():
    dosya_yolu = "outputs/temizlenmis_menu.csv"
    
    if not os.path.exists(dosya_yolu):
        print(f"Hata: {dosya_yolu} bulunamadı! Lütfen önce veri temizleme adımını çalıştırın.")
        return
        
    print("Temizlenmiş menü verisi okunuyor ve birliktelik analizi hazırlanıyor...")
    df = pd.read_csv(dosya_yolu)
    
    yemek_sutunlari = [col for col in df.columns if 'Yemek' in col]
    
    sepetler = []
    for _, row in df.iterrows():
        sepet = [str(row[col]).strip() for col in yemek_sutunlari if pd.notna(row[col]) and str(row[col]).strip() != ""]
        if sepet:
            sepetler.append(sepet)
            
    print(f"Toplam analiz edilen menü (sepet) sayısı: {len(sepetler)}")
    
    te = TransactionEncoder()
    te_ary = te.fit(sepetler).transform(sepetler)
    df_trans = pd.DataFrame(te_ary, columns=te.columns_)
    
    frequent_itemsets = apriori(df_trans, min_support=0.01, use_colnames=True)
    
    if frequent_itemsets.empty:
        print("Uyarı: Belirlenen minimum destek oranında sık tekrar eden öğe bulunamadı. Veri seti genişledikçe kurallar artacaktır.")
        return
        
    kurallar = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
    
    print("\n--- Elde Edilen Birliktelik Kuralları (Örnekler) ---")
    if not kurallar.empty:
        print(kurallar[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))
        
        os.makedirs("outputs", exist_ok=True)
        cikti_yolu = "outputs/birliktelik_sonuclari.csv"
        kurallar.to_csv(cikti_yolu, index=False)
        print(f"\nBirliktelik analizi sonuçları başarıyla {cikti_yolu} konumuna kaydedildi!")
    else:
        print("Yeterli güven eşiğinde kural üretilemedi.")

if __name__ == "__main__":
    menu_birliktelik_analizi()