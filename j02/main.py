import turtle
import typer

from rich.console import Console

console = Console()

app = typer.Typer()

def init_draw(size: float):

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.color(0.0, 0.0, 1.0)
    t.pensize(2)
    t.goto(-size / 2, size / 3)
    t.pendown()

    return t

def koch_curve(t: turtle.Turtle, deep: int, size: float):
    if deep == 0:
        t.forward(size)
    else:
        for angle in [60.0, -120.0, 60.0, 0.0]:
            koch_curve(t, deep - 1, size / 3)
            t.left(angle)


@app.command()
def draw(deep: int = 4, size: float = 600.0):
    console.print("[bold blue]Draw Koch snowflake[/bold blue]")
    console.print(f"Level: {deep}" )
    
    win = turtle.Screen()
    win.bgcolor("yellow")

    t = init_draw(size)

    koch_curve(t, deep, size)
    t.right(120.0)
    koch_curve(t, deep, size)
    t.right(120.0)
    koch_curve(t, deep, size)

    win.mainloop()

def main():
    app()    