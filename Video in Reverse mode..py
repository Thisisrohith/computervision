import cv2*

# Load the video
cap = cv2.VideoCapture("C:/Users/Dama Prasoona/OneDrive/Pictures/Camera Roll/WIN_20230513_10_41_29_Pro.mp4")

# Get the number of frames in the video
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Set the current frame to the last frame
current_frame = num_frames - 1

# Loop through the frames in reverse order
while current_frame >= 0:
    # Set the current frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

    # Read the current frame
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video in Reverse', frame)

    # Wait for a key press and check if the 'q' key was pressed to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # Decrement the current frame
    current_frame -= 1

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
