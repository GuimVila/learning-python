# SOLID.py

"""
Aquest arxiu conté explicacions pedagògiques sobre els principis SOLID.
Cada principi està explicat amb exemples de codi en anglès i amb explicacions en català.
Inclou explicacions detallades sobre conceptes com:
- Què significa "una sola raó per canviar"
- El concepte de polimorfisme
- El principi de substitució de Liskov
- La segregació d'interfícies
- Diferència entre mòduls d'alt nivell i de baix nivell
"""

# Single Responsibility Principle
# Principi de responsabilitat única

# Una classe ha de tenir una sola raó per canviar, això significa que una classe ha de tenir només una feina.
# Això implica que cada classe hauria d'estar especialitzada en un aspecte concret del programa.
# Si una classe assumeix múltiples responsabilitats, esdevé difícil de mantenir perquè un canvi en una responsabilitat
# pot afectar altres parts de la classe.

# Expliquem-ho amb un exemple:

class Journal:
    """Una classe que gestiona les entrades d'un diari."""
    def __init__(self):
        """El mètode __init__ s'utilitza per inicialitzar atributs d'una instància de classe.
        És necessari quan cal configurar valors inicials per a un objecte, com en aquest cas, una llista d'entrades i un comptador."""
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        """Afegeix una entrada al diari."""
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        """Elimina una entrada del diari."""
        del self.entries[pos]

    def __str__(self):
        """Retorna el contingut del diari com una cadena."""
        return '\n'.join(self.entries)

    # Aquí es viola el principi de responsabilitat única:
    # Aquesta funcionalitat gestiona l'emmagatzematge del diari en un fitxer, però aquesta responsabilitat
    # no hauria d'estar dins de la classe Journal. Això la fa menys especialitzada.
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

    def load(self, filename):
        pass

# Solució: separem aquesta responsabilitat en una altra classe
class JournalPersistence:
    """Una classe separada per gestionar la persistència del diari."""
    @staticmethod
    def save_to_file(journal, filename):
        """Aquesta línia defineix un mètode estàtic, que no depèn de cap instància de la classe.
        És útil per funcionalitats que no necessiten accedir a atributs o mètodes de l'objecte."""
        with open(filename, 'w') as file:
            file.write(str(journal))

    @staticmethod
    def load_from_file(filename):
        pass

# Aquesta separació fa que Journal només s'encarregui de gestionar entrades i que JournalPersistence
# gestioni la persistència, complint així amb el principi.

# Open/Closed Principle
# Principi obert/tancat

# Els objectes han d'estar oberts a l'extensió però tancats a la modificació.
# Això significa que podem afegir funcionalitats noves sense modificar el codi existent.

from abc import ABC, abstractmethod

class Shape(ABC):
    """Una interfície per a formes geomètriques."""
    @abstractmethod
    def area(self):
        """Aquesta línia defineix un mètode abstracte, que obliga les subclasses a implementar aquest mètode.
        És útil per garantir que totes les subclasses tinguin una implementació d'aquest comportament.
        Això assegura que totes les formes derivades (com Rectangle o Circle) compleixin amb aquesta interfície i
        implementin la lògica de càlcul de l'àrea."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        """El mètode __init__ aquí configura els valors inicials per al rectangle: amplada i alçada."""
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        """El mètode __init__ aquí configura el radi inicial del cercle."""
        self.radius = radius

    def area(self):
        return 3.14159265359 * self.radius ** 2

class AreaCalculator:
    """Una classe que calcula l'àrea total de diverses formes."""
    def __init__(self, shapes):
        """El mètode __init__ aquí configura una llista de formes que es calcularan."""
        self.shapes = shapes

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

# Aquí estem fent ús del polimorfisme: la classe AreaCalculator no necessita saber quines són
# les formes específiques. Simplement sap que cada forma té un mètode `area`.

# Liskov Substitution Principle
# Principi de substitució de Liskov

# Els objectes de la classe base han de ser substituïbles pels objectes de les seves subclasses sense
# alterar la correcció del programa.

# Expliquem-ho millor:
class Bird:
    """Una classe base que representa un ocell."""
    def fly(self):
        raise NotImplementedError("Aquest ocell no pot volar")

class Duck(Bird):
    def fly(self):
        return "Duck flying!"

class Ostrich(Bird):
    # Això viola el principi perquè un Ostrich no pot volar, i estem canviant el comportament esperat.
    def fly(self):
        raise Exception("No puc volar!")

# Solució: canviem el disseny perquè no tots els ocells assumeixin que poden volar.

class Bird:
    """Una classe base per a tots els ocells."""
    pass

class FlyingBird(Bird):
    def fly(self):
        return "Flying!"

class Duck(FlyingBird):
    def fly(self):
        return "Duck flying!"

class Ostrich(Bird):
    pass

# Interface Segregation Principle
# Principi de segregació d'interfícies

# Una interfície no hauria de forçar els clients a implementar funcionalitats que no necessiten.

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self, document):
        print("Imprimint document")

    def scan(self, document):
        print("Escanejant document")

# Aquí el principi s'aplica correctament perquè només implementem els mètodes que necessitem.

# Dependency Inversion Principle
# Principi d'inversió de dependències

# Els mòduls d'alt nivell no haurien de dependre dels mòduls de baix nivell. Tots dos haurien de dependre d'abstraccions.

# Un mòdul de baix nivell és aquell que interactua directament amb detalls concrets (com ara una bombeta).
# Un mòdul d'alt nivell és aquell que defineix la lògica del programa i que hauria de ser independent de com es fan els detalls.

class LightBulb:
    """Una bombeta."""
    def turn_on(self):
        print("La bombeta està encesa")

    def turn_off(self):
        print("La bombeta està apagada")

class ElectricPowerSwitch:
    """Un interruptor per controlar la bombeta."""
    def __init__(self, l: LightBulb):
        """El mètode __init__ inicialitza l'objecte amb una bombeta específica i configura l'estat inicial."""
        self.lightbulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightbulb.turn_off()
            self.on = False
        else:
            self.lightbulb.turn_on()
            self.on = True

# Aquí el problema és que ElectricPowerSwitch depèn directament de LightBulb. Si canviem la bombeta per un altre tipus,
# caldria modificar ElectricPowerSwitch. La solució és introduir una interfície abstracta per la bombeta:

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("La bombeta està encesa")

    def turn_off(self):
        print("La bombeta està apagada")

class ElectricPowerSwitch:
    def __init__(self, device: Switchable):
        """El mètode __init__ inicialitza l'objecte amb un dispositiu que implementa la interfície Switchable."""
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True

if __name__ == "__main__":
    # Exemple d'ús
    l = LightBulb()
    switch = ElectricPowerSwitch(l)
    switch.press()
    switch.press()
