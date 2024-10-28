# Sistema de Gestión de Calificaciones Estudiantiles

## Descripción
Este proyecto es una implementación en Python de un sistema de gestión de calificaciones estudiantiles que utiliza múltiples estructuras de datos: Arrays Vectoriales, Archivos y XML. El sistema permite gestionar información de estudiantes y sus calificaciones de manera eficiente y organizada.

## Requisitos
- Python 3.10 o superior
- Bibliotecas estándar de Python (no se requieren dependencias externas)

## Instalación
1. Clone o descargue este repositorio
2. Asegúrese de tener Python 3.10 o superior instalado
3. No se requieren instalaciones adicionales ya que el proyecto utiliza solo bibliotecas estándar de Python

## Uso

### Iniciar el Programa
```bash
python main.py
```

### Menú Principal
El sistema ofrece las siguientes opciones:
1. Agregar Estudiante
2. Eliminar Estudiante
3. Actualizar Calificaciones
4. Mostrar Todos los Estudiantes
5. Ordenar Estudiantes
6. Buscar Estudiantes
7. Exportar Datos
8. Salir

### Funcionalidades Principales

#### 1. Agregar Estudiante
- Ingrese apellidos y nombres
- Ingrese 4 calificaciones mensuales (0-100)
- El sistema calcula automáticamente el promedio

#### 2. Eliminar Estudiante
- Busque por apellidos y nombres
- Confirme la eliminación

#### 3. Actualizar Calificaciones
- Busque el estudiante por apellidos y nombres
- Ingrese las nuevas calificaciones
- El promedio se actualiza automáticamente

#### 4. Mostrar Estudiantes
- Muestra una lista completa de estudiantes
- Incluye calificaciones mensuales y promedio

#### 5. Ordenar Estudiantes
Opciones de ordenamiento:
- Por apellidos (A-Z)
- Por apellidos (Z-A)
- Por promedio (Mayor a menor)
- Por promedio (Menor a mayor)

#### 6. Buscar Estudiantes
Métodos de búsqueda:
- Por nombre (parcial o completo)
- Por rango de calificaciones

#### 7. Exportar Datos
Formatos disponibles:
- CSV
- JSON
- XML
- Todos los formatos anteriores

## Estructura de Datos

### Vector Array
- Implementación personalizada para almacenamiento en memoria
- Operaciones CRUD optimizadas
- Métodos de ordenamiento y búsqueda eficientes

### Almacenamiento en Archivos
- Formato de texto plano para persistencia de datos
- Separación de campos mediante delimitadores
- Recuperación automática al inicio del programa

### Documento XML
- Estructura jerárquica de datos
- Formato estandarizado para intercambio de información
- Generación automática al guardar cambios

## Validación de Datos
- Control de rango de calificaciones (0-100)
- Validación de nombres (solo letras y espacios)
- Verificación de cantidad de calificaciones
- Control de decimales (máximo 2 lugares)

## Formatos de Exportación

### CSV
```csv
Apellidos,Nombres,Nota Mes 1,Nota Mes 2,Nota Mes 3,Nota Mes 4,Promedio
```

### JSON
```json
{
  "apellidos": "Apellido",
  "nombres": "Nombre",
  "calificaciones": {
    "notaMes1": 85.5,
    "notaMes2": 90.0,
    "notaMes3": 88.5,
    "notaMes4": 92.0
  },
  "promedio": 89.0
}
```

### XML
```xml
<students>
  <student>
    <name>
      <apellidos>Apellido</apellidos>
      <nombres>Nombre</nombres>
    </name>
    <calificaciones>
      <notaMes1>85.5</notaMes1>
      <notaMes2>90.0</notaMes2>
      <notaMes3>88.5</notaMes3>
      <notaMes4>92.0</notaMes4>
    </calificaciones>
    <promedio>89.0</promedio>
  </student>
</students>
```

## Manejo de Errores
- Validación de entrada de datos
- Mensajes de error descriptivos
- Confirmación de operaciones críticas
- Recuperación ante fallos de archivo

## Notas Importantes
- Los datos se guardan automáticamente después de cada operación
- Se mantiene una copia de seguridad en múltiples formatos
- Las búsquedas son insensibles a mayúsculas/minúsculas
- El sistema permite nombres con espacios y caracteres especiales
