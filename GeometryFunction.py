import turtle

# Bienvenidos a Geometry FUN(ction)
# Hoy vamos a aprender el concepto de funciones mediante un juego basado en crear
# figuras geométricas con una tortuga.

def empezar_juego():
    ## En primer lugar vamos a crear una ventana para dibujar
    screen = turtle.Screen()
    screen.title("Geometry FUN(ction)")

    ## Podemos personalizar la propia pantalla con las funciones bgcolor(), 
    # screen.bgcolor("yellow")

    ## En segundo lugar vamos a crear y personalizar una tortuga
    ##Para crearla:
    tortuga = turtle.Turtle()
    ##Para personalizarla vamos a usar las FUNCIONES shape(), color(), pencolor(), pensize() y speed()
    # tortuga.shape("turtle")
    # tortuga.color("green")
    # tortuga.pencolor("orange")
    # tortuga.pensize(3)
    # tortuga.speed(1)


    ## Ahora que tenemos la tortuga lista, vamos a hacer que se mueva.
    ## Los movimientos básicos de la tortuga son representados por las siguientes funciones:
    ##  forward(n), con n = metros avanzados
    ##  backward(n), con n = metros retrocedidos
    ##  right(n), con n = grados del giro a la derecha
    ##  left(n), con n = grados del giro a la izquierda
    ##  circle(x,y), con x = radio del círculo, y = grados del giro (360 para giro completo)

    ## Para invocar a la función, escribimos tortuga.<nombre_función>

    ## NIVEL 1: hacer que la tortuga avance 75 metros

    
    ## NIVEL 2: hacer que la tortuga avance 75 metros, gire a la izquierda 90 grados y avance otros 75 metros


    ## NIVEL 3: hacer que la tortuga dibuje un cuadrado de 2500 metros cuadrados de área


    ## NIVEL 4: hacer que la tortuga dibuje un circulo de radio 60


    ## NIVEL 5: hacer que la tortuga dibuje un triángulo equilatero de perímetro 240 metros

    ##Aumentamos el nivel con 4 nuevas funciones
    ## penup, para levantar a la tortuga y hacer que no dibuje
    ## pendown, para bajar a la tortuga y hacer que dibuje
    ## home, para hacer que la tortuga vuelva al origen (coordenadas 0,0)
    ## goto(x,y), siendo x e y dos coordenadas de la pantalla.

    ## NIVEL BONO CON PREMIO


    turtle.Screen().exitonclick()

empezar_juego()