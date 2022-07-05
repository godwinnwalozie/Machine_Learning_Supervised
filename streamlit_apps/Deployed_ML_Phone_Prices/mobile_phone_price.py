import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dython.nominal import associations
import seaborn as sns
from joblib import dump, load
import pickle
import  joblib
st.set_page_config(layout="wide")
from PIL import Image



# loading the saved model
pickled_model = pickle.load(open('C:/Users/godwi/GitHub/Machine_Learning_Supervised/streamlit_apps/Deployed_ML_Phone_Prices/estimator.pkl', 'rb'))

# Function to predict the prices
def phone_price (input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = pickled_model.predict(input_data_reshaped)
    print(prediction)


    if prediction [0] == 0:
        return "The price is in the LOW CLASS RANGE ! "
    elif prediction[0]  == 1:
        return "The price is in the MID CLASS RANGE!"
    elif prediction[0] == 2:
        return "The price is in the HIGH CLASS RANGE!"
    else:
        return "The price is in the SUPER CLASS RANGE!"
    




    
# user input
def main():
    
   
    st.sidebar.header(' Select features to make predictions')

    # getting data from user
    four_g = st.sidebar.radio('Has 4G ? (0 is No, 1 is Yes)',('1','0'))
    ##################################################

    # getting data from user
    three_g = st.sidebar.radio('Has 3G ? (0 is No, 1 is Yes)',('1','0'))
    ##################################################

    battery_power = st.sidebar.slider('The battery power in mAh',0,5000,2000)
    ##################################################

    ram = st.sidebar.slider('The RAM size in Gigabyte',2,8,4)
    ##################################################

    screen_height = st.sidebar.slider('The screen height in cm',8,25,10)
    ##################################################

    screen_width = st.sidebar.slider('The screen width in cm',5,25,12)
    ###########################################################


    Rear_camera = st.sidebar.slider('Rear Camera in Mega Pixels',0,64,48)
    ###########################################################

    front_camera = st.sidebar.slider('Front facing camera in Mega Pixels',0,20,15)
    ###########################################################

    pixel_height = st.sidebar.slider('The height in pixel',100,1500,1000)
    ###########################################################

    pixel_width = st.sidebar.slider('The width in pixel',100,1500,1000)
    ###################################################

    
    # code for prediction
    prediction =  ''

    # creating a button for prediction
    
    with col2:
        if st.sidebar.button("Predict Price Class"):
            prediction = phone_price([battery_power,four_g,ram,screen_height,screen_width,	three_g	,
            Rear_camera,front_camera,pixel_width,pixel_height])
            st.success(prediction)
        else:
            st.write('##### Your Prediction will display here !!')
            
            
        image = Image.open('C:/Users/godwi/Pictures/deep_learning.jpg') 
        st.image(image)



if __name__ == "__main__":
    
    
   
    st.write(' ### **Thank you for visiting my Machine Learning WebApp**')
    st.write('###### Scikit-learn is a free software tool, designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.')
    st.markdown("""
        Estimator used is **RandomForestClassifier** \
            to predict the **price class range** based on features . I hope you will appreciate my work
        """)
      
    #displaying the image on streamlit app
    col1, col2 = st.columns(2)

    with col1:
        #opening the image
        image = Image.open('C:/Users/godwi/Pictures/mazi6.JPG')
        st.image(image, caption=' ',width=300, use_column_width=258)
        st.markdown('Designed on Streamlit **_isn''t it_really cool !**')
        
        
        

    with col2:
    # streamlit preparation
        image = Image.open('C:/Users/godwi/Pictures/sklearn.png')
        st.image(image, caption='',width=120, use_column_width=120)
        

        

         


    main()
    
    with col1:
        image = Image.open('C:/Users/godwi/Pictures/deep_learning.jpg') 
        st.image(image)
