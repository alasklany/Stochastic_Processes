import streamlit as st
from BlModel import ChurnBL

model = ChurnBL("../Datasets/Churn/Telecom_Train.csv", "../Datasets/Churn/Telecom_Test.csv")

st.markdown("# Main ")
st.sidebar.markdown("# Main")

st.write("Dataset Test ratio: ", model.get_test_ratio())

