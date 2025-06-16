import streamlit as st

# --- Page settings ---
st.set_page_config(page_title="Wave Simulation Lab", layout="wide")

# --- Title and intro ---
st.title("🌐 Wave Simulation Laboratory")
st.markdown("""
Welcome to the **Wave Simulation Lab** — an interactive environment where you can explore wave phenomena using simulations.

This tool is designed for students, researchers, and enthusiasts interested in physics, mathematics, acoustics, and signal processing.

---  
""")

# --- Project overview ---
st.header("📘 Project Overview")

st.markdown("""
This project includes simulations of:

🔹 **1D Wave Propagation** – Study of waves on a string with damping and external forces  
🔹 **2D Wave Interference** – Visualization of constructive and destructive interference  
🔹 **Wave Packets** – Localized groups of waves representing quantum behavior  
🔹 **Fourier Transform** – Decomposition of waves into frequency components  
🔹 **Energy Analysis** – Tracking wave energy over time  
🔹 **Sound Wave Modeling** – Understanding real acoustic phenomena

Each module allows you to interactively modify parameters and visualize the effects.
""")

# --- Navigation Tips ---
st.header("🧭 How to Navigate")

st.markdown("""
Use the sidebar on the left to navigate between different simulation modules.

Each page offers:
- Interactive sliders for parameters
- Visual output (2D/3D/animated)
- Descriptions and physical interpretations

""")

# --- Footer ---
st.markdown("""---""")
st.caption("👩‍💻 Developed by Leila Yerzhankyzy  2025")
