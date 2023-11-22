import turtle
import sys

# Mover la tortuga hacia delante
def move_forward():
    print("¿Cuántos metros quieres avanzar?")
    x = input()
    turtle.forward(x)
    print("La tortuga ha avanzado " + x + " metros")

# Mover la tortuga hacia atrás
def move_backward():
    print("¿Cuántos metros quieres retroceder?")
    x = input()
    turtle.backward(x)
    print("La tortuga ha retrocedido " + x + " metros")

# Girar la tortuga a la derecha
def move_right():
    print("¿Cuántos grados quieres girar a la derecha?")
    x = input()
    turtle.right(x)
    print("La tortuga ha girado " + x + " grados a la derecha")

# Girar la tortuga a la izquierda
def move_left():
    print("¿Cuántos grados quieres girar a la izquierda?") 
    x = input()
    turtle.left(x)
    print("La tortuga ha girado " + x + " grados a la izquierda")

# Levantar la tortuga
def move_penup():
    turtle.penup()
    print("La tortuga ha sido levantada, ya no dibujará")

# Bajar la tortuga
def move_pendown():
    turtle.pendown()
    print("La tortuga ha sido bajada, ahora dibujará")

# Dibujar un circulo
def move_circle():
    print("¿De cuanto quieres que sea el radio del circulo?")
    x = input()
    print("¿Cuántos grados quieres que gire la tortuga? (360 para un circulo completo))")
    y = input()
    turtle.circle(x,y)
    print("La tortuga ha dibujado un circulo de radio " + x + " y ha girado " + y + " grados")

# Resetear la tortuga
def reset():
    turtle.reset()
    print("La tortuga ha sido reseteada")



# Main del programa
def play_game():
    # Creamos una ventana para dibujar
    screen = turtle.Screen()
    screen.title("Geometric Fun(ction)")


    #Menú de inicio
    print("Bienvenido a Geometric Fun(ction)")
    print("En este juego deberás controlar una tortuga para dibujar figuras geométricas")

    acciones = "0. Salir\n1. Avanzar\n2. Retroceder\n3. Girar a la derecha\n4. Girar a la izquierda\n5. Levantar a la tortuga\n6. Bajar a la tortuga\n7. Dibujar un circulo\n8. Reset\n 9. Mostrar acciones disponibles\n"
    print("Las acciones disponibles para el jugador son: ")
    print(acciones)

    # Limpiamos la consola y la tortuga
    sys.clear()
    turtle.clear()

    action = -1
    while(action != "0"):
        print("¿Qué acción quieres realizar?")
        action = input()
        if action == "0":
            break
        elif action == "1":
            move_forward()
        elif action == "2":
            move_backward()
        elif action == "3":
            move_right()
        elif action == "4":
            move_left()
        elif action == "5":
            move_penup()
        elif action == "6":
            move_pendown()
        elif action == "7":
            move_circle()
        elif action == "8":
            reset()
        elif action == "9":
            print(acciones)
        else:
            print("Acción no válida")


    # Salir del juego
    print("Gracias por jugar a Geometric Fun(ction)")
    turtle.done()
    screen.exitonclick()

# Start the game
play_game()
