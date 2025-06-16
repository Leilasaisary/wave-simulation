import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Wave Animation", page_icon="🎞️")
st.title("🎞️ Real-time Wave Animation")

st.markdown("""
This animation shows a **traveling wave** along a string.
You can adjust the amplitude, speed, and frequency for visual experimentation.
""")

# Parameters
wave_amplitude = st.slider("Amplitude", 0.1, 2.0, 1.0)
wave_speed = st.slider("Speed", 0.1, 2.0, 1.0)
wave_freq = st.slider("Frequency", 0.5, 5.0, 1.0)
duration = st.slider("Animation Duration (sec)", 2, 10, 5)

x = np.linspace(0, 2*np.pi, 300)
frame_rate = 30
n_frames = duration * frame_rate

placeholder = st.empty()

for i in range(n_frames):
    t = i / frame_rate
    y = wave_amplitude * np.sin(wave_freq * x - wave_speed * t)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, color="royalblue", linewidth=2)
    ax.set_ylim(-2, 2)
    ax.set_title(f"Wave at t = {t:.2f} s", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")
    ax.grid(True)
    placeholder.pyplot(fig)
    time.sleep(1.0 / frame_rate)

st.success("Animation complete ✅")