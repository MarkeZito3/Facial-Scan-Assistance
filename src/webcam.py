import cv2
import os
import mediapipe as mp
from datetime import datetime
import pandas as pd
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


def camara(person_name):
    dataPath = "data"
    personPath = os.path.join(dataPath, person_name)

    os.makedirs(personPath, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = len(os.listdir(personPath))
    limit = count + 150
    direction_counter = 0

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        while cap.isOpened() and count < limit:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)  # Modo espejo
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(frame_rgb)

            progress = int((count / limit) * 100)

            if results.detections:
                for detection in results.detections:
                    bbox = detection.location_data.relative_bounding_box
                    h, w, _ = frame.shape
                    x, y, bw, bh = int(bbox.xmin * w), int(bbox.ymin * h), int(bbox.width * w), int(bbox.height * h)
                    x = max(0, x)
                    y = max(0, y)
                    x2 = min(w, x + bw)
                    y2 = min(h, y + bh)

                    rostro = frame[y:y2, x:x2]
                    # rostro = frame[y:y + bh, x:x + bw]
                    rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(os.path.join(personPath, f"rostro_{count}.jpg"), rostro)
                    count += 1
                    # cv2.waitKey(100)

                    cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)


            # Barra de progreso
            bar_width = 200
            bar_height = 20
            filled_width = int((progress / 100) * bar_width)
            cv2.putText(frame, f"Progreso: {progress}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(frame, (10, 40), (10 + bar_width, 40 + bar_height), (0, 255, 0), 2)
            cv2.rectangle(frame, (10, 40), (10 + filled_width, 40 + bar_height), (0, 255, 0), -1)

            direction_counter += 1
            cv2.imshow("Captura de rostros", frame)
            if cv2.waitKey(1) == 27:  # Escape key
                break


    cap.release()
    cv2.destroyAllWindows()


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
    os.makedirs(dataPath, exist_ok=True)
    return os.listdir(dataPath)


def assistance():
    presentes = []
    horas_presentes = {}
    
    # Configuración de paths
    dataPath = "data"
    os.makedirs(dataPath, exist_ok=True)
    imagePath = os.listdir(dataPath)
    
    filePath = "Presentes/"
    os.makedirs(filePath, exist_ok=True)

    # Fechas y horas
    fecha_archivo = datetime.now().strftime("%d-%m-%Y")
    
    # Configurar reconocedor facial
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.read("modeloEigenFace.xml")

    cap = cv2.VideoCapture(0)

    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(frame_rgb)

            if results.detections:
                for detection in results.detections:
                    bbox = detection.location_data.relative_bounding_box
                    h, w, _ = frame.shape
                    x = int(bbox.xmin * w)
                    y = int(bbox.ymin * h)
                    bw = int(bbox.width * w)
                    bh = int(bbox.height * h)

                    x = max(0, x)
                    y = max(0, y)
                    x2 = min(w, x + bw)
                    y2 = min(h, y + bh)

                    rostro = frame[y:y2, x:x2]

                    # rostro = frame[y:y + bh, x:x + bw]
                    rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                    rostro_gray = cv2.cvtColor(rostro, cv2.COLOR_BGR2GRAY)

                    result = face_recognizer.predict(rostro_gray)

                    if result[1] < 6700:
                        nombre = imagePath[result[0]]
                        cv2.putText(frame, nombre, (x, y - 25), 1, 1.3, (0, 255, 0), 2, cv2.LINE_AA)
                        cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)

                        if nombre not in presentes:
                            presentes.append(nombre)
                            horas_presentes[nombre] = datetime.now().strftime('%H:%M:%S')
                    else:
                        cv2.putText(frame, "Desconocido", (x, y - 20), 1, 1.3, (0, 0, 255), 2, cv2.LINE_AA)
                        cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 0, 255), 2)

            # Mostrar lista de asistencia
            altura = 30
            for nombre in imagePath:
                color = (0, 255, 0) if nombre in presentes else (0, 0, 255)
                cv2.putText(frame, nombre, (10, altura), 1, 1.2, color, 2)
                altura += 25

            cv2.imshow("Tomando asistencia", frame)
            if cv2.waitKey(1) == 27:  # Escape key
                break

    cap.release()
    cv2.destroyAllWindows()

    # Guardar resultados
    with open(filePath + fecha_archivo + ".txt", "a") as f:
        for nombre in presentes:
            f.write(f"{nombre} - {horas_presentes[nombre]}\n")

    df = pd.DataFrame({"Nombre": presentes, "Hora": [horas_presentes[n] for n in presentes]})
    df.to_excel(filePath + fecha_archivo + ".xlsx", index=False)

    return 0