from PIL import Image
import os.path

fileName = input("Enter image name and format: ")
while os.path.isfile("invert colors/"+fileName) == False:
    print("File not found")
    fileName = input("Enter image name: ")
image = Image.open("invert colors/"+fileName)
#image.show()
outputName = input("Enter output image name and format: ")
while os.path.isfile("invert colors/"+outputName) == True:
    print("File allready exist!")
    outputName = input("Enter output image name and format: ")
pixelMap = image.load()
size = image.size
for c in range(size[0]):
    for r in range(size[1]):
        pixel = pixelMap[c, r]
        pixelMap[c, r] = (255-pixel[0], 255-pixel[1], 255-pixel[2])
#image.show()
image = image.save("invert colors/"+outputName); 