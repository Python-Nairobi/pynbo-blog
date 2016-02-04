
Title: Tracking Vehicles on Access Kenya Camera's
Date: 2016-01-09 18:11:00
Tags: python, image analysis, opencv, access kenya, traffic
Slug: image_analysis_by_chris_orwa
Author: Chris Orwa
Summary: Description of a python API I built to track vehicular movement on Access Kenya cameras
email: chrisorwa@gmail.com
about_author: <p> Chris Orwa is a Data Scientist currently residing in Nairobi, Kenya. He's main focus is on computational techniques for unstructured data. To that end, he has learned to code in Python and R, and retained both languages as the core-analysis software/language with an occasional dash of C and Java. </p><p>His crazy analysis monologues can be found at <a href="http://blackorwa.com" target="_blank">http://blackorwa.com </a></p>

Hello everyone, here's my blog post on how I built an API to return traffic conditions from Access Kenya cameras. The API would work by specifiying a road name at the URL endpoint and a json reponse would have number of cars that moved and the speed of movement. 

#### Data Capture
To begin the process I decided to test if is possible to capture Image from each camera. After exploration of the website I realized each camera had a url with a JPEG file extension at the end. I figured the cameras wrote a new image to the JPEG file on the URL. So, can I captured every new image? Yes - I used the **urllib** library to capture the image and store it on the disk.

I organized the camera urls into a dict so as to have a means of calling and referencing each road.

    cameras = dict (
    museum='http://traffic.accesskenya.com/images/traffic/feeds/purshotam.jpg',
    ojijo='http://traffic.accesskenya.com/images/traffic/feeds/mhcojijo.jpg',
    forest_limuru='http://traffic.accesskenya.com/images/traffic/feeds/forestlimuru.jpg?',
    kenyatta_uhuru_valley='http://traffic.accesskenya.com/images/traffic/feeds/barclaysplaza.jpg',)
    
After that, I wrote a function that take a url and extract three images after every 6 seconds.

    def capture_images(self):
        for i in 'abc':
            if self.name in way:
                    urllib.urlretrieve(way[self.name],'img_'+i+'.jpg')
                    time.sleep(6)

#### Image Processing
The images captured from the camera are stored on a folder with the name of the road. Next task involves processing the images for analysis. I utlize two libraries for this task; **PIL** for loading the images and **numpy** to convert pixel values to numerical array values. All these are wrapped in a function (shown below) that takes the image folder directory as input then proceeds to load all 3 images, converts them to numpy arrays, deletes the images and return a python dict holding arrays on all the images.

    # load images
    def load(self):
        files = os.listdir(self.path)
        a = dict()
        b = dict()
        k = 0

            while k <= len(files):
                for names in files:
                    if names != '.DS_Store':
                        a[names] = Image.open(names).convert('L')
                        a[names].load()
                        b[names] = np.asarray(a[names])     
                k +=1

        # delete image folder
        shutil.rmtree(os.getcwd())
            
        return b

#### Motion Detection
The first important step in analysis of the images is checking if there has been movements within the 6 second period. To achieve this, I utilized the concept of differential imaging - a means of measuring motion detection by subtracting the pixel values of subsquent images. In my function, I calculate the number of pixels that have moved, this helps in quantifying the movement (standstill, moderate traffic).

    # differential imaging
    def diffImg(self,img1,img2,img3):

        # calculate absolute difference
        d1 = cv2.absdiff(img1,img2)
        d2 = cv2.absdiff(img2,img3)
        bit = cv2.bitwise_and(d1,d2)
        ret,thresh = cv2.threshold(bit,35,255,cv2.THRESH_BINARY)

        #get number of different pixels
        moving = list()
        for cell in thresh.flat:
            if cell == 255:
                move = 'True'
                moving.append(move)
            pixie = len(moving)

        return pixie

#### Calibrating Movement
Once movement is detected, it is important to then quantify trafficc in km/h. To aid in this calculation is the optical flow algorithm. A concept in computer vision that allow tracking features in an image. I utilized this functionality to find features to track (cars) in the first images, and get their corresponding positions in the second and third image. I then proceeded to calculate the avaerage distance (euclidean distance) that the feature has moved. Dividing the pixel distance by 12 seconds gives me speed at which the objects(cars) are moving. My function returns this value.

    # calculate optical flow of points on images
    def opticalFlow(self,img1,img2,img3):

        #set variables
        lk_params = dict(winSize = (10,10),
                        maxLevel = 5,
                        criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,0.03))

        features_param = dict( maxCorners = 3000,
                                qualityLevel = 0.5,
                                minDistance = 3,
                                blockSize = 3)

        # feature extraction of points to track 
        pt = cv2.goodFeaturesToTrack(img1,**features_param)
        p0 =np.float32(pt).reshape(-1,1,2)

        # calaculate average movement
        dist = list()
        for loop in p0: 
            p1,st,err =cv2.calcOpticalFlowPyrLK(img1, img2,loop,
                                                None,**lk_params)
      
            p0r,st,err =cv2.calcOpticalFlowPyrLK(img2,img1,p1,
                                            None,**lk_params)

            if abs(loop-p0r).reshape(-1, 2).max(-1) < 1:
                dst = distance.euclidean(loop,p0r)
                dist.append(dst)
        
        return round(max(dist)*10,2)

#### The API
The API (underconstruction) is based on flask. By specifying a road name at the HTTP endpoint, the API returns speed of traffic and level of movement (stanstill, moderate rate, no traffic). 

    # load required libraries
    import image_processing
    import numpy as np
    from flask import Flask
    import links
    import json
    import scipy as sp

    # create flask web server 
    app = Flask(__name__)

    # create HTTP endpoint
    @app.route('/ImPro/<road>')

    # main function
    def get_route(road):
        # initialize route class
        road = 'sarit'
        traffic = image_processing.route(road)

        # setup working directory
        traffic.set_dir()

        # get image from traffic camera
        traffic.capture_images()

        # load image stack
        x = traffic.load()

        # differential imaging
        y =  traffic.diffImg(x['img_a.jpg'],x['img_b.jpg'],x['img_c.jpg'])

        # calculate optical flow
        z = traffic.opticalFlow(x['img_a.jpg'],x['img_b.jpg'],x['img_c.jpg'])

    if __name__ == "__main__":
    app.run()

I hope you enjoyed it. Feel free to drop me an e-mail at chrisorwa@gmail.com for any queries.
