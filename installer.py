import youtube

url = input("introduce la url del video")

youtube = youtube(url)

streams = youtube.streams.filter(
    progresive=True, file_extension='mp4'
).order_by('resolution').desc()

for i, streams in enumerate(streams):
    print(f"{i+1}. {streams.resolution} ({streams.fps}fps)")

selection = int(input("seleccione el numero de streams que desea descargar: "))
video = streams[selection-1]

try:
    video.download(output_path='./descargas')
except Exception as e:
    print("ha ocurrido un error al descargar", e)
    