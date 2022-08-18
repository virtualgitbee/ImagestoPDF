# from PIL import Image
# 
# path = "C:/Users/hardi/OneDrive/Pictures/Screenshots/Untitled.jpg"
# pdf = Image.open(path)
# pdf.save("D:/New folder/Unitiled.pdf")


# To begin, here is a template that you may use to convert a png image to PDF using Python (for JPEG, use the file extension of ‘jpg’):

# Step 1: Install the PIL package
# To start, install the PIL package using the command below (under Windows):
from PIL import Image

'''Step 2: Capture the path where your image is stored
Next, capture the path where your image is stored.

For example, let’s suppose that a png image called ‘view_1‘ is stored under the following path:'''

'''Convert a List of Images to PDF using Python
What if you have a list of images and you’d like to store all of them in a single PDF file?

For example, let’s add few more images under the same path:'''

image_1 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/bsvuds (1).png")
image_2 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/bsvuds (2).png")
# image_3 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/bsvud (3).png")
# image_4 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/bsvud (4).png")
# image_5 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/bsvud (5).png")
# image_6 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/bsvud (6).png")
# image_7 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/bsvud (7).png")
# image_8 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (8).png")
# image_9 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (9).png")
# image_10 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (10).png")
# image_11 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (11).png")
# image_12 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (12).png")
# image_13 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (13).png")
# image_14 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (14).png")
# image_15 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (15).png")
# image_16 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (16).png")
# image_17 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (17).png")
# image_18 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (18).png")
# image_19 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (19).png")
# image_20 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (20).png")
# image_21 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (21).png")
# image_22 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (22).png")
# image_23 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (23).png")
# image_24 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (24).png")
# image_25 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (25).png")
# image_26 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (26).png")
# image_27 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (27).png")
# image_28 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (28).png")
# image_29 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (29).png")
# image_30 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (30).png")
# image_31 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (31).png")
# image_32 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (32).png")
# image_33 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (33).png")
# image_34 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (34).png")
# image_35 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (35).png")
# image_36 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (36).png")
# image_37 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (37).png")
# image_38 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (38).png")
# image_39 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (39).png")
# image_40 = Image.open(r"C:/Users/hardi/OneDrive/Pictures/Screenshots/fr (40).png")






# Next, perform the conversion:


im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')
# im_3 = image_3.convert('RGB')
# im_4 = image_4.convert('RGB')
# im_5 = image_5.convert('RGB')
# im_6 = image_6.convert('RGB')
# im_7 = image_7.convert('RGB')
# im_8 = image_8.convert('RGB')
# im_9 = image_9.convert('RGB')
# im_10 = image_10.convert('RGB')
# im_11 = image_11.convert('RGB')
# im_12 = image_12.convert('RGB')
# im_13 = image_13.convert('RGB')
# im_14 = image_14.convert('RGB')
# im_15 = image_15.convert('RGB')
# im_16 = image_16.convert('RGB')
# im_17 = image_17.convert('RGB')
# im_18 = image_18.convert('RGB')
# im_19 = image_19.convert('RGB')
# im_20 = image_20.convert('RGB')
# im_21 = image_21.convert('RGB')
# im_22 = image_22.convert('RGB')
# im_23 = image_23.convert('RGB')
# im_24 = image_24.convert('RGB')
# im_25 = image_25.convert('RGB')
# im_26 = image_26.convert('RGB')
# im_27 = image_27.convert('RGB')
# im_28 = image_28.convert('RGB')
# im_29 = image_29.convert('RGB')
# im_30 = image_30.convert('RGB')
# im_31 = image_31.convert('RGB')
# im_32 = image_32.convert('RGB')
# im_33 = image_33.convert('RGB')
# im_34 = image_34.convert('RGB')
# im_35 = image_35.convert('RGB')
# im_36 = image_36.convert('RGB')
# im_37 = image_37.convert('RGB')
# im_38 = image_38.convert('RGB')
# im_39 = image_39.convert('RGB')
# im_40 = image_40.convert('RGB')





# Then, create a new image_list (excluding the first image):

image_list = [im_2]# im_3, im_4, im_5,im_6,im_7] #im_8,im_9,im_10,im_11,im_12,im_13,
# im_14,im_15,im_16,im_17,im_18,im_19,im_20,im_21,im_22,im_23,im_24,im_25,im_26,im_27,im_28,im_29,im_30,im_31,im_32,im_33,im_34,im_35,im_36,
# im_37,im_38,im_39,im_40]

# And finally, apply the following syntax to save the PDF (note the ‘im_1’ at the beginning):



im_1.save(r'D:/New folder/Bash_SPE_V.pdf', save_all=True, append_images=image_list)

print("PDF Created")
