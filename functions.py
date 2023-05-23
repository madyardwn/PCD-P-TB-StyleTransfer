import os
import streamlit as st
import time
import cv2
import shutil
import re
from photorealistic_style_transfer.model import WCT2
from photorealistic_style_transfer.utils import read_img, download_weight, display_outputs
from moviepy.editor import AudioFileClip, VideoFileClip

# Fungsi untuk mengekstrak frame dari video
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
    my_bar.progress(100, text=progress_text)

# Fungsi untuk mengekstrak audio dari video
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
    my_bar.progress(100, text=progress_text)

    # Close Video dan Audio
    clip.close()
    audio.close()

# Fungsi untuk menggabungkan audio ke dalam video
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
    my_bar.progress(100, text=progress_text)

    video.release()

# Fungsi untuk menggabungkan audio ke dalam video
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
    my_bar.progress(100, text=progress_text)

    # Close video dan audio
    video.close()
    audio.close()

    # Menghapus input_video_path atau video temp yang tidak ada audio
    os.remove(input_video_path)

# Fungsi untuk melakukan style transfer
def perform_style_transfer(frames_directory, style_image_path, output_directory, image_size=512):
    # Menghapus dan Membuat output_directory jika sudah ada
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    os.mkdir(output_directory)

    # Mengambil semua frame yang ada di direktori frames
    frames = os.listdir(frames_directory)
    frames = sorted(frames, key=lambda x: int(re.findall(r'\d+', x)[0]))

    content_img = []

    # Baca semua gambar content
    for frame in frames:
        frame = frames_directory + "/" + frame
        content_img.append(frame)

    # Menggunakan model WCT2
    model = WCT2()
    model.load_weight('photorealistic_style_transfer/checkpoints/wtc2.h5')

    # Inisialisasi progress bar
    progress_text = "Melakukan style transfer..."
    my_bar = st.progress(0, text=progress_text)

    # Membaca gambar style
    style_image = read_img(style_image_path, image_size, expand_dims=True)

    # Lakukan transfer gaya pada setiap content dengan satu gambar style
    for idx, content in enumerate(content_img):
        content = read_img(content, image_size, expand_dims=True)
        gen = model.transfer(content, style_image, 1.0)
        output_path = os.path.join(output_directory, f'{idx}.png')
        # cv2.imwrite(output_path, content[0][..., ::-1])
        cv2.imwrite(output_path, gen[0][..., ::-1])

        # Update progress bar
        progress_percent = (idx + 1) / len(content_img)
        my_bar.progress(progress_percent, text=progress_text)
        time.sleep(0.1)
    my_bar.progress(100, text=progress_text)

# Fungsi untuk menyaring frame yang hitam
def filter_black_frames(frames_directory, output_directory):
    # Menghapus dan Membuat output_directory jika sudah ada
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    os.mkdir(output_directory)

    # Mengambil semua frame yang ada di direktori frames
    frames = os.listdir(frames_directory)
    frames = sorted(frames, key=lambda x: int(re.findall(r'\d+', x)[0]))

    img = []

    # Baca semua gambar
    for frame in frames:
        frame = frames_directory + "/" + frame
        img.append(frame)

    # Inisialisasi progress bar
    progress_text = "Menyaring frame yang hitam..."
    my_bar = st.progress(0, text=progress_text)

    # Menyaring frame yang hitam
    for idx, image in enumerate(img):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray) != 0:
            output_path = os.path.join(output_directory, f'{idx}.png')
            cv2.imwrite(output_path, img)
        else:
            print("Frame ", idx, " berwarna hitam")

        # Update progress bar
        progress_percent = (idx + 1) / len(img)
        my_bar.progress(progress_percent, text=progress_text)
        time.sleep(0.1)
    my_bar.progress(100, text=progress_text)

# Fungsi untuk melakukan style transfer pada satu 
def perform_single_style_transfer(content_image_path, style_image_path, output_directory, image_size=1024):
    # Menggunakan model WCT2
    model = WCT2()
    model.load_weight('photorealistic_style_transfer/checkpoints/wtc2.h5')

    # Membaca gambar content
    content_image = read_img(content_image_path, image_size, expand_dims=True)

    # Membaca gambar style
    style_image = read_img(style_image_path, image_size, expand_dims=True)

    # Menampilkan progress bar
    progress_text = "Sedang melakukan style transfer..."
    my_bar = st.progress(0, text=progress_text)

    # Lakukan transfer gaya pada satu gambar content dengan satu gambar style
    gen = model.transfer(content_image, style_image, 1.0)
    output_path = os.path.join(output_directory, f'output.png')

    # Menghapus terlebih dahulu output_path jika sudah ada
    if os.path.exists(output_path):
        os.remove(output_path)

    # Menuliskan gambar hasil style transfer
    cv2.imwrite(output_path, gen[0][..., ::-1])

    # Update progress bar menjadi 100%
    my_bar.progress(100, text=progress_text)

    # Menampilkan gambar hasil style transfer
    st.image(output_path)