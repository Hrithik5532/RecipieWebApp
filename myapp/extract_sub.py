from videocr import get_subtitles

print(get_subtitles('fairytail.mp4', lang='eng', sim_threshold=70, conf_threshold=65))
