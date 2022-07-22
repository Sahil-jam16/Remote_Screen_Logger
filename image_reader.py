from PIL import Image
path = "G:\\College Work\\SEMESTER - 2\\PYTHON LAB\\Package\\"
# open method used to open different extension image file
images = ["one.png","two.png","three.png","four.png","five.png"]
for i in images:
    im = Image.open(i,"r") 
    im.show()
print("EXIT")    