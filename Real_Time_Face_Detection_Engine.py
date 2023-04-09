import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("Welcome to the Face Detection Engine !")
print("press -> 1 for performing face detection from image files")
print("press -> 2 for performing face detection from live web cam")


key = int(input())

if key == 1:
    img = cv2.imread(
        "C:/Users/dell/Downloads/op/Profile Picture(N S K K K Naga Jayanth).jpeg", 1)  # for reading the image file

    # converting color to gray image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Trying to detect the exact position of the face in the image
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

    # designing an artifact with desirable specifications
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("updated_image", img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

if key == 2:
    cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

    while True:
        _, img = cap.read()

    # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
        cv2.imshow('img', img)

    # Stop if escape key is pressed
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break

# Release the VideoCapture object
    cap.release()
