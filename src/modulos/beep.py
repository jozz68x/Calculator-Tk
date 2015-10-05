
__author__ = "Jose Diaz"

import winsound

class Beep(object):
    def frecuencia(halfNotesFromA4):
        valor = 440 * ((2)**(1.0/12.0)) ** halfNotesFromA4
        return (int)(valor)
    
    def sonido(nota, tiempo=200):
            frecuencia = Beep.frecuencia(nota)
            winsound.Beep(frecuencia, tiempo)
            
        