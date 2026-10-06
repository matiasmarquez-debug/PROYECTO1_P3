# Casos de COVID-19 en Colombia

Programa en Python que consulta los casos positivos de COVID-19 en Colombia usando la API de Socrata del portal de datos abiertos [datos.gov.co](https://www.datos.gov.co) (dataset `gt2j-8ykr`).

El usuario ingresa un departamento y un límite de registros, y el programa muestra en pantalla una tabla con: municipio, departamento, edad, tipo, estado y país de procedencia.

## Estructura

```
├── main.py      # Punto de entrada: coordina la UI y la API
├── api.py       # Consulta a Socrata y conversión a DataFrame de pandas
└── ui.py    # Entrada de datos y visualización con format
```

## Requisitos

- Python 3.10 o superior
- [pandas](https://pandas.pydata.org/)
- [sodapy](https://github.com/xmunoz/sodapy)

```bash
pip install pandas sodapy
```

Ejemplo:

```
Ingrese el nombre del departamento: Risaralda
Ingrese el límite de registros: 10
```

## Notas

- El nombre del departamento se convierte a mayúsculas, porque así está escrito en los datos.

## Autor

Matias, estudiante de Ingeniería de Sistemas, Universidad Tecnológica de Pereira (UTP).
