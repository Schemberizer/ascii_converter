#Ascii art

import cv2

def img_load():

    img_in = input("Image: ")
    file_in = input("File Name: ")
    aspect = int(input("Aspect Ratio: "))
    
    img = cv2.imread(img_in, cv2.IMREAD_GRAYSCALE)
    txt_file = open(file_in, "w+")

    px_x = img.shape[1]
    px_y = img.shape[0]

    rat_x = aspect
    rat_y = aspect * 2

    for i in range(0,px_y,rat_y):
        for j in range(0,px_x, rat_x):

            px_val = img[(i - 1),(j - 1)]
            
            if px_val <= 25:
                txt_file.write("M")

            elif (px_val > 18) and (px_val <= 36):
                txt_file.write("N")

            elif (px_val > 36) and (px_val <= 54):
                txt_file.write("#")

            elif (px_val > 54) and (px_val <= 72):
                txt_file.write("%")

            elif (px_val > 72) and (px_val <= 90):
                txt_file.write("@")

            elif (px_val > 90) and (px_val <= 108):
                txt_file.write("u")

            elif (px_val > 108) and (px_val <= 126):
                txt_file.write("I")

            elif (px_val > 126) and (px_val <= 144):
                txt_file.write("=")

            elif (px_val > 144) and (px_val <= 162):
                txt_file.write("+")

            elif (px_val > 162) and (px_val <= 180):
                txt_file.write("|")

            elif (px_val > 180) and (px_val <= 198):
                txt_file.write(":")

            elif (px_val > 198) and (px_val <= 216):
                txt_file.write(".")

            elif (px_val > 216) and (px_val <= 234):
                txt_file.write("`")

            else:
                txt_file.write(" ")
            
        txt_file.write("\n")

    txt_file.close()
    
    return

img_load()
