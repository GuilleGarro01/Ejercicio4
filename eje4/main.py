from Ventana import Ventana

def test():
    print('Prueba'.center(30,'-'))
    objeto = Ventana('Prueba',20,30,100,200)
    objeto.mostrar()
    objeto.moverDerecha(10)
    objeto.mostrar()
    objeto.moverIzquierda(20)
    objeto.mostrar()
    objeto.bajar(10)
    objeto.mostrar()
    objeto.subir(10)
    objeto.mostrar()
    print('Prueba'.center(30,'-'))
if __name__ ==  '__main__':
    test()
    print('==== Ventana Inicio ====')
    ventanaInicio= Ventana('Inicio')
    ventanaInicio.mostrar()
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('==== Ventana Cargar ====')
    ventanaCargar= Ventana('Cargar',10,20)
    ventanaCargar.mostrar()
    print('*** Mueve a la derecha ***')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()
    print('*** Mueve a la izquierda ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()
    print('*** Bajar ***')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()
    print('==== Ventana Borrar ====')
    ventanaBorrar = Ventana('Borrar', 10,20,100,200)
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir(5)   
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir()
    ventanaBorrar.mostrar()
    print('*** Bajar ***')
    ventanaBorrar.bajar()
    ventanaBorrar.mostrar()