# import cv2
# cam = cv2.VideoCapture()
# while True:

#     cv2.imshow()
import cv2

# Kamerani tanlash
cap = cv2.VideoCapture(0)  # 0 - standart kamera

while True:
    # Kameradan rasm olish
    ret, frame = cap.read()

    # Rasmni ekran yoki oynaga chiqarish
    cv2.imshow('Camera', frame)

    # "Esc" tugmasi orqali dasturni to'xtatish
    if cv2.waitKey(1) == 27:
        break

# Kamerani yopish
cap.release()
cv2.destroyAllWindows()
