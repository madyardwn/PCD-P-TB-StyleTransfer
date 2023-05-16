import streamlit as st
import cv2
import os
import tempfile

def extract_frames(video_path, output_directory):
    # Membaca video
    video = cv2.VideoCapture(video_path.name)
    success, image = video.read()
    count = 0

    # Membuat direktori output jika belum ada
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Ekstraksi frame dari video
    while success:
        # Menyimpan setiap frame sebagai gambar
        frame_path = os.path.join(output_directory, f"frame_{count}.jpg")
        cv2.imwrite(frame_path, image)
        
        # Membaca frame berikutnya
        success, image = video.read()
        count += 1

    video.release()

# Tampilan aplikasi Streamlit
def main():
    st.title("Ekstraksi Frame dari Video")
    st.write("Unggah video untuk mengekstrak frame-frame darinya.")

    # Mengunggah video
    uploaded_file = st.file_uploader("Unggah video", type=["mp4", "avi"])
    if uploaded_file is not None:
        # Menentukan direktori output
        output_directory = "frames"
        
        # Ekstraksi frame jika tombol ditekan
        if st.button("Ekstrak Frame"):
            st.write("Sedang mengekstrak frame...")
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                extract_frames(temp_file, output_directory)
            st.write("Ekstraksi selesai!")

            # Menampilkan frame-frame yang diekstrak
            frames = os.listdir(output_directory)
            for frame in frames:
                frame_path = os.path.join(output_directory, frame)
                st.image(frame_path)

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
