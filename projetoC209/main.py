import cv2
import os

def detect_image():
    cars_tracker = cv2.CascadeClassifier("xml/cars.xml")
    cars = cars_tracker.detectMultiScale(gray_img)
    person_tracker = cv2.CascadeClassifier("xml/pedestrian.xml")
    person = person_tracker.detectMultiScale(gray_img)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(img, 'Carro', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    for (x,y,w,h) in person:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2)
        cv2.putText(img, 'Pessoa', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow('Detecção', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def detect_video():
    cars_tracker = cv2.CascadeClassifier("xml/cars.xml")
    person_tracker = cv2.CascadeClassifier("xml/pedestrian.xml")
    bus_tracker = cv2.CascadeClassifier("xml/Bus_front.xml")
    two_tracker = cv2.CascadeClassifier("xml/two_wheeler.xml")
    
    while True:
        (read_successful, frame) = video.read()

        if read_successful:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            break

        cars = cars_tracker.detectMultiScale(gray_frame, 1.1, 9)
        person = person_tracker.detectMultiScale(gray_frame, 1.1, 9)
        bus = bus_tracker.detectMultiScale(gray_frame, 1.1, 9)
        twowheeler = two_tracker.detectMultiScale(gray_frame, 1.1, 9)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, 'Carro', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            # cv2.rectangle(gray_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        for (x, y, w, h) in person:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.putText(frame, 'Pessoa', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        for (x, y, w, h) in bus:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, 'Onibus', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        for (x, y, w, h) in twowheeler:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (216, 255, 0), 2)
            cv2.putText(frame, 'Bicicleta', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (216, 255, 0), 2)

        cv2.imshow('Detectar objetos na estrada', frame)

        key = cv2.waitKey(1)

        if key == 27:  # 27 para parar quando for pressionado o ESC
            break

    video.release()
    cv2.destroyAllWindows()

def detect_camera():
    face = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
    eye = cv2.CascadeClassifier('xml/haarcascade_eye_tree_eyeglasses.xml')

    camera = cv2.VideoCapture(0)
    if camera.isOpened():
        validation, frame = camera.read()
        while validation:
            validation, frame = camera.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face.detectMultiScale(gray)  # results=clsfr.predict(features)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'Rosto', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                face_img = gray[y:y + w, x:x + w]
                eyes = eye.detectMultiScale(face_img)

                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2)
                    cv2.putText(frame, 'Olho', (x + ex, y + ey - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            cv2.imshow('Camera', frame)
            result = cv2.waitKey(1)

            if result == 27:     # 27 para parar quando for pressionado o ESC
                break

        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    img_file = "midias/img1.jpg"
    video_file = "midias/traffic.mp4"
    
    img = cv2.imread(img_file)
    video = cv2.VideoCapture(video_file)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    while True:
        print('+---------------------------------------+')
        print('|    Projeto de Detecção de objetos     |')
        print('|                                       |')
        print('|  (1) - Detecção em Imagem             |')
        print('|  (2) - Detecção em Vídeo              |')
        print('|  (3) - Detecção em Camera             |')
        print('|  (4) - Sair                           |')
        print('+---------------------------------------+')
        x = int(input('Entre com uma opção: '))
        if x == 4:
            break
        elif x == 1:
            detect_image()
            os.system('cls')
        elif x == 2:
            detect_video()
            os.system('cls')
        elif x == 3:
            detect_camera()
            os.system('cls')
        else:
            print('Opção inválida!')
    print('Fim da execução do script!')


