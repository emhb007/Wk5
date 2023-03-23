# Example of a user function with parameter passing
# and default values.
# say_hello(*,) => enforces named parameter passing.
# Annotations - preferred data types to be passed in (Not enforced).
#def say_hello(greeting:str="awrite", recipient:str="mates"):
def say_hello(greeting, recipient):
    message = f"Hello {greeting} {recipient}"
    print(message)
    return

say_hello("bonjour", "mes amis") # Positional parameter passing.
say_hello(greeting="hola", recipient="mi amigos") # Named parameter passing.
say_hello(recipient="mere yearon", greeting="namaste") # Named parameter passing (in different order)
say_hello("ciao", recipient="amici") # Mixed parameter passing (positional->named)
say_hello("Hello", "42")