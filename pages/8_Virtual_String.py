import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import tempfile
import os

# --- Page config ---
st.set_page_config(page_title="🎻 Virtual String Simulator", layout="wide")

# --- Title and Theory ---
st.title("🎼 Virtual String Simulation")

st.markdown("""
Explore how string instruments generate sound! Adjust **frequency**, **amplitude**, and **duration** – then choose an instrument and **play the string** 🎶.

""")

with st.expander("📘 How It Works", expanded=False):
    st.markdown("""
    - A string vibrates at a fundamental frequency.  
    - The waveform is **sine-shaped**, and the frequency determines the **pitch**.  
    - Instruments differ by their **timbre** (sound color), modeled here by modifying the waveform.
    """)

# --- Sidebar: Controls ---
st.sidebar.title("🎛 Controls")

instrument = st.sidebar.selectbox("Instrument", ["🎸 Guitar", "🎻 Violin", "🎹 Synth"])
frequency = st.sidebar.slider("Frequency (Hz)", 100, 2000, 440)
duration = st.sidebar.slider("Duration (seconds)", 1, 5, 2)
amplitude = st.sidebar.slider("Amplitude", 0.1, 1.0, 0.5)

# --- Time array ---
sampling_rate = 44100
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# --- Generate waveform ---
def generate_waveform(instr, f, A, t):
    if instr == "🎸 Guitar":
        # Simple sine with exponential decay
        return A * np.sin(2 * np.pi * f * t) * np.exp(-2 * t)
    elif instr == "🎻 Violin":
        # Richer harmonics
        return A * (np.sin(2 * np.pi * f * t) +
                    0.5 * np.sin(2 * np.pi * 2 * f * t) +
                    0.25 * np.sin(2 * np.pi * 3 * f * t)) * np.exp(-1.5 * t)
    elif instr == "🎹 Synth":
        # Clean triangle-ish waveform
        return A * np.sign(np.sin(2 * np.pi * f * t)) * np.exp(-1 * t)

signal = generate_waveform(instrument, frequency, amplitude, t)

# --- Plot waveform ---
st.subheader("📊 Waveform (Zoomed In)")
fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(t[:1000], signal[:1000], color='teal')
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Initial Oscillation of the String")
st.pyplot(fig)

# --- Audio file generation ---
st.subheader("🎧 Play the String Sound")

with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
    sf.write(tmpfile.name, signal, samplerate=sampling_rate)
    st.audio(tmpfile.name, format="audio/wav")

# --- Cleanup temp file ---
os.remove(tmpfile.name)

# --- Footer ---
st.markdown("---")
st.markdown("🎵 Created as part of the **Wave Simulation Lab** for audio-visual learning.")
