from modules.guardar_cargar_datos import cargar_datos, guardar_datos
from rich import print # Importamos el print de rich para dar estilos
from rich.console import Console
from rich.table import Table

# Inicializamos la consola de rich
console = Console()

def matricular_estudiante():
    datos_matriculas = cargar_datos("sg-matriculas/data/matriculas.json")
    datos_estudiantes = cargar_datos("sg-matriculas/data/estudiantes.json")
    datos_cursos = cargar_datos("sg-matriculas/data/cursos.json")

    # 1. INGRESAR ID DEL ESTUDIANTE

    # definimos tabla dde estudiantes
    tabla_estudiantes = Table(title="\nLISTADO DE ESTUDIANTES", title_style="bold cyan", header_style="bold cyan")
    tabla_estudiantes.add_column("ID", style="cyan", justify="right")
    tabla_estudiantes.add_column("Nombre", style="white")

    for estudiante in datos_estudiantes:
        # Aseguramos que los datos pasen como texto (str) a la tabla
        tabla_estudiantes.add_row(str(estudiante['id_estudiante']), str(estudiante['nombre']))
    
    # Imprimimos la tabla
    console.print(tabla_estudiantes)

    # Validar ID Estudiante
    id_estudiante = None
    while True:
        entrada = input("\nIngrese el ID del estudiante a matricular: ").strip()
        #buscamos el id en los registros de los estudiantes
        for estudiante in datos_estudiantes: 
            if str(estudiante['id_estudiante']) == entrada:  
                id_estudiante = entrada 
                break  #si existe, tomamos el id y lo guardamos en id_estudiante
        
        if id_estudiante: #si la variable deja de tener valor none, rompe el bucle
            break
        print("[bold red]Error:[/bold red] ID de estudiante no encontrado. Intente de nuevo.") # en caso de que no exista el id

    # 2. INGRESAR ID DEL CURSO

    # definimos tabla de cursos
    tabla_cursos = Table(title="\nLISTADO DE CURSOS", title_style="bold magenta", header_style="bold magenta")
    tabla_cursos.add_column("ID", style="magenta", justify="right")
    tabla_cursos.add_column("Curso", style="white")

    for curso in datos_cursos:
        tabla_cursos.add_row(str(curso['id_curso']), str(curso['nombre_curso']))
    
    # Imprimimos la tabla
    console.print(tabla_cursos)

    #Validar ID de curso
    id_curso = None
    while True:
        entrada = input("\nIngrese el ID del curso: ").strip()
        for curso in datos_cursos:
            if str(curso['id_curso']) == entrada:
                id_curso = entrada
                break
        
        if id_curso:
            break
        print("[bold red]Error:[/bold red] ID de curso no encontrado. Intente de nuevo.")

    # 3.VALIDAR SI EL ESTUDIANTE YA ESTA MATRICULADO EN ESE CURSO
    for matricula in datos_matriculas:
        # extraemos los id de los cursos
        cursos_matriculados = [str(curso) for curso in matricula['id_curso']]
        
        # Verificamos si el ID del estudiante coincide Y si el ID del curso está dentro de su lista
        if str(matricula['id_estudiante']) == id_estudiante and id_curso in cursos_matriculados:
            print("[bold yellow]Error:[/bold yellow] El estudiante ya está matriculado en este curso.")
            return # si las condiciones se cumplen, la funcion no devuelve nada
        
    # 4. INGRESAR PERIODO ACADEMICO
    periodo_academico = input("\nIngrese el periodo académico (e.g., 2026-2): ").strip()

    # 5. Guardar
    nueva_matricula = {
        "id_matricula": len(datos_matriculas) + 1, # le asignamos un id incrementado en 1 a la nueva matricula
        "id_estudiante": int(id_estudiante), 
        "id_curso": [int(id_curso)], #ponemos el id del curso y lo pasamos a un int
        "periodo_academico": periodo_academico
    }

    #6. GUARDAR LA MATRICULA EN SU RESPECTIVO ARCHIVO JSON
    datos_matriculas.append(nueva_matricula)
    guardar_datos("sg-matriculas/data/matriculas.json", datos_matriculas)
    print(f"\n[bold green]¡Éxito![/bold green] Estudiante [bold]{id_estudiante}[/bold] matriculado correctamente en el curso [bold]{id_curso}[/bold].")