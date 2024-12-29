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

from dataclasses import dataclass

@dataclass
class Entry:
    """Representa una entrada del diari."""
    id: int
    text: str

class EntryAdder:
    """Gestiona l'addició d'entrades."""
    def __init__(self):
        self.count = 0

    def add_entry(self, entries, text):
        self.count += 1
        entries.append(Entry(id=self.count, text=text))

class EntryRemover:
    """Gestiona l'eliminació d'entrades."""
    def remove_entry(self, entries, entry_id):
        return [entry for entry in entries if entry.id != entry_id]

class EntryLister:
    """Gestiona la visualització d'entrades."""
    def list_entries(self, entries):
        return "\n".join(f"{entry.id}: {entry.text}" for entry in entries)

class EntryManager:
    """Coordina l'addició, eliminació i visualització d'entrades."""
    def __init__(self):
        self.entries = []
        self.adder = EntryAdder()
        self.remover = EntryRemover()
        self.lister = EntryLister()

    def add_entry(self, text):
        self.adder.add_entry(self.entries, text)

    def remove_entry(self, entry_id):
        self.entries = self.remover.remove_entry(self.entries, entry_id)

    def list_entries(self):
        return self.lister.list_entries(self.entries)

class Journal:
    """Un diari que coordina la gestió d'entrades."""
    def __init__(self):
        self.manager = EntryManager()

    def __str__(self):
        return self.manager.list_entries()

class JournalPersistence:
    """Gestiona la persistència del diari."""
    @staticmethod
    def save_to_file(journal: Journal, filename: str):
        with open(filename, 'w') as file:
            file.write(str(journal))

    @staticmethod
    def load_from_file(filename: str) -> str:
        with open(filename, 'r') as file:
            return file.read()

# Exemple d'ús
if __name__ == "__main__":
    journal = Journal()
    journal.manager.add_entry("Vaig aprendre sobre el principi SOLID.")
    journal.manager.add_entry("El principi de responsabilitat única és clau.")
    print("Diari actual:")
    print(journal)

    # Persistim el diari
    filename = "journal.txt"
    JournalPersistence.save_to_file(journal, filename)

    print(f"Diari guardat a {filename}")
    print("Carreguem contingut des del fitxer:")
    print(JournalPersistence.load_from_file(filename))

# Open/Closed Principle
# Principi obert/tancat

# Els objectes han d'estar oberts a l'extensió però tancats a la modificació.
# Això significa que podem afegir funcionalitats noves sense modificar el codi existent.

from abc import ABC, abstractmethod

class Shape(ABC):
    """Una interfície per a formes geomètriques."""
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * self.radius ** 2

class AreaCalculator:
    """Calcula l'àrea total de diverses formes."""
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

# Exemple d'ús
if __name__ == "__main__":
    shapes = [Rectangle(4, 5), Circle(3)]
    calculator = AreaCalculator(shapes)
    print(f"L'àrea total és: {calculator.total_area()}")

# Liskov Substitution Principle
# Principi de substitució de Liskov

# Els objectes de la classe base han de ser substituïbles pels objectes de les seves subclasses sense alterar
# la correcció del programa.

class Bird:
    """Una classe base per a ocells."""
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

# Dependency Inversion Principle
# Principi d'inversió de dependències

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
        self.device = device
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True

# Exemple d'ús
if __name__ == "__main__":
    bulb = LightBulb()
    switch = ElectricPowerSwitch(bulb)
    switch.press()
    switch.press()
