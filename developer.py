from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2


class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        title_lbl = Label(self.root, text="DEVELOPER", font=(
                "times new roman", 32, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=-4, width=1550, height=45)

        
        img3 = Image.open(
            r"images\12063788_4893415.jpg")
        img3 = img3.filter(ImageFilter.GaussianBlur(
            radius=5))  # Adjust the radius as needed
        img3 = img3.resize((1550, 1100), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=41, width=1550, height=1100)
        
        
        # Frame
        main_frame = Frame(bg_img, bd=2, bg='white')
        main_frame.place(x=1000, y=30, width=500, height=700)
        
        # developer info
        dev_label = Label(main_frame, text="This project has been developed by our team\n of final-year students as a Major Project\n submission. \nIt represents a culmination of our academic\n learnings and practical skills acquired over the\n course of our studies.", font=(
            "times new roman", 17, "bold"), bg='white')
        dev_label.place(x=0,y=5)
        
        dev_label = Label(main_frame, text="Group Members", font=(
            "times new roman", 15, "bold"), bg='white')
        dev_label.place(x=180,y=190)

        dev_label = Label(main_frame, text="  Derek Austin - 20BCS6489\nVasu Dev - 20BCS6554\nPooja Jain - 20BCS6551\n  Ayush Sharma - 20BCS6550", font=(
            "times new roman", 15, "bold"), bg='white')
        dev_label.place(x=120,y=220)

        img = Image.open(
            r"images\251742-P4JUKC-71.jpg") 
        img = img.resize((500, 500), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(main_frame, image=self.photoimg)
        bg_img.place(x=10, y=400, width=500, height=500)


if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()