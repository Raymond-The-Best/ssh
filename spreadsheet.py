
from typing import Union

class SpreadSheet:
    OPERATORS = ["+", "-", "*", "/", "%"]

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> Union[int, str]:
        if cell in self._evaluating:
            return "#Circular"
        self._evaluating.add(cell)
        
        value = self.get(cell)
        if value.isdigit():
            result = int(value)
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        elif value.startswith("='") and value.endswith("'"):
            result = value[2:-1]
        elif value.startswith("="):
            ref = value[1:]
            if ref.isdigit():
                result = int(ref)
            elif ref in self._cells:
                result = self.evaluate(ref)
            elif any(operator in ref for operator in self.OPERATORS):
                try:
                    result = eval(ref)
                    if not isinstance(result, int):
                        result = "#Error"
                except:
                    result = "#Error"
            else:
                result = "#Error"
        else:
            try:
                float(value)
                result = "#Error"
            except ValueError:
                result = "#Error"
        
        self._evaluating.remove(cell)
        return result

