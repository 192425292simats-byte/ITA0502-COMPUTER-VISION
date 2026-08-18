import cv2

image = cv2.imread(r"C:\Users\sunil sharma\OneDrive\Desktop\OPENCV\tree (3).jpg")

if image is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

image = cv2.resize(image, (500, 400))
edges = cv2.resize(edges, (500, 400))

edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

combined = cv2.hconcat([image, edges])

cv2.imshow("Original | Edge", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
