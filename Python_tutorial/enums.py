# Importem llibreries necessàries
from enum import Enum, Flag, auto

# Definició d'una enumeració bàsica amb Enum
# Les enumeracions (enums) s'utilitzen per definir un conjunt de valors fixos i coneguts.
class Color(Enum):
    RED: str = 'R'  # Color vermell
    GREEN: str = 'G'  # Color verd
    BLUE: str = 'B'  # Color blau

# Exemple d'ús d'aquesta enumeració
print(Color.RED)  # Sortida: Color.RED
print(repr(Color.RED))  # Representació interna: 'Color.RED'
print(Color.RED.value)  # Valor associat al color: 'R'

# Funcionalitat per crear cotxes segons el color
# Utilitzem "match" per avaluar el color triat i executar un bloc de codi corresponent.
def create_car(color: Color) -> None:
    match color:
        case Color.RED:
            print('Creating a red car')
        case Color.GREEN:
            print('Creating a green car')
        case Color.BLUE:
            print('Creating a blue car')
        case _:
            print(f'Creating a car with an unknown color {color}')

# Exemple d'ús de la funció
create_car(Color.RED)  # Sortida: "Creating a red car"

# Una altra forma de definir enums és amb Flag, que permet combinar valors mitjançant operadors binaris.
class Color2(Flag):
    RED: int = auto()  # Assignació automàtica de valors (1, 2, 4, ...)
    GREEN: int = auto()
    BLUE: int = auto()
    YELLOW: int = auto()
    BLACK: int = auto()
    ALL: int = RED | GREEN | BLUE | YELLOW | BLACK  # Combinació de tots els colors

# Exemple de combinació de colors
yellow_and_red: Color2 = Color2.YELLOW | Color2.RED
print(yellow_and_red)  # Sortida: Color2.YELLOW|Color2.RED

# Iterem per sobre dels colors combinats
for color in yellow_and_red:
    print(color)  # Sortida: Color2.YELLOW, Color2.RED

# Definim un conjunt de "colors frescos" i comprovem si un color hi pertany
cool_colors: Color2 = Color2.BLUE | Color2.GREEN | Color2.BLACK
my_car_color: Color2 = Color2.BLACK

if my_car_color in cool_colors:
    print('My car is cool!')
else:
    print('My car is not cool :(')

# Comprovem el valor combinat d'un conjunt de colors
combination: Color2 = Color2.RED | Color2.YELLOW
print(combination.value)  # Sortida: 9 (binari: 1001)

# Exemple amb un estat binari utilitzant Enum
class State(Enum):
    ON: int = 1  # Estat activat
    OFF: int = 0  # Estat desactivat

# Comprovació d'un interruptor segons el seu estat
switch: State = State.OFF

match switch:
    case State.ON:
        print('The switch is on')
    case State.OFF:
        print('The switch is off')
    case _:
        print('The switch is in an unknown state')
