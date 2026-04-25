# ⚖️ Obesity Risk Classification

Bu proje, [Kaggle Playground Series S4E2](https://www.kaggle.com/competitions/playground-series-s4e2) yarışması kapsamında obezite riskini tahmin etmek amacıyla geliştirilmiştir. Çok sınıflı sınıflandırma (multi-class classification) yaklaşımıyla bireylerin obezite risk sınıfı tahmin edilmektedir.

---

## 📁 Proje Yapısı

```
├── train.csv                                    # Eğitim verisi
├── test.csv                                     # Test verisi
├── obesity-risk-classification-with-ml.ipynb   # EDA, Feature Engineering, Modelleme
├── train_model.py                               # Modeli eğitip kaydeder
├── app.py                                       # Streamlit uygulaması
├── model.pkl                                    # Eğitilmiş model
├── requirements.txt                             # Gerekli kütüphaneler
└── README.md
```

---

## 🎯 Hedef Değişken

`NObeyesdad` — 7 farklı obezite sınıfı:

| Sınıf | Açıklama |
|---|---|
| Insufficient_Weight | Yetersiz Kilo |
| Normal_Weight | Normal Kilo |
| Overweight_Level_I | Fazla Kilo - Seviye I |
| Overweight_Level_II | Fazla Kilo - Seviye II |
| Obesity_Type_I | Obezite - Tip I |
| Obesity_Type_II | Obezite - Tip II |
| Obesity_Type_III | Obezite - Tip III |

---

## 🔧 Kullanılan Özellikler

### Orijinal Değişkenler
| Değişken | Açıklama |
|---|---|
| Gender | Cinsiyet |
| Age | Yaş |
| Height | Boy (m) |
| Weight | Kilo (kg) |
| family_history_with_overweight | Ailede obezite geçmişi |
| FAVC | Yüksek kalorili yiyecek tüketimi |
| FCVC | Sebze tüketim sıklığı |
| CAEC | Öğünler arası yeme alışkanlığı |
| CH2O | Günlük su tüketimi |
| SCC | Kalori takibi |
| FAF | Fiziksel aktivite sıklığı |
| TUE | Teknoloji kullanım süresi |
| CALC | Alkol tüketimi |

### Türetilen Değişkenler
| Değişken | Formül | Açıklama |
|---|---|---|
| BMI | Weight / Height² | Vücut kitle indeksi |
| Weight_Height_Ratio | Weight / Height | Ağırlık/boy oranı |
| Active_Score | FAF − TUE | Aktif yaşam skoru |
| Diet_Score | CH2O + FCVC | Beslenme kalitesi skoru |

---

## 📊 Proje Adımları

1. **EDA & Görselleştirme** — Dağılımlar, korelasyon analizi, kategorik değişken analizi
2. **Feature Engineering** — BMI türetme, ordinal & binary encoding
3. **Model Karşılaştırma** — 10 farklı algoritma test edildi
4. **Final Model** — XGBoost seçildi

---

## 🤖 Model Performansı

Karşılaştırılan modeller:

- BernoulliNB
- LogisticRegression
- DecisionTreeClassifier
- RandomForestClassifier
- GradientBoostingClassifier
- KNeighborsClassifier
- AdaBoostClassifier
- **XGBClassifier** ✅ En iyi
- LGBMClassifier
- CatBoostClassifier

---

## 🚀 Kurulum & Çalıştırma

```bash
# 1. Repoyu klonla
git clone https://github.com/tugcesi/Obesity-Risk-Classification.git
cd Obesity-Risk-Classification

# 2. Gereksinimleri yükle
pip install -r requirements.txt

# 3. Modeli eğit
python train_model.py

# 4. Uygulamayı başlat
streamlit run app.py
```

---

## 🖥️ Streamlit Uygulaması

Uygulama aracılığıyla:
- Kişisel bilgilerinizi (yaş, boy, kilo vb.) girerek obezite risk sınıfınızı öğrenebilirsiniz
- Her sınıf için tahmin olasılıklarını grafik olarak görebilirsiniz

---

## 🛠️ Kullanılan Teknolojiler

![Python](https://img.shields.io/badge/Python-3.10-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-latest-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-latest-red)
![Pandas](https://img.shields.io/badge/Pandas-latest-150458?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-latest-F7931E)

---

## 📄 Lisans

Bu proje MIT lisansı ile lisanslanmıştır.
