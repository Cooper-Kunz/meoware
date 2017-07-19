from PIL import Image

theImages = ["cat_test1.jpeg", "cat_test2.jpeg", "cat_test3.jpeg", "cat_test4.jpeg", "cat_test5.jpeg",
             "cat_test1.jpeg", "cat_test2.jpeg", "cat_test3.jpeg", "cat_test4.jpeg", "cat_test5.jpeg",
             "cat_test1.jpeg", "cat_test2.jpeg", "cat_test3.jpeg", "cat_test4.jpeg", "cat_test5.jpeg"]

for image in theImages:
    display = Image.open("./images/"+image)
    display.show()
