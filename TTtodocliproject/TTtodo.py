import typer
from rich.console import Console
from rich.table import Table
from rich import box
from model import TTtodo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()

app = typer.Typer()

@app.command(short_help='adds a task')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo = TTtodo(task, category)
    insert_todo(todo)
    show()

@app.command(short_help='deletes a task')
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_todo(position-1)
    show()

@app.command(short_help='updates a task', )
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_todo(position-1, task, category)
    show()

@app.command(short_help='marks a task as Done')
def complete(position: int):
    typer.echo(f"complete {position}")
    complete_todo(position-1)
    show()

@app.command(short_help='shows a list of all tasks')
def show():
    tasks = get_all_todos()
    console.print("[bold magenta]TT's Todo's[/bold magenta]")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("ID", width = 6)
    table.add_column("Task", min_width = 20)
    table.add_column("Category", min_width = 20)
    table.add_column("Done", min_width = 6)

    for idx, task in enumerate(tasks, start=1):
        is_done_str = '✅' if task.status == 2 else '❌'
        table.add_row(str(idx), task.task, f"{task.category}", is_done_str)
    console.print(table)

if __name__ == "__main__":
    app()