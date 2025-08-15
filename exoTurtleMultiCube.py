"""
**Énoncé :**

On souhaite créer un programme en Python utilisant la bibliothèque **turtle** pour dessiner une série de cubes en perspective isométrique, chacun ayant trois faces colorées différemment.

1. Écrire une fonction `cube(taille, color_1, color_2, color_3)` qui :

   * Trace un cube en perspective avec **3 faces visibles**,
   * Remplit chaque face avec une couleur différente (`color_1`, `color_2`, `color_3`),
   * Utilise des angles précis (60° et 120°) pour créer l'effet isométrique.

2. Écrire une fonction `clone(ligne, coter, fin, bep)` qui :

   * Positionne la tortue à une coordonnée de départ,
   * Dessine **plusieurs cubes alignés** horizontalement,
   * Puis dessine une seconde ligne de cubes légèrement décalée pour donner un effet d'empilement.

3. Tester le programme en :

   * Fixant `coter = 100` et `ligne = 2`,
   * Utilisant les couleurs `"red"`, `"blue"`, `"black"` pour les faces,
   * Appelant deux fois `clone` pour dessiner deux rangées de cubes à des positions différentes.

**Objectif :**
Obtenir à l'écran un motif composé de plusieurs cubes isométriques, alignés en deux rangées, chacun avec des faces de couleurs différentes.
"""

import turtle

def cube(taille, color_1, color_2, color_3):
    """
    Dessine un cube isométrique avec 3 faces visibles colorées
    
    Args:
        taille (int): Taille du côté du cube
        color_1 (str): Couleur de la face avant
        color_2 (str): Couleur de la face droite  
        color_3 (str): Couleur de la face dessus
    """
    turtle.down()
    
    # Face avant (color_1)
    turtle.color(color_1)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(taille)
        turtle.right(120)
        turtle.forward(taille)
        turtle.right(60)
    turtle.end_fill()
    
    # Face droite (color_2)
    turtle.color(color_2)
    turtle.begin_fill()
    turtle.forward(taille)
    turtle.left(120)
    turtle.forward(taille)
    turtle.left(60)
    turtle.forward(taille)
    turtle.left(120)
    turtle.forward(taille)
    turtle.end_fill()
    
    # Face dessus (color_3)
    turtle.color(color_3)
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(taille)
    turtle.right(120)
    turtle.forward(taille)
    turtle.right(60)
    turtle.forward(taille)
    turtle.right(120)
    turtle.forward(taille)
    turtle.end_fill()
    
    # Repositionner pour le cube suivant
    turtle.left(60)
    turtle.up()

def clone(ligne, coter, x_start, y_start):
    """
    Dessine plusieurs rangées de cubes
    
    Args:
        ligne (int): Nombre de cubes par ligne
        coter (int): Taille des cubes
        x_start (int): Position X de départ
        y_start (int): Position Y de départ
    """
    # Première rangée
    turtle.goto(x_start, y_start)
    for i in range(ligne):
        cube(coter, "red", "blue", "black")
        turtle.forward(coter * 1.5)  # Espacement entre cubes
    
    # Deuxième rangée décalée
    turtle.goto(x_start + coter/2, y_start + coter * 0.87)
    for i in range(ligne):
        cube(coter, "red", "blue", "black")
        turtle.forward(coter * 1.5)

def main():
    """Fonction principale pour exécuter le programme"""
    try:
        # Configuration de la fenêtre
        turtle.setup(800, 600)
        turtle.title("Cubes Isométriques")
        turtle.speed(5)
        
        # Paramètres
        coter = 100
        ligne = 2
        
        # Dessiner les cubes
        clone(ligne, coter, -200, -100)
        clone(ligne, coter, -200, 75)
        
        # Finaliser
        turtle.hideturtle()
        turtle.exitonclick()
        
    except Exception as e:
        print(f"Erreur lors de l'exécution: {e}")
        turtle.bye()

if __name__ == "__main__":
    main()
