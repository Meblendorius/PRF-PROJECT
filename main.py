import cv2
import os

entrada = cv2.imread("./images/finger2.tif")
for file in [file for file in os.listdir("database")]:
    original = cv2.imread("database/"+file)

    sift = cv2.xfeatures2d.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(original, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(entrada, None)

    comp = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
                                    dict()).knnMatch(descriptors_1, descriptors_2, k=2)
    ponts = []

    for x, y in comp:
        if x.distance < 0.1 * y.distance:
            ponts.append(x)
    keypoints = 0
    if len(keypoints_1) <= len(keypoints_2):
        keypoints = len(keypoints_1)
    else:
        keypoints = len(keypoints_2)

    compt=(len(ponts) / keypoints)
    if compt > 0.95:

        print("% Compatibilidade "+file+": ", compt * 100)

