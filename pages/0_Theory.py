import streamlit as st

st.set_page_config(page_title="Wave Equation - Theory", layout="wide")

st.title("📘 Theory: 1D Wave Equation")

st.markdown("""
The **1D wave equation** models how waves propagate along a string:

$$
\\frac{\\partial^2 u}{\\partial t^2} = c^2 \\cdot \\frac{\\partial^2 u}{\\partial x^2}
$$

Where:
- \( u(x,t) \) — wave displacement at position \( x \) and time \( t \)  
- \( c \) — wave speed  
- Domain: \( x \\in [0, L] \), \( t \\in [0, T] \)

---

### 🧩 Initial Conditions
To solve the equation, we need:
- Initial displacement: \( u(x, 0) = f(x) \)
- Initial velocity: \( u_t(x, 0) = g(x) \)

### 🎯 Boundary Conditions
- Fixed ends: \( u(0,t) = u(L,t) = 0 \)
- Or other variants (free, periodic)

---

### ⚙️ Numerical Scheme (Finite Difference)
We use the finite-difference method (central differences in time and space):

$$
u_i^{n+1} = 2(1 - r^2)u_i^n - u_i^{n-1} + r^2(u_{i+1}^n + u_{i-1}^n)
$$

Where:
- \( r = \\frac{c \\cdot \\Delta t}{\\Delta x} \) — Courant number  
- Stability condition: \( r \\leq 1 \)

---

### 📌 Applications
- Vibrating guitar string  
- Sound wave in tube  
- Seismic wave modeling  
- Wave propagation in physics and engineering  
""")