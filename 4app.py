# app.py
# Interactive Generative Poster in Streamlit

import random
import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# --- Streamlit UI ---
st.set_page_config(page_title="Interactive Generative Poster", layout="centered")

st.title("🎨 Interactive Generative Poster")
st.caption("Week 2 • Arts & Advanced Big Data")

# --- Sidebar Controls ---
st.sidebar.header("🎛️ Controls")

layers = st.sidebar.slider("Number of Layers", 1, 50, 11)
wobble = st.sidebar.slider("Wobble Amount", 0.0, 0.8, 0.26, 0.01)
seed = st.sidebar.number_input("Random Seed", min_value=0, max_value=10000, value=7015, step=1)
palette_mode = st.sidebar.radio("Palette", ['pastel', 'vivid', 'autumn', 'ocean'])

generate_button = st.sidebar.button("🎲 Generate Poster")

# --- Functions ---
def random_palette(k=6, mode='pastel'):
    if mode == 'vivid':
        return [(random.random(), random.random(), random.random()) for _ in range(k)]
    elif mode == 'autumn':
        return [((1 + random.random()) / 2, random.uniform(0.3, 0.8), random.uniform(0, 0.2)) for _ in range(k)]
    elif mode == 'ocean':
        return [(random.uniform(0, 0.2), random.uniform(0.3, 0.7), (1 + random.random()) / 2) for _ in range(k)]
    else:  # pastel
        return [((1 + random.random()) / 2, (1 + random.random()) / 2, (1 + random.random()) / 2) for _ in range(k)]

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    angles = np.linspace(0, 2 * math.pi, points)
    radii = r * (1 + wobble * (np.random.rand(points) - 0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# --- Generate artwork ---
if generate_button or seed >= 0:
    random.seed(seed)
    np.random.seed(seed)
    
    fig, ax = plt.subplots(figsize=(7,10))
    ax.axis('off')
    ax.set_facecolor((0.98, 0.98, 0.97))

    palette = random_palette(6, mode=palette_mode)

    for _ in range(layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(0.15, 0.45)
        x_coords, y_coords = blob(center=(cx, cy), r=rr, wobble=wobble)
        color = random.choice(palette)
        alpha = random.uniform(0.25, 0.6)
        ax.fill(x_coords, y_coords, color=color, alpha=alpha, edgecolor=(0,0,0,0))

    ax.text(0.05, 0.95, f"Interactive Poster • {palette_mode}", fontsize=18, weight='bold', transform=ax.transAxes)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    st.pyplot(fig)
