def calculate_value(x: float, y: float, op: str) -> float | None:
    """Example of a docstring."""
    if op == "add":
        return x + y
    elif op == "sub":
        return x - y
    elif op == "mul":
        return x * y
    elif op == "div":
        if y == 0:
            raise ValueError("Division by zero")
            # return None
        return x / y
    else:
        return 0


print(calculate_value(10, 5, "add"))
