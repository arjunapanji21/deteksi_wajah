import cv2

# initial value
cap = cv2.VideoCapture(0)
cascPath = "wajah.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

while True:
    # Read the image
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect object in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("{0} wajah terdeteksi!".format(len(faces)))

    # Draw a rectangle around object
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, '@arjunapanji21', (x,y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Deteksi", frame)

    # press ESC to quit program
    if cv2.waitKey(1) & 0xFF == 27:
        break
