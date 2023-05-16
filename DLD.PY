import cv2 # sudo apt install python3-opencv
import numpy as np

def is_lens_dirty(ref_image, current_image):
    # Convert images to grayscale
    ref_gray = cv2.cvtColor(ref_image, cv2.COLOR_BGR2GRAY)
    current_gray = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)

    # Calculate absolute difference between the images
    diff = cv2.absdiff(ref_gray, current_gray)

    # Threshold the difference image to highlight the changes
    threshold = 30  # Adjust this value according to your needs
    _, thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Count the number of non-zero pixels
    non_zero_pixels = np.count_nonzero(thresholded)

    # Determine if lens is dirty based on a threshold
    dirty_threshold = 500  # Adjust this value according to your needs
    is_dirty = non_zero_pixels > dirty_threshold

    return is_dirty
# Load the reference image and the current image
ref_image = cv2.imread('reference_image.jpg')
current_image = cv2.imread('current_image.jpg')

# Check if the lens is dirty
dirty_status = is_lens_dirty(ref_image, current_image)

# Output the result
if dirty_status:
    print("The lens is dirty.")
else:
    print("The lens is clean.")