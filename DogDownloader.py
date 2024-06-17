#!/bin/env python
# Requires: yt_dlp module
# Requires: ffmpeg

# pip install youtube-search
# pip install yt-dlp

import os
import re
import yt_dlp as youtube_dl
from youtube_search import YoutubeSearch

def clear_previous_files():
    if os.path.exists("./video"):
        arquivos = os.listdir('./video')
        for arquivo in arquivos:
            caminho_arquivo = os.path.join('./video', arquivo)
            os.remove(caminho_arquivo)
        print("Arquivos anteriores deletados com sucesso.")

def get_user_choice():
    while True:
        mensagem = input("Deseja deletar os arquivos anteriores? (S/N): ").strip().lower()
        if mensagem in ['s', 'n']:
            return mensagem
        print("Opção inválida. Por favor, escolha 'S' ou 'N'.")

class YouTubeDownloader:
    def __init__(self, path: str):
        self.path = path
        self.ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'ignoreerrors': True,
            'merge_output_format': 'mp4',
            'nocheckcertificate': True,
            'quiet': False,
            'postprocessors': [{
                'key': 'FFmpegMerger',
            }],
        }

    def get_info_by_ytlink(self, link):
        video_info = youtube_dl.YoutubeDL(self.ydl_opts).extract_info(link, download=False)
        title = video_info.get('title', '')
        duration = video_info.get('duration', '')
        return title, duration

    def find_video_link_by_name(self, name):
        results = YoutubeSearch(name, max_results=1).to_dict()
        if not results:
            print("Nenhum vídeo encontrado com esse nome.")
            return None
        video = results[0]
        video_id = video['id']
        ylink = f"https://www.youtube.com/watch?v={video_id}"
        return ylink

    def download_by_name(self, name):
        ylink = self.find_video_link_by_name(name)
        if ylink:
            return self.download_by_ytlink(ylink)
        else:
            return "Nenhum vídeo encontrado"

    def download_by_ytlink(self, link):
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([link])
        title, _ = self.get_info_by_ytlink(link)
        return title

    def change_path(self, new_path):
        self.path = new_path
        self.ydl_opts['outtmpl'] = os.path.join(new_path, '%(title)s.%(ext)s')

def main():
    print("\n\033[1;32m Bem-vindo ao DogVideoDownloader \033[0m\n")
    mensagem = get_user_choice()

    if mensagem == "s":
        clear_previous_files()
    else:
        print("Ok, vamos começar o script então.\n")

    downloader   = YouTubeDownloader('./video')
    search_query = input("Digite o nome ou o link do vídeo: ").strip()
    youtube_link = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+'

    if re.match(youtube_link, search_query):
        title = downloader.download_by_ytlink(search_query)
    else:
        title = downloader.download_by_name(search_query + 'Official')
    print(f"Vídeo '{title}' baixado com sucesso!")

if __name__ == "__main__":
    main()
