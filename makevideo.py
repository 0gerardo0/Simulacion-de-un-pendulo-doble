import cv2
import os
import imageio.v2 as imageio

directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

directorio_imagenes = "trayectoria-b"

archivos_imagenes = [os.path.join(directorio_imagenes, archivo) for archivo in os.listdir(directorio_imagenes)]

fps = 10
salida_video = 'movimiento_pendulo.mp4'

imagen = cv2.imread(archivos_imagenes[0])
alto, ancho, _ = imagen.shape

salida_video = os.path.join(os.getcwd(), salida_video)

codec = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(salida_video, codec, fps, (ancho, alto))

for archivo_imagen in archivos_imagenes:
    imagen = cv2.imread(archivo_imagen)
    video.write(imagen)

video.release()

print(f"El video se ha creado en {salida_video}")

salida_video_gif = 'movimiento_pendulo.gif'
with imageio.get_writer(salida_video_gif, mode='I', duration=1/fps) as writer:
    for archivo_imagen in archivos_imagenes:
        imagen = imageio.imread(archivo_imagen)
        writer.append_data(imagen)

print(f"El video GIF se ha creado en {salida_video_gif}")
