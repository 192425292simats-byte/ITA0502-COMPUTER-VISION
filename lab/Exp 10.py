import cv2
img = cv2.imread(r"C:\Users\pavan\OneDrive\Opencv\image.png")
if img is None:
    print("Error: Image not found.")
else:
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
