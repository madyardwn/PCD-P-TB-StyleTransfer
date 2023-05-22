import os
import streamlit as st
import time
import cv2
import shutil
import re
from moviepy.editor import AudioFileClip, concatenate_videoclips, VideoFileClip

def extract_frame(video_directory, frames_directory, gap=10):
    # Menghapus direktori frames jika sudah ada
    if os.path.exists(frames_directory):
        shutil.rmtree(frames_directory)

    # Membuat direktori frames kembali
    if not os.path.exists(frames_directory):
        os.makedirs(frames_directory)

    # Membaca video
    cap = cv2.VideoCapture(video_directory)
    idx = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total jumlah frame dalam video

    # Ekstraksi frame dari video
    progress_text = "Extracting frames..."
    my_bar = st.progress(0, text=progress_text)

    while True:
        ret, frame = cap.read()

        if ret == False:
            cap.release()
            break

        if idx == 0:
            cv2.imwrite(f"{frames_directory}/{idx}.png", frame)
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{frames_directory}/{idx}.png", frame)

        idx += 1
        progress_percent = int((idx / total_frames) * 100)
        my_bar.progress(progress_percent, text=progress_text)

        # Tambahkan delay kecil untuk menghindari tampilan progress bar yang terlalu cepat
        time.sleep(0.01)

def extract_audio(video_directory, audio_directory):
    audio_path = os.path.join(audio_directory, "audio.wav")

    # Menghapus audio_path jika sudah ada
    if os.path.exists(audio_path):
        os.remove(audio_path)

    clip = VideoFileClip(video_directory)
    audio = clip.audio
    audio.write_audiofile(audio_path, codec='pcm_s16le', fps=44100)

    progress_text = "Extracting audio..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(0, 100, 10): 
        time.sleep(0.1)
        my_bar.progress(percent_complete + 10, text=progress_text)

    # Close Video dan Audio
    clip.close()
    audio.close()

def combine_frames_to_video(frames_directory, video_directory):
    # Mengambil semua frame yang ada di direktori frames
    frames = os.listdir(frames_directory)
    frames = sorted(frames, key=lambda x: int(re.findall(r'\d+', x)[0]))

    # Menentukan output_video_path
    output_video_path = os.path.join(video_directory, "temp_video.mp4")

    # Menghapus output_video_path jika sudah ada
    if os.path.exists(output_video_path):
        os.remove(output_video_path)

    # Memasukkan semua frame ke dalam list
    img = []
    for frame in frames:
        frame = frames_directory + "/" + frame
        img.append(frame)
    
    # Membuat video dari frame-frame yang ada
    cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    frame = cv2.imread(img[0])
    size = list(frame.shape)
    del size[2]
    size.reverse()

    video = cv2.VideoWriter(output_video_path, cv2_fourcc, 24, size) #output video name, fourcc, fps, size

    progress_text = "Menggabungkan frames menjadi video..."
    my_bar = st.progress(0, text=progress_text)

    for i in range(len(img)): 
        video.write(cv2.imread(img[i]))
        print('frame ', i+1, ' of ', len(img))
        my_bar.progress((i + 1) / len(img), text=progress_text)

    video.release()

def combine_audio_to_video(audio_directory, video_directory):
    # Menentukan input_video_path, output_video_path, dan audio_path
    input_video_path = os.path.join(video_directory, "temp_video.mp4")
    output_video_path = os.path.join(video_directory, "output_video.mp4")
    audio_path = os.path.join(audio_directory, "audio.wav")

    # Menghapus output_video_path jika sudah ada
    if os.path.exists(output_video_path):
        os.remove(output_video_path)

    # Menggabungkan video dengan audio
    video = VideoFileClip(input_video_path)
    audio = AudioFileClip(audio_path)

    # Memangkas video jika durasi lebih panjang dari audio
    if video.duration > audio.duration:
        video = video.subclip(0, audio.duration)

    # Memangkas audio jika durasi lebih panjang dari video
    if audio.duration > video.duration:
        audio = audio.subclip(0, video.duration)

    final = video.set_audio(audio)

    # Menuliskan video tanpa menggunakan progress_bar
    final.write_videofile(output_video_path, temp_audiofile='temp-audio.m4a', remove_temp=True,
                          codec="libx264", audio_codec="aac")

    progress_text = "Menggabungkan audio dengan video..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(0, 100, 10): 
        time.sleep(0.1)
        my_bar.progress(percent_complete + 10, text=progress_text)

    # Close video dan audio
    video.close()
    audio.close()

    # Menghapus input_video_path atau video temp yang tidak ada audio
    os.remove(input_video_path)

# Tampilan aplikasi Streamlit
def main():
    video_directory = "videos"
    frames_directory = "frames"
    audio_directory = "audios"
    wct_frames_directory = "wct_frames"

    st.title("Ekstraksi Frame dan Audio dari Video")
    st.write("Unggah video untuk mengekstrak frame-frame dan audio darinya.")

    # Mengunggah video
    video_file = st.file_uploader("Unggah video", type=["mp4", "avi"])
    if video_file is not None:
        # Menampilkan preview file yang baru diupload
        st.video(video_file)

        # Mengatur path untuk menyimpan video yang baru diupload
        uploaded_video = os.path.join(video_directory, "input_video.mp4")

        # Menghapus video yang diunggah jika sudah ada
        if os.path.exists(uploaded_video):
            os.remove(uploaded_video)

        # Simpan video yang diunggah
        with open(uploaded_video, "wb") as f:
            f.write(video_file.getbuffer())

        # Ekstraksi frame dan audio jika tombol ditekan
        if st.button("Ekstrak Frame dan Audio"):
            st.write("Sedang mengekstrak frame")

            # Extract frames
            extract_frame(uploaded_video, frames_directory, 50)

            # Extract audio
            extract_audio(uploaded_video, audio_directory)

            # Combine frames to video
            combine_frames_to_video(frames_directory, video_directory)

            # Combine audio to video
            combine_audio_to_video(audio_directory, video_directory)

            st.write("Ekstraksi selesai!")
        
            # Menampilkan video hasil ekstraksi
            st.write("Video hasil ekstraksi")
            video_file = open(os.path.join(video_directory, "output_video.mp4"), "rb")
            video_bytes = video_file.read()
            st.video(video_bytes)

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
