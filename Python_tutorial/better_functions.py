# utilities_with_documentation.py

from datetime import datetime
from collections.abc import Iterable

# **1. Get the Current Time**
# Aquesta funció retorna l'hora actual de l'usuari en format local com una cadena de text.
def get_time() -> str:
    """
    Get the current local time as a formatted string.
    
    :return: The current time in the format HH:MM:SS
    :rtype: str
    
    :Example:
    >>> get_time()
    "07:24:02"
    """
    now: datetime = datetime.now()  # Obtenim l'hora actual
    return f'{now:%X}'  # Formatem com a hora local (HH:MM:SS)

# Exemple d'ús:
print("Current time:", get_time())

# **2. Calculate Total Discount**
# Aquesta funció calcula el preu total després d'aplicar un descompte.
def get_total_discount(prices: Iterable[float], percent: float) -> float:
    """
    Calculate the total price after applying a discount.
    
    This function calculates the total sum of prices in the provided list and applies
    a discount based on the given discount rate. If the discount rate is invalid 
    (e.g., negative or greater than 1), the function raises ValueError. 
    
    :param prices: A list of item prices
    :type prices: Iterable[float]
    :param percent: The discount rate to apply. Must be between 0 and 1 inclusive.
    :type percent: float
    :return: The total price after applying the discount
    :rtype: float
    
    :raises ValueError: If the discount rate or prices are invalid.
    
    :Example:
    >>> get_total_discount([100.0, 50.0, 25.0], 0.2)
    140.0
    """
    # **Validació d'entrades**
    if not (0 <= percent <= 1): 
        raise ValueError(f'Invalid discount rate: {percent}. Must be between 0 and 1 inclusive.')
    
    if not all(isinstance(price, (int, float)) and price >= 0 for price in prices):
        raise ValueError('All prices must be non-negative numbers.')

    total: float = sum(prices)  # Suma dels preus
    return total * (1 - percent)  # Aplicació del descompte

# **3. Main Function**
# La funció `main` encapsula el codi principal del programa.
# Permet executar la lògica principal sense que aquesta interfereixi si el fitxer
# s'importa en un altre script.
def main() -> None:
    """
    Entry point of the program. Demonstrates usage of the above functions.
    """
    try:
        # Exemple: calcular el descompte d'una llista de preus amb un 50% de descompte.
        discounted_total = get_total_discount([1, 100, 40, 35], 0.5)
        print(f"Total after discount: {discounted_total}")
    except ValueError as e:
        print(f"Error: {e}")

# **4. Execució principal**
# Aquest bloc controla si el fitxer s’executa directament o s'importa com a mòdul.
# - Si s’executa directament (`better_functions.py`), `__name__` serà `'__main__'`
#   i s'executarà la funció `main`.
# - Si s'importa des d'un altre fitxer, `__name__` NO serà `'__main__'` i aquest bloc no s'executarà.
if __name__ == '__main__':
    main()
