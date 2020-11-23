import cv2
import os
import imutils
import numpy as np
from datetime import date

def camara(person_name):

    dataPath = "data/"
    personPath = dataPath + "/" + person_name

    if not os.path.exists(personPath):
        print("Capturando rostro de: ", person_name)
        os.makedirs(personPath)

    cap = cv2.VideoCapture(0)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    start = len(os.listdir(personPath))

    count = start

    limint = start + 300

    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 15)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + "/rostro_{}.jpg".format(count), rostro)
            count += 1

        cv2.imshow("Horizontal", frame)

        k = cv2.waitKey(1)
        if k == 27 or count >= limint:
            break

    cap.release()
    cv2.destroyAllWindows()

    return 0

def training():
    dataPath = "data"
    peopleList = os.listdir(dataPath)
    labels = []
    facesData = []
    label = 0
    for nameDir in peopleList:
        personPath_M = dataPath + "/" + nameDir

        for fileName in os.listdir(personPath_M):
            labels.append(label)
            facesData.append(cv2.imread(personPath_M + "/" + fileName, 0))

        label += 1

    face_recognizer = cv2.face.EigenFaceRecognizer_create()

    # Entrenando el reconocedor de rostros
    print("Entrenando Reconocimiento de Rostros...")
    print("(Esto puede tardar unos minutos)")
    face_recognizer.train(facesData, np.array(labels))

    # Almacenando el modelo obtenidio
    face_recognizer.write("modeloEigenFace.xml")

    return 0

def lista():
    dataPath = "data"
    list_students = os.listdir(dataPath)

    return list_students

def assistance():

    precentes = []

    dataPath = "data"
    imagePath = os.listdir(dataPath)

    filePath = str("Presentes" + "/")

    if not os.path.exists(filePath):
        os.makedirs(filePath)

    fecha= str(date.today().day) + "-" + str(date.today().month) + "-" + str(date.today().year) + ".txt"

    face_recognizer = cv2.face.EigenFaceRecognizer_create()

    # Leyendo el modelo
    face_recognizer.read("modeloEigenFace.xml")

    cap = cv2.VideoCapture(0)

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        ret, frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 15)

        if fecha in os.listdir(filePath):
            cv2.putText(frame, '"ESC" para salir. ', (10, 20), 2, 0.5, (128, 0, 255), 1, cv2.LINE_AA)
        else:
            cv2.putText(frame, '"ESC" para salir. Solo si estan todos los Alumnos PRESENTES', (10, 20), 2, 0.5,
                        (128, 0, 255), 1, cv2.LINE_AA)

        for (x, y, w, h) in faces:
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)

            # print("result: ", result)
            # print(type(result))

            #cv2.putText(frame, "{}".format(result), (x, y - 15), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)



            # eigenFaces
            if result[1] < 5700:
                cv2.putText(frame, "{}".format(imagePath[result[0]]), (x, y - 25), 1, 1.3, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if imagePath[result[0]] in precentes:
                    pass
                else:
                    precentes.append(imagePath[result[0]])

            else:
                cv2.putText(frame, "desconocido", (x, y - 20), 1, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


    if fecha in os.listdir(filePath):
        file = open(filePath + fecha, "a")
        file.write("==========================================================================\n")
        file.write("Alumnos Presentes Tarde: \n")
        for x in range(len(precentes)):
            file.write(precentes[x] + "\n")
        file.close()
    else:
        file = open(filePath + fecha, "a")
        file.write("==========================================================================\n")
        file.write("Alumnos Presentes: \n")
        for x in range(len(precentes)):
            file.write(precentes[x] + "\n")
        file.close()

    return 0