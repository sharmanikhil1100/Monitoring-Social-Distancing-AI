import cv2 as cv

frame_array = []
fps = 20
for i in range(199):
		i = str(i).zfill(4)
		filename='../video/View_004/frame_'+i +'.jpg'
		#print(filename)
		img = cv.imread(filename)
		###print(filename)
		#print(img)
		#if(img):
		height, width, layers = img.shape
		size = (width,height)
		###print(img.shape)
		height = 500
		width = 900
		dim = (width, height)
		# resize image
		img = cv.resize(img, dim, interpolation = cv.INTER_AREA)  
		cv.imwrite(filename, img)
		#inserting the frames into an image array
		frame_array.append(img)
pathOut = 'pets24.mp4'
out = cv.VideoWriter(pathOut,cv.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
	# writing to a image array
	out.write(frame_array[i])
out.release() 