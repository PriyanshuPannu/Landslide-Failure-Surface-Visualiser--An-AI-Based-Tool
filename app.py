import pyslope
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import joblib
from pyslope import (Slope,Material)

# Create a Streamlit web app
def main():
    st.title("Landslide Prediction and Failure Surface Visualizer")
    h = st.number_input('Enter the Slope height')
    l = st.number_input('Enter the Slope length')
    
    def get_predictions(h,l):
        model = joblib.load("fos_model.sav")
        return model.predict([[h,l]])
    
    if st.button('Visualize'):
        s = Slope(height=h,length=l, angle=None)
        m1 = Material(unit_weight=18.7,friction_angle=28.2,cohesion=10,depth_to_bottom=30)
        s.set_materials(m1)
        s.set_water_table(1)
        s.set_analysis_limits(s.get_top_coordinates()[0] - 5, s.get_bottom_coordinates()[0] + 5)
        # run calculations on the created slope
        s.analyse_slope()
        # plot all failure planes with a FOS below 2
        fig_1=s.plot_all_planes(max_fos=2)
        fig_1.update_layout(width=800, height=600) 
        st.plotly_chart(fig_1)
    
    if st.button("Predict Factor of Safety"):
        result = get_predictions(h,l)
        st.write("Factor of Safety is : ", result[0])
        if result[0] > 1:
            st.subheader("It is safe")
        else:
            st.subheader("It is not safe")


if __name__ == "__main__":
    main()
