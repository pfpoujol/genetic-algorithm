# Exemple d'utilisation :
Ajouter dans `main()` de main.py
```python
Generation(500, proportion_elu=0.9).find_master_race(proba_mutation=0.1)
```

# Réponse question 2: Dressez un bilan de l’impact de ces changements sur la rapidité d’exécution de l’algorithme.

A noter que le temps de génération de la génération initiale n'est pas comptabilisé ici.

| x | 500 individus | 2000 individus |
| --- | ------------ | ------------- |
| proportion_elu=90%, proba_mutation=10% | Found in 3.079 seconds, after 503 cycles. | Found in 3.897 seconds, after 80 cycles. |
| proportion_elu=50%, proba_mutation=50% | Found in 0.348 seconds, after 63 cycles. | Found in 1.202 seconds, after 34 cycles. |
| proportion_elu=10%, proba_mutation=90% | Found in 0.224 seconds, after 43 cycles. | Found in 0.529 seconds, after 22 cycles. |

Bilan : On constate que lorsque la population est plus élevée il y a moins de cycle, mais la durée pour retrouver la phrase secrète est plus élevé.
En revanche avec une petite proportion d'élu (phrases de la génération ayant un meilleur fitness) et un fort tôt de mutation, on obtient le nombre de cycles le plus faible et la durée la plus courte pour retrouver la phrase secrète.

Phrase secrète : "Omae wa mō shinde iru. NANI ?!!"

Bon choix de paramètre :
- Nombre d'individus : 500
- Proportion d'élu : 0,1
- Probabilité de mutation : 0,9

=> Phrase secrète retrouvé en 0.224 secondes.

PS : origine de la phrase secrète. : https://youtu.be/dNQs_Bef_V8
