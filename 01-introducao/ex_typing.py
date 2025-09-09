from typing import Dict

def add(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return {"sum": response}

val1 = add(1, 3)
val2 = add(2.34, 4.56)
val3 = add("Hello", " World")

print(val1)
print(val2)
print(val3)