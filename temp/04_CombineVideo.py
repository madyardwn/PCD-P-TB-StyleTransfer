import streamlit as st
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

def combine_frames_and_audio(frame_directory, audio_path, output_video_path):
    # Mendapatkan daftar file frame
    frame_files = sorted(os.listdir(frame_directory))

    # Membaca audio
    audio = AudioFileClip(audio_path)

    # Menggabungkan frame menjadi video
    clips = []
    for frame_file in frame_files:
        frame_path = os.path.join(frame_directory, frame_file)
        frame = VideoFileClip(frame_path)
        clips.append(frame)

    video_combined = concatenate_videoclips(clips)

    # Menggabungkan video dengan audio
    video_with_audio = video_combined.set_audio(audio)

    # Menyimpan video dengan audio
    video_with_audio.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

    # Menutup objek video dan audio
    for clip in clips:
        clip.close()
    video_combined.close()
    audio.close()

def main():
    st.title("Video Combining App")
    frame_directory = "frames"
    audio_path = "audios/audio.wav"
    output_video_path = "wct_videos/output_video.mp4"

    # Tombol untuk menggabungkan video
    if st.button("Combine Video"):
        st.write("Sedang menggabungkan video...")
        combine_frames_and_audio(frame_directory, audio_path, output_video_path)
        st.write("Penggabungan video selesai!")

    # Menampilkan video pada Streamlit
    st.markdown("### Video Output")
    if os.path.exists(output_video_path):
        st.video(output_video_path, format='video/mp4')
    else:
        st.write("Belum ada video yang digabungkan. Klik tombol Combine Video untuk menggabungkan.")

if __name__ == "__main__":
    main()
