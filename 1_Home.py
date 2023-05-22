import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carousel Profile

st.markdown(
    """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>

    <div class="d-flex justify-content-center">
        <h1 class="text-primary">Creators</h1>
    </div>
    """,
    unsafe_allow_html=True
)

components.html(
    """	
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>

    <style>
        body {
            background-color: transparent;
        }

        /* Menetapkan lebar carousel */
        .carousel {
            width: 800px;
            margin: auto;
        }

        .carousel-item img {
            height: 600px;
            width: 400px;
            object-fit: cover;
            object-position: center;
        }
    </style>

    <div id="carouselProfile" class="carousel slide carousel-dark" data-bs-ride="carousel">
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselProfile" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselProfile" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselProfile" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>
    <div class="carousel-inner text-center">
        <div class="carousel-item active">
        <img src="https://images.pexels.com/photos/1438761/pexels-photo-1438761.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2>Achmadya Ridwan Ilyawan</h2>
            <p>Some representative placeholder content for the first slide.</p>
        </div>
        </div>
        <div class="carousel-item">
        <img src="https://images.pexels.com/photos/3509970/pexels-photo-3509970.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2>Fahmi Ahmad Fadilah</h2>
            <p>Some representative placeholder content for the second slide.</p>
        </div>
        </div>
        <div class="carousel-item">
        <img src="https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2>Hilman Permana</h2>
            <p>Some representative placeholder content for the third slide.</p>
        </div>
        </div>
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


    """,
    height=600,
)


# st.snow()
# st.title("Home Page")
# st.markdown("""---""")

# # Creator
# st.markdown("<h2 style='color: red;'>Creator</h2>", unsafe_allow_html=True)
# st.markdown(
#     "<h2 style='color: white;'>Nama : Achmadya Ridwan Ilyawan</h2>",
#     unsafe_allow_html=True,
# )
# st.markdown("<h2 style='color: white;'>NIM : 211511001</h2>",
#             unsafe_allow_html=True)
# st.markdown("<br>", unsafe_allow_html=True)
# st.markdown(
#     "<h2 style='color: white;'>Nama : Fahmi Ahmad Fadilah</h2>", unsafe_allow_html=True
# )
# st.markdown("<h2 style='color: white;'>NIM : 211511013</h2>",
#             unsafe_allow_html=True)
# st.markdown("<br>", unsafe_allow_html=True)
# st.markdown(
#     "<h2 style='color: white;'>Nama : Hilman Permana</h2>", unsafe_allow_html=True
# )
# st.markdown("<h2 style='color: white;'>NIM : 211511015</h2>",
#             unsafe_allow_html=True)
# st.markdown("""---""")

# # Requirements
# st.markdown("<h3 style='color: blue;'>Requirements</h3>",
#             unsafe_allow_html=True)
# st.markdown("<h6 style='color: white;'>- Streamlit</h6>",
#             unsafe_allow_html=True)
# st.code("pip install streamlit", language="python")
# st.markdown("<h6 style='color: white;'>- Numpy</h6>", unsafe_allow_html=True)
# st.code("pip install numpy", language="python")
# st.markdown("<h6 style='color: white;'>- OpenCV</h6>", unsafe_allow_html=True)
# st.code("pip install opencv-python-headless", language="python")
# st.markdown("<h6 style='color: white;'>- Pandas</h6>", unsafe_allow_html=True)
# st.code("pip install pandas", language="python")
# st.markdown("<h6 style='color: white;'>- Matplotlib</h6>",
#             unsafe_allow_html=True)
# st.code("pip install matplotlib", language="python")
# st.markdown("""---""")

# # Copy Right
# st.markdown(
#     "<h6 style='color: green;'>© 2023 - MatPilot.Inc</h6>", unsafe_allow_html=True
# )
