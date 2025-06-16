import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fourier Transform", layout="wide")

st.title("🔬 Fourier Transform of a Wave Signal")
st.markdown("""
Visualize how any time-domain signal can be decomposed into a sum of **sine waves** of different frequencies.

We simulate a composite wave and display its **frequency spectrum** using the Fast Fourier Transform (FFT).
""")

# Parameters
st.sidebar.header("🎛️ Signal Parameters")
f1 = st.sidebar.slider("Frequency f₁ (Hz)", 1.0, 10.0, 3.0)
f2 = st.sidebar.slider("Frequency f₂ (Hz)", 1.0, 10.0, 6.0)
f3 = st.sidebar.slider("Frequency f₃ (Hz)", 0.0, 10.0, 0.0)  # optional third frequency
A1 = st.sidebar.slider("Amplitude A₁", 0.0, 2.0, 1.0)
A2 = st.sidebar.slider("Amplitude A₂", 0.0, 2.0, 0.5)
A3 = st.sidebar.slider("Amplitude A₃", 0.0, 2.0, 0.0)

# Time and signal
T = 1.0  # seconds
fs = 500
t = np.linspace(0, T, int(T*fs), endpoint=False)
signal = A1*np.sin(2*np.pi*f1*t) + A2*np.sin(2*np.pi*f2*t) + A3*np.sin(2*np.pi*f3*t)

# FFT
fft_vals = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(len(t), 1/fs)
mask = fft_freqs >= 0

# Plot signal and FFT
fig1, ax1 = plt.subplots()
ax1.plot(t, signal)
ax1.set_title("🕒 Time Domain Signal")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")

fig2, ax2 = plt.subplots()
ax2.stem(fft_freqs[mask], np.abs(fft_vals[mask]), basefmt=" ")
ax2.set_title("📈 Frequency Domain (FFT Spectrum)")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")

st.pyplot(fig1)
st.pyplot(fig2)