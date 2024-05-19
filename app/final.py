import streamlit as st
import pandas as pd
import joblib
#loading model and preprocessing so that user input undergoes same preprocessing to predict
preprocessing_pipeline = joblib.load('preprocessing_pipeline.joblib')
model = joblib.load('dt_model.joblib')

input_features = [
    'acrs_report_type',
    'collision_type',
    'weather',
    'driver_substance_abuse',
    'driver_at_fault',
    'driver_distracted_by',
    'vehicle_damage_extent',
    'vehicle_movement',
    'speed_limit',
    'vehicle_year',
    'vehicle_make',
    'latitude',
    'longitude',
    'road_name',
    'cross_street_type',
    'year',
    'day_of_week',
    'month',
    'hour',
    'vehicle_size',
    'day_or_night',
    'weekend'
]

import streamlit as st
import openai

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://t4.ftcdn.net/jpg/05/92/45/97/360_F_592459728_f9Cz94gzA8smJp0NGWtWMYkbpz6RWDjQ.jpg");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)

st.title("Injury Severity Predictor")

with st.form(key='input_form'):
    st.subheader("Crash Information")
    acrs_report_type = st.selectbox("ACRS Report Type", ['Property Damage Crash', 'Injury Crash', 'Fatal Crash'])
    collision_type = st.selectbox("Collision Type", [
        'SAME DIR REAR END',
        'STRAIGHT MOVEMENT ANGLE',
        'OTHER',
        'SAME DIRECTION SIDESWIPE',
        'SINGLE VEHICLE',
        'HEAD ON LEFT TURN',
        'SAME DIRECTION RIGHT TURN',
        'SAME DIRECTION LEFT TURN',
        'HEAD ON',
        'OPPOSITE DIRECTION SIDESWIPE',
        'ANGLE MEETS LEFT TURN',
        'ANGLE MEETS RIGHT TURN',
        'SAME DIR REND LEFT TURN',
        'SAME DIR BOTH LEFT TURN',
        'SAME DIR REND RIGHT TURN',
        'ANGLE MEETS LEFT HEAD ON',
        'OPPOSITE DIR BOTH LEFT TURN'])
    weather = st.selectbox("Weather", [
        'CLEAR',
        'RAINING',
        'CLOUDY',
        'OTHERS',
        'SNOW',
        'FOGGY'])
    driver_substance_abuse = st.selectbox("Driver Substance Abuse", [
        'NONE DETECTED',
        'OTHER',
        'ALCOHOL PRESENT',
        'ALCOHOL CONTRIBUTED',
        'ILLEGAL DRUG PRESENT',
        'MEDICATION PRESENT',
        'ILLEGAL DRUG CONTRIBUTED',
        'COMBINED SUBSTANCE PRESENT',
        'MEDICATION CONTRIBUTED',
        'COMBINATION CONTRIBUTED'])
    driver_at_fault = st.selectbox("Driver at Fault", ['Yes', 'No', 'Unknown'])
    driver_distracted_by = st.selectbox("Driver Distracted By", [
        'NOT DISTRACTED',
        'UNKNOWN',
        'LOOKED BUT DID NOT SEE',
        'INATTENTIVE OR LOST IN THOUGHT',
        'OTHER DISTRACTION',
        'DISTRACTED BY OUTSIDE PERSON OBJECT OR EVENT',
        'BY OTHER OCCUPANTS',
        'OTHER CELLULAR PHONE RELATED',
        'OTHER ELECTRONIC DEVICE (NAVIGATIONAL PALM PILOT)',
        'TALKING OR LISTENING TO CELLULAR PHONE',
        'NO DRIVER PRESENT',
        'BY MOVING OBJECT IN VEHICLE',
        'EATING OR DRINKING',
        'ADJUSTING AUDIO AND OR CLIMATE CONTROLS',
        'USING OTHER DEVICE CONTROLS INTEGRAL TO VEHICLE',
        'TEXTING FROM A CELLULAR PHONE',
        'USING DEVICE OBJECT BROUGHT INTO VEHICLE',
        'DIALING CELLULAR PHONE',
        'SMOKING RELATED'])
    st.subheader("Vehicle Information")
    vehicle_damage_extent = st.selectbox("Vehicle Damage Extent", ['DISABLING', 'FUNCTIONAL', 'SUPERFICIAL', 'DESTROYED', 'NO DAMAGE'])
    vehicle_movement = st.selectbox("Vehicle Movement", [
        'MOVING CONSTANT SPEED',
        'SLOWING OR STOPPING',
        'STOPPED IN TRAFFIC LANE',
        'MAKING LEFT TURN',
        'OTHERS',
        'ACCELERATING',
        'BACKING',
        'MAKING RIGHT TURN',
        'CHANGING LANES',
        'STARTING FROM LANE',
        'PARKED'])
    vehicle_make = st.selectbox("Vehicle Make", [
        'TOYOTA',
        'HONDA',
        'OTHERS',
        'FORD',
        'NISSAN',
        'CHEVROLET',
        'HYUNDAI',
        'DODGE',
        'VOLKSWAGEN',
        'MERCEDES BENZ',
        'LEXUS',
        'ACURA',
        'JEEP',
        'SUBARU',
        'BMW',
        'MAZDA',
        'KIA',
        'CHRYSLER',
        'AUDI',
        'INFINITY',
        'CADILLAC',
        'LINCOLN',
        'ISUZU',
        'LAND ROVER',
        'PORSCHE',
        'HARLEY DAVIDSON',
        'YAMAHA'])
    speed_limit = st.number_input("Speed Limit")
    vehicle_year = st.number_input("Vehicle Year")
    vehicle_size = st.selectbox("Vehicle Size", ['Light', 'Heavy'])

    st.subheader("Location Information")
    latitude = st.slider("Latitude", 38.0, 40.0, step=0.01)
    longitude = st.slider("Longitude", -79.0, -75.0, step=0.01)
    df = pd.DataFrame({'latitude': [latitude], 'longitude': [longitude]})
    st.map(df)


    road_name = st.selectbox("Road Name", [
        'OTHER',
        'GEORGIA AVE',
        'NEW HAMPSHIRE AVE',
        'FREDERICK RD',
        'ROCKVILLE PIKE',
        'CONNECTICUT AVE',
        'VEIRS MILL RD',
        'COLUMBIA PIKE',
        'RANDOLPH RD',
        'COLESVILLE RD',
        'SHADY GROVE RD',
        'UNIVERSITY BLVD E',
        'RIVER RD',
        'UNIVERSITY BLVD W',
        'OLD GEORGETOWN RD',
        'NORBECK RD',
        'RIDGE RD',
        'MONTGOMERY VILLAGE AVE',
        'CLOPPER RD',
        'GERMANTOWN RD',
        'WOODFIELD RD'])
    cross_street_type = st.selectbox("Cross Street Type", [
        'County',
        'Maryland (State)',
        'Municipality',
        'OTHER',
        'Unknown',
        'Ramp',
        'Other Public Roadway',
        'US (State)',
        'Government',
        'Interstate (State)',
        'Service Road'])

    st.subheader("Time Information")
    year = st.number_input("Year")
    day_of_week = st.selectbox("Day of Week", ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    month = st.selectbox("Month", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    hour = st.number_input("Hour")
    day_or_night = st.selectbox("Day or Night", ['day', 'night'])
    weekend = st.selectbox("Weekend", [True, False])

    submit_button = st.form_submit_button(label='Submit')

# Processing the input data
if submit_button:
    input_data = pd.DataFrame({
        'acrs_report_type': [acrs_report_type],
        'collision_type': [collision_type],
        'weather': [weather],
        'driver_substance_abuse': [driver_substance_abuse],
        'driver_at_fault': [driver_at_fault],
        'driver_distracted_by': [driver_distracted_by],
        'vehicle_damage_extent': [vehicle_damage_extent],
        'vehicle_movement': [vehicle_movement],
        'speed_limit': [speed_limit],
        'vehicle_year': [vehicle_year],
        'vehicle_make': [vehicle_make],
        'latitude': [latitude],
        'longitude': [longitude],
        'road_name': [road_name],
        'cross_street_type': [cross_street_type],
        'year': [year],
        'day_of_week': [day_of_week],
        'month': [month],
        'hour': [hour],
        'vehicle_size': [vehicle_size],
        'day_or_night': [day_or_night],
        'weekend': [weekend]
    })
    # using same pipeline as used for training
    input_data_encoded = pd.DataFrame(preprocessing_pipeline.transform(input_data))
    prediction = model.predict(input_data_encoded)
    st.write(f'Predicted injury severity: {prediction[0]}')
