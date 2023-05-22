import streamlit as st
import os
from moviepy.editor import VideoFileClip, AudioFileClip

def combine_frames_and_audio(frame_directory, audio_path, output_video_path):
    # Mendapatkan daftar file frame
    frame_files = sorted(os.listdir(frame_directory))

    # Mendapatkan informasi frame pertama
    frame_path = os.path.join(frame_directory, frame_files[0])
    frame = VideoFileClip(frame_path)

    # Membaca audio
    audio = AudioFileClip(audio_path)

    # Menggabungkan frame dan audio
    video_with_audio = frame.set_audio(audio)

    # Menyimpan video dengan audio
    video_with_audio.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

    # Menutup objek video dan audio
    frame.close()
    audio.close()

# Contoh penggunaan
frame_directory = "frames"
audio_path = "audios"
output_video_path = "output_video"

combine_frames_and_audio(frame_directory, audio_path, output_video_path)

# Menampilkan video pada Streamlit
st.video(output_video_path)
