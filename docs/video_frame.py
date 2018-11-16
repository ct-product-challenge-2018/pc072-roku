import cv2
interval = 1 # every 1 seconds

if __name__ == '__main__' :
 
    video = cv2.VideoCapture("trailer.mp4");
     
    # # Find OpenCV version
    # (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # if int(major_ver)  < 3 :
    #     fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    #     print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    # else :
    fps = round(video.get(cv2.CAP_PROP_FPS))
    print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    success, image = video.read()
    image_count = 0
    frame_count = 1
    success = True

    while success:
        success, image = video.read()
        # print('read a new frame:',success)
        if frame_count == fps * interval:
            image_count += 1
            cv2.imwrite('screenshots/image%d.jpg' % image_count, image)
            print('success')
            frame_count = 0
        frame_count += 1
    video.release(); 