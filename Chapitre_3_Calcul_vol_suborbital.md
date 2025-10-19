# Chapitre 3 : Le calcul du vol suborbital

## 3.1 Le cas Alan Shepard : un vol parabolique

### Le contexte historique (mai 1961)

Le 5 mai 1961, à 9h34 du matin, Alan Shepard devint le premier américain dans l'espace. Son vol à bord de Freedom 7 dura 15 minutes et 28 secondes. Il monta jusqu'à une altitude de 116 km et redescendit en parachute dans l'Atlantique.

Ce n'était **pas une orbite**. C'était un vol **suborbital** — une trajectoire balistique simple qui montait et retombait. Mais c'était un test crucial pour les nouvelles technologies spatiales américaines.

Et **Katherine Johnson** fut responsable de calculer la trajectoire.

### Modélisation de la trajectoire

#### De l'ascension au point culminant

Le vol de Shepard peut être divisé en trois phases :

**Phase 1 : Propulsion** (0-2 minutes)
- Le moteur Redstone accélère la capsule verticalement
- L'accélération n'est pas constante mais suit une courbe décrite par les ingénieurs
- À 2 minutes environ, le moteur s'éteint à une altitude d'environ 62 km

**Phase 2 : Ascension balistique** (2-4 minutes)
- La capsule continue à monter sous l'inertie seule
- La gravité la ralentit progressivement
- Elle atteint son point culminant à ~116 km

**Phase 3 : Descente** (4-15 minutes)
- Retombée libre avec redirection de la capsule
- Entrée dans la denser atmosphère inférieure
- Déploiement du parachute
- Descente jusqu'à amerrissage

#### Les équations du mouvement

Pendant les phases d'ascension balistique et de descente (après extinction du moteur), le mouvement obéit à une équation très simple : la **deuxième loi de Newton** en une dimension avec la gravité comme unique force.

En prenant \(z\) comme la hauteur (distance de la surface terrestre), et en ignorant la résistance de l'air pour l'instant :

\[
\frac{d^2z}{dt^2} = -g
\]

Où \(g\) est l'accélération due à la gravité, environ \(9.81 \text{ m/s}^2\) près de la surface, mais qui diminue avec l'altitude :

\[
g(z) = \frac{GM}{(R + z)^2}
\]

Où \(R\) est le rayon terrestre (\(6371\) km).

À l'altitude de Shepard (116 km), la variation de \(g\) n'était pas négligeable, mais on pouvait l'approcher comme constante pour un calcul rapide :

\[
g(116 \text{ km}) \approx 0.966 \, g_0 \approx 9.47 \text{ m/s}^2
\]

#### Influence de la gravité terrestre

Un point subtil mais important : la Terre **n'est pas un point**. Elle a une étendue, et la gravité varie avec l'altitude.

De plus, pendant les 15 minutes du vol, la Terre continue de tourner. Un point qui était sous le spacecraft à 0 minute n'était plus le même point à 15 minutes, car la Terre avait tourné d'environ 3,8 degrés sur son axe.

Katherine Johnson devait tenir compte de :

1. **La variation de g avec l'altitude** : mesurable et correcte, en utilisant la formule inverse du carré de la distance
2. **La rotation terrestre** : elle affectait la localisation du point d'amarrissage prévu
3. **Le profil d'accélération du moteur** : pas constant, mais variant selon le temps
4. **Les conditions atmosphériques** : la densité de l'air, qui affecte la trajectoire

> **Note historique** : Katherine Johnson n'utilisait pas d'ordinateur pour ces calculs. Elle utilisait une calculatrice mécanique et des logarithmes imprimés. Pour chaque équation à résoudre, elle déterminait la meilleure approche numérique, puis effectuait les calculs étape par étape.

### 3.2 Les équations différentielles du mouvement

#### Application de F = ma en 3D

Pour une trajectoire complète, nous ne pouvons pas simplement considérer la dimension verticale. Nous devons considérer trois dimensions :

