import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="🎵 Sound Waves", layout="wide")

st.title("🎵 Sound Wave Simulation")
st.markdown("""
Adjust the frequency and duration of the wave to simulate a simple sound wave (sine wave).
""")

# Input parameters
col1, col2 = st.columns(2)
with col1:
    frequency = st.slider("Frequency (Hz)", 100, 2000, 440)
with col2:
    duration = st.slider("Duration (s)", 0.1, 2.0, 1.0)

sample_rate = 44100  # Hz
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
signal = np.sin(2 * np.pi * frequency * t)

# Plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t[:1000], signal[:1000])
ax.set_title("Sound Wave (First 1000 samples)")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")
st.pyplot(fig)
