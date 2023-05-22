import streamlit as st
import cv2
import os
import tempfile
import shutil
from moviepy.editor import VideoFileClip

def extract_frames_and_audio(video_path, output_frame_directory, output_audio_directory):
    # Menghapus folder frame jika sudah ada
    if os.path.exists(output_frame_directory):
        shutil.rmtree(output_frame_directory)

    # Menghapus folder audio jika sudah ada
    if os.path.exists(output_audio_directory):
        shutil.rmtree(output_audio_directory)
    
    # Membuat direktori output frame jika belum ada
    if not os.path.exists(output_frame_directory):
        os.makedirs(output_frame_directory)

    # Membuat direktori output audio jika belum ada
    if not os.path.exists(output_audio_directory):
        os.makedirs(output_audio_directory)

    # Membaca video
    video = cv2.VideoCapture(video_path.name)
    success, image = video.read()
    count = 0

    # Ekstraksi frame dari video
    while success:
        # Menyimpan setiap frame sebagai gambar
        frame_path = os.path.join(output_frame_directory, f"frame_{count}.png")
        cv2.imwrite(frame_path, image)
        
        # Membaca frame berikutnya
        success, image = video.read()
        count += 1
    
    video.release()

    # Ekstraksi audio dari video
    output_audio_path = os.path.join(output_audio_directory, "audio.wav")

    video = VideoFileClip(video_path.name)
    audio = video.audio
    audio.write_audiofile(output_audio_path, codec='pcm_s16le', fps=44100)
    video.close()

# Tampilan aplikasi Streamlit
def main():
    st.title("Ekstraksi Frame dan Audio dari Video")
    st.write("Unggah video untuk mengekstrak frame-frame dan audio darinya.")

    # Mengunggah video
    uploaded_file = st.file_uploader("Unggah video", type=["mp4", "avi"])
    if uploaded_file is not None:
        # Menentukan direktori output frame dan audio
        output_frame_directory = "frames"
        output_audio_directory = "audios"
        
        # Ekstraksi frame dan audio jika tombol ditekan
        if st.button("Ekstrak Frame dan Audio"):
            st.write("Sedang mengekstrak frame dan audio...")
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                extract_frames_and_audio(temp_file, output_frame_directory, output_audio_directory)
            st.write("Ekstraksi selesai!")

            # # Menampilkan frame-frame yang diekstrak
            # frames = os.listdir(output_frame_directory)
            # for frame in frames:
            #     frame_path = os.path.join(output_frame_directory, frame)
            #     st.image(frame_path)

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
