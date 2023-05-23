import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inisialisasi direktori jika belum ada
# Direktori images
if not os.path.exists("images"):
    os.makedirs("images")

# Direktori videos
if not os.path.exists("videos"):
    os.makedirs("videos")

# Direktori audios
if not os.path.exists("audios"):
    os.makedirs("audios")

# Direktori frames
if not os.path.exists("frames"):
    os.makedirs("frames")

# Direktori wct_frames
if not os.path.exists("wct_frames"):
    os.makedirs("wct_frames")

st.snow()
st.markdown(
    """
    <div class="text-bundle">
        <h1 class="text-title">Home Page</h1>
    </div>

    <style>
        .text-title {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 32px;
            color: #FFFFFF;
        }

        .text-bundle {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""---""")

# Penjelasan Photorealistic Style Transfer
st.markdown(
    """
    <div class="text-bundle">
        <h2 class="text-pst">Photorealistic Style Transfer</h2>
    </div>

    <style>
        .text-pst {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 28px;
            color: #FF00FF;
        }

        .text-bundle {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="text-bundle">
        <p class="text-content">Photorealistic style transfer adalah teknik yang digunakan untuk mengubah gaya visual sebuah gambar dengan mempertahankan keaslian citra yang asli.  
        Tujuan dari teknik ini adalah untuk mentransfer gaya dari satu gambar ke gambar lainnya, sehingga gambar yang dihasilkan memiliki penampilan yang mirip dengan citra asli, 
        tetapi dengan gaya visual yang baru.</p>
    </div>

    <style>
        .text-content {
            font-family: 'Poppins', sans-serif;
            font-weight: 400;
            font-size: 16px;
            color: #FFFFFF;
            text-align: center;
        }

        .text-bundle {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""---""")

# Penjelasan Singkat WCT2
st.markdown(
    """
    <div class="text-bundle">
        <h2 class="text-wct2">WCT2</h2>
    </div>

    <style>
        .text-wct2 {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 28px;
            color: #FFA500;
        }

        .text-bundle {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="text-bundle">
        <p class="text-content">WCT2 adalah teknik yang digunakan untuk mentransfer gaya dari satu gambar ke gambar lainnya.
        Teknik ini merupakan pengembangan dari WCT yang dikembangkan oleh Li et al. (2017) dengan menggabungkan beberapa teknik yang ada sebelumnya,
        seperti whitening and coloring transform (WCT), histogram matching, dan photorealistic style transfer.
    </div>

    <div class="text-bundle">
        <p class="text-content">Proses WCT2 melibatkan dua tahap utama: whitening (pencerahan) dan coloring (pewarnaan). Tahap whitening melibatkan perubahan statistik warna dari gambar gaya 
        dan gambar target untuk menghilangkan korelasi warna yang ada. Hal ini dilakukan dengan memperoleh matriks kovariansi warna dari kedua gambar dan melakukan 
        dekomposisi nilainya. Setelah tahap whitening, tahap coloring dilakukan dengan mengambil matriks kovariansi warna yang telah diubah dari gambar gaya dan 
        menerapkannya pada gambar target.</p>
    </div>

    <style>
        .text-content {
            font-family: 'Poppins', sans-serif;
            font-weight: 400;
            font-size: 16px;
            color: #FFFFFF;
            text-align: center;
        }

        .text-bundle {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
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
            margin: auto;
        }

        .carousel-item img {
            height: 800px;
            width: 800px;
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
        <img src="https://i.ibb.co/whG6vSY/in52.png" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2 class="text-danger">Content Image</h2>
            <p></p>
        </div>
        </div>
        <div class="carousel-item">
        <img src="https://i.ibb.co/cT0YJwR/tar52.png" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2 class="text-warning">Style Image</h2>
            <p></p>
        </div>
        </div>
        <div class="carousel-item">
        <img src="https://i.ibb.co/dkDx4sV/out52.png" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2 class="text-success">Result Image</h2>
            <p></p>
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
    height=800,
)

st.markdown("""---""")

# Carousel Profile
st.markdown(
    """
    <div class="text-bundle">
        <h1 class="text">Creators</h1>
    </div>

    <style scoped>
        .text {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 32px;
            color: #00FFFF;
        }

        .text-bundle {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
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
        <img src="https://i.ibb.co/NjDyjxb/achmadya.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2 class="text-danger">Achmadya Ridwan Ilyawan</h2>
            <p class="text-danger" style="font-size: 18px; font-weight: 600;">211511001</p>
        </div>
        </div>
        <div class="carousel-item">
        <img src="https://i.ibb.co/4KtZG2t/fahmi.jpg" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2 class="text-warning">Fahmi Ahmad Fadilah</h2>
            <p class="text-warning" style="font-size: 18px; font-weight: 600;">211511013</p>
        </div>
        </div>
        <div class="carousel-item">
        <img src="https://i.ibb.co/qBYnNJj/hilman.png" class="d-block w-100" alt="...">
        <div class="carousel-caption d-none d-md-block">
            <h2 class="text-success">Hilman Permana</h2>
            <p class="text-success" style="font-size: 18px; font-weight: 600;">211511015</p>
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

st.markdown("""---""")

# Requirements
st.markdown(
    """
    <div class="text-bundle">
        <h1 class="text-req">Requirements</h1>
    </div>

    <style scoped>
        .text-req {
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 32px;
            color: #00FF00;
        }

        .text-bundle {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h6 style='color: white;'>- Streamlit</h6>",
            unsafe_allow_html=True)
st.code("pip install streamlit", language="python")
st.markdown("<h6 style='color: white;'>- Numpy</h6>", unsafe_allow_html=True)
st.code("pip install numpy", language="python")
st.markdown("<h6 style='color: white;'>- OpenCV</h6>", unsafe_allow_html=True)
st.code("pip install opencv-python-headless", language="python")
st.markdown("<h6 style='color: white;'>- Pandas</h6>", unsafe_allow_html=True)
st.code("pip install pandas", language="python")
st.markdown("<h6 style='color: white;'>- Pillow</h6>",
            unsafe_allow_html=True)
st.code("pip install Pillow", language="python")
st.markdown("<h6 style='color: white;'>- Tensorflow</h6>",
            unsafe_allow_html=True)
st.code("pip install tensorflow", language="python")
st.markdown("<h6 style='color: white;'>- Moviepy</h6>",
            unsafe_allow_html=True)
st.code("pip install moviepy", language="python")
st.markdown("""---""")

# Copy Right
st.markdown(
    "<h6 style='color: green;'>© 2023 - AFH_PCD.Inc</h6>", unsafe_allow_html=True
)
