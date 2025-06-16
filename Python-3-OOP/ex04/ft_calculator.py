class calculator:

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = float(0)
        for x in range(len(V1)):
            result += V1[x] * V2[x]
        print(f"Dot product is : {int(result)}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        vector = []
        for x in range(len(V1)):
            vector.append(float(V1[x] + V2[x]))
        print(f"Add Vector is : {vector}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        vector = []
        for x in range(len(V1)):
            vector.append(float(V1[x] - V2[x]))
        print(f"Sous Vector is : {vector}")
