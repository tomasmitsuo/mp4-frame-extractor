import cv2
import os
import args

arguments = args.setup()

videoSource = arguments.video
requestedFrameNumber = int(arguments.frame)
videoDestinationPath = arguments.out

if __name__ == '__main__':
  if videoSource == '':
    raise Exception('requested frame is longer than video.')

  if not os.path.isfile(videoSource):
    raise Exception('video not found.')

  video = cv2.VideoCapture(videoSource)

  videoLength = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
  fps = int(video.get(cv2.CAP_PROP_FPS))

  # Cria um novo Diretório com o videoDestinationPath (Por o nome da Pessoa)

  current_directory = os.getcwd()
  final_directory = os.path.join(current_directory, videoDestinationPath)
  if not os.path.exists(final_directory):
    os.makedirs(final_directory)

  for i in range(20):

    frameNumber = (requestedFrameNumber / (videoLength * fps))   # Formula do numero do frame

    if frameNumber > videoLength:
      raise Exception('requested frame is longer than video.')

    # 1 is the prop for frame position in cv2 in python 3

    video.set(1, frameNumber)
    success, image = video.read()

    if success == False:
      raise Exception('failed to read the frame.')

    dest = os.path.realpath(os.getcwd() + '/assets/output')

    if videoDestinationPath:
      dest = os.path.abspath(videoDestinationPath)

    cv2.imwrite(dest + '/frame-%d.jpg' % requestedFrameNumber, image)

    requestedFrameNumber = requestedFrameNumber + 10000  #Atualiza o frame

  video.release()
