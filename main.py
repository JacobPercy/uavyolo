import cv2
import numpy as np

def to_color(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame_blurred = cv2.GaussianBlur(frame, (3, 3), 0)
    edges = cv2.Canny(frame_blurred, 60, 100)
    edges_color = to_color(edges)

    test = np.clip((-edges_color.astype(np.float32) + 2 * frame.astype(np.float32)) / 2, 0, 255).astype(np.uint8)


    #cv2.imshow('Camera', np.ones((edges.shape), dtype=np.uint8)*255 - edges)
    cv2.imshow('Edges', edges)
    #cv2.imshow('Camera', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
