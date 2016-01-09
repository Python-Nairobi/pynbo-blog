
Title: Tracking Vehicles on Access Kenya Camera's
Date: 2016-01-09 18:11:00
Tags: python, image analysis, opencv, access kenya, traffic
Slug: image_analysis_by_chris_orwa
Author: Chris Orwa
Summary: Description of a python API I built to track vehicular movement on Access Kenya cameras
email: chrisorwa@gmail.com
about_author: <p> Chris Orwa is a Data Scientist currently residing in Nairobi, Kenya. He's main focus is on computational techniques for unstructured data. To that end, he has learned to code in Python and R, and retained both languages as the core-analysis software/language with an occasional dash of C and Java. </p><p>His crazy analysis monologues can be found at <a href="http://blackorwa.com" target="_blank">http://blackorwa.com </a></p>

Hello everyone, here's my blog post on how I built an API to return traffic conditions from Access Kenya cameras. The API would work by specifiying a road name at the URL endpoint and a json reponse would have number of cars that moved and the speed of movement. 

#### The Process
To begin the process I decided to test if is possible to capture Image from each camera. After exploration of the website I realized each camera had a url with a JPEG file extension at the end. I figured the cameras wrote a new image to the JPEG file on the URL. So, can I captured every new image? Yes - I used the **urllib** library to capture the image and store it on the disk. 
