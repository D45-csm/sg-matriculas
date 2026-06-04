import os, json
from typing import List, Dict, Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from modules.guardar_cargar_datos import cargar_datos, guardar_datos

# ==========================
# CONFIGURACIÓN DE RUTAS Y CONSOLA
# ==========================
console = Console()
BASE_DIR = os.path.dirname(__file__)  # Carpeta actual: sg-matriculas/modules
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")  # Carpeta donde están los archivos JSON

# Rutas de los archivos de datos
RUTA_CURSOS = os.path.join(DATA_DIR, "cursos.json")
RUTA_ESTUDIANTES = os.path.join(DATA_DIR, "estudiantes.json")
RUTA_MATRICULAS = os.path.join(DATA_DIR, "matriculas.json")

# ==========================
# FUNCIONES AUXILIARES
# ==========================
def buscar_curso(cursos: List[Dict], id_curso: int) -> Optional[Dict]:
    """Busca un curso por su ID dentro de la lista de cursos."""
    return next((c for c in cursos if c["id_curso"] == id_curso), None)

def mostrar_tabla(titulo: str, columnas: List[str], filas: List[List[str]]) -> None:
    """Muestra una tabla formateada con Rich."""
    tabla = Table(title=titulo, show_lines=True, header_style="bold cyan", title_style="bold magenta")
    [tabla.add_column(c, justify="center") for c in columnas]
    [tabla.add_row(*f) for f in filas]
    console.print(tabla)

# ==========================
# CRUD DE CURSOS
# ==========================
def crear_curso() -> None:
    """Crea un nuevo curso y lo guarda en cursos.json."""
    cursos = cargar_datos(RUTA_CURSOS)
    try:
        id_curso = int(input("ID del curso: "))
        if buscar_curso(cursos, id_curso):
            return console.print("[red]⚠ ID ya existe.[/red]")
        cursos.append({
            "id_curso": id_curso,
            "nombre_curso": input("Nombre: ").strip(),
            "creditos": int(input("Créditos: "))
        })
        guardar_datos(RUTA_CURSOS, cursos)
        console.print("[green]✔ Curso creado.[/green]")
    except ValueError:
        console.print("[red]✖ ID y créditos deben ser numéricos.[/red]")

def listar_cursos() -> None:
    """Lista todos los cursos registrados."""
    cursos = cargar_datos(RUTA_CURSOS)
    if not cursos:
        return console.print("[yellow]⚠ No hay cursos.[/yellow]")
    mostrar_tabla("📚 LISTA DE CURSOS", ["ID", "Nombre", "Créditos"],
                  [[str(c["id_curso"]), c["nombre_curso"], str(c["creditos"])] for c in cursos])

def actualizar_curso() -> None:
    """Actualiza el nombre y créditos de un curso existente."""
    cursos = cargar_datos(RUTA_CURSOS)
    try:
        id_curso = int(input("ID a actualizar: "))
        curso = buscar_curso(cursos, id_curso)
        if not curso:
            return console.print("[red]❌ Curso no encontrado.[/red]")
        curso.update({
            "nombre_curso": input("Nuevo nombre: ").strip(),
            "creditos": int(input("Nuevos créditos: "))
        })
        guardar_datos(RUTA_CURSOS, cursos)
        console.print("[green]✔ Curso actualizado.[/green]")
    except ValueError:
        console.print("[red]✖ Entrada inválida.[/red]")

def eliminar_curso() -> None:
    """Elimina un curso por su ID."""
    cursos = cargar_datos(RUTA_CURSOS)
    try:
        id_curso = int(input("ID a eliminar: "))
        if not buscar_curso(cursos, id_curso):
            return console.print("[red]❌ Curso no encontrado.[/red]")
        guardar_datos(RUTA_CURSOS, [c for c in cursos if c["id_curso"] != id_curso])
        console.print("[green]🗑️ Curso eliminado.[/green]")
    except ValueError:
        console.print("[red]✖ Entrada inválida.[/red]")

