"""
**Énoncé :**

On dispose de différents billets et pièces pour payer un montant donné.
Les valeurs sont stockées dans une liste `billet` où :

* `billet[0]` représente **le montant à payer**.
* Les autres éléments de la liste représentent la valeur totale disponible pour chaque type de billet/pièce :

  * `billet[1]` : total en billets de 20 €
  * `billet[2]` : total en billets de 10 €
  * `billet[3]` : total en billets de 5 €
  * `billet[4]` : total en pièces de 2 €
  * `billet[5]` : total en pièces de 1 €

**Tâches :**

1. Calculer la somme totale d'argent disponible à partir des billets/pièces.
2. Comparer cette somme avec le montant à payer (`billet[0]`).
3. Si la somme disponible est **inférieure** au montant demandé → afficher `(None, None, None, None, None)`.
4. Si la somme disponible est **exactement égale** au montant demandé → afficher `(0, 0, 0, 0, 0)`.
5. Sinon, afficher la **monnaie à rendre** (somme disponible - montant demandé).
"""

def calculer_monnaie(billet):
    """
    Calcule la monnaie à rendre ou vérifie si le paiement est possible
    
    Args:
        billet (list): [montant_à_payer, billets_20, billets_10, billets_5, pieces_2, pieces_1]
    
    Returns:
        tuple ou int: Résultat selon les cas
    """
    montant_a_payer = billet[0]
    somme_disponible = sum(billet[1:])
    
    if somme_disponible < montant_a_payer:
        return (None, None, None, None, None)
    elif somme_disponible == montant_a_payer:
        return (0, 0, 0, 0, 0)
    else:
        return somme_disponible - montant_a_payer

# Test de l'exercice
if __name__ == "__main__":
    # Test avec les valeurs de l'exemple
    billet = [56, 5*20, 0*10, 0*5, 0*2, 0*1]
    resultat = calculer_monnaie(billet)
    print(f"Montant à payer: {billet[0]}€")
    print(f"Somme disponible: {sum(billet[1:])}€")
    print(f"Résultat: {resultat}")
