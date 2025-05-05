import yt_dlp
import os

def get_music_list(file_path):
    """Lê a lista de músicas do arquivo txt"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return [musica.strip() for musica in content.split(';') if musica.strip()]

def setup_output_dir():
    """Cria o diretório de saída para os karaokês"""
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Karaokes baixados")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def download_karaoke(nome_musica, numero, output_dir, progress_callback=None):
    """Baixa e converte um vídeo de karaokê"""
    termo_pesquisa = f"{nome_musica} karaoke"
    nome_arquivo = f"{numero} - {nome_musica}"
    caminho_saida = os.path.join(output_dir, f"{nome_arquivo}.%(ext)s")

    ydl_opts = {
        'format': 'mp4',  # Formato simplificado
        'outtmpl': caminho_saida,
        'noplaylist': True,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'prefer_ffmpeg': True,
        'keepvideo': True
    }

    try:
        if progress_callback:
            progress_callback(f"Baixando: {nome_musica}")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{termo_pesquisa}"])
        
        if progress_callback:
            progress_callback(f"Download concluído: {nome_musica}")
        return True
    except Exception as e:
        if progress_callback:
            progress_callback(f"Falha ao baixar: {nome_musica} - Erro: {str(e)}")
        return False

def process_music_list(file_path, numero_inicial, progress_callback=None):
    """Processa toda a lista de músicas"""
    musicas = get_music_list(file_path)
    output_dir = setup_output_dir()
    falhas = []

    for i, musica in enumerate(musicas):
        numero = numero_inicial + i
        success = download_karaoke(musica, numero, output_dir, progress_callback)
        if not success:
            falhas.append(f"{numero} - {musica}")

    return falhas