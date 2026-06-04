# Sistema de Gestion de Matriculas Academicas 📓
>es una aplicacion hecha para para consola, programada con **Python** y con estilos de la biblioteca de **rich** para mejorar la experiencia del usuario

>diseñada para la gestion de estudiantes, cursos y las matriculas de los estudiantes

## Developers del proyecto 🌟👨‍💻👩‍💻
 * Juan Sebastian Girata (usuario de Github: **[Juanchis2004](https://github.com/Juanchis2004)**)
 * Leidy Daniela Perez Rodriguez (usuario de Github: **[danii-11](https://github.com/danii-11))**
 * Daniel Acosta Gonzalez (usuario de Github: **[D45-csm](https://github.com/D45-csm)**)

**Instructores:**  
- 🧑‍🏫 Instructor: Andres Felipe Sandoval 

## Descripcion general

### Entidades 
***estudiantes**
 *id del estudiante: int
 *nombre str:
 *carrera str:

***cursos**
 *id del curso: int
 *nombre del curso: str
 *numero de creditos: int

* **matriculas(relacion entre estudiante y curso)**
 * id de matricula: int
 * id estudiante: int
 * id curso: int
 * periodo academico: str

### Modulos del proyecto:
-modulo de estudiantes👨‍🎓
-modulo de cursos 📖🔬
-matriculas ✏️
-guardar y cargar datos

### Descripcion detallada
Este es un sistema integral diseñado para **optimizar el control académico**, permitiendo la gestión eficiente de estudiantes 👨‍🎓 (registro, listar estudiantes,cantidad de creditos), la administración de cursos 🔬📔(si estan disponibles, agregar o eliminar cursos) y el proceso de matrículas (asignación de alumnos a cursos), tambien dando un campo visual 👀 de la relacion entre estudiantes y cursos, asi centralizando la información para facilitar la toma de decisiones y el seguimiento administrativo.


## formato de datos ℹ️
los datos se guardan en 3 archivos json, que son estudiantes, cursos y matriculas, cada uno sigue la misma estructura:

**lista**[

  * **diccionario(registro)**{

   * **datos(clave:valor)**

   }

]

>ejemplo en archivo json:
```json 
[
    {
        "id_curso": 101,
        "nombre_curso": "Bases de Datos",
        "creditos": 2
    },
    {
        "id_curso": 105,
        "nombre_curso": "JavaScript",
        "creditos": 2
    },
    {
        "id_curso": 107,
        "nombre_curso": "Logica de programacion",
        "creditos": 2
    }
] 
```

😀 **_¡agradecemos tu interes en nuestro proyecto, nos motivamos cada dia por mejorar!_**  😸😸😸
grupo numero 3
