import streamlit as st
import joblib
import numpy as np

# تحميل النموذج
model = joblib.load("model.pkl")

# عنوان
st.title("🚗 توقع سعر السيارة")

# واجهة إدخال بيانات
year = st.number_input("سنة الإنتاج", 1990, 2025, 2015)
mileage = st.number_input("عدد الكيلومترات", 0, 1000000, 50000)
engine = st.number_input("حجم المحرك", 0.5, 8.0, 2.0)
cylinders = st.slider("عدد السلندرات", 1, 16, 4)
doors = st.slider("عدد الأبواب", 2, 5, 4)

# عند الضغط على زر التوقع
if st.button("توقّع السعر"):
    input_data = np.array([[year, mileage, engine, cylinders, doors]])
    prediction = model.predict(input_data)
    st.success(f"✅ السعر المتوقع: {prediction[0]:,.0f} ريال")
