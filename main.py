#CARREGA AS DEPENDENCIAS
import cv2
import time

#Cores das Classes
COLORS = [(0, 255, 255), (255, 255, 0),(255, 0, 0)]

#CARREGA AS CLASSES
class_names = []
with open("coco.names","r") as f:
        class_names = [cname.strip() for cname in f.readlines()]

#Captura do Vide
cap = cv2.VideoCapture(0)

#Carregandos os pesos da rede neural
net = cv2.dnn.readNet("yolov4-tiny.weights","yolov4-tiny.cfg")

#setando os parametros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

#lendo os frames do video
while True:

    #captura do frame
    _, frame = cap.read()

    #começo da contagem do MS
    start = time.time()

    #detecção
    classes, scores, boxes = model.detect(frame, 0.1, 0.2)

    #fim da contagem do ms
    end = time.time()

    #percorrer todas as detecções
    for (classid, score, box) in zip(classes, scores, boxes):

        #gerando uma cor para a classe
        color = COLORS[int(classid) % len(COLORS)]

        #pegando o nome da classe pelo id e o seu score de acuracia
        label = f"{class_names[classid]} : {score}"

        #desenhando a box da detecção
        cv2.rectangle(frame, box, color, 2)

        #escrevendo o nome da classe em cima da box do obj
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    #calculando o tempo que levou para fazer a detecção
    fps_label = f"FPS: {round((1.0/(end - start)),2)}"

    #escrevendo o fps na imagem
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    #mostrando a imagem
    cv2.imshow("detections", frame)

    #espera da resposta
    if cv2.waitKey(1) == 27:
        break

# liberação da camera e destroi de todas as janelas
cap.release()
cv2.destroyAllWindows()



