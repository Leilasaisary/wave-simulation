import streamlit as st

# --- Page settings ---
st.set_page_config(page_title="🌐 Wave Simulation Lab", layout="wide")

# --- Title and intro ---
st.title("🌊 Wave Simulation Laboratory")
st.markdown("""
Welcome to the **Wave Simulation Lab** — a modern interactive environment to explore and simulate wave phenomena through visual, mathematical and auditory experiments.

This lab is designed for:
- 🧑‍🎓 Students studying physics or computer simulations  
- 🧑‍🔬 Researchers in acoustics, quantum modeling, or signal processing  
- 👩‍💻 Developers interested in scientific visualization and interaction  
""")

# --- Project Overview ---
st.header("📘 Project Overview")

st.markdown("""
Our lab includes the following modules:

1. **1D Wave Propagation** – Modeling waves on a string using finite difference methods, including damping and forcing  
2. **2D Wave Interference** – Visualizing how two waves interfere constructively or destructively  
3. **Wave Energy** – Tracking and comparing kinetic and potential energy over time  
4. **Fourier Transform** – Transforming signals from time to frequency domain  
5. **Wave Packet** – Simulating localized bursts of wave energy, resembling quantum behavior  
6. **Sound Wave** – Creating and listening to simulated audio waves  
7. **Wave Animation** – Real-time animation of standing and traveling waves in 3D  
8. **Virtual String** – Musical string simulation with sound, waveform, and instrument selection  

Each simulation provides:
- 🔧 Parameter sliders for full control  
- 📊 Real-time visualization (2D, 3D, animated)  
- 🧠 Theoretical explanations and formulas  
- 🎵 Interactive sound when applicable  
""")

# --- Navigation Tips ---
st.header("🧭 How to Navigate")

st.markdown("""
Use the left sidebar to select a simulation topic.  
You can interact with each simulation using sliders and checkboxes.

> 🔁 Come back to this **main home** any time by clicking "main home" in the sidebar.
""")

# --- Footer ---
st.markdown("---")
st.caption("👩‍💻 Created by Leila Yerzhankyzy (2025) — Wave Simulation Lab")