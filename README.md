# VisionBased_drowsiness_detector
Drowsiness detection system to do continuous monitorinfg of the driver and will able to alert the driver from falling asleep.
In this program we check how long a person's eyes have been closed for. If the eyes have been closed for a long period i.e. 
beyond a certain threshold value, the program will alert the user by playing an alarm sound,text notification and text to speech call using nexmo api.

<img src="https://github.com/AjinkyaAshok/VisionBased_drowsiness_detector/blob/master/Test%20Images/test.jpeg">

##### Test image.

<img src="https://github.com/AjinkyaAshok/VisionBased_drowsiness_detector/blob/master/Test%20Images/aftermath_face_detection.png">

##### Frontal_face_detection.

1. #### frontal_face_detector_single_image_test.py - Detects face and eye in a webcam feed by user Webcam Face and Eye Detection.
2. #### visionbased_drowsiness_detector_main.py- This script detects if person is drowsy or not, using webcam video feed and alerts(sound alert,text,call) the person.
3. https://github.com/AjinkyaAshok/VisionBased_drowsiness_detector/blob/master/Test%20Images/call_notification.mp4
(Click view raw and download the video from above link)

__Video shows how text to speech call works using nexmo.__

## Requirements > > IMPORTANT
* Download shape_predictor_68_face_landmarks.dat.bz2 from Shape Predictor 68 features Extract the file in the project folder using bzip2 -dk shape_predictor_68_face_landmarks.dat.bz2

__Install all libraries using pip3__
* numpy==1.16.2
* dlib==19.20.0
* pygame==1.9.4
* imutils==0.5.3
* opencv_python==3.4.6  (cv2)
* scipy==1.1.0

__Nexmo Libs__
* client
* nexmo==2.4.0
* time
* pprint

Here I used the raspberry pi 4 controller with raspbian os, One can use Ubuntu server also.

## How to use Nexmo API

#### SMS
First, sign up for a Nexmo account if you don't already have one, and make a note of your API key and secret on the dashboard getting started page.
Replace the following placeholder values in the sample code:

#### Call
Create an application, make a note of your application id on the dashboard getting started(voice) page, download the private key then copy and paste the path of private key in the program.
