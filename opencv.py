import numpy as np
import cv2
import random


#Colors			=	(  R,   G,   B)
AQUA			=	(  0, 255, 255)
BLACK			=	(  0,   0,   0)
BLUE			=	(  0,   0, 255)
FUCHSIA			=	(255,   0, 255)
GRAY			=	(128, 128, 128)
LIGHTGREEN 		= 	(130, 229, 052)
GREEN			=	(  0, 255,   0)
LIME			=	(  0, 128,   0)
MAROON			=	(128,   0,   0)
LIGHTBLUE 		= 	(025, 192, 241)
NAVYBLUE		=	(  0,   0, 128)
OLIVE			=	(128, 128,   0)
PURPLE			=	(128,   0, 128)
RED				=	(255,   0,   0)
SILVER			=	(192, 192, 192)
TEAL			=	(  0, 128, 128)
WHITE			=	(255, 255, 255)
YELLOW			=	(255, 255,   0)
ALLCOLOUR 		=	[AQUA, BLACK, BLUE, FUCHSIA, GRAY, LIGHTGREEN, GREEN, LIME, MAROON, LIGHTBLUE, NAVYBLUE, OLIVE, PURPLE, RED, SILVER, TEAL, WHITE, YELLOW]



#font
font	=	cv2.FONT_HERSHEY_SIMPLEX





'''def mouseEvent(event, x, y, flags, param):
	global show, Isgraph
	if event == cv2.EVENT_LBUTTONDOWN:
		if 30 <= x <= 230 and 20 <= y <= 90:
			print "hello"
			show = cv2.imread("graph.jpg")
			Isgraph = True
			#cv2.imshow('graph', show)
'''


def draw(subjectName, choice):
	cap = cv2.VideoCapture(0)

	#Values
	WIDTH					=	640
	HEIGHT					=	480
	COLOR 					=	(0, 0, 0)
	prevx, prevy 			= 	-1, -1 			#Storing previous cooordinates
	drawit					=	False
	cursorx, cursory		=	-1, -1
	coorX					=	[]
	coorY					=	[]
	show 					= 	np.ndarray((HEIGHT, WIDTH, 3))
	Isgraph					=	False

	cap.set(3, WIDTH)
	cap.set(4, HEIGHT)
	#print cap.get(4),cap.get(3)

	display = np.ndarray((int(cap.get(4)) + 100, int(cap.get(3)), 3))
	
	fileName = None

	if choice == 1:				#Make diagram
		show.fill(255)
	if choice == 2:
		show = cv2.imread("graph.jpg")	#Make graph
	#display.fill(255)

	

	
	cv2.namedWindow("noteCV")
	#cv2.setMouseCallback("noteCV", mouseEvent)


	while True:

		

		ret, img = cap.read()
		img = cv2.flip(img, 1)

		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		# define range of blue color in HSV
		lower_blue = np.array([110,50,50])
		upper_blue = np.array([150,255,255])

	    # define range of green color in HSV
		lower_green = np.array([40,100,100])
		upper_green = np.array([80,255,255])
		
	    # define range of orange color in HSV
		lower_orange = np.array([0,210,0])
		upper_orange = np.array([10,255,255])

		
		#mask = cv2.inRange(hsv, lower_orange, upper_orange)
		mask = cv2.inRange(hsv, lower_green, upper_green)

		#img = cv2.bitwise_and(img, img, mask = mask)
		#blur = cv2.GaussianBlur(img,(5,5),0)
		#kernel = np.ones((5,5),np.uint8)

		erosion = cv2.erode(mask.copy(), None, iterations = 2)
		dilation = cv2.dilate(erosion, None, iterations = 2)
		
		#Check OpenCV version(No backward compatibility between versions)
		#OpenCV version 2.*
		if cv2.__version__.startswith("2."):
			contours, hierarchy = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)		#OpenCV version dependency 
		#OpenCV version 3.*
		elif cv2.__version__.startswith("3."):
			_,contours, hierarchy = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)		#OpenCV version dependency

		#cv2.rectangle(show,(0,0),(int(cap.get(3)), int(cap.get(4))), WHITE, -1)

		flag = False

		for contour in contours:
			# get rectangle bounding contour
			x,y,w,h = cv2.boundingRect(contour)

#######################################################################################
			#Adjust these conditions
	    	# discard areas that are too large
			if h>200 and w>200:
				continue
			# discard areas that are too small
			if h<100 or w<100:
				continue
#######################################################################################

			#print "current points: ", (x, y)

			if cursorx != -1:
				#cv2.circle(show, (cursorx, cursory), 2, WHITE, -1)
				for i in range(max(0,cursorx-2),min(WIDTH, cursorx+3)):
					for j in range(max(0, cursory-2),min(HEIGHT, cursory+3)) :
						show[j][i] = tmp[j][i]
			#print "(cursorx, cursory)", (cursorx, cursory)

			# (cx-2, cy-2) -> (cx+2, cy+2)

			tmp = np.ndarray((HEIGHT, WIDTH,3))
			tmp.fill(255)
			for i in range(max(x-2,0),min(x+3,WIDTH)):
				for j in range(max(0,y-2), min(y+3,HEIGHT)) :
					tmp[j][i] = show[j][i]

			#print "(x, y)",(x, y)



			cv2.circle(show, (x, y), 2, NAVYBLUE, -1)
			#cv2.rectangle(show, (x, y), (x+2, y+2), NAVYBLUE, -1)


			
			cursorx = x
			cursory = y

			if drawit:
				if prevx == -1:
					cv2.circle(show, (x, y), 3, COLOR, -1)
				else:
					cv2.line(show, (x, y), (prevx, prevy), COLOR, 3)

			#print "previous points: ", (prevx, prevy)
			prevx = x
			prevy = y

		if choice == 1:	
			'''
			for i in range(100):
				display[i,:] = OLIVE

			#print display[99,:]

			for i in range(HEIGHT):
				display[100+i,:] = show[i,:]

			print display[100,:], show[0,:] 
			
			cv2.rectangle(display, (30,20), (200,70),FUCHSIA, 0)
			cv2.putText(display, "MAKE GRAPH", (50, 50), font, 0.7, (0,0,0), 2, cv2.CV_AA)
			'''
			cv2.imshow('noteCV', show)

		else:
			'''
			for i in range(100):
				display[i,:] = OLIVE

			#print display[99,:]

			for i in range(HEIGHT):
				display[100+i,:] = show[i,:]

			#print display[100,:] 
			
			cv2.rectangle(display, (30,20), (200,70),FUCHSIA, 0)
			cv2.putText(display, "MAKE DIAGRAM", (50, 50), font, 0.7, (0,0,0), 2, cv2.CV_AA)
			'''
			cv2.imshow('noteCV', show)

		k = cv2.waitKey(1) & 0xFF
		if k == ord('q') :
			break
		elif k == ord('x') or k == ord('X'):
			drawit = not drawit
		elif k == ord('g') or k == ord('G') :
			COLOR = (0, 255, 0)
		elif k == ord('r') or k == ord('R') :
			COLOR = (0, 0, 255)
		elif k == ord('b') or k == ord('B') :
			COLOR = (255, 0, 0)
		elif k == ord('l') or k == ord('L'):
			pass
		elif k == ord('s') or k == ord('S') :
			fileName = "AppData" + "/" + str(random.randint(0,10000000)) + str(".jpg")
			cv2.imwrite(fileName, show)
			break

	cv2.destroyAllWindows()
	cap.release()

	return fileName
