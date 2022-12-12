from moviepy.editor import VideoFileClip, concatenate_videoclips
from os.path import isfile, join
from collections import defaultdict
from pathlib import Path
import config,os

cwd = os.getcwd()
down = str(Path.home()/"Downloads")
def makeCompilation(path =cwd+"/Bot/Reddit/",
                    introName = 'intro_vid',
                    outroName = 'Outro_vid',
                    totalVidLength = 10*60,
                    outputFile = down+"/"+config.name):

    allVideos = []
    seenLengths = defaultdict(list)
    totalLength = 0
    for fileName in os.listdir(path):

        filePath = join(path, fileName)
        if isfile(filePath) and fileName.endswith(".mp4"):
            print(fileName)

            # Destination path
            clip = VideoFileClip(filePath)
            clip = clip.resize((1920,1080))
            duration = clip.duration
            print(duration)
            allVideos.append(clip)
            seenLengths[duration].append(fileName)
            totalLength += duration

    # Add intro vid
    videos = []
    if introName != '':
        introVid = VideoFileClip(config.intro_video)
        introVid = introVid.resize((1920,1080))
        videos.append(introVid)
        duration += introVid.duration

    # Create videos
    transition = VideoFileClip(config.transition_video)
    transition = transition.resize((1920,1080))
    for clip in allVideos:
        videos.append(clip)
        videos.append(transition)
        duration += clip.duration
        duration += transition.duration
        print(duration)
        if duration >= totalVidLength:
            # Just make one video
            break

    # Add outro vid
    if outroName != '':
        outroVid = VideoFileClip(config.outro_video)
        outroVid = outroVid.resize((1920,1080))
        videos.append(outroVid)
        duration += outroVid.duration

    finalClip = concatenate_videoclips(videos, method="compose")

    finalClip.write_videofile(outputFile, threads=8, remove_temp=True, codec="libx264", audio_codec="aac", preset="medium", fps=20)

    return "Finished Editing"

if __name__ == "__main__":
    makeCompilation(path = "Bot/Reddit/",outputFile = down+"/"+config.name)