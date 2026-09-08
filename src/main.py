def get_user_input():
    try:
        name = input("Por favor, ingresa tu nombre: ")
        age = int(input("Por favor, ingresa tu edad: "))
        return name, age
    except ValueError:
        print("Error: La edad ingresada no es un número válido.")
        return None, None

def print_personalized_message(name, age):
    print(f"Hola {name}, tienes {age} años.")

if __name__ == "__main__":
    name, age = get_user_input()
    if name and age:
        print_personalized_message(name, age)