# ==========================
# CONSULTAS
# ==========================
def ver_estudiantes_de_curso() -> None:
    """Muestra los estudiantes inscritos en un curso específico."""
    cursos, estudiantes, matriculas = cargar_datos(RUTA_CURSOS), cargar_datos(RUTA_ESTUDIANTES), cargar_datos(RUTA_MATRICULAS)
    try:
        id_curso = int(input("ID del curso: "))
        curso = buscar_curso(cursos, id_curso)
        if not curso:
            return console.print("[red]❌ Curso no encontrado.[/red]")

        # Crear mapas para acceder rápido a datos
        mapa_cursos = {c["id_curso"]: c["creditos"] for c in cursos}
        mapa_estudiantes = {e["id_estudiante"]: e for e in estudiantes}

        # Buscar estudiantes matriculados en el curso
        estudiantes_curso = [m["id_estudiante"] for m in matriculas if (
            id_curso in m.get("id_curso", []) if isinstance(m.get("id_curso"), list) else m.get("id_curso") == id_curso)]

        if not estudiantes_curso:
            return console.print(f"[yellow]⚠ No hay estudiantes en {curso['nombre_curso']}.[/yellow]")

        filas = []
        for id_est in estudiantes_curso:
            est = mapa_estudiantes.get(id_est)
            if est:
                cursos_est = sum(mapa_cursos.get(c, 0) for m in matriculas if m["id_estudiante"] == id_est
                                 for c in (m["id_curso"] if isinstance(m["id_curso"], list) else [m["id_curso"]]))
                filas.append([str(est["id_estudiante"]), est["nombre"], est["carrera"], str(cursos_est)])

        mostrar_tabla(f"👥 Estudiantes en {curso['nombre_curso']}", ["ID", "Nombre", "Carrera", "Créditos acumulados"], filas)
    except ValueError:
        console.print("[red]✖ ID debe ser numérico.[/red]")

# ==========================
# RETO FINAL
# ==========================
def ver_creditos_estudiante() -> None:
    """
    🔥 Reto Final:
    Calcula y muestra el total de créditos matriculados por un estudiante.
    Esta función cumple el objetivo final del proyecto: integrar los datos de estudiantes,
    cursos y matrículas para obtener el total de créditos cursados.
    """
    estudiantes, cursos, matriculas = cargar_datos(RUTA_ESTUDIANTES), cargar_datos(RUTA_CURSOS), cargar_datos(RUTA_MATRICULAS)
    try:
        id_est = int(input("ID del estudiante: "))
        est = next((e for e in estudiantes if e["id_estudiante"] == id_est), None)
        if not est:
            return console.print("[red]❌ Estudiante no encontrado.[/red]")

        # Buscar los cursos en los que el estudiante está matriculado
        cursos_est = [c for m in matriculas if m["id_estudiante"] == id_est
                      for c in (m["id_curso"] if isinstance(m["id_curso"], list) else [m["id_curso"]])]
        if not cursos_est:
            return console.print(f"[yellow]⚠ {est['nombre']} no tiene cursos.[/yellow]")

        # Crear un mapa de cursos para acceder rápido a los créditos
        mapa_cursos = {c["id_curso"]: c for c in cursos}

        # Sumar los créditos de todos los cursos matriculados
        total = sum(mapa_cursos.get(c, {"creditos": 0})["creditos"] for c in cursos_est)

        # Mostrar los cursos y el total de créditos
        filas = []
        for c in cursos_est:
            if c in mapa_cursos:
                curso = mapa_cursos[c]
                filas.append([str(curso["id_curso"]), curso["nombre_curso"], str(curso["creditos"])])

        mostrar_tabla(f"📚 Cursos de {est['nombre']}", ["ID", "Nombre", "Créditos"], filas)
        console.print(f"\n[bold green]✔ Total de créditos: {total}[/bold green]")
    except ValueError:
        console.print("[red]✖ ID debe ser numérico.[/red]")

# ==========================
# MENÚ DE GESTIÓN DE CURSOS
# ==========================
def menu_gestion_cursos():
    while True:
        menu_texto = (
            "[bold cyan]1.[/bold cyan] Crear curso\n"
            "[bold cyan]2.[/bold cyan] Ver lista de cursos\n"
            "[bold cyan]3.[/bold cyan] Actualizar curso\n"
            "[bold cyan]4.[/bold cyan] Eliminar curso\n"
            "[bold cyan]5.[/bold cyan] Ver estudiantes de un curso\n"
            "[bold cyan]6.[/bold cyan] Ver creditos de un estudiante\n"
            "[bold cyan]7.[/bold cyan] Volver al menu principal"
        )

        console.print("\n")
        console.print(
            Panel(
                menu_texto,
                title="[bold cyan]📚 GESTION DE CURSOS[/bold cyan]",
                border_style="cyan",
                width=45
            )
        )

        opcion = input("\nSeleccione una opcion: ").strip()

        match opcion:
            case "1":
                crear_curso()
            case "2":
                listar_cursos()
            case "3":
                actualizar_curso()
            case "4":
                eliminar_curso()
            case "5":
                ver_estudiantes_de_curso()
            case "6":
                ver_creditos_estudiante()
            case "7":
                break
            case _:
                console.print("[bold red]Opcion no valida.[/bold red]")