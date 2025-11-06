import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer


class Test:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
        self.current = 0
        self.score = 0

        # GUI setup
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry("600x400")
        self.root.config(bg="#f0f4f7")

        # Heading
        tk.Label(self.root, text=self.title, font=("Helvetica", 20, "bold"),
                 fg="#2c3e50", bg="#f0f4f7").pack(pady=15)

        # Frame for Question + Options
        self.frame = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.q_label = tk.Label(self.frame, text="", font=("Arial", 14), 
                                wraplength=500, justify="left", bg="white")
        self.q_label.pack(pady=20, anchor="w")

        self.var = tk.IntVar()
        self.buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.frame, text="", variable=self.var, value=i,
                                 font=("Arial", 12), anchor="w",
                                 bg="white", fg="#34495e",
                                 activebackground="#ecf0f1", selectcolor="#dfe6e9")
            btn.pack(fill="x", padx=30, pady=5)
            self.buttons.append(btn)

        # Next button
        self.next_btn = tk.Button(self.root, text="Next ➡", command=self.next_question,
                                  font=("Arial", 14, "bold"),
                                  bg="#27ae60", fg="white",
                                  activebackground="#2ecc71",
                                  activeforeground="white", width=12)
        self.next_btn.pack(pady=10)

        self.show_question()
        self.root.mainloop()

    def show_question(self):
        q = self.questions[self.current]
        self.q_label.config(text=f"Q{self.current + 1}. {q.text}")
        for i, opt in enumerate(q.options):
            self.buttons[i].config(text=opt)
        self.var.set(-1)

    def next_question(self):
        q = self.questions[self.current]
        choice = self.var.get()
        if choice == -1:
            messagebox.showwarning("Warning", "Please select an option!")
            return

        if q.options[choice] == q.answer:
            self.score += 1

        self.current += 1
        if self.current < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Result", f"🎉 Final Score: {self.score}/{len(self.questions)}")
            self.root.destroy()


# Create Questions
questions = [
    Question("Python file extension?", [".txt", ".py", ".java", ".exe"], ".py"),
    Question("Keyword to define a function?", ["func", "def", "function", "define"], "def"),
    Question("Immutable type?", ["List", "Tuple", "Set", "Dict"], "Tuple"),
    Question("Comment symbol in Python?", ["//", "#", "<!--", "--"], "#"),
    Question("Which loop for sequence?", ["for", "while", "loop", "repeat"], "for"),
    Question("Which creates object?", ["class", "function", "def", "method"], "class"),
    Question("Constructor method?", ["create", "init", "__init__", "start"], "__init__"),
    Question("What is OOP?", ["Order of Program", "Official Process", "Object Oriented Programming", "None"], "Object Oriented Programming"),
    Question("Input from user?", ["read()", "get()", "input()", "scanner()"], "input()"),
    Question("Type of 10?", ["str", "float", "int", "bool"], "int")
]

# Run Test
Test("MCQs Project - Weekly Test", questions)
