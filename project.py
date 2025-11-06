class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def ask(self):
        print(self.text)
        for i, opt in enumerate(self.options, 1):
            print(f"{i}. {opt}")
        choice = int(input("Your answer: "))
        return self.options[choice - 1] == self.answer


class Test:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, q):
        self.questions.append(q)

    def start(self):
        print("\n===", self.title, "===")
        score = 0
        for q in self.questions:
            if q.ask():
                print("Correct!\n")
                score += 1
            else:
                print("Wrong!\n")
        print("Final Score:", score, "/", len(self.questions))


test = Test("Saylani Test - Weekly Test")

test.add_question(Question("Python file extension?", [".txt", ".py", ".java", ".exe"], ".py"))
test.add_question(Question("Keyword to define a function?", ["func", "def", "function", "define"], "def"))
test.add_question(Question("Immutable type?", ["List", "Tuple", "Set", "Dict"], "Tuple"))
test.add_question(Question("Comment symbol in Python?", ["//", "#", "<!--", "--"], "#"))
test.add_question(Question("Which loop for sequence?", ["for", "while", "loop", "repeat"], "for"))
test.add_question(Question("Which creates object?", ["class", "function", "def", "method"], "class"))
test.add_question(Question("Constructor method?", ["create", "init", "__init__", "start"], "__init__"))
test.add_question(Question("What is OOP?", ["Order of Program", "Official Process", "Object Oriented Programming", "None"], "Object Oriented Programming"))
test.add_question(Question("Input from user?", ["read()", "get()", "input()", "scanner()"], "input()"))
test.add_question(Question("Type of 10?", ["str", "float", "int", "bool"], "int"))


# Run the test
test.start()
