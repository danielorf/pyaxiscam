# **pyaxiscam**

pyaxiscam is a Python library used to control Axis Communications IP cameras.  You can access information about the
camera as well as grab images (and video stream in the future).



## **Getting Started**

Your Axis camera must fir be set up using its web interface.  It is recommended to do this with Internet Explorer on a
Windows PC for the best compatibility.  Once set up, you now have a host name (or IP address), username ('root' by
default), and the password.  Initialize and AxisCam object using the following line - make sure to replace 'host',
'username', and 'password' with the IP address, username and password determined in the setup:

cam = AxisCam('host', 'username', 'password')

A live image can be retrieved by using the following command:

    image = cam.get_live_image()

This image can then be processed using OpenCV for example.

A live image can be retrieved and displayed by using the following command:

    image = cam.display_live_image()

The image is displayed by the default image viewer.



## **Prerequisites**

requests,
io,
PIL
