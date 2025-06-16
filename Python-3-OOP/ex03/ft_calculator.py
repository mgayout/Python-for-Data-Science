class calculator:

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        vector = []
        for x in self.vector:
            vector.append(x + object)
        self.vector = vector
        print(self.vector)

    def __mul__(self, object) -> None:
        vector = []
        for x in self.vector:
            vector.append(x * object)
        self.vector = vector
        print(self.vector)

    def __sub__(self, object) -> None:
        vector = []
        for x in self.vector:
            vector.append(x - object)
        self.vector = vector
        print(self.vector)

    def __truediv__(self, object) -> None:
        try:
            if object == 0:
                raise AssertionError("A division by 0 is forbiden")
            vector = []
            for x in self.vector:
                vector.append(x / object)
            self.vector = vector
            print(self.vector)
        except AssertionError as error:
            print(AssertionError.__name__ + ":", error)
