class division:
    def __init__(self) -> None:
        pass

    def division(self,num1:int,num2:int):
        if num1 == 0 or num2 == 0:
            return "no se puede dividir por 0"
        else:
            return  f"{num1 / num2:.2f}"