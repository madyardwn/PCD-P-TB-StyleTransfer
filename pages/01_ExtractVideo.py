import streamlit as st
import os
import functions as func

# Tampilan aplikasi Streamlit
def main():
    video_directory = "videos"
    frames_directory = "frames"
    audio_directory = "audios"
    image_directory = "images"
    wct_frames_directory = "wct_frames"

    st.title("Ekstraksi Frame dan Audio dari Video")
    st.write("Unggah video untuk mengekstrak frame-frame dan audio darinya.")

    # Mengunggah video
    video_file = st.file_uploader("Unggah video", type=["mp4", "avi", "mov", "mkv"])
    style_file = st.file_uploader("Unggah style", type=["jpg", "jpeg", "png"])
    if video_file is not None and style_file is not None:
        # Menampilkan preview file yang baru diupload
        st.video(video_file)

        # Menampilkan preview style yang baru diupload
        st.image(style_file)

        # Mengatur path untuk menyimpan video yang baru diupload
        uploaded_video = os.path.join(video_directory, "input_video.mp4")

        # Mengatur path untuk menyimpan style yang baru diupload
        uploaded_style = os.path.join(image_directory, "style.png")

        # Menghapus video yang diunggah jika sudah ada
        if os.path.exists(uploaded_video):
            os.remove(uploaded_video)
        
        # Menghapus style yang diunggah jika sudah ada
        if os.path.exists(uploaded_style):
            os.remove(uploaded_style)

        # Simpan video yang diunggah
        with open(uploaded_video, "wb") as f:
            f.write(video_file.getbuffer())
        
        # Simpan style yang diunggah
        with open(uploaded_style, "wb") as f:
            f.write(style_file.getbuffer())

        # Ekstraksi frame dan audio jika tombol ditekan
        if st.button("Ekstrak Frame dan Audio"):
            st.write("Sedang mengekstrak frame")

            # Extract frames
            func.extract_frame(uploaded_video, frames_directory, 2)

            # Extract audio
            func.extract_audio(uploaded_video, audio_directory)

            # Perform Style Transfer
            func.perform_style_transfer(frames_directory, uploaded_style, wct_frames_directory)

            # Combine frames to video
            func.combine_frames_to_video(wct_frames_directory, video_directory)

            # Combine audio to video
            func.combine_audio_to_video(audio_directory, video_directory)

            st.write("Ekstraksi selesai!")
        
            # Menampilkan video hasil ekstraksi
            st.write("Video hasil ekstraksi")
            video_file = open(os.path.join(video_directory, "output_video.mp4"), "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
