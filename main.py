from modules.crud_estudiantes import menu_gestion_estudiantes, ver_cursos_estudiante
from modules.matriculas import matricular_estudiante
from modules.crud_cursos import menu_gestion_cursos, ver_creditos_estudiante, ver_estudiantes_de_curso, menu_gestion_cursos
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def mostrar_menu():
    menu = (
        "[bold cyan]1.[/] Gestion de estudiantes\n"
        "[bold cyan]2.[/] Gestion de cursos\n"
        "[bold cyan]3.[/] matricular a un estudiante\n"
        "[bold cyan]4.[/] Ver cursos de un estudiante\n"
        "[bold cyan]5.[/] Ver estudiantes de un curso\n"
        "[bold cyan]6.[/] Ver creditos totales de un estudiante\n"
        "[bold cyan]0.[/] Salir"
    )
    
    console.print(Panel(
        menu, 
        title="[bold cyan]MENU PRINCIPAL[/]", 
        title_align="center",
        box=box.ROUNDED,
        border_style="cyan",
        expand=False
    ))

def main():
    while True:
        mostrar_menu()
        opcion = console.input("\nSeleccione una opcion: ").strip()

        match opcion:
            case "1":
                menu_gestion_estudiantes()

            case "2":
                menu_gestion_cursos()

            case "3":
                console.print("[bold blue]PROCESO DE MATRICULA DE UN ESTUDIANTE[/bold blue]")
                matricular_estudiante()
            case "4":
                ver_cursos_estudiante()

            case "5":
                ver_estudiantes_de_curso()
                
            case "6":
                ver_creditos_estudiante()

            case "0":
                console.print("[bold red]Saliendo del sistema...[/bold red]")
                break

            case _:
                console.print("[bold red]Opcion no valida, intente de nuevo.[/bold red]")

if __name__ == "__main__":
    main()

