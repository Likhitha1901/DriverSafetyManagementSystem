import cv2
from phone_detection import detect_phone
from ai_detection import face_mesh, eye_aspect_ratio

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    phone = detect_phone(frame)
    status = "NORMAL"

    if phone:
        status = "PHONE USAGE"

    cv2.putText(frame, status, (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow("Driver Monitor", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()