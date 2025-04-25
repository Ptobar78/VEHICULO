class vehiculo:
    def __init__(self, marca:str, modelo:str, color:str=None, anio=2025):
    #son funciones, que reciben parametros y crean objetos
        self._color = color
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
    def __str__(self):
    #son funciones que reciben parametros y crean
        #return f'vehiculo: {self._marca} modelo: {self._modelo} anio: {self._anio}'
        return f'vehiculo: {self.__dict__.__str__()}'
if __name__ == '__main__':
    v1 = vehiculo('BMW', 'Arizona', 'rojo', '2023')
    print('Vehículo 1')
    print(v1._marca)
    print(v1._modelo)
    print(v1._color)
    print(v1._anio)

    v2 = vehiculo('FORD', 'F150', 'NEGRO', '1999')
    print('Vehiculo 2')
    print(v2._marca)
    print(v2._modelo)
    print(v2._color)
    print(v2._anio)

    v3 = vehiculo('TESLA', 'version 1', 'blanco' '2025')
    print('Vehiculo 3')
    print(v3._marca)
    print(v3._modelo)
    print(v3._color)
    print(v3._anio)

    V4 = vehiculo('LAMBORGINI', 'PUZZLE', 'ROJO', '2024')
    print('Vehiculo 4')
    print(V4._marca)
    print(V4._modelo)
    print(V4._color)
    print(V4._anio)

    V5 = vehiculo(modelo='Aruba', marca='Arizona', color='MIel', anio='2026')

    print('Vehiculo 5')
    print(V5)
