from S1E9 import Character


class Baratheon(Character):

    """"""

    def __init__(self, first_name, is_alive=True):

        """"""

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):

        """"""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):

        """"""

        return self.__str__()


class Lannister(Character):

    """"""

    def __init__(self, first_name, is_alive=True):

        """"""

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):

        """"""

        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):

        """"""

        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):

        """"""

        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance
