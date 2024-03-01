import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from fpdf import FPDF
from PIL import Image, ImageTk

class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.canvas = tk.Canvas(self, bg="black", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="black")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def update_scrollregion(self):
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class MainWindow:
    def __init__(self):
        self.main = tk.Tk()
        self.main_width = self.main.winfo_screenwidth()
        self.main_height = self.main.winfo_screenheight()
        self.main.title("RESUME")
        self.main.iconbitmap("assets/ICO/seo_website_internet_coding_homepage_portal_web_icon_261572.ico")
        

        self.main.geometry(f"{self.main_width}x{self.main_height}")
        bg_image = Image.open("assets/milad-fakurian-nY14Fs8pxT8-unsplash.jpg")
        bg_image_resized = bg_image.resize((self.main_width, self.main_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image_resized)
        self.bg_label = tk.Label(self.main, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.canvas = tk.Canvas(self.main, width=self.main_width, height=self.main_height, highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
        self.canvas.create_text(5, 400, anchor="w", text=" R E S U M E    G E N E R A T O R ", fill="white", font=("Anurati", 54, "bold"))

        self.button1 = tk.Button(self.main, text="W A N T   Y O U R   O W N   R E S U M E ", bg="#5a3996", fg="white", font="Arial", command=self.button1_c)
        self.button1.pack(anchor='w')
        self.button1.place(x=5, y=500, anchor='w')

        self.light_i=tk.PhotoImage(file="assets/mode__1_.png")
        self.light_b=tk.Button(self.main,image=self.light_i,bg="white",width=50,height=50,command=self.light)
        self.light_b.pack(side="right",anchor="ne")

        '''gifImage="C:Users/Shahu/Downloads/output-onlinegiftools.gif"
        openImage = Image.open(gifImage)
        frames = openImage.n_frames

        imageObject=[ tk.PhotoImage(file=gifImage,format=f"gif -index {i}") for i in range(frames) ]
        count = 0
        showAnimation = None
        def animation(count):
            global showAnimation
            newImage = imageObject[count]

            gif_Label.configure(image=newImage)
            count+=1
            if count == frames:
                count = 0
            showAnimation= self.main.after(50, lambda: animation(count))

        gif_Label=tk.Label(self.main,image="")
        gif_Label.place(x=155,y=20,width=64,height=64)
        animation(count)'''


        self.home_frame = ScrollableFrame(self.main)
        self.home_frame.propagate(False)

    def light(self):
        #self.label.config(bg="white", fg="black")
        self.button1.config(bg="white", fg="black")
        self.main.configure(bg="white")
        #self.label_team.config(bg="white", fg="black")
        #self.label_name.config(bg="white", fg="black")
        self.light_b.configure(command=self.dark)
        self.label2.config( bg="white", fg="black")
        self.frame1.config(bg="white")
        self.home_frame.scrollable_frame.config(bg="white")
        self.label3.config(bg="white", fg="black")
        self.label4.config(bg="white", fg="black")
        self.label4_1.config(bg="white", fg="black")
        self.label4_2.config(bg="white", fg="black")
        self.label4_3.config(bg="white", fg="black")
        self.label4_4.config(bg="white", fg="black")
        self.label5.config(bg="white", fg="black")
        self.label6.config(bg="white", fg="black")
        self.label7.config(bg="white", fg="black")
        self.label7_1.config(bg="white", fg="black")
        self.label8.config(bg="white", fg="black")
        self.label9.config(bg="white", fg="black")
        self.label10.config(bg="white", fg="black")
        self.label11.config(bg="white", fg="black")
        self.label12.config(bg="white", fg="black")
        self.label13.config(bg="white", fg="black")
        self.label13_1.config(bg="white", fg="black")
        self.label13_2.config(bg="white", fg="black")
        self.label13_3.config(bg="white", fg="black")
        #self.label14.config(bg="white", fg="black")
        self.entry1.config(bg="white", fg="black")
        self.entry3.config(bg="white", fg="black")
        self.entry4.config(bg="white", fg="black")
        self.entry5.config(bg="white", fg="black")
        self.entry6.config(bg="white", fg="black")
        self.entry7.config(bg="white", fg="black")
        self.entry8.config(bg="white", fg="black")
        self.entry9_1.config(bg="white", fg="black")
        self.entry9_2.config(bg="white", fg="black")
        self.entry9_3.config(bg="white", fg="black")
        self.entry9_4.config(bg="white", fg="black")
        self.entry9_5.config(bg="white", fg="black")
        self.entry10.config(bg="white", fg="black")
        self.entry11.config(bg="white", fg="black")
        self.entry12.config(bg="white", fg="black")

        self.frame11.config(bg="white")
        self.frame3.config(bg="white")
        self.frame2.config(bg="white")
        self.frame4.config(bg="white")
        self.frame5.config(bg="white")
        self.frame6.config(bg="white")
        self.frame7.config(bg="white")
        self.frame8.config(bg="white")
        self.frame9.config(bg="white")
        self.frame10.config(bg="white")
        self.frame11.config(bg="white")
        self.frame12.config(bg="white")
        self.frame6_f.config(bg="white")
        self.label6_1.config(bg="white",fg="black")
        self.label6_2.config(bg="white",fg="black")
        self.label6_3.config(bg="white",fg="black")
        self.label6_4.config(bg="white",fg="black")
        self.frame_edu_f.config(bg="white")
        self.label_edu.config(bg="white",fg="black")
        self.label_edu_3.config(bg="white",fg="black")
        self.label_edu_6_4.config(bg="white",fg="black")
        self.label_edu_college.config(bg="white",fg="black")
        self.label_edu_degree.config(bg="white",fg="black")
        self.entry_college.config(bg="white",fg="black")
        self.entry_degree.config(bg="white",fg="black")
        self.entry6_1.config(bg="white",fg="black")
        self.entry6_2.config(bg="white",fg="black")
        self.entry7_1.config(bg="white",fg="black")
        self.entry7_2.config(bg="white",fg="black")
        self.entry13_1.config(bg="white",fg="black")
        self.entry13_2_2.config(bg="white",fg="black")
        self.entry13_3_2.config(bg="white",fg="black")
        self.entry13_2.config(bg="white",fg="black")
        self.entry13_3.config(bg="white",fg="black")
        self.label14.config(bg="white",fg="black")

        self.gen.config(bg="white", fg="black")

    def dark(self):
        #self.label.config(bg="black", fg="white")
        self.button1.config(bg="black", fg="white")
        self.main.configure(bg="black")
        #self.label_team.config(bg="black", fg="white")
        #self.label_name.config(bg="black", fg="white")
        self.light_b.configure(command=self.dark)
        self.label2.config(bg="black", fg="white")
        self.frame1.config(bg="black")
        self.home_frame.scrollable_frame.config(bg="black")
        self.label3.config(bg="black", fg="white")
        self.label4.config(bg="black", fg="white")
        self.label4_1.config(bg="black", fg="white")
        self.label4_2.config(bg="black", fg="white")
        self.label4_3.config(bg="black", fg="white")
        self.label4_4.config(bg="black", fg="white")
        self.label5.config(bg="black", fg="white")
        self.label6.config(bg="black", fg="white")
        self.label7.config(bg="black", fg="white")
        self.label7_1.config(bg="black", fg="white")
        self.label8.config(bg="black", fg="white")
        self.label9.config(bg="black", fg="white")
        self.label10.config(bg="black", fg="white")
        self.label11.config(bg="black", fg="white")
        self.label12.config(bg="black", fg="white")
        self.label13.config(bg="black", fg="white")
        self.label13_1.config(bg="black", fg="white")
        self.label13_2.config(bg="black", fg="white")
        self.label13_3.config(bg="black", fg="white")
        #self.label14.config(bg="black", fg="white")
        self.entry1.config(bg="black", fg="white")
        self.entry3.config(bg="black", fg="white")
        self.entry4.config(bg="black", fg="white")
        self.entry5.config(bg="black", fg="white")
        self.entry6.config(bg="black", fg="white")
        self.entry7.config(bg="black", fg="white")
        self.entry8.config(bg="black", fg="white")
        self.entry9_1.config(bg="black", fg="white")
        self.entry9_2.config(bg="black", fg="white")
        self.entry9_3.config(bg="black", fg="white")
        self.entry9_4.config(bg="black", fg="white")
        self.entry9_5.config(bg="black", fg="white")
        self.entry10.config(bg="black", fg="white")
        self.entry11.config(bg="black", fg="white")
        self.entry12.config(bg="black", fg="white")

        self.frame11.config(bg="black")
        self.frame3.config(bg="black")
        self.frame2.config(bg="black")
        self.frame4.config(bg="black")
        self.frame5.config(bg="black")
        self.frame6.config(bg="black")
        self.frame7.config(bg="black")
        self.frame8.config(bg="black")
        self.frame9.config(bg="black")
        self.frame10.config(bg="black")
        self.frame11.config(bg="black")
        self.frame12.config(bg="black")
        self.frame6_f.config(bg="black")
        self.label6_1.config(bg="black", fg="white")
        self.label6_2.config(bg="black", fg="white")
        self.label6_3.config(bg="black", fg="white")
        self.label6_4.config(bg="black", fg="white")
        self.frame_edu_f.config(bg="black")
        self.label_edu.config(bg="black", fg="white")
        self.label_edu_3.config(bg="black", fg="white")
        self.label_edu_6_4.config(bg="black", fg="white")
        self.label_edu_college.config(bg="black", fg="white")
        self.label_edu_degree.config(bg="black", fg="white")
        self.entry_college.config(bg="black", fg="white")
        self.entry_degree.config(bg="black", fg="white")
        self.entry6_1.config(bg="black", fg="white")
        self.entry6_2.config(bg="black", fg="white")
        self.entry7_1.config(bg="black", fg="white")
        self.entry7_2.config(bg="black", fg="white")
        self.entry13_1.config(bg="black", fg="white")
        self.entry13_2_2.config(bg="black", fg="white")
        self.entry13_3_2.config(bg="black", fg="white")

        self.light_b.configure(command=self.light)


    def button1_c(self):
        self.canvas.pack_forget()
        self.button1.pack_forget()
        self.light_b.pack_forget()

        self.light_image=tk.PhotoImage(file="assets/mode__1_.png")
        self.light_button=tk.Button(self.home_frame.scrollable_frame , image=self.light_image  ,bg="white",width=50,height=50,command=self.light)
        self.light_button.pack(padx=1400,anchor="n")

        self.home_frame.pack(fill="both", expand=True)

        self.label2 = tk.Label(self.main, text=" Add Your Personal Information", bg="black", fg="white", font=("Orbitron", 35, "bold"))
        self.label2.place(x=5, y=5, anchor='nw')

        self.frame1 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame1.pack(anchor="w", pady=80)

        self.label3 = tk.Label(self.frame1,text="Enter Your Name: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label3.pack(side="left")
        self.entry1 = tk.Entry(self.frame1, bg="black", fg="white", font=("Arial", 16))
        self.entry1.pack(side="left")

        self.label4 = tk.Label(self.home_frame.scrollable_frame, text=" Contact Information", bg="black", fg="white", font=("Poppins", 35, "bold"))
        self.label4.pack(anchor='w',pady=50)

        self.label4_1 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Date Of Birth: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label4_1.pack(anchor='w',pady=5)
        self.frame2 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame2.pack(anchor='w')

        self.comb1 = ttk.Combobox(self.frame2, width=5, font=("Arial", 16))
        self.comb1['values'] = tuple(range(1, 32))
        self.comb1.set("Day")
        self.comb1.pack(side="left")

        self.month_names = [
            "January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December"
        ]
        
        self.comb2 = ttk.Combobox(self.frame2, width=8, font=("Arial", 16))
        self.comb2['values'] = tuple(self.month_names)
        self.comb2.set("Month")
        self.comb2.pack(side="left")

        self.comb3 = ttk.Combobox(self.frame2, width=5, font=("Arial", 16))
        self.comb3['values'] = tuple(range(1970, 2028))
        self.comb3.set("Year")
        self.comb3.pack(side="left")

        self.label4_2 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Email: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label4_2.pack(anchor='w',pady=5)
        self.entry3 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry3.pack(anchor='w')

        self.label4_3 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Address: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label4_3.pack(anchor='w',pady=5)
        self.entry4 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry4.pack(anchor='w')

        self.label4_4 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Phone Number: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label4_4.pack(anchor='w',pady=5)
        self.entry5 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry5.pack(anchor='w')

        self.label5 = tk.Label(self.home_frame.scrollable_frame, text="Professional Experience", bg="black", fg="white", font=("Poppins", 35, "bold"))
        self.label5.pack(anchor='w',pady=50)

        self.label6 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Work Experience: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label6.pack(anchor='w',pady=5)
        self.frame6_f = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame6_f.pack(anchor='w')
        self.entry6 = tk.Entry(self.frame6_f, bg="black", fg="white", width=10, font=("Arial", 16))
        self.entry6.pack(side="left")
        self.label6_1 = tk.Label(self.frame6_f, text="Company",bg="black", fg="white", font=("League Gothic", 20, "bold"))
        self.label6_1.pack(side="left")
        self.entry6_1= tk.Entry(self.frame6_f, bg="black", fg="white", width=7, font=("Arial", 16))
        self.entry6_1.pack(side="left")
        self.label6_2 = tk.Label(self.frame6_f, text="Role",bg="black", fg="white", font=("League Gothic", 20, "bold"))
        self.label6_2.pack(side="left")
        self.entry6_2= tk.Entry(self.frame6_f, bg="black", fg="white", width=7, font=("Arial", 16))
        self.entry6_2.pack(side="left")
        self.label6_3 = tk.Label(self.frame6_f, text="from",bg="black", fg="white", font=("League Gothic", 20, "bold"))
        self.label6_3.pack(side="left")
        self.comb_6 = ttk.Combobox(self.frame6_f, width=4, font=("Arial", 16))
        self.comb_6['values'] = tuple(range(1, 32))
        self.comb_6.set("Day")
        self.comb_6.pack(side="left")
        self.comb_6_2 = ttk.Combobox(self.frame6_f, width=6, font=("Arial", 16))
        self.comb_6_2['values'] = tuple(self.month_names)
        self.comb_6_2.set("Month")
        self.comb_6_2.pack(side="left")
        self.comb_6_3 = ttk.Combobox(self.frame6_f, width=4, font=("Arial", 16))
        self.comb_6_3['values'] = tuple(range(1970, 2028))
        self.comb_6_3.set("Year")
        self.comb_6_3.pack(side="left")

        self.label6_4 = tk.Label(self.frame6_f, text="to:",bg="black", fg="white", font=("League Gothic", 20, "bold"))
        self.label6_4.pack(side="left",anchor="se")
        self.comb_6_1= ttk.Combobox(self.frame6_f, width=4, font=("Arial", 16))
        self.comb_6_1['values'] = tuple(range(1, 32))
        self.comb_6_1.set("Day")
        self.comb_6_1.pack(side="left",anchor="se")
        self.comb_6_1_2 = ttk.Combobox(self.frame6_f, width=6, font=("Arial", 16))
        self.comb_6_1_2['values'] = tuple(self.month_names)
        self.comb_6_1_2.set("Month")
        self.comb_6_1_2.pack(side="left",anchor="se")
        self.comb_6_1_3 = ttk.Combobox(self.frame6_f, width=4, font=("Arial", 16))
        self.comb_6_1_3['values'] = tuple(range(1970, 2028))
        self.comb_6_1_3.set("Year")
        self.comb_6_1_3.pack(side="left",anchor="se")

        self.label_edu = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Education : ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label_edu.pack(anchor='w',pady=5)
        self.frame_edu_f = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame_edu_f.pack(anchor='w')
        self.label_edu_3 = tk.Label(self.frame_edu_f, text="from",bg="black", fg="white", font=("League Gothic", 20, "bold"))
        self.label_edu_3.pack(side="left")
        self.comb_edu_6_3 = ttk.Combobox(self.frame_edu_f, width=5, font=("Arial", 16))
        self.comb_edu_6_3['values'] = tuple(range(1970, 2028))
        self.comb_edu_6_3.set("Year")
        self.comb_edu_6_3.pack(side="left")

        self.label_edu_6_4 = tk.Label(self.frame_edu_f, text="to:",bg="black", fg="white", font=("League Gothic", 20, "bold"))
        self.label_edu_6_4.pack(side="left")
        self.comb_edu_6_1_3 = ttk.Combobox(self.frame_edu_f, width=5, font=("Arial", 16))
        self.comb_edu_6_1_3['values'] = tuple(range(1970, 2028))
        self.comb_edu_6_1_3.set("Year")
        self.comb_edu_6_1_3.pack(side="left")

        self.label_edu_college= tk.Label(self.frame_edu_f, text="College : ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label_edu_college.pack(side="left")
        self.entry_college= tk.Entry(self.frame_edu_f, bg="black", fg="white", font=("Arial", 16))
        self.entry_college.pack(side="left")

        self.label_edu_degree= tk.Label(self.frame_edu_f, text="Degree : ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label_edu_degree.pack(side="left")
        self.entry_degree= tk.Entry(self.frame_edu_f, bg="black", fg="white", font=("Arial", 16))
        self.entry_degree.pack(side="left")

        self.label7 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Skills: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label7.pack(anchor='w',pady=5)
        self.entry7 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry7.pack(anchor='w')
        self.entry7_1 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry7_1.pack(anchor='w')
        self.entry7_2 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry7_2.pack(anchor='w')



        self.label7_1 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Projects: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label7_1.pack(anchor='w',pady=5)
        self.entry8 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry8.pack(anchor='w')

        self.label8 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Programming Languages: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label8.pack(anchor='w',pady=5)
        self.frame3 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame3.pack(anchor='w')
        
        self.check_var1 = tk.IntVar()
        self.entry9_1 = tk.Checkbutton(self.frame3, bg="black", fg="white", font=("Arial", 16), width=12,text="Java",variable=self.check_var1)
        self.entry9_1.pack(side="left")
        self.check_var2 = tk.IntVar()
        self.entry9_2 = tk.Checkbutton(self.frame3, bg="black", fg="white", font=("Arial", 16), width=12,text="Python",variable=self.check_var2)
        self.entry9_2.pack(side="left")
        self.check_var3 = tk.IntVar()
        self.entry9_3 = tk.Checkbutton(self.frame3, bg="black", fg="white", font=("Arial", 16), width=12,text="C++",variable=self.check_var3)
        self.entry9_3.pack(side="left")
        self.check_var4 = tk.IntVar()
        self.entry9_4 = tk.Checkbutton(self.frame3, bg="black", fg="white", font=("Arial", 16), width=12,text="Dart",variable=self.check_var4)
        self.entry9_4.pack(side="left")
        self.check_var5 = tk.IntVar()
        self.entry9_5 = tk.Checkbutton(self.frame3, bg="black", fg="white", font=("Arial", 16), width=12,text="html",variable=self.check_var5)
        self.entry9_5.pack(side="left")

        self.label9 = tk.Label(self.home_frame.scrollable_frame, text="Links", bg="black", fg="white", font=("Poppins", 35, "bold"))
        self.label9.pack(anchor='w',pady=50)

        self.label10 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your LinkedIn: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label10.pack(anchor='w',pady=5)
        self.entry10 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry10.pack(anchor='w')

        self.label11 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Github: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label11.pack(anchor='w',pady=5)
        self.entry11 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry11.pack(anchor='w')

        self.label12 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Instagram: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label12.pack(anchor='w',pady=5)
        self.entry12 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry12.pack(anchor='w')

        self.label13 = tk.Label(self.home_frame.scrollable_frame, text="Achievements", bg="black", fg="white", font=("Poppins", 35, "bold"))
        self.label13.pack(anchor='w',pady=50)

        self.label13_1 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Certifications: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label13_1.pack(anchor='w',pady=5)
        self.entry13_1 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry13_1.pack(anchor='w')
        self.entry13_2_2 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry13_2_2.pack(anchor='w')
        self.entry13_3_2 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry13_3_2.pack(anchor='w')

        self.label13_2 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Awards: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label13_2.pack(anchor='w',pady=5)
        self.entry13_2 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry13_2.pack(anchor='w')

        self.label13_3 = tk.Label(self.home_frame.scrollable_frame, text="Enter Your Publications: ", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label13_3.pack(anchor='w',pady=5)
        self.entry13_3 = tk.Entry(self.home_frame.scrollable_frame, bg="black", fg="white", font=("Arial", 16))
        self.entry13_3.pack(anchor='w')

        self.label14 = tk.Label(self.home_frame.scrollable_frame, text="Choose Theme", bg="black", fg="white", font=("League Gothic", 24, "bold"))
        self.label14.pack(anchor='w',pady=5)

        self.rad_var1 = tk.IntVar(value=2)
        self.entry14 = tk.Radiobutton(self.home_frame.scrollable_frame, bg="white", fg="black", font=("Arial", 16), width=12,text="Red",variable=self.rad_var1,value=1)
        self.entry14.pack(side="left")
        self.entry14_1 = tk.Radiobutton(self.home_frame.scrollable_frame, bg="white", fg="black", font=("Arial", 16), width=12,text="Blue",variable=self.rad_var1,value=2)
        self.entry14_1.pack(side="left")
        self.entry14_2 = tk.Radiobutton(self.home_frame.scrollable_frame, bg="white", fg="black", font=("Arial", 16), width=12,text="Green",variable=self.rad_var1,value=3)
        self.entry14_2.pack(side="left")

        self.gen=tk.Button(self.home_frame.scrollable_frame, text="Generate PDF", bg="black", fg="white", font=("Arial", 16),command=self.generate_pdf)
        self.gen.pack(anchor="w",pady=50,padx=100)

        
        self.frame4 = tk.Frame(self.home_frame.scrollable_frame, bg="black",width=500)
        self.frame4.pack(anchor="nw")

        self.frame5 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame5.pack(anchor="nw")

        self.frame6 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame6.pack(anchor="nw")

        self.frame7 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame7.pack(anchor="nw")

        self.frame8 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame8.pack(anchor="nw")

        self.frame9 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame9.pack(anchor="nw")

        self.frame10 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame10.pack(anchor="nw")

        self.frame11 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame11.pack(anchor="nw")

        self.frame12 = tk.Frame(self.home_frame.scrollable_frame, bg="black")
        self.frame12.pack(anchor="nw")

    def generate_pdf(self):

        pdf = FPDF()
        
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)
        if self.rad_var1.get()==2:
            pdf.set_fill_color(204, 229, 255) 
        elif self.rad_var1.get()==1:
            pdf.set_fill_color(255, 204, 204)
        elif self.rad_var1.get()==3:
            pdf.set_fill_color(204, 255, 209)
        pdf.rect(10,0, 79, 300, 'F')
        pdf.set_text_color(0, 0, 0) 
        pdf.set_xy(130, 10)        

        name_icon_path = "assets/Profile - 1.png"
        git_icon_path="assets/kisspng-github-computer-icons-icon-design-github-5ab8a31e334e73.4114704215220498222102-removebg-preview.png"
        add_icon_path = "assets/Location.png"
        mail_icon_path = "assets/Message.png"
        phone_icon_path = "assets/Call.png"
        dob_icon_path = "assets/Calendar - 1.png"
        linkedin_icon_path = "assets/image-removebg-preview.png"
        instagram_icon_path = "assets/image-removebg-preview (1).png"

        if self.rad_var1.get()==2:
            pdf.set_fill_color(5, 117, 232)
        elif self.rad_var1.get()==1:
            pdf.set_fill_color(232, 5, 5)
        elif self.rad_var1.get()==3:
            pdf.set_fill_color(5, 232, 5) 
        pdf.rect(17, 7, 185, 50, 'F')
        pdf.set_text_color(255,255,255) 
        pdf.set_xy(130, 10)

        pdf.image(name_icon_path, x=20, y=7, w=5)
        pdf.set_xy(30,6)
        pdf.set_font("Helvetica", size=12,style='B') 
        pdf.multi_cell(0, 10,self.entry1.get())

        

        pdf.image(mail_icon_path, x=20, y=17, w=5)
        pdf.set_xy(30,16)
        pdf.multi_cell(0, 10, self.entry3.get())

        pdf.image(phone_icon_path, x=20, y=27, w=5)
        pdf.set_xy(30,26)
        pdf.multi_cell(0, 10, self.entry5.get())

        pdf.image(add_icon_path, x=20, y=37, w=5)
        pdf.set_xy(30,36)
        pdf.multi_cell(0, 10, self.entry4.get())

        pdf.image(dob_icon_path,x=20, y=47,w=5)
        pdf.set_xy(30,46)
        pdf.multi_cell(0, 10,f"{self.comb1.get()} - {self.comb2.get()} - {self.comb3.get()}")

        pdf.set_text_color(0, 0, 0)     
        pdf.set_xy(15, 60)
        pdf.set_font("Times", size=16, style='B')  
        pdf.cell(0, 10, txt="Social Media Links:", ln=True, align="L")

        pdf.image(linkedin_icon_path, x=15, y=72, w=5) 
        pdf.set_xy(25,70)
        pdf.set_font("Helvetica", size=8,style='B')
        pdf.multi_cell(0, 10, self.entry10.get())

        pdf.image(instagram_icon_path, x=15, y=82, w=5) 
        pdf.set_xy(25,80)
        pdf.multi_cell(0, 10, self.entry12.get()) 

        pdf.image(git_icon_path, x=15, y=92, w=5) 
        pdf.set_xy(25,90)
        pdf.multi_cell(0, 10, self.entry11.get())

        pdf.set_xy(15,105)
        pdf.set_font("Times", size=16, style='B')  
        pdf.cell(0, 10, txt="Skills:", ln=True, align="L")

        pdf.set_xy(15, 115)
        pdf.set_font("Helvetica", size=8) 
        pdf.multi_cell(0, 10, f"-{self.entry7.get()}")

        pdf.set_xy(15, 120)
        pdf.multi_cell(0, 10, f"-{self.entry7_1.get()}")

        pdf.set_xy(15, 125)
        pdf.multi_cell(0, 10, f"-{self.entry7_2.get()}")

        pdf.set_text_color(0, 0, 0)     
        pdf.set_xy(15, 135)
        pdf.set_font("Times", size=16, style='B')  
        pdf.cell(0, 10, txt="Coding Languages:", ln=True, align="L")

        java_icon_path = "assets/java.png"
        python_icon_path = "assets/python.png"
        cpp_icon_path = "assets/pngwing.com (2).png"
        html_icon_path="assets/html.png"
        dart_icon_path="assets/icons8-dart-language-50.png"
        pdf.set_font("Helvetica", size=8,style='B')   
        if self.check_var1.get()==1 :
            pdf.image(java_icon_path, x=20, y=145, w=5)
            pdf.set_xy(30,142)
            pdf.multi_cell(0, 10, "Java" )

        if self.check_var2.get()==1:
            pdf.image(python_icon_path, x=20, y=152, w=5)
            pdf.set_xy(30,149)
            pdf.multi_cell(0, 10, "Python")

        if self.check_var3.get()==1:
            pdf.image(cpp_icon_path, x=20, y=160, w=5)
            pdf.set_xy(30,157)
            pdf.multi_cell(0, 10, "C++")

        if self.check_var4.get()==1:
            pdf.image(dart_icon_path, x=20, y=170, w=5)
            pdf.set_xy(30,167)
            pdf.multi_cell(0, 10, "Dart")

        if self.check_var5.get()==1:
            pdf.image(html_icon_path, x=20, y=180, w=5)
            pdf.set_xy(30,177)
            pdf.multi_cell(0, 10,"html")

        pdf.set_text_color(0, 0, 0)     
        pdf.set_xy(15, 185)
        pdf.set_font("Times", size=16, style='B')  
        pdf.cell(0, 10, txt="Awards:", ln=True, align="L")
        
        pdf.set_xy(15, 190)
        pdf.set_font("Helvetica", size=8,style='B')
        pdf.multi_cell(0, 10, f"-{self.entry13_2.get()}")



        
        pdf.set_xy(90,60)
        if self.rad_var1.get()==2:
            pdf.set_fill_color(151, 177, 247)
        elif self.rad_var1.get()==1:
            pdf.set_fill_color(247, 151, 151)
        elif self.rad_var1.get()==3:
            pdf.set_fill_color(165, 247, 151)
        pdf.rect(90, 60,30, 10, 'F')
        pdf.set_text_color(255,255,255)
        pdf.set_font("Times", size=17, style='B')  
        pdf.cell(0, 10, txt="Education:", ln=True, align="L")
        
        pdf.set_text_color(0, 0, 0)     
        pdf.set_xy(90, 70)
        pdf.set_font("Times", size=12, style='B')  
        pdf.multi_cell(0, 10, f"College - {self.entry_college.get()}")
        pdf.set_xy(90, 77)
        pdf.multi_cell(0, 10, f"Degree - {self.entry_degree.get()}")
        pdf.set_xy(150,65)
        pdf.set_font("Times", size=12)
        pdf.multi_cell(0, 10, f"From:{self.comb_edu_6_3.get()}")
        pdf.set_xy(172,65)
        pdf.multi_cell(0, 10, f"To: {self.comb_edu_6_1_3.get()}")


             
        pdf.set_xy(90,120)
        pdf.set_font("Times", size=17, style='B')
        if self.rad_var1.get()==2:    
            pdf.set_fill_color(151, 177, 247)
        elif self.rad_var1.get()==1:
            pdf.set_fill_color(247, 151, 151)
        elif self.rad_var1.get()==3:
            pdf.set_fill_color(165, 247, 151) 
        pdf.rect(90, 120,50, 10, 'F')
        pdf.set_text_color(255,255,255)  
        pdf.cell(0, 10, txt="Work Experience:", ln=True, align="L")
        pdf.set_xy(90, 130)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Times", size=12, style='B')
        pdf.multi_cell(0, 10, f"Company - {self.entry6_1.get()}")
        pdf.set_xy(90, 137)
        pdf.set_font("Times", size=12, style='B')
        pdf.multi_cell(0, 10, f"Role - {self.entry6_2.get()}")
        pdf.set_font("Times", size=12)
        pdf.set_xy(155,130)
        pdf.multi_cell(0, 10, f"From:{self.comb_6.get()}-{self.comb_6_2.get()}-{self.comb_6_3.get()}")
        pdf.set_xy(155,137)
        pdf.multi_cell(0, 10, f"To: {self.comb_6_1.get()}-{self.comb_6_1_2.get()}-{self.comb_6_1_3.get()}")

             
        pdf.set_xy(90,180)
        pdf.set_font("Times", size=17, style='B')  
        if self.rad_var1.get()==2:    
            pdf.set_fill_color(151, 177, 247)
        elif self.rad_var1.get()==1:
            pdf.set_fill_color(247, 151, 151)
        elif self.rad_var1.get()==3:
            pdf.set_fill_color(165, 247, 151)
        pdf.rect(90, 180,40, 10, 'F')
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 10, txt="Certificates:", ln=True, align="L")
        
        pdf.set_xy(90, 190)
        pdf.set_font("Times", size=12, style='B')
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 10, f"- {self.entry13_1.get()}")
        pdf.set_xy(90, 200)
        pdf.multi_cell(0, 10, f"- {self.entry13_2_2.get()}")
        pdf.set_xy(90, 210)
        pdf.multi_cell(0, 10, f"- {self.entry13_3_2.get()}")

        pdf.set_text_color(0, 0, 0)     
        pdf.set_xy(90,240)
        pdf.set_font("Times", size=17, style='B')  
        if self.rad_var1.get()==2:
            pdf.set_fill_color(151, 177, 247)
        elif self.rad_var1.get()==1:
            pdf.set_fill_color(247, 151, 151) 
        elif self.rad_var1.get()==3:
            pdf.set_fill_color(165, 247, 151)
        pdf.rect(90, 240,40, 10, 'F')
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 10, txt="Publications:", ln=True, align="L")
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(90,250)
        pdf.set_font("Times", size=12, style='B')
        pdf.multi_cell(0, 10,f"- {self.entry13_3.get()}" )


        


        pdf.set_xy(10, 265)
        pdf.set_font("Helvetica", size=8, style='I')
        pdf.cell(0, 10, txt="Generated by THUNDERBOLTZ>>>>", ln=True, align="L")

        pdf_file_name = "resume_output.pdf"
        pdf.output(pdf_file_name)
        print(f"PDF generated: {pdf_file_name}")

        

        
        if any(value == "" for value in [ self.entry1.get(),self.entry5.get(),self.entry4.get(),self.entry3.get()]):
            messagebox.showerror("Error", "Please fill in all required fields.")
        else :
            pdf_file_name = "resume_output.pdf"
            pdf.output(pdf_file_name)    
            messagebox.showinfo("PDF Generated", "Your PDF Resume has been generated successfully!")
        

app = MainWindow()
app.main.mainloop()
