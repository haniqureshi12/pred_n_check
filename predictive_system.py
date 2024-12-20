import numpy as np
import pandas as pd
import pickle 
loaded_model = pickle.load(open('C:/Users/TAQI SHAH/Documents/Hani doc/ML projects/ml_project/trained_model.sav', 'rb'))

feature_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
                 "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
input_data = (5,166,72,19,175,25.8,0.587,51)
input_data_df = pd.DataFrame([input_data], columns=feature_names)
input_data_as_numpy_array = np.asarray(input_data_df)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
# std_data = scaler.transform(input_data_df)
# print(std_data)
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
if (prediction[0] == 0):
    print("the person is not diabetic")
else:
    print("the person is diabetic")