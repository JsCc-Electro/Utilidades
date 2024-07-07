from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def split_video(input_path, output_dir, chunk_duration):
    """
    Divide un video en partes de una duración específica.
    
    :param input_path: Ruta del video de entrada.
    :param output_dir: Directorio donde se guardarán las partes divididas.
    :param chunk_duration: Duración de cada parte en segundos.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video = VideoFileClip(input_path)
    total_duration = video.duration
    num_chunks = int(total_duration // chunk_duration) + (1 if total_duration % chunk_duration > 0 else 0)

    for i in range(num_chunks):
        start_time = i * chunk_duration
        end_time = min((i + 1) * chunk_duration, total_duration)
        
        chunk = video.subclip(start_time, end_time)
        output_path = os.path.join(output_dir, f'part_{i + 1}.mp4')
        chunk.write_videofile(output_path, codec='libx264')

    video.close()

# Ejemplo de uso
input_video_path = r"C:\Users\Andres Cardenas\Downloads\IA_ ¿oportunidad o riesgo para el empleo_\IA_oportunidad.mp4"
output_directory = r"C:\Users\Andres Cardenas\Downloads\IA_ ¿oportunidad o riesgo para el empleo_\partes"
duracion_por_parte = 119  # Duración en segundos de cada parte

split_video(input_video_path, output_directory, duracion_por_parte)
