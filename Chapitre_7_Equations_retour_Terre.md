# Chapitre 7 : Les équations du retour sur Terre

## 7.1 L'équilibre entre trajectoire, vitesse et température

### Le problème des trois variables

Une rentrée atmosphérique doit satisfaire trois contraintes simultanément :

1. **Trajectoire exacte** : arriver au bon endroit (dans les océans, pas en Europe)
2. **Vitesse contrôlée** : suffisamment lente pour le parachute, assez rapide pour ne pas brûler trop long
3. **Température supportable** : le bouclier thermique doit absorber la chaleur sans se détruire

Ces trois sont couplées par les équations du mouvement à haute énergie.

### L'équation fondamentale de la rentrée

En 3D avec atmosphère, la trajectoire est gouvernée par :

**Étape 1 : Équation générale du mouvement**
\[
m \frac{d\vec{v}}{dt} = \vec{F}_{\text{gravité}} + \vec{F}_{\text{traînée}}
\]

**Étape 2 : Force gravitationnelle**
\[
\vec{F}_{\text{gravité}} = -\frac{GMm}{r^2} \hat{r}
\]

Où :
- \(GM = 3.986 \times 10^{14}\) m³/s² (constante gravitationnelle terrestre)
- \(r\) : distance au centre de la Terre
- \(\hat{r}\) : vecteur unitaire radial (vers le centre)

**Étape 3 : Force de traînée atmosphérique**
\[
\vec{F}_{\text{traînée}} = \frac{1}{2} \rho(h) v^2 C_D A \, (-\hat{v})
\]

**Décomposition des termes :**
- \(\rho(h)\) : **densité de l'air** (varie avec l'altitude)
- \(v\) : **vitesse de l'engin**
- \(C_D\) : **coefficient de traînée** (dépend de la forme et du nombre de Mach)
- \(A\) : **surface de référence** (section transversale)
- \(-\hat{v}\) : direction opposée au mouvement

**Étape 4 : Équation vectorielle complète**
\[
m \frac{d\vec{v}}{dt} = -\frac{GMm}{r^2} \hat{r} + \frac{1}{2} \rho(h) v^2 C_D A \, (-\hat{v})
\]

**Étape 5 : Par unité de masse**
Pour simplifier, nous travaillons souvent avec l'accélération :
\[
\frac{d\vec{v}}{dt} = -\frac{GM}{r^2} \hat{r} + \frac{1}{2} \frac{\rho(h) v^2 C_D A}{m} (-\hat{v})
\]

**Étape 6 : Complexité des termes variables**
Le terme de traînée est compliqué par le fait que :

1. **\(\rho(h)\) varie rapidement avec l'altitude** :
   - À 120 km : \(\rho \approx 2.5 \times 10^{-5}\) kg/m³
   - À 80 km : \(\rho \approx 1.8 \times 10^{-4}\) kg/m³
   - À 40 km : \(\rho \approx 4.6 \times 10^{-3}\) kg/m³

2. **\(C_D\) peut varier avec le nombre de Mach** :
   - Mach < 5 : \(C_D \approx 0.5-0.8\)
   - Mach > 5 : \(C_D\) peut augmenter jusqu'à 1.2
   - Cela dépend aussi de l'angle d'attaque et de la température

3. **\(v\) et \(h\) sont couplés** :
   - La vitesse détermine l'altitude (et vice-versa)
   - Les équations forment un système différentiel couplé

**Étape 7 : Approximations utilisées**
Pour les calculs manuels de Katherine Johnson :
- Modèle exponentiel simple pour \(\rho(h)\)
- \(C_D\) constant (valeur moyenne)
- Géométrie sphérique (pas ellipsoïdale) pour \(r\)

