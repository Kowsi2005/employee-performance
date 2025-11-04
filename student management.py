import tkinter as tk
from tkinter import messagebox

# List to store student details
students = []

# Main Application Class
class StudentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("500x400")
        self.resizable(False, False)

        # Container for all frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Dictionary to hold pages
        self.frames = {}

        for F in (HomePage, RegisterPage, StudentListPage, AboutPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page_class):
        """Show a frame for the given page class"""
        frame = self.frames[page_class]
        frame.tkraise()


# ------------------ PAGE 1 : HOME PAGE ------------------
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#e8f0fe")
        tk.Label(self, text="🎓 Welcome to Student Management System", font=("Arial", 16, "bold"), bg="#e8f0fe").pack(pady=40)

        tk.Button(self, text="Register Student", width=25, command=lambda: controller.show_frame(RegisterPage)).pack(pady=10)
        tk.Button(self, text="View Student List", width=25, command=lambda: controller.show_frame(StudentListPage)).pack(pady=10)
        tk.Button(self, text="About App", width=25, command=lambda: controller.show_frame(AboutPage)).pack(pady=10)
        tk.Button(self, text="Exit", width=25, command=controller.destroy).pack(pady=10)


# ------------------ PAGE 2 : REGISTRATION PAGE ------------------
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#fefae0")

        tk.Label(self, text="📝 Student Registration", font=("Arial", 16, "bold"), bg="#fefae0").pack(pady=20)

        # Input Fields
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.course_var = tk.StringVar()

        form_frame = tk.Frame(self, bg="#fefae0")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:", bg="#fefae0").grid(row=0, column=0, sticky="e", pady=5)
        tk.Entry(form_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Age:", bg="#fefae0").grid(row=1, column=0, sticky="e", pady=5)
        tk.Entry(form_frame, textvariable=self.age_var, width=30).grid(row=1, column=1, pady=5)

        tk.Label(form_frame, text="Gender:", bg="#fefae0").grid(row=2, column=0, sticky="e", pady=5)
        tk.Entry(form_frame, textvariable=self.gender_var, width=30).grid(row=2, column=1, pady=5)

        tk.Label(form_frame, text="Course:", bg="#fefae0").grid(row=3, column=0, sticky="e", pady=5)
        tk.Entry(form_frame, textvariable=self.course_var, width=30).grid(row=3, column=1, pady=5)

        tk.Button(self, text="Save Student", command=self.save_student).pack(pady=10)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage)).pack(pady=5)

    def save_student(self):
        """Save student details into list"""
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        gender = self.gender_var.get().strip()
        course = self.course_var.get().strip()

        if not (name and age and gender and course):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        students.append({"Name": name, "Age": age, "Gender": gender, "Course": course})
        messagebox.showinfo("Success", f"Student '{name}' registered successfully!")

        # Clear entries
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.course_var.set("")


# ------------------ PAGE 3 : STUDENT LIST PAGE ------------------
class StudentListPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#faedcd")

        tk.Label(self, text="📋 Registered Students", font=("Arial", 16, "bold"), bg="#faedcd").pack(pady=20)

        self.listbox = tk.Listbox(self, width=60, height=10)
        self.listbox.pack(pady=10)

        tk.Button(self, text="Refresh List", command=self.refresh_list).pack(pady=5)
        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage)).pack(pady=5)

    def refresh_list(self):
        """Update the listbox with current student data"""
        self.listbox.delete(0, tk.END)
        if not students:
            self.listbox.insert(tk.END, "No students registered yet.")
        else:
            for i, s in enumerate(students, start=1):
                entry = f"{i}. {s['Name']} | Age: {s['Age']} | Gender: {s['Gender']} | Course: {s['Course']}"
                self.listbox.insert(tk.END, entry)


# ------------------ PAGE 4 : ABOUT PAGE ------------------
class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d8e2dc")

        tk.Label(self, text="ℹ️ About This Application", font=("Arial", 16, "bold"), bg="#d8e2dc").pack(pady=20)

        info = (
            "Student Management System\n"
            "Version: 1.0\n\n"
            "Developed using Python Tkinter\n"
            "Features:\n"
            "• Student registration\n"
            "• List viewing\n"
            "• Multi-page navigation\n\n"
            "👩‍💻 Developer: S. Kowsika Kowsalya"
        )
        tk.Label(self, text=info, justify="left", bg="#d8e2dc", font=("Arial", 12)).pack(pady=10)

        tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage)).pack(pady=20)


# ------------------ MAIN DRIVER CODE ------------------
if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
