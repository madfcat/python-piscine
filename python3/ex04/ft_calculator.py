class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f"Dot product is: {sum([x * y for x,y in zip(V1, V2)])}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [x + y for x, y in zip(V1, V2)]
        formatted_result = ', '.join([f"{x:.1f}" for x in result])
        print(f"Add Vector is : [{formatted_result}]")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [x - y for x, y in zip(V1, V2)]
        formatted_result = ', '.join([f"{x:.1f}" for x in result])
        print(f"Sous Vector is : [{formatted_result}]")
