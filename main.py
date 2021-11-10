import cv2
import os
from tkinter import filedialog
import mysql.connector

caminho = filedialog.askopenfilename()
entrada = cv2.imread(caminho)
con = mysql.connector.connect(host='localhost',database='Digital',user='thiago',password='Tmysql@4581')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = con.cursor()


    cursor.execute("select * from func;")
    linha = cursor.fetchall()
    for i in linha:
        print("{}".format(i[6]))
        original = cv2.imread("{}".format(i[6]))

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

        compt = (len(ponts) / keypoints)
        # if compt > 0.95:
        print(compt * 100)

