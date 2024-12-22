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

# **3. Unimplemented Function**
# En lloc d'utilitzar `pass` per funcions sense implementar, utilitza `NotImplementedError` per indicar clarament
# que una funcionalitat està pendent.
def connect() -> None:
    """
    Placeholder for a database connection function.
    
    Raises a NotImplementedError indicating the function is not yet implemented.
    """
    raise NotImplementedError('connect() is missing code')

# Exemple d'ús:
try:
    connect()
except NotImplementedError as e:
    print(f"Error: {e}")

# **4. Specify Return Types**
# Aquesta funció retorna un diccionari d'usuaris, amb ID com a claus i noms com a valors.
# Especificar el tipus de retorn amb `-> dict[int, str]` millora la claredat i ajuda amb verificació estàtica.
def get_users() -> dict[int, str]: 
    """
    Retrieve a dictionary of users with their IDs and names.
    
    :return: A dictionary where keys are user IDs (int) and values are user names (str).
    :rtype: dict[int, str]
    
    :Example:
    >>> get_users()
    {1: 'Bob', 2: 'Jef', 3: 'Tom'}
    """
    users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Tom'}
    return users

# Exemple d'ús:
print("Users:", get_users())

# **5. Main Function**
# La funció `main` encapsula la lògica principal del programa.
def main() -> None:
    """
    Entry point of the program. Demonstrates usage of the above functions.
    """
    print("Demonstrating get_total_discount:")
    try:
        discounted_total = get_total_discount([1, 100, 40, 35], 0.5)
        print(f"Total after discount: {discounted_total}")
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nDemonstrating get_users:")
    print(get_users())

# **6. Execució principal**
# Aquest bloc controla si el fitxer s’executa directament o s'importa com a mòdul.
if __name__ == '__main__':
    main()
