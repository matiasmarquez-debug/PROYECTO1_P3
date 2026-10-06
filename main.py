
from ui import UI
from api import Api

def main():
    UI.mensaje()
    dep = UI.departamento()
    numero = UI.num_casos()
    informacion = Api.casos(numero, dep)
    UI.mostrar_casos(informacion)

if __name__ == '__main__':
    main()