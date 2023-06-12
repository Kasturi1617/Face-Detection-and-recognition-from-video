import cv2
import os

# Set the path to the input video file
input_path = 'test_video.mp4'

# Set the path to the directory where the output images will be saved
output_dir = 'Photos2'

# Open the video file
cap = cv2.VideoCapture(input_path)

# Initialize a counter to keep track of the current second
current_second = 0

# Set the frame rate (frames per second)
frame_rate = cap.get(cv2.CAP_PROP_FPS)

# Loop through the video frames
while cap.isOpened():
    # Read the next frame
    ret, frame = cap.read()

    # If there are no more frames, break out of the loop
    if not ret:
        break

    # Calculate the current time in seconds
    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

    # If one second has passed since the last image was saved, save the current frame as an image
    if current_time > current_second:
        # Set the file name for the output image
        file_name = os.path.join(output_dir, f'image_{int(current_time)}.jpg')

        # Save the frame as an image
        cv2.imwrite(file_name, frame)

        # Increment the current second counter
        current_second += 1

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