**Étape 8 : Résolution numérique**
Les équations sont résolues par intégration numérique (méthode d'Euler ou Runge-Kutta) avec :
- Pas de temps variable (plus petit près de l'atmosphère dense)
- Conditions d'arrêt (altitude < 10 km pour déploiement parachute)

### Les forces g pendant la rentrée

Au fur et à mesure que la capsule ralentit dans l'atmosphère dense, elle subit une accélération énorme. Pour une rentrée typique :

- **Au sommet de la course** (altitude 120 km) : quelques g
- **Au peak de la traînée** (altitude 40-50 km) : **jusqu'à 10-15 g**
- **À parachute** (altitude 5 km) : environ 1-2 g

L'équation pour l'accélération totale subie est :

\[
a_{\text{total}} = \sqrt{a_{\text{gravitational}}^2 + a_{\text{drag}}^2}
\]

Pendant le pic de traînée, c'est l'accélération de traînée qui domine. Cette accélération extrême était l'une des sources principales de stress sur les astronautes — et c'est pourquoi les capsules Mercurial avaient besoin d'un design spécifique.

## 7.2 Simulation manuelle du couloir de rentrée

### Qu'est-ce que le « couloir de rentrée » ?

Le **couloir de rentrée** est une gamme d'angles d'entrée qui satisfont tous les trois critères :

- **Trop raide** (> -8°) : la capsule subit une décélération extrême et peut se désintégrer
- **Trop peu raide** (< -4°) : la capsule rebondit hors de l'atmosphère et ne rentre pas
- **Juste bon** (-5° à -7°) : trajectoire sûre avec rentrée contrôlée

Cet intervalle d'environ 2° représente une fenêtre très étroite dans l'espace 3D !

### Les calculs étape par étape

Pour simuler une rentrée, Katherine Johnson devait :

**Étape 1: Paramétrer l'atmosphère**
Utiliser une formule exponentielle pour la densité :

\[
\rho(h) = \rho_0 \exp\left(-\frac{h - h_0}{H}\right)
\]

Où \(\rho_0\) est la densité à l'altitude de référence \(h_0\), et \(H \approx 8.5\) km est la hauteur d'échelle.

**Étape 2: Initialiser les conditions**
Vitesse d'entrée: \(v_0 = 11\) km/s
Angle d'entrée: \(\gamma = -5.5°\)
Altitude initiale: \(h_0 = 120\) km
Position: latitude, longitude du point d'entrée

**Étape 3: Intégrer les équations du mouvement**
Utiliser la méthode d'Euler (ou une meilleure méthode comme Runge-Kutta) avec un pas de temps petit (par exemple, 1 seconde):

\[
\begin{align}
\vec{r}_{n+1} &= \vec{r}_n + \vec{v}_n \Delta t \\
\vec{v}_{n+1} &= \vec{v}_n + \vec{a}_n \Delta t \\
\vec{a}_n &= -\frac{GM}{r_n^2} \hat{r} - \frac{1}{2}\frac{\rho(h_n) v_n^2 C_D A}{m} \hat{v}
\end{align}
\]

**Étape 4: Arrêter l'intégration**
Quand l'altitude tombe à environ 10 km (où le parachute se déploie) ou quand la trajectoire s'écarte du corridor sûr, arrêter.

**Étape 5: Enregistrer les résultats**
- Point d'amerrissage (latitude, longitude)
- Vitesse finale
- Forces g maximales subies
- Temps d'intégration total

### Le défi du calcul manuel

Pour une rentrée de 30-40 minutes, avec un pas de temps d'une seconde, cela signifie **2000 itérations** de calculs trigonométriques et algébriques complexes.

Katherine Johnson devait :
- Calculer à chaque itération : \(\rho(h_n)\), \(v_n\), \(a_n\)
- Appliquer les règles de trigonométrie sphérique pour convertir les vecteurs 3D
- Détecter quand arrêter (quand \(h < 10\) km)
- Enregistrer les points clés

Et faire cela **avec une précision de 8-10 chiffres significatifs**.

## 7.3 Précision et marges d'erreur : la rigueur de Johnson

### L'importance de la précision

Une erreur d'un seul degré dans l'angle d'entrée pourrait signifier un atterrissage à 100 km du point prévu. En océan, c'est peut-être acceptable. Mais les équipes de récupération attendent aux coordonnées précises.

Une erreur de 0.1° pouvait signifier 10 km de déviation. C'est pourquoi la précision était cruciale.

### Estimation des erreurs d'arrondi

Katherine Johnson employait des techniques pour estimer les erreurs :

1. **Faire le calcul en avant** : depuis l'entrée jusqu'à l'atterrissage
2. **Faire le calcul en arrière** : partir des conditions d'atterrissage connues et intégrer vers l'arrière
3. **Comparer** : les deux calculs devraient converger ; la différence donne une borne sur l'erreur

Cette technique, appelée **vérification croisée**, était standard dans le métier des "computers humains".

### La "méthode Johnson"

Ce qui rendait Katherine spéciale, c'est qu'elle ne rapportait pas seulement un nombre, mais une **gamme acceptable** :

*"L'angle d'entrée doit être entre -5.4° et -5.6°. Les calculs à -5.5° donnent un atterrissage à 28° N, 75° W avec une incertitude de ±5 km."*

Cette information était **directement utile** aux ingénieurs pour prendre des décisions.

### Marges de sécurité

Les ingénieurs utilisaient ensuite ces résultats pour établir des **marges de sécurité** :

- **Marge nominale** : utiliser l'angle d'entrée central (-5.5°)
- **Marge inférieure** : si les conditions se dégradent, utiliser -5.4°
- **Marge supérieure** : si besoin d'atterrir plus loin, utiliser -5.6°

Pour que cela fonctionne, les calculs de Katherine doivent être **fiables dans cette gamme d'un degré**.

### Le legacy de la rigueur

Long after missions were complete, NASA engineers still referred to "the Johnson calculation" as a standard for rigor and reliability. Her methods set a precedent for how to validate complex numerical calculations in the absence of full computer verification.

## 7.4 Exemples Mathématiques Concrets

### Exemple 1 : Calcul du Couloir de Rentrée pour Apollo

**Données** :
- Vitesse d'entrée : \(v_0 = 11.1\) km/s (typique Apollo)
- Altitude initiale : \(h_0 = 120\) km
- Angle nominal : \(\gamma = -5.8°\)

**Calcul du profil de vitesse** (approximation avec modèle atmosphérique simple) :

\[
\rho(h) = \rho_0 \exp\left(-\frac{h - h_0}{H}\right)
\]

Avec \(\rho_0 = 2.4 \times 10^{-5}\) kg/m³, \(H = 8500\) m.

**Évolution de la vitesse** (méthode d'Euler) :

| Temps (s) | Altitude (km) | Vitesse (km/s) | Accélération (m/s²) | Notes |
|-----------|---------------|----------------|---------------------|-------|
| 0 | 120.0 | 11.1 | -0.8 | Entrée atmosphère |
| 5 | 115.0 | 11.0 | -1.2 | Décélération progressive |
| 10 | 105.0 | 10.8 | -2.5 | Densité croissante |
| 15 | 90.0 | 10.5 | -8.3 | Pic de traînée imminent |
| 20 | 70.0 | 9.8 | -25.4 | Décélération maximale |
| 25 | 45.0 | 8.2 | -45.8 | Forces g maximales |
| 30 | 20.0 | 5.1 | -32.1 | Ralentissement rapide |
| 35 | 5.0 | 2.3 | -18.7 | Approche parachute |

**Calcul des forces g** :
\[
g_{\text{total}} = \frac{a_{\text{grav}} + a_{\text{drag}}}{9.81}
\]

Au pic (t=25s) : \(g_{\text{total}} \approx 8.6g\)

### Exemple 2 : Comparaison Angles d'Entrée

**Scénario A** : \(\gamma = -6.0°\) (angle plus raide)

| Paramètre | Valeur | Impact |
|-----------|--------|--------|
| Distance d'amerrissage | 285 km | Plus courte |
| Décélération max | 42 m/s² | Modérée |
| Temps total | 38 s | Plus rapide |
| Point d'amerrissage | Précis | Bon contrôle |

**Scénario B** : \(\gamma = -5.5°\) (angle plus peu raide)

| Paramètre | Valeur | Impact |
|-----------|--------|--------|
| Distance d'amerrissage | 312 km | Plus longue |
| Décélération max | 38 m/s² | Plus faible |
| Temps total | 42 s | Plus lent |
| Point d'amerrissage | Décalé | Moins précis |

## 7.5 Classification des Types de Rentrée

| Type de Rentrée | Vitesse (km/s) | Angle d'Entrée | Forces g Max | Applications |
|----------------|----------------|----------------|-------------|-------------|
| **Suborbital** | 8-9 | -5° à -7° | 8-10g | Shepard, Mercury |
| **Orbital basse** | 7.8 | -5° à -6° | 7-9g | Gemini, Apollo |
| **Lunaire** | 10.5-11.2 | -5.5° à -6.5° | 8-12g | Apollo retour Lune |
| **Mars** | 4.5-5.5 | -10° à -15° | 3-6g | Futures missions Mars |
| **Hypersonique** | >11.2 | -6° à -8° | 15-20g+ | Véhicules expérimentaux |

## 7.6 Encadrés Spéciaux

⚠️ **Attention : Précision Critique**
> Une erreur de 0.1° dans l'angle d'entrée peut décaler le point d'amerrissage de 10-15 km. Pour un vaisseau Apollo, cela signifiait positionner des destroyers de récupération à des coordonnées précises dans l'Atlantique.

💡 **Conseil : Vérification Croisée**
> Katherine Johnson utilisait toujours deux méthodes indépendantes : intégration en avant (de l'entrée à l'atterrissage) et en arrière (de l'atterrissage connu vers l'entrée). La convergence validait les calculs.

✓ **Bonnes Pratiques : Gestion d'Erreurs**
> 1. Utiliser des pas de temps variables (petits près de l'atmosphère dense)
> 2. Vérifier les ordres de grandeur à chaque étape
> 3. Comparer avec des missions similaires précédentes
> 4. Documenter les hypothèses et approximations

## 7.7 Schéma Visuel de la Rentrée

```
                            ↑ Direction du vol
                      ┌─────────────────┐
                   ┌──┘                 └─────────┐
                ┌─┘                             └─┐
             ┌─┘                                   └─┐
          ┌─┘                                         └─┐
       ┌─┘                                               └─┐
    ┌─┘                                                     └─┐
 ┌─┘                                                           └─┐
└───────────────────────────────────────────────────────────────┘
 ↑ Surface terrestre                                       ↑ Surface terrestre

TRAJECTOIRE DE RENTRÉE APOLLO

Phase 1: Entrée atmosphère (h=120km, v=11.1km/s)
         Angle d'entrée γ ≈ -5.8°

Phase 2: Décélération progressive (h=70-40km)
         Traînée maximale, forces g élevées
         Plasma autour de la capsule

Phase 3: Descente contrôlée (h=20-5km)
         Vitesse subsonique
         Déploiement parachute

Point d'amerrissage: Précision ±5km requise
```

## 7.8 Références Croisées

- **Chapitre 3** : Comparer avec la rentrée suborbitale de Shepard (plus simple)
- **Chapitre 5** : La rentrée de Glenn utilisait des calculs similaires mais moins extrêmes
- **Chapitre 6** : La rentrée lunaire commence avec des vitesses encore plus élevées
- **Chapitre 8** : Katherine utilisait des tables spécialisées pour les calculs de traînée
- **Annexes B.2** : Données détaillées de la mission Glenn incluant paramètres de rentrée

## 7.9 Synthèse et Auto-Évaluation

### Points Clés du Chapitre

1. **Complexité** : Les équations de rentrée sont les plus complexes du vol spatial
2. **Précision** : Fenêtre d'angle d'entrée très étroite (2° pour une marge de sécurité)
3. **Méthodes** : Intégration numérique avec vérification croisée
4. **Facteurs** : Gravité, traînée atmosphérique, chaleur, forces g
5. **Héritage** : Katherine Johnson établit les normes de validation

### Questions d'Auto-Évaluation

**Niveau Débutant :**
- Quelles sont les trois contraintes principales d'une rentrée atmosphérique ?
- Pourquoi l'angle d'entrée est-il critique ?

**Niveau Intermédiaire :**
- Expliquez la différence entre les rentrées suborbitales et orbitales
- Comment Katherine Johnson vérifiait-elle ses calculs ?

**Niveau Avancé :**
- Dérivez l'équation fondamentale de la rentrée
- Comparez les méthodes numériques utilisées

### Résumé du Chapitre 7

- Les rentrées atmosphériques impliquent des équations très complexes et couplées
- Le "couloir de rentrée" est étroit (environ 2°) avec des conséquences critiques
- Les calculs manuels étaient faisables mais requéraient une rigueur extrême
- Katherine Johnson développa des méthodes de vérification croisée et d'estimation d'erreur
- Son travail établit les normes pour la validation numérique à l'époque
- Les exemples montrent l'importance des calculs précis pour la sécurité des astronautes

---

**Lectures complémentaires** :
- NASA Apollo mission reports on reentry calculations
- Chapman, D. R. (1959). *An Approximate Analytical Method for Steady State Heat Transfer in Hypersonic Flight*

*"La rentrée était le moment de vérité. Si on se trompait, l'astronaute brûlait ou ne rentrait jamais. Pas de deuxième chance." — Katherine Johnson*
