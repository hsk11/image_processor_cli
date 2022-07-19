from PIL import Image
import os
import sys
import time

# ------------WELCOME SCREEN START
print("### Welcome to IMAGE PROCESSING project by HSK ####")
nameStart=str(input("\n\n# Instructions Manual \n1. The Names Entered by you are case Sensitive, make sure you enter Correct image name.\n"
               "2. Always enter your CHOICE from the displayed list in Number\n3. You are ready to begin! press Enter Key to start"))
os.system("clear")

'''
loading = "..............................#"
print("\n# Loading for you .")
for l in loading:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)
'''

img_name=input("\nEnter the Name of the Image: ")

# IMAGE DETAILS
image = Image.open(img_name)
image_size = image.size

ext_names = [".jpg", '.png', '.jpeg', ".gif"]
ext = image.format
print(f"\nImage Name: {img_name}  / Width: {image_size[0]} Height:{image_size[1]}  / Format: {image.format}")
print("\nWelcome to Image Processing")
print("1. Crop Image")
print("2. Add Border to image")
print("3. Convert to Black and White")
print("4. Resize Image")
print("5. Convert to PNG or JPG vica-versa")
print("6. Add Watermark on the image")
print("7. Rotate image")
print("8. Flip Image")
print("9. Draw text on image")

choice = input("\nEnter your Choice: ")

def  save_image():
    save_img = input("Enter the image Name to Save: ").lower()
    # MAKE SURE USER image name is with extension
    with_ext = True
    for s_img in ext_names:
        if s_img in save_img:
            with_ext = True
            break;
        else:
            with_ext = False

    if not with_ext: save_img = save_img + "." + ext
    return save_img

# CROPPED IMAGE
if choice=="1":
    print(f"\n Image is of / Width: {image_size[0]} Height:{image_size[1]}")
    print("\nEnter Starting (x1,y1) and Ending (x2,y2) coordinates: Format x1 y1 x2 y2")
    x1, y1, x2, y2 = list(map(int, input().split()))
    box = (x1, y1, x2, y2)
    cropped_image = image.crop(box)
    #SAVE IMAGE
    new_save= save_image();
    cropped_image.save(new_save)
    print(f"\nImage saved as {new_save}")
    cropped_image.show() 

# BORDER IMAGE
elif choice=="2":

    print("\nEnter the border Size Vertically and Horizontally: ")
    brV, brH = list(map(int, input().split()))
    new_size = (image_size[0]+brH, image_size[1]+brV)
    print('Enter the Color Name (red,green, blue) or Css Style Color name (#eeeeee):  ')
    br_color = input()
    br_im = Image.new("RGB", new_size,  br_color)
    br_im.paste(image,  (int((new_size[0]-image_size[0]) / 2), int((new_size[1]-image_size[1])/2)))

    #SAVE IMAGE
    new_save= save_image();
    br_im.save(new_save)
    print(f"\nImage saved as {new_save}")
    br_im.show() 

# BLACK & WHITE IMAGE
elif choice=="3":
    bW_im = image.convert('1')

    #SAVE IMAGE
    new_save= save_image();
    bW_im.save(new_save)
    print(f"\nImage saved as {new_save}")
    br_im.show() 

# RESIZE IMAGE
elif choice=="4":

    print("\nEnter the desired Width and Height of the image: ")
    wd, hg = list(map(int, input().split()))
    rsize_im= image.resize((wd, hg))
    #SAVE IMAGE
    new_save= save_image()
    rsize_im.save(new_save)
    print(f"\nImage saved as {new_save}")
    rsize_im.show() 

elif choice=="5":

    print("Your Current Image is in "+image.format+" format.")
    #SAVE IMAGE
    new_save= save_image()
    conv_im=image.copy()
    conv_im.save(new_save)
    print(f"\nImage saved as {new_save}")
    conv_im.show() 


elif choice=="6":
    logo = Image.open('logo.png')
    water_im = image.copy()
    loc = int(input("\nChoose Location for watermark:\n1. Top Left \n2. Top Right \n3. Bottom Left\n4. Bottom Right\n5. Center\n# default bottom left\n Enter your choice:"))
    # LOCATION OF THE WATERMARK
    if loc == 1:
        position = (0,0)
    elif loc == 2:
        position = ((water_im.width - logo.width), 0)
    elif loc == 3:
        position = (0,(water_im.height - logo.height))
    elif loc == 4:
        position = ((water_im.width - logo.width), (water_im.height - logo.height))
    elif loc == 5:
        position = (int(water_im.width/2), int(water_im.height/2))
    else:
        position = ((water_im.width - logo.width), (water_im.height - logo.height))

    # BACKGROUND FOR THE Watermark
    #same
    water_im.paste(logo, position, logo)
    #SAVE IMAGE
    new_save = save_image()
    water_im.save(new_save)
    print(f"\nImage saved as {new_save}")
    water_im.show() 


elif choice=="7":
    degree = int(input("Enter the degrees to rotate the image: "))
    rotate_im= image.rotate(degree)
    #SAVE IMAGE
    new_save = save_image()
    rotate_im.save(new_save)
    print(f"\nImage saved as {new_save}")
    rotate_im.show() 
elif choice=="8":
    trans_choice= int(input("\nEnter your choice:\n1. Left to Right\n2. TOP to bottom\n3. Transpose\n"))
    if trans_choice==1:
        flip_img= image.transpose(Image.FLIP_LEFT_RIGHT)
    elif trans_choice==2:
        flip_img = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif trans_choice==3:
        flip_img = image.transpose(Image.TRANSPOSE)
    #SAVE IMAGE
    new_save = save_image()
    flip_img.save(new_save)
elif choice=="9":

    draw = input("Enter the Text you want to paste on image:")
    draw_im= image.text((1000, 1000), draw, fill='black')
    #SAVE IMAGE
    new_save = save_image()
    draw_im.save(new_save)
    print(f"\nImage saved as {new_save}")
    draw_im.show() 

#im = Image.open("Ba_b_do8mag_c6_big.png")
#rgb_im = im.convert('RGB')
#rgb_im.save('colors.jpg',quality=95) )
