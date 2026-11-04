import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # TensorFlow uyarılarını gizler

import os
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.dummy import DummyClassifier
import numpy as np

def cnn_ve_baseline_model_kurulumu():
    print("Derin Öğrenme (CNN) ve Baseline model altyapısı hazırlanıyor...")
    
    # Simüle edilmiş özellik ve görüntü tensörleri (Kaggle/Özgün veri entegrasyonu öncesi mimari testi)
    X_dummy_images = np.random.rand(100, 128, 128, 3) # 100 adet 128x128 RGB görsel simülasyonu
    y_dummy_labels = np.random.randint(0, 4, 100)      # 4 farklı yemek sınıfı
    
    # 1. Baseline Model (Dummy Classifier - Karşılaştırma için temel eşik)
    print("\n--- Baseline Model Eğitiliyor ---")
    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_dummy_images.reshape(100, -1), y_dummy_labels)
    baseline_skor = baseline.score(X_dummy_images.reshape(100, -1), y_dummy_labels)
    print(f"Baseline (Temel) Model Doğruluk Oranı: {baseline_skor:.4f}")
    
    # 2. CNN Model Mimarisi (Özgün Derin Öğrenme Modeli)
    print("\n--- CNN Model Mimarisi İnşa Ediliyor ---")
    model = models.Sequential([
        layers.Input(shape=(128, 128, 3)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(4, activation='softmax') # 4 yemek sınıfı çıkışı
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print(model.summary())
    
    os.makedirs("outputs/models", exist_ok=True)
    model_yolu = "outputs/models/adu_ yemek_cnn.keras"
    model.save(model_yolu)
    print(f"\nCNN modeli başarıyla derlendi ve {model_yolu} konumuna kaydedildi!")

if __name__ == "__main__":
    cnn_ve_baseline_model_kurulumu()