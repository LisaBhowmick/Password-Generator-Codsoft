import string
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class GUI():
    def __init__(self, master):
        self.master = master
        self.passwordlen = IntVar()
        self.generatedpassword = StringVar()

        root.title('Password Generator')
        root.geometry('550x220')
        root.configure(bg='#FFF5E1')  # Light pastel background
        root.resizable(False, False)

        style = ttk.Style()
        style.theme_use("default")

        # Light cartoony theme
        style.configure("TLabel", foreground="#444444", background="#FFF5E1", font=("Comic Sans MS", 12, "bold"))
        style.configure("TEntry", padding=6, font=("Comic Sans MS", 11))
        style.configure("TButton",
                        font=("Comic Sans MS", 11, "bold"),
                        padding=6,
                        background="#FF91A4",
                        foreground="white")
        style.map("TButton", background=[("active", "#FF6F91")])

        # Title
        self.title_label = Label(text="Password Generator", 
                                 font=("Comic Sans MS", 18, "bold"), 
                                 bg="#FFF5E1", fg="#FF6F91")
        self.title_label.pack(pady=(15, 10))

        # Control frame
        control_frame = Frame(root, bg="#FFF5E1")
        control_frame.pack(pady=5, fill="x")

        self.length_label = ttk.Label(control_frame, text="🔢 Length:")
        self.length_label.grid(row=0, column=0, padx=5)
        self.length_entry = ttk.Entry(control_frame, textvariable=self.passwordlen, width=8)
        self.length_entry.grid(row=0, column=1, padx=5)

        self.generate_btn = ttk.Button(control_frame, text="✨ Generate", command=self.generate_pass)
        self.generate_btn.grid(row=0, column=2, padx=5)

        self.reset_btn = ttk.Button(control_frame, text="🧹 Reset", command=self.reset_fields)
        self.reset_btn.grid(row=0, column=3, padx=5)

        # Output frame
        output_frame = Frame(root, bg="#FFF5E1")
        output_frame.pack(pady=15, fill="x")

        self.generated_label = ttk.Label(output_frame, text="🔒 Your Password:")
        self.generated_label.grid(row=0, column=0, padx=5)
        self.generated_entry = ttk.Entry(output_frame, textvariable=self.generatedpassword, width=30, foreground="#B8336A")
        self.generated_entry.grid(row=0, column=1, padx=5)

    def generate_pass(self):
        upper = list(string.ascii_uppercase)
        lower = list(string.ascii_lowercase)
        chars = list("@#%&()\"?!")
        numbers = list(string.digits)

        try:
            length = int(self.passwordlen.get())
        except ValueError:
            messagebox.showerror("Oops!", "Length must be a number")
            return

        if length < 6:
            messagebox.showerror("Too Short!", "Password must be at least 6 characters 💡")
            return

        u = random.randint(1, length - 3)
        l = random.randint(1, length - 2 - u)
        c = random.randint(1, length - 1 - u - l)
        n = length - u - l - c

        password = (
            random.sample(upper, u)
            + random.sample(lower, l)
            + random.sample(chars, c)
            + random.sample(numbers, n)
        )
        random.shuffle(password)
        gen_passwd = "".join(password)

        self.generated_entry.delete(0, END)
        self.generated_entry.insert(0, gen_passwd)

    def reset_fields(self):
        self.length_entry.delete(0, END)
        self.generated_entry.delete(0, END)

if __name__ == '__main__':
    root = Tk()
    pass_gen = GUI(root)
    root.mainloop()
