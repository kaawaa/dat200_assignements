import turtle


# Tegner snøflaket, rekursivt
# Kjøretid er O(n**2)
def koch_snowflake(lenght: int, order: int) -> None:
    # Base case
    if order <= 0:
        turtle.forward(lenght)
    else:
        koch_snowflake(lenght / 3, order - 1)
        turtle.left(60)
        koch_snowflake(lenght / 3, order - 1)
        turtle.right(120)
        koch_snowflake(lenght / 3, order - 1)
        turtle.left(60)
        koch_snowflake(lenght / 3, order - 1)

# Starter å tegne, kjører koch_snowflake 3 ganger for å få et full snøflak
def koch_snowflake_start(lenght: int, order: int, color: str) -> None:
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        koch_snowflake(lenght, order)
        turtle.right(120)
    turtle.end_fill()

def main() -> None:
    turtle.setup(800,800, 0, 0)
    turtle.pendown()
    koch_snowflake_start(200, 2, "blue")
    turtle.done()

if __name__ == "__main__":
    main()