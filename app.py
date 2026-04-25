import streamlit as st
import pandas as pd
import numpy as np
import pickle

# ── Model Yükleme ─────────────────────────────────────────────────────────────
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

target_map_inverse = {
    0: 'Insufficient Weight',
    1: 'Normal Weight',
    2: 'Overweight Level I',
    3: 'Overweight Level II',
    4: 'Obesity Type I',
    5: 'Obesity Type II',
    6: 'Obesity Type III'
}

label_colors = {
    'Insufficient Weight' : '#3498db',
    'Normal Weight'       : '#2ecc71',
    'Overweight Level I'  : '#f1c40f',
    'Overweight Level II' : '#e67e22',
    'Obesity Type I'      : '#e74c3c',
    'Obesity Type II'     : '#c0392b',
    'Obesity Type III'    : '#922b21'
}

# ── Sayfa Ayarları ────────────────────────────────────────────────────────────
st.set_page_config(page_title='Obezite Risk Tahmini', page_icon='⚖️', layout='centered')
st.title('⚖️ Obezite Risk Tahmini')
st.markdown('Bilgilerinizi girerek obezite risk sınıfınızı öğrenin.')
st.divider()

# ── Kullanıcı Girdileri ───────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    gender  = st.selectbox('Cinsiyet', ['Male', 'Female'])
    age     = st.slider('Yaş', 14, 65, 25)
    height  = st.number_input('Boy (m)', 1.45, 1.98, 1.70, step=0.01)
    weight  = st.number_input('Kilo (kg)', 39.0, 170.0, 70.0, step=0.5)
    family  = st.selectbox('Ailede Obezite Geçmişi', ['yes', 'no'])
    favc    = st.selectbox('Yüksek Kalorili Yiyecek Tüketimi (FAVC)', ['yes', 'no'])

with col2:
    fcvc    = st.slider('Sebze Tüketimi (FCVC)', 1.0, 3.0, 2.0, step=0.1)
    ch2o    = st.slider('Günlük Su Tüketimi (CH2O)', 1.0, 3.0, 2.0, step=0.1)
    faf     = st.slider('Fiziksel Aktivite Sıklığı (FAF)', 0.0, 3.0, 1.0, step=0.1)
    tue     = st.slider('Teknoloji Kullanım Süresi (TUE)', 0.0, 2.0, 1.0, step=0.1)
    caec    = st.selectbox('Öğünler Arası Yeme (CAEC)', ['no', 'Sometimes', 'Frequently', 'Always'])
    calc    = st.selectbox('Alkol Tüketimi (CALC)', ['no', 'Sometimes', 'Frequently', 'Always'])
    scc     = st.selectbox('Kalori Takibi (SCC)', ['yes', 'no'])

st.divider()

# ── Tahmin ────────────────────────────────────────────────────────────────────
if st.button('🔍 Tahmin Et', use_container_width=True):

    caec_map = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}
    calc_map = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always': 3}

    bmi                 = weight / (height ** 2)
    weight_height_ratio = weight / height
    active_score        = faf - tue
    diet_score          = ch2o + fcvc

    input_data = pd.DataFrame([{
        'Gender'                        : 1 if gender == 'Male' else 0,
        'Age'                           : age,
        'Height'                        : height,
        'Weight'                        : weight,
        'family_history_with_overweight': 1 if family == 'yes' else 0,
        'FAVC'                          : 1 if favc == 'yes' else 0,
        'FCVC'                          : fcvc,
        'CAEC'                          : caec_map[caec],
        'SCC'                           : 1 if scc == 'yes' else 0,
        'FAF'                           : faf,
        'TUE'                           : tue,
        'CALC'                          : calc_map[calc],
        'BMI'                           : bmi,
        'Active_Score'                  : active_score,
        'Diet_Score'                    : diet_score,
        'Weight_Height_Ratio'           : weight_height_ratio
    }])

    pred        = model.predict(input_data)[0]
    pred_proba  = model.predict_proba(input_data)[0]
    label       = target_map_inverse[pred]
    color       = label_colors[label]

    st.markdown(f"""
    <div style='background-color:{color}22; border-left:6px solid {color};
                padding:20px; border-radius:8px; margin-top:10px'>
        <h2 style='color:{color}; margin:0'>🎯 {label}</h2>
        <p style='margin:5px 0 0 0; color:#555'>BMI: <b>{bmi:.1f}</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('#### 📊 Sınıf Olasılıkları')
    proba_df = pd.DataFrame({
        'Sınıf'    : list(target_map_inverse.values()),
        'Olasılık' : pred_proba
    }).sort_values('Olasılık', ascending=False)

    st.bar_chart(proba_df.set_index('Sınıf')['Olasılık'])