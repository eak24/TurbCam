# TurbCam
An extremely simple Python program to turn any camera into a turbidimeter using two samples of known samples. 
Use any light source on the opposite side of the sample.

Major challenges/upgrades: 
  Accounting for/turning off white balance on the camera. 
  Determining the proper scattering theory to predict the calibration curve... Back-scatter v. forward scatter?
  Dealing with edge effects when the whole field of view is not taken up by the sample.
  Developing an intuitive Gui that allows one to graph NTU changes over time.
  Adding the capability to sense DOM using the camera
  Saving to an Excel file for further analysis
  Saving video/histograms?
