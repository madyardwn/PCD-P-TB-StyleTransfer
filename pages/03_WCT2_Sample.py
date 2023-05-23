import streamlit as st
import os
import functions as func

# Tampilan aplikasi Streamlit
def main():
    st.title("Implementasi WCT2 pada Citra yang sudah tersedia")
    st.write("Pilih citra berdasarkan nomor yang sudah tersedia untuk melakukan style transfer.")
    
    # Memilih citra yang akan diimplementasikan WCT2
    number = st.number_input('Pilih nomor', min_value=1, max_value=60, value=1, step=1)
    st.write('Citra nomor: ', number)

    # Mengatur Ukuran citra yang akan ditampilkan
    image_size = st.number_input('Ukuran citra', min_value=256, max_value=2048, value=256, step=256)
    st.write('Ukuran citra yang akan ditampilkan: ', image_size)

    content_path = os.path.join("photorealistic_style_transfer", "examples", "input", "in" + str(number) + ".png")
    style_path = os.path.join("photorealistic_style_transfer", "examples", "style", "tar" + str(number) + ".png")
    output_path = "images"

    # Menampilkan preview citra yang dipilih
    st.write("Citra konten")
    st.image(content_path)

    st.write("Citra style")
    # Menampilkan preview style yang dipilih
    st.image(style_path)

    if st.button("Proses citra"):
        st.write("Memulai proses implementasi WCT2 pada citra...")
        func.perform_single_style_transfer(content_path, style_path, output_path, image_size)

        # Menampilkan citra hasil style transfer
        st.write("Citra hasil style transfer")
        st.image(os.path.join(output_path, "output.png"))

# Menjalankan aplikasi
if __name__ == "__main__":
    main()