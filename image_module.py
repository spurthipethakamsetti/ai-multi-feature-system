import cv2


def classify_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return "Invalid Image"
    height, width, _ = img.shape

    # Very simple logic (for demo)
    if width > height:
        return "Landscape Image 🏞️"
    elif width < height:
        return "Portrait Image 🧍"
    else:
        return "Square Image 🟦"
