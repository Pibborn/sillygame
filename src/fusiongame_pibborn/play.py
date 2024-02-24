import PyInquirer
from rich import print
from rich.console import Console
from rich.table import Table
from utils import Const
from pet import load_from_file

if __name__ == '__main__':
    console = Console()
    console.print('..........Sangue.......... il gioco........', style=Const.STYLE_TITLE)
    pets = load_from_file(Const.PETS_PATH)
    table = Table(title="Available Pets")
    table.add_column('ID')
    table.add_column('Name', style="cyan")
    table.add_column('Class', style="green")
    for pet in pets:
        table.add_row(pet.id, pet.name, pet.petclass)
    console.print(table)
    
