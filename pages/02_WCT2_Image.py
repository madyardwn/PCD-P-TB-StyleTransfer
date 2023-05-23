import streamlit as st
import os
import functions as func

# Tampilan aplikasi Streamlit
def main():
    image_directory = "images"

    st.title("Implementasi WCT2 pada Video")
    st.write("Unggah citra konten dan style untuk melakukan style transfer.")

    # Mengunggah citra konten
    content_file = st.file_uploader("Unggah citra konten", type=["jpg", "jpeg", "png"])
    style_file = st.file_uploader("Unggah citra style", type=["jpg", "jpeg", "png"])
    if content_file is not None and style_file is not None:
        # Menampilkan preview file yang baru diupload
        st.write("Citra Konten")
        st.image(content_file, width=1024)

        # Menampilkan preview style yang baru diupload
        st.write("Citra Style")
        st.image(style_file, width=1024)

        # Mengatur path untuk menyimpan citra konten yang baru diupload
        uploaded_content = os.path.join(image_directory, "content.png")

        # Mengatur path untuk menyimpan citra style yang baru diupload
        uploaded_style = os.path.join(image_directory, "style.png")

        # Menghapus citra konten yang diunggah jika sudah ada
        if os.path.exists(uploaded_content):
            os.remove(uploaded_content)

        # Menghapus citra style yang diunggah jika sudah ada
        if os.path.exists(uploaded_style):
            os.remove(uploaded_style)

        # Simpan citra konten yang diunggah
        with open(uploaded_content, "wb") as f:
            f.write(content_file.getbuffer())

        # Simpan citra style yang diunggah
        with open(uploaded_style, "wb") as f:
            f.write(style_file.getbuffer())

        # Lakukan style transfer jika tombol ditekan
        if st.button("Proses citra"):
            st.write("Memulai proses implementasi WCT2 pada citra...")

            # Perform Style Transfer
            func.perform_single_style_transfer(uploaded_content, uploaded_style, "images")

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
