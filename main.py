import cv2
import easyocr
import matplotlib.pyplot as plt

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# initialize camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame")
        break

    # detect text on frame
    text_ = reader.readtext(frame)

    threshold = 0.25
    # draw bbox and text
    for t_, t in enumerate(text_):
        bbox, text, score = t

        if score > threshold:
            cv2.rectangle(frame, bbox[0], bbox[2], (0, 255, 0), 5)
            cv2.putText(frame, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

    # Convert BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    plt.imshow(frame_rgb)
    plt.axis('off')  # Turn off axis
    plt.show()

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
