import cv2
import os
import json
import shutil


def manual_frame(videoPath, videoFileName, seconds, defaultH, defaultW):
    videoFolderName = str(videoFileName).split('.', 1)[0]
    pathOfDest = videoPath + "/" + videoFolderName

    if os.path.isdir(pathOfDest):
        shutil.rmtree(pathOfDest)
        createDir(videoPath, videoFolderName) 
        process(videoFileName, videoPath, seconds,
                pathOfDest, defaultH, defaultW)
        json_output = json.dumps(
            {'error': 'false', 'data': 'completed'})
        return json_output
    else:
        createDir(videoPath, videoFolderName)
        process(videoFileName, videoPath, seconds,
                pathOfDest, defaultH, defaultW)
        json_output = json.dumps(
            {'error': 'false', 'data': 'completed'})
        return json_output


def createDir(videoPath, videoFolderName):
    os.makedirs(videoPath + "/" + videoFolderName, exist_ok=True)


def process(videoFileName, videoPath, seconds, pathOfDest, defaultH, defaultW):

    vidcap = cv2.VideoCapture(videoPath + "/" + videoFileName)

    success = True

    fps = vidcap.get(cv2.CAP_PROP_FPS)
    multiplier = int(fps) * int(seconds)

    while success:
        frameId = int(round(vidcap.get(1)))
        success, image = vidcap.read()

        if frameId % multiplier == 0:
            cv2.imwrite(pathOfDest + "/" + "%d-shot.jpg" %
                        frameId, cv2.resize(image, (defaultH, defaultW),
                                            interpolation=cv2.INTER_NEAREST))

    vidcap.release()
    cv2.destroyAllWindows()
