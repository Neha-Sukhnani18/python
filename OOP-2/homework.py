class ExpressionSolver:
    """A class to solve mathematical expressions using OOP."""
    def __init__(self, expression):
        self.expression = expression
        self.result = None
    def solve(self):
        """Evaluates the expression string safely."""
        try:
            self.result = eval(self.expression)
        except Exception as e:
            self.result = f"Error: {e}"
    def display_result(self):
        """Prints the expression and its result."""
        print(f"Expression: {self.expression}")
        print(f"Result: {self.result}")
        print("-" * 20)
if __name__ == "__main__":
    calc1 = ExpressionSolver("5 + 10 * 2")
    calc2 = ExpressionSolver("(100 / 4) + 3**2")
    calc1.solve()
    calc1.display_result()
    calc2.solve()
    calc2.display_result()