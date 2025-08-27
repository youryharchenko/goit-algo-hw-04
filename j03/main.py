import pathlib
from collections import deque

from rich.console import Console
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory

from j01.classes import Service

script_path = pathlib.Path(__file__)

commands = {
    "exit": 0
}

console = Console()

history_path = script_path.with_name('.history')
history = FileHistory(history_path)
completer = WordCompleter(list(commands.keys()))


session = PromptSession(
        history=history, completer=completer, reserve_space_for_menu=True)

service = Service()

def parse_input(msg_prompt: str):
        msg: str = session.prompt(msg_prompt)
        return msg.lower().strip()

def is_palindrome_simple(text: str):
    text = text.replace(" ", "")
    l = len(text)
    part1 = text[:l//2]
    if l % 2: 
        part2 = text[l//2+1:] 
    else:
        part2 = text[l//2:]

    part2 = part2[::-1]

    #print(f"{part1} - {part2}")
   
    return part1 == part2

def is_palindrome_dequeue(text: str):
    text = text.replace(" ", "")
    l = len(text)
    part1 = text[:l//2]
    if l % 2: 
        part2 = text[l//2+1:] 
    else:
        part2 = text[l//2:]

    dq2 = deque()
    dq2.extendleft(part2)
    dq1 = deque()
    dq1.extend(part1)

    return list(dq1) == list(dq2)


def main():
    
    console.print("[bold green]Welcome to the Test a Palindrome![/bold green]")
    console.print(
        "Type text or 'exit' to quit.")
    
    while True:
        repl = parse_input("Enter text: ")
        try:
            match repl:
                case 'exit':
                    console.print("[bold green]Good bye![/bold green]")
                    break
                case text:
                    if is_palindrome_dequeue(text):
                        console.print(f"[bold green]Yes[/bold green]")
                    else:
                        console.print(f"[bold red]No[/bold red]")
        except Exception as ex:
            console.print(f"[bold red]{ex}[/bold red]")


    
