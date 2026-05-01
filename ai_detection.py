import cv2
import mediapipe as mp
import time

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

EYE_AR_THRESH = 0.20
DROWSY_TIME = 2
start_time = None

def eye_aspect_ratio(landmarks, eye):
    vertical = abs(landmarks[eye[1]].y - landmarks[eye[5]].y)
    horizontal = abs(landmarks[eye[0]].x - landmarks[eye[3]].x)
    return vertical / horizontal

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    status = "Normal"

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        left_eye = [33, 160, 158, 133, 153, 144]
        ear = eye_aspect_ratio(landmarks, left_eye)

        if ear < EYE_AR_THRESH:
            if start_time is None:
                start_time = time.time()
            elif time.time() - start_time > DROWSY_TIME:
                status = "DROWSY"
        else:
            start_time = None

    cv2.putText(frame, status, (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("Driver Monitor", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