\[
\vec{F} = m\vec{g}(\vec{r})
\]

En trois dimensions cartésiennes :

\[
\begin{align}
\frac{d^2x}{dt^2} &= -\frac{GM}{r^3} x + a_x(\text{moteur}) \\
\frac{d^2y}{dt^2} &= -\frac{GM}{r^3} y + a_y(\text{moteur}) \\
\frac{d^2z}{dt^2} &= -\frac{GM}{r^3} z + a_z(\text{moteur})
\end{align}
\]

Où \(r = \sqrt{x^2 + y^2 + z^2}\) est la distance du centre terrestre, et \(a_x, a_y, a_z\) sont les composantes de l'accélération due au moteur (nulles après extinction).

#### Résolution numérique par méthodes manuelles

Il n'y a pas de solution analytique fermée à ce système d'équations différentielles couplées. Il faut utiliser une méthode numérique.

##### La méthode d'Euler

La méthode la plus simple est la **méthode d'Euler** :

**Étape 1 : Conditions initiales**
Nous commençons avec :
- Position initiale : \((x_0, y_0, z_0)\)
- Vitesse initiale : \((v_{x0}, v_{y0}, v_{z0})\)
- Temps initial : \(t_0 = 0\)

**Étape 2 : Calcul de l'accélération**
À chaque pas, nous devons calculer l'accélération actuelle :

\[
\vec{a}_n = -\frac{GM}{r_n^3} \vec{r}_n
\]

Où :
- \(r_n = \sqrt{x_n^2 + y_n^2 + z_n^2}\) est la distance au centre terrestre
- \(\vec{r}_n = (x_n, y_n, z_n)\) est le vecteur position
- \(GM = 3.986 \times 10^{14}\) m³/s² pour la Terre

**Étape 3 : Mise à jour de la vitesse**
La nouvelle vitesse est :

\[
v_{x,n+1} = v_{x,n} + a_{x,n} \Delta t
\]

\[
v_{y,n+1} = v_{y,n} + a_{y,n} \Delta t
\]

\[
v_{z,n+1} = v_{z,n} + a_{z,n} \Delta t
\]

**Pourquoi cette formule ?**
- La vitesse change proportionnellement à l'accélération
- \(\Delta t\) est petit, donc l'approximation linéaire est bonne
- Cette formule vient directement de l'intégration numérique : \(\frac{dv}{dt} \approx \frac{\Delta v}{\Delta t}\)

**Étape 4 : Mise à jour de la position**
La nouvelle position est :

\[
x_{n+1} = x_n + v_{x,n} \Delta t
\]

\[
y_{n+1} = y_n + v_{y,n} \Delta t
\]

\[
z_{n+1} = z_n + v_{z,n} \Delta t
\]

**Pourquoi cette formule ?**
- La position change proportionnellement à la vitesse
- Nous utilisons la vitesse au début de l'intervalle (\(v_n\)) pour calculer le déplacement
- Cette approximation est correcte au premier ordre

**Étape 5 : Incrémentation du temps**
\[
t_{n+1} = t_n + \Delta t
\]

**Étape 6 : Répétition**
Répéter les étapes 2-5 jusqu'à atteindre le temps final ou une condition d'arrêt (par exemple, amerrissage).

**Étape 7 : Choix du pas de temps**
Pour la mission Shepard, Katherine utilisait généralement :
- \(\Delta t = 1\) seconde pour les calculs préliminaires
- \(\Delta t = 0.1\) seconde près de l'apogée pour plus de précision
- \(\Delta t = 0.01\) seconde près de l'amerrissage

**Étape 8 : Gestion des erreurs**
- **Erreur locale** (par pas) : proportionnelle à \((\Delta t)^2\)
- **Erreur globale** : proportionnelle à \(\Delta t\)
- Pour 900 pas avec \(\Delta t = 1\) s : erreur globale acceptable pour les calculs préliminaires

