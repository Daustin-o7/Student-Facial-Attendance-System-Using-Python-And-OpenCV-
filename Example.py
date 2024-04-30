from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from tkinter import filedialog

my_data = []


class attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # variables
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()

        # Header
        title_lbl = Label(self.root, text="Student Attendance System", font=("times new roman", 32, "bold"),
                          bg="white", fg="#4da8da")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(self.root, bd=2, bg='white')
        main_frame.place(x=10, y=55, width=1510, height=830)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE,
                                text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=740, height=790)

        # Left Inside Frame
        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg='white')
        left_inside_frame.place(x=6, y=155, width=725, height=305)

        # Attendance ID
        attendance_id = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 12, "bold"),
                              bg='white')
        attendance_id.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        AttendanceID_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_attend_id,
                                       font=("times new roman", 12, "bold"))
        AttendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll number
        Roll_id = Label(left_inside_frame, text="Roll:", font=("times new roman", 12, "bold"), bg='white')
        Roll_id.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        RollID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_roll, width=20,
                                  font=("times new roman", 12, "bold"))
        RollID_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        Name_id = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg='white')
        Name_id.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        NameID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_name, width=20,
                                  font=("times new roman", 12, "bold"))
        NameID_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        Department_id = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"),
                               bg='white')
        Department_id.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        DepartmentID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_dep, width=20,
                                       font=("times new roman", 12, "bold"))
        DepartmentID_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        Time_id = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg='white')
        Time_id.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        TimeID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_time, width=20,
                                  font=("times new roman", 12, "bold"))
        TimeID_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        Date_id = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg='white')
        Date_id.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DateID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_date, width=20,
                                  font=("times new roman", 12, "bold"))
        DateID_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance status
        attendance_status = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"),
                                  bg='white')
        attendance_status.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.attendance_status_combo = ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"),
                                                    state="readonly", width=18)
        self.attendance_status_combo['values'] = ("Status", "Present", "Absent", "Other")
        self.attendance_status_combo.grid(row=3, column=1, padx=9, pady=5, sticky=W)
        self.attendance_status_combo.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=260, width=720, height=37)

        import_btn = Button(btn_frame, text="Import CSV", command=self.import_csv,
                            font=("times new roman", 12, "bold"), bg="#4da8da", fg="white", width=19)
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", command=self.export_csv,
                            font=("times new roman", 12, "bold"), bg="#4da8da", fg="white", width=19)
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", font=("times new roman", 12, "bold"), bg="#4da8da",
                            fg="white", width=19)
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"),
                           bg="#4da8da", fg="white", width=19)
        reset_btn.grid(row=0, column=3)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE,
                                 text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=760, y=10, width=740, height=790)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=6, y=5, width=725, height=775)

        # Scrollbar table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                  column=("id", "roll", "name", "department", "time", "date",
                                                          "attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll No")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor_data)

    # Import CSV
    def import_csv(self):
        global my_data
        my_data.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV File",
                                         filetypes=(("CSV File", "*.csv"), ("ALL Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                my_data.append(i)
            self.fetch_data(my_data)

    # Export CSV
    def export_csv(self):
        try:
            if len(my_data) < 1:
                messagebox.showerror("No data", "No data to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV File",
                                                filetypes=(("CSV File", "*.csv"), ("ALL Files", "*.*")),
                                                parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported ")
        except Exception as e:
            messagebox.showerror("Error", f"Due to :{str(e)}", parent=self.root)

    # Fetch data function
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # Get cursor data
    def get_cursor_data(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    # Reset Data
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()
