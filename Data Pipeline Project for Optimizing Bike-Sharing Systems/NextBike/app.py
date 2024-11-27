import cv2

# Initialize the camera
cam = cv2.VideoCapture(0)

# Create a window to display the camera feed
cv2.namedWindow("Camera Feed")

# Collect the data
while True:
    # Read a frame from the camera
    ret, frame = cam.read()

    # Display the frame in the window
    cv2.imshow("Camera Feed", frame)

    # Press 'q' to exit the loop and stop collecting data
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and destroy the window
cam.release()
cv2.destroyAllWindows()