**Exemple concret pour Shepard :**
- Temps total : 15 minutes = 900 secondes
- Nombre d'itérations : 900 (avec \(\Delta t = 1\) s)
- Calculs par itération : 6 additions + 1 calcul de distance + 1 calcul d'accélération
- Total : environ 900 × 8 = 7200 opérations arithmétiques de base

**Limites de la méthode :** L'erreur s'accumule, donc pour des simulations très précises, on utilise des méthodes plus sophistiquées (Runge-Kutta).

##### Corrections et itérations

Les méthodes numériques simples accumulent des erreurs. Pour cette raison, Katherine Johnson devait :

1. Effectuer les calculs avec des pas de temps petits
2. Vérifier les résultats par une deuxième méthode ou une approche différente
3. Estimer les erreurs d'arrondi et ajuster en conséquence
4. Recommencer si les résultats ne convergeaient pas vers une solution acceptable

### 3.3 L'art de vérifier sans ordinateur

#### Les sources d'erreur

Même avec une calculatrice mécanique, les sources d'erreur étaient nombreuses :

1. **Erreurs d'arrondi** : chaque calcul n'était précis que jusqu'à 8-10 chiffres significatifs
2. **Erreurs d'accumulation** : après 900 itérations, les petites erreurs s'ajoutaient
3. **Erreurs de transcription** : copier un nombre d'une ligne à l'autre pouvait introduire une erreur
4. **Erreurs conceptuelles** : utiliser la mauvaise formule ou la mauvaise valeur de paramètre

#### Les techniques de vérification

Katherine Johnson utilisait plusieurs techniques pour vérifier son travail :

**Vérification croisée** : Elle résolvait le même problème par deux méthodes différentes et vérifiait que les réponses convergeaient.

**Vérification de cohérence physique** : Elle vérifiait que les résultats avaient du sens. Par exemple, l'altitude maximale devrait être positive et inférieure à 200 km. La vitesse à l'amerrissage devrait être positive. La durée du vol devrait être comprise entre 10 et 20 minutes.

**Vérification des ordres de grandeur** : Elle estimait l'ordre de grandeur attendu et vérifiait que la réponse était raisonnablement proche.

**Comparaison avec les données expérimentales** : Pour les vols précédents (comme les tests sans équipage), elle comparait ses prédictions théoriques avec les observations réelles.

#### Le facteur humain

Un aspect souvent oublié : Katherine Johnson était **excellente en communication** de ses résultats. Elle ne fournissait pas simplement un nombre. Elle expliquait :

- Comment elle avait obtenu le résultat
- Quelles hypothèses elle avait faites
- Quelles étaient les sources d'incertitude
- Quels étaient les facteurs de risque

Cela faisait que les ingénieurs et les astronautes lui faisaient confiance. Quand Katherine disait que la trajectoire était bonne, elle était **vraiment** bonne.

## 3.4 Références Croisées

- **Chapitre 1** : Katherine commence sa carrière avec ces calculs simples
- **Chapitre 2** : Utilise les lois de Kepler pour prédire la trajectoire parabolique
- **Chapitre 5** : Contraste avec la complexité des orbites (Glenn vs Shepard)
- **Chapitre 7** : Extension aux rentrées atmosphériques complexes
- **Chapitre 8** : Katherine utilise des outils rudimentaires pour ces calculs
- **Annexes B.1** : Données détaillées de la mission Shepard

### Résumé du Chapitre 3

- Le vol suborbital de Shepard était une trajectoire balistique simple, mais son calcul précis était crucial
- Les équations différentielles du mouvement 3D n'ont pas de solution analytique fermée
- Des méthodes numériques itératives (comme la méthode d'Euler) doivent être utilisées
- Katherine Johnson effectuait ces calculs à la main, accumulation d'une rigueur remarquable
- La vérification était aussi importante que le calcul lui-même

---

**Lectures complémentaires** :
- NASA archives sur Freedom 7
- Technique d'intégration numérique en analyse classique

*"Chaque chiffre comptait. Littéralement. Un arrondi incorrect pouvait tuer quelqu'un." — Katherine Johnson*
