import numpy as np
import cv2

def mouse(event, x, y, flags, param):
    global clonel, mask, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(clone1, (x, y), 5, (0, 0, 0), -1)
            cv2.circle(mask, (x, y), 5, (255, 255, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        
drawing = False
img = cv2.imread("cat_damaged.png")
clone1 = img.copy()
clone2 = img.copy()

# Creating two more windows one for showing the mask that the user will draw manually and one for the destination image.
dst = np.zeros(img.shape, np.uint8)
mask = np.zeros(img.shape[:2], dtype=np.uint8)

cv2.namedWindow("Input")
cv2.namedWindow("Output")
cv2.setMouseCallback("Input", mouse)

while(True):
    k = cv2.waitKey(1)
    # After drawing the part user wants to be healed with mouse, click "i" on the keyboard to apply the healing and give out the result.
    if k == ord("i"):
        dst = cv2.inpaint(clone2, mask, 3, cv2.INPAINT_TELEA)
    
    # Click "r" to reset everything back and be able to draw fresh.
    elif k == ord("r"):
        clone1 = img.copy()
        mask = np.zeros(clone1.shape[:2], dtype= np.uint8)
        dst = np.zeros(clone1.shape, np.uint8)
    
    # Click "esc" to close the program.
    elif k == 27:
        break

    cv2.imshow("Input", clone1)
    cv2.imshow("Mask", mask)
    cv2.imshow("Output", dst)

cv2.destroyAllWindows()