class human():
    eyes = 0
    steps = 0
    def __init__(self):
        eyes = 2
        steps = 0

    def walk(self):
        steps += 1


man = human()

man.walk()

print(man.steps)
