"""
A partir de la clase Hora diseñada en el ejercicio anterior, implementar la clase
HoraExacta, que incluye en la hora los segundos. Además de los métodos heredados
desde la clase Hora, dispondrá de:
• __init__(hora,minutos,segundos): construye un objeto con los datos pasados
como argumentos.
1
• set_segundos(valor): asigna un valor (si está comprendido entre 0 y
59) a los segundos. Devuelve True o False según se haya podido cambiar los
segundos o no.
• inc(): incrementa la hora en un segundo
"""
class Hora:
    def __init__(self, hora, minutos):
        if not self.set_hora(hora):
            raise ValueError ("Rango de horas invalido (00-23)")
        if not self.set_minutos(minutos):
            raise ValueError ("Rango de minutos invalido (00-59")

    def inc(self):
        if self.get_minutos() == 59:
            if self.get_hora() == 23:
                self.set_hora(0)
            else:
                self.set_minutos(self.get_minutos() + 1)
                self.set_minutos(0)
        self.set_minutos(self.get_minutos() + 1)

    def get_hora(self):
        return self.hora

    def get_minutos(self):
        return self.minutos

    def set_minutos(self, minutos):
        if minutos in range(0,60):
            self.minutos = minutos
            return True
        return False

    def set_hora(self, hora):
        if hora in range(0,24):
            self.hora = hora
            return True
        return False

    def __str__(self):
        return f"La hora es: {self.get_hora()}:{self.get_minutos()}"

class HoraExacta(Hora):
    def __init__(self, hora, minutos, segundos):
        super().__init__(hora, minutos)
        if not self.set_segundos(segundos):
            raise ValueError ("Rango de segundos invalido (00-59)")

    def set_segundos(self, segundos):
        if segundos in range(0,60):
            self.segundos = segundos
            return True
        return False

    def get_segundos(self):
        return self.segundos

    def inc(self):
        if self.get_segundos() == 59:
            super().inc()
            self.set_segundos(0)
        else:
            self.set_segundos(self.get_segundos() + 1)

    def __str__(self):
        return f"La hora exacta es: {self.get_hora()}:{self.get_minutos()}:{self.get_segundos()}"
