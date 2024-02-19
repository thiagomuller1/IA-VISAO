Olá,

Segue projeto sobre visão computacional com IA

Utilizado Rede neural Yolo v4
https://github.com/AlexeyAB/darknet

Database CocoNames

Dependencias a serem instaladas:
pip install opencv-python   
pip install opencv-contrib-python

Dependencias a serem importadas
import cv2
import time


*UTILIZAÇÃO COM CAMERA IP*

1° ATIVAR O PROTOCOLO RTSP NA SUA CAMERA IP (CASO NÃO VENHA DE FABRICA)
https://www.youtube.com/watch?v=tFlEbYWBDLE
2° ALTERAR O ALGORITIMO ONDE ESTÁ COMENTADO PARA SEU ACESSO RTSP, COM IP
#CAPTURA DE VIDEO PARA: cap = cv2.VideoCapture("rtsp://192.168.0.1//live/ch00_1")

