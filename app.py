import pyslope
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import joblib
from pyslope import (Slope,Material)

# Create a Streamlit web app
def main():
    st.title("Landslide Failure Surface Visualizer")
    st.markdown("""<h2 style='text-align: center; color: black;'>An AI Based Tool</h2>""",unsafe_allow_html=True)
    l = st.number_input('Enter the Slope Length')
    h = st.number_input('Enter the Slope Height')
    d = st.number_input('Enter the Water Depth')
    w = st.number_input('Enter the Unit Weight')
    a = st.number_input('Enter the Friction Angle')  
    c = st.number_input('Enter the Effective Cohesion')
    
    if st.button('Visualize'):
        s = Slope(height=h,length=l, angle=None)
        m1 = Material(unit_weight=w,friction_angle=a,cohesion=c,depth_to_bottom=30)
        s.set_materials(m1)
        s.set_water_table(1)
        s.set_analysis_limits(s.get_top_coordinates()[0] - 5, s.get_bottom_coordinates()[0] + 5)
        # run calculations on the created slope
        s.analyse_slope()
        # plot all failure planes with a FOS below 2
        fig_1=s.plot_all_planes(max_fos=2)
        fig_1.update_layout(width=800, height=600) 
        st.plotly_chart(fig_1)
    
    def apply_text_color(text, color):
        return f'<span style="color:{color}">{text}</span>'
    
    safe = apply_text_color("If FOS is > 1 : It is safe.", "green")
    unsafe = apply_text_color("If FOS is < 1 : It is unsafe.", "red")
    st.markdown(safe, unsafe_allow_html=True)
    st.markdown(unsafe, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
