import numpy as np
import cv2

# Mission:
# TurbCam determines the turbidity of a sample using
# a camera, any clear container, and at least two known turbidity 
# samples. 

# Functionality:
# Scattering Theories: 
# Define the types of calibration curves that can be used. 
# The calibration curve is determined by the experimental 
# setup. Back-scatter turbidimeters should use a linear curve
# while forward-scatter should use a log curve.


# cap is capturing video on camera with address 0 
cap = cv2.VideoCapture(0)

# TODO: Set the White Balance manually
cap.set(cv2.cv.CV_CAP_PROP_FPS, 2);

# Input: camera capture instance
# Output: grayscale frame
def getFrameGray(cap):
	# Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Input: Two calibration points 
# Output: (l,i_in)
def getTurbCalLin(t1,i1,t2,i2):
    # Find the path length, l
    l = np.log(i2/i1)/(t1-t2)
	# Find the incoming light intensity, i_in
    i_in = i2/(np.exp(-t2*l))
    return (l,i_in)

# Input: Calibration Values and light intensity
# Output: Turbidity
def getTurbValLin(raw_val,l,i_in):
    return np.log(raw_val/i_in)/(-l)
	
# Record 0 NTU calibration value
t1=int(raw_input("ENTER NTU VALUE OF NTU ON CAMERA \n"))
i1=np.mean(getFrameGray(cap))

# Record 0 NTU calibration value
t2=int(raw_input("ENTER NTU VALUE OF NTU ON CAMERA \n"))
i2=np.mean(getFrameGray(cap))

(l,i_in) = getTurbCalLin(t1,i1,t2,i2)
# main loop
while(True):
	# Get the next frame
    gray = getFrameGray(cap)

    # Calculate the mean of the image
    raw_val = np.mean(gray)

    # Find the turbidity
    print(getTurbValLin(raw_val,l,i_in))

     # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()