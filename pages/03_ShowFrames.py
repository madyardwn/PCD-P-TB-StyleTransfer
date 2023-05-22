import glob
import os
import streamlit as st
import streamlit.components.v1 as components

output_path = "images"
frame_files = glob.glob(os.path.join(output_path, "*.png"))

carousel_html = """
<div id="carouselProfile" class="carousel slide carousel-dark" data-bs-ride="carousel">
<div class="carousel-indicators">
"""

# Membuat tombol indikator untuk setiap file frame
for i, frame_file in enumerate(frame_files):
    active_class = "active" if i == 0 else ""
    carousel_html += f'<button type="button" data-bs-target="#carouselProfile" data-bs-slide-to="{i}" class="{active_class}" aria-label="Slide {i+1}"></button>'

carousel_html += """
</div>
<div class="carousel-inner text-center">
"""

# Menambahkan item carousel untuk setiap file frame
for i, frame_file in enumerate(frame_files):
    active_class = "active" if i == 0 else ""
    carousel_html += f"""
    <div class="carousel-item {active_class}">
        <img src="{frame_file}" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2>Creator {i+1}</h2>
            <p>Some representative placeholder content for slide {i+1}.</p>
        </div>
    </div>
    """

carousel_html += """
</div>
<button class="carousel-control-prev" type="button" data-bs-target="#carouselProfile" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
</button>
<button class="carousel-control-next" type="button" data-bs-target="#carouselProfile" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
</button>
</div>
"""

st.markdown(
    carousel_html,
    unsafe_allow_html=True,
    height=600,
)
