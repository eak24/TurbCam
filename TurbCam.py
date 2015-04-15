import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Input: camera capture instance
# Output: grayscale frame
def getFrameGray(cap):
	# Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Input: a raw value to find the turbidity of, and two calibration 
# points (value a for x turbidity and b for y turbidity)
# Output: estimated turbidity value of raw_val
def getTurbValue(raw_val,(a,x),(b,y)):
	# Find Inverse Slope
	m = (y-x)*(b-a)
	# Find Adjustmant Constant
	i = m/a-x
	return m/raw_val+i

# Record 0 NTU calibration value
x=int(raw_input("ENTER NTU VALUE OF NTU ON CAMERA"))
a=np.mean(getFrameGray(cap))

# Record 0 NTU calibration value
y=int(raw_input("ENTER NTU VALUE OF NTU ON CAMERA"))
b=np.mean(getFrameGray(cap))

# main loop
while(True):
	# Get the next frame
    gray = getFrameGray(cap)

    # Calculate the mean of the image
    raw_val = np.mean(gray)

    # Find the turbidity
    print getTurbValue(raw_val,(a,x),(b,y))

     # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()