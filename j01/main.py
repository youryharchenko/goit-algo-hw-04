import pathlib
import typer

from shutil import copy
from rich.console import Console

console = Console()

app = typer.Typer()


def walk(from_path: pathlib.Path, to_path: pathlib.Path, verbose: bool, dry: bool):
        if from_path.is_dir():

            for item in from_path.iterdir():
                walk(item, to_path, verbose, dry)

        elif from_path.is_file():

            ext = from_path.suffix.replace(".", "")
            if ext:
                dst = to_path.joinpath(ext)
            else:
                dst = to_path

            try:
                if not dst.exists():
                    dst.mkdir(parents=True)
                elif not dst.is_dir():
                    console.print(f"[bold red]Path {dst} must be directory[/bold red]")
                    return
                
                if verbose:
                    console.print(f"[bold green]{from_path} -> {dst}[/bold green]")
                
                if not dry:
                    copy(from_path, dst)

            except Exception as e:
                console.print(f"[bold red]Error: {e}[/bold red]")

        else:
            console.print(f"[bold red]Path {from_path} unknown[/bold red]")

@app.command()
def sort(from_dir: str = ".", to_dir: str = "dist", verbose: bool = False, dry: bool = False):

    console.print("[bold blue]Sort directory by extension[/bold blue]")

    from_path = pathlib.Path(from_dir).resolve()
    
    to_path = pathlib.Path(to_dir).resolve()
    if to_path.exists() and not to_path.is_dir():
        console.print(f"[bold red]Path {to_path} must be directory[/bold red]")
        return

    console.print(f"[bold blue]from: {from_path}[/bold blue]")
    console.print(f"[bold blue]to: {to_path}[/bold blue]")

    walk(from_path, to_path, verbose, dry)



def main():
    app()    


    
