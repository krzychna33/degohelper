import os
import cv2

inputDir = 'C:\\Users\krzyc\OneDrive\Pulpit\dego'
outputDir = "C:\\Users\krzyc\Documents\degoczas"

print(cv2.__version__)
vidcap = cv2.VideoCapture(os.path.join(inputDir, 'znakowanie-czasem.mp4'))
count=1
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite(outputDir + '\\frame_' + str(count) + ".jpg", image)  # Save frame as JPG file
    return hasFrames

sec = 0
frameRate = 1  # Change this number to 1 for each 1 second

success = getFrame(sec)
while success:
    print(success)
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)