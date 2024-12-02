import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('trains1.sav', 'rb'))

def diabetes_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data_df)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
# std_data = scaler.transform(input_data_df)
# print(std_data)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return "the person is not diabetic"
    else:
        return"the person is diabetic"
    

def main():
    st.title('pred n check')

    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
    Glucose= st.text_input('glucose level')
    BloodPresure= st.text_input('BP value')
    SkinThickness = st.text_input(' Skin Thickness')
    Insulin = st.text_input('insuli level')
    BMI = st.text_input('BMIvalue')
    DiabetesPedigreeFunction = st.text_input(' Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')


    diagnosis = ' '

    if st.button('RESULT'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

        st.success(diagnosis)

if __name__ == '__main__':
    main()

