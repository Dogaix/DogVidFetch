# DogVidFetch

Bem-vindo ao DogVidFetch! 🐾✨
Este script permite que você baixe vídeos do YouTube utilizando `yt-dlp` e `ffmpeg`.





## Requisitos

Para usar o DogVidFetch, certifique-se de ter os seguintes requisitos instalados:

- Python 3.6 ou superior
- Módulo `yt_dlp`
- Módulo `youtube-search`
- `ffmpeg`





## Instalação

1. Clone este repositório ou baixe os arquivos do script.

2. Instale as dependências necessárias utilizando `pip`:

    ```bash
    pip install yt-dlp youtube-search
    ```


3. Baixe e instale o `ffmpeg`:

    - Para Windows, baixe o executável do `ffmpeg` [aqui](https://www.ffmpeg.org/download.html) e adicione-o ao seu PATH.
    - Para Linux, instale o `ffmpeg` usando o gerenciador de pacotes da sua distribuição. Por exemplo:

    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```





## Uso

1. Execute o script:

    ```bash
    python dog_video_downloader.py
    ```

2. Siga as instruções no terminal:

    - O script perguntará se você deseja deletar os arquivos anteriores na pasta `./video`.
    - Digite "S" para deletar os arquivos ou "N" para manter os arquivos existentes.

3. Insira o nome do vídeo ou o link do YouTube quando solicitado.




## Exemplo de Execução

```py
$ python dog_video_downloader.py

Bem-vindo ao DogVidFetch

Deseja deletar os arquivos anteriores? (S/N): S
Arquivos anteriores deletados com sucesso.
Digite o nome ou o link do vídeo: <Nome ou link do vídeo>
Vídeo '<Título do Vídeo>' baixado com sucesso!
```




## Funcionamento Interno

```py
clear_previous_files(): Deleta todos os arquivos na pasta ./video.
get_user_choice(): Solicita ao usuário se deseja deletar os arquivos anteriores.
YouTubeDownloader: Classe que gerencia o download dos vídeos.

    get_info_by_ytlink(link): Obtém informações do vídeo pelo link do YouTube.
    find_video_link_by_name(name): Procura o vídeo pelo nome.
    download_by_name(name): Baixa o vídeo pelo nome.
    download_by_ytlink(link): Baixa o vídeo pelo link do YouTube.
    change_path(new_path): Altera o caminho onde os vídeos serão salvos.
```

## Contato
Se você encontrar algum problema ou tiver sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato.

> Feito com por Dogaix
