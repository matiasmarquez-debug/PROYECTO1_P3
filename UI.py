def mensaje():
    print('Casos por covid 19')

def departamento():
    dep = input('Ingrese el nombre del departamento del cual quiere obtener los datos: ').strip()
    return dep
def num_casos():
    limite = int(input('Ingrese el numero de datos que quiere obtener: '))
    if limite <= 1000 and limite > 0:
        return limite
    else:
        print('Por favor ingrese un numero menor a mil y mayor a 0.')
        return(num_casos())
COLUMNAS = [
    "ciudad_municipio_nom", "departamento_nom", "edad",
    "fuente_tipo_contagio", "estado", "pais_viajo_1_nom"
]
FORMATO = "{:<25} {:<20} {:<5} {:<15} {:<12} {:<20}"
def mostrar_casos(casos):
    if casos.empty:
        print('No se encontro registro.')
        return
    casos = casos.reindex(columns = COLUMNAS).fillna('N/A')
    titulos = FORMATO.format('Municipio', 'Departamento', 'Edad', 'Tipo', 'Estado', 'Pais')
    print(titulos)
    print('-' * len(titulos))
    for fila in casos.itertuples(index = False):
        print(FORMATO.format(*fila))



