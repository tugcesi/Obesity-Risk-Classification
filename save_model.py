import pandas as pd
import numpy as np
import pickle
from xgboost import XGBClassifier

# ── Veri Yükleme ──────────────────────────────────────────────────────────────
train = pd.read_csv('train.csv')

# ── Feature Engineering ───────────────────────────────────────────────────────
def feature_engineering(df):
    df = df.copy()
    df['BMI']                = df['Weight'] / (df['Height'] ** 2)
    df['Weight_Height_Ratio']= df['Weight'] / df['Height']
    df['Active_Score']       = df['FAF'] - df['TUE']
    df['Diet_Score']         = df['CH2O'] + df['FCVC']

    df['Gender']                          = (df['Gender'] == 'Male').astype(int)
    df['family_history_with_overweight']  = (df['family_history_with_overweight'] == 'yes').astype(int)
    df['FAVC']  = (df['FAVC']  == 'yes').astype(int)
    df['SMOKE'] = (df['SMOKE'] == 'yes').astype(int)
    df['SCC']   = (df['SCC']   == 'yes').astype(int)

    caec_map   = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}
    calc_map   = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}
    mtrans_map = {'Walking': 0, 'Bike': 1, 'Public_Transportation': 2, 'Motorbike': 3, 'Automobile': 4}

    df['CAEC']   = df['CAEC'].map(caec_map)
    df['CALC']   = df['CALC'].map(calc_map)
    df['MTRANS'] = df['MTRANS'].map(mtrans_map)

    df.drop(columns=['id', 'SMOKE', 'NCP', 'MTRANS'], inplace=True, errors='ignore')
    return df

target_map = {
    'Insufficient_Weight': 0, 'Normal_Weight': 1,
    'Overweight_Level_I': 2,  'Overweight_Level_II': 3,
    'Obesity_Type_I': 4,      'Obesity_Type_II': 5, 'Obesity_Type_III': 6
}

df = feature_engineering(train)
X = df.drop(columns=['NObeyesdad'])
y = df['NObeyesdad'].map(target_map)

# ── Model Eğitimi ─────────────────────────────────────────────────────────────
model = XGBClassifier(eval_metric='mlogloss', verbosity=0, random_state=42)
model.fit(X, y)

# ── Kaydet ───────────────────────────────────────────────────────────────────
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model kaydedildi → model.pkl")
print(f"Feature sayısı: {X.shape[1]}")
