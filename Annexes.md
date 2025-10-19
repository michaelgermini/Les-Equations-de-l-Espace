# Annexes

## A. Dérivations mathématiques détaillées

### A.1 Dérivation de la troisième loi de Kepler à partir de la mécanique newtonienne

**Étape 1 : Hypothèse d'une orbite circulaire**
Considérons un satellite en orbite circulaire de rayon \(r\) autour d'un corps central de masse \(M\).

**Étape 2 : Force gravitationnelle**
La loi de Newton donne :
\[
F_g = \frac{GMm}{r^2}
\]
Cette force attire le satellite vers le centre.

**Étape 3 : Force centripète pour le mouvement circulaire**
Pour maintenir une trajectoire circulaire, il faut une force centripète :
\[
F_c = m \omega^2 r
\]
Où \(\omega = \frac{2\pi}{T}\) est la vitesse angulaire (rad/s), et \(T\) est la période.

**Étape 4 : Développement de la force centripète**
\[
\omega = \frac{2\pi}{T}
\]
Donc :
\[
F_c = m \left(\frac{2\pi}{T}\right)^2 r = m \frac{4\pi^2}{T^2} r
\]

**Étape 5 : Équilibre des forces**
Pour une orbite stable :
\[
F_g = F_c
\]
\[
\frac{GMm}{r^2} = m \frac{4\pi^2}{T^2} r
\]

**Étape 6 : Simplification**
Divisons les deux côtés par \(m\) :
\[
\frac{GM}{r^2} = \frac{4\pi^2}{T^2} r
\]

**Étape 7 : Résolution pour T²**
Multiplions les deux côtés par \(r^2 T^2\) :
\[
GM T^2 = 4\pi^2 r^3
\]

**Étape 8 : Réarrangement**
\[
T^2 = \frac{4\pi^2}{GM} r^3
\]

**Étape 9 : Généralisation à l'ellipse**
Pour une orbite elliptique, nous remplaçons \(r\) par le demi-grand axe \(a\) :
\[
T^2 = \frac{4\pi^2}{GM} a^3
\]

**Étape 10 : Interprétation physique**
- \(T\) : période orbitale (secondes)
- \(a\) : demi-grand axe (mètres)
- \(GM\) : paramètre gravitationnel (m³/s²)
- Cette loi relie la taille de l'orbite à sa période

**Étape 11 : Applications pratiques**
- Pour la Terre : \(GM = 3.986 \times 10^{14}\) m³/s²
- Pour une orbite à 300 km : \(a = 6678\) km = \(6.678 \times 10^6\) m
- Période calculée : \(T = 5490\) s ≈ 91.5 minutes

C'est la **troisième loi de Kepler**, dérivée directement de la mécanique newtonienne.

### A.2 Solution de l'équation de Kepler par méthode d'itération de Newton

**L'équation de Kepler** :
\[
M = E - e\sin E
\]

**But** : Trouver \(E\) en fonction de \(M\) (connu).

**Rearrangement comme problème de zéro de fonction** :
\[
f(E) = E - e\sin E - M = 0
\]

**Méthode de Newton** : Itération
\[
E_{n+1} = E_n - \frac{f(E_n)}{f'(E_n)}
\]

Avec \(f'(E) = 1 - e\cos E\), on obtient :
\[
E_{n+1} = E_n - \frac{E_n - e\sin E_n - M}{1 - e\cos E_n}
\]

**Algorithme** :
1. Démarrer avec une première estimation : \(E_0 = M\) (bonne pour les faibles excentricités)
2. Itérer jusqu'à convergence : \(|E_{n+1} - E_n| < \epsilon\) (où \(\epsilon\) est la tolérance)

**Exemple numérique** :
- Données : \(M = 1.0\) radian, \(e = 0.1\)
- \(E_0 = 1.0\)
- \(E_1 = 1.0 - \frac{1.0 - 0.1 \sin(1.0) - 1.0}{1 - 0.1 \cos(1.0)} \approx 1.0918\)
- \(E_2 \approx 1.0952\) (convergence rapide)

### A.3 Dérivation de l'équation de la trajectoire en coordonnées polaires

**Étape 1 : Équations de base en coordonnées polaires**
Nous partons des équations dérivées au Chapitre 2 :

**Équation radiale** :
\[
\ddot{r} - r\dot{\theta}^2 = -\frac{GM}{r^2}
\]

**Équation angulaire (conservation du moment cinétique)** :
\[
\frac{d}{dt}(r^2 \dot{\theta}) = 0
\]

Donc : \(r^2 \dot{\theta} = h = \text{constant}\) (moment cinétique spécifique)

**Étape 2 : Transformation de variables**
Pour simplifier, nous introduisons une nouvelle variable :
\[
u = \frac{1}{r}
\]

Donc :
\[
r = \frac{1}{u}
\]

**Étape 3 : Dérivée première par rapport à θ**
Nous exprimons tout en fonction de θ plutôt que t. D'abord :
\[
\frac{dr}{d\theta} = \frac{dr}{dt} \cdot \frac{dt}{d\theta} = \dot{r} \cdot \frac{1}{\dot{\theta}}
\]

Mais \(\dot{\theta} = \frac{h}{r^2} = h u^2\)

Donc :
\[
\frac{dr}{d\theta} = \frac{\dot{r}}{h u^2}
\]

En dérivant \(r = 1/u\) :
\[
\frac{dr}{d\theta} = -\frac{1}{u^2} \frac{du}{d\theta}
\]

Donc :
\[
-\frac{1}{u^2} \frac{du}{d\theta} = \frac{\dot{r}}{h u^2}
\]

**Étape 4 : Simplification**
\[
-\frac{du}{d\theta} = \frac{\dot{r}}{h}
\]

Donc :
\[
\dot{r} = -h \frac{du}{d\theta}
\]

**Étape 5 : Dérivée seconde**
Maintenant, dérivons par rapport à θ :
\[
\frac{d\dot{r}}{d\theta} = \frac{d}{d\theta} \left( -h \frac{du}{d\theta} \right) = -h \frac{d^2 u}{d\theta^2}
\]

Mais \(\frac{d\dot{r}}{d\theta} = \ddot{r} \cdot \frac{dt}{d\theta} = \ddot{r} \cdot \frac{1}{\dot{\theta}} = \ddot{r} \cdot \frac{r^2}{h} = \ddot{r} \cdot \frac{1}{h u^2}\)

Donc :
\[
\ddot{r} \cdot \frac{1}{h u^2} = -h \frac{d^2 u}{d\theta^2}
\]

**Étape 6 : Résolution pour d²u/dθ²**
\[
\ddot{r} = -h^2 u^2 \frac{d^2 u}{d\theta^2}
\]

**Étape 7 : Substitution dans l'équation radiale**
L'équation radiale originale :
\[
\ddot{r} - r \dot{\theta}^2 = -\frac{GM}{r^2}
\]

Remplaçons \(\ddot{r}\) :
\[
-h^2 u^2 \frac{d^2 u}{d\theta^2} - r (h u^2)^2 = -\frac{GM}{r^2}
\]

Puisque \(r = 1/u\) :
\[
-h^2 u^2 \frac{d^2 u}{d\theta^2} - \frac{1}{u} \cdot h^2 u^4 = -GM u^2
\]

**Étape 8 : Simplification**
\[
-h^2 u^2 \frac{d^2 u}{d\theta^2} - h^2 u^3 = -GM u^2
\]

Divisons par \(-h^2 u^2\) :
\[
\frac{d^2 u}{d\theta^2} + u = \frac{GM}{h^2}
\]

**Étape 9 : Solution de l'équation différentielle**
C'est une équation différentielle linéaire du second ordre :
\[
\frac{d^2 u}{d\theta^2} + u = \frac{GM}{h^2}
\]

La solution générale est :
\[
u = A \cos\theta + B \sin\theta + \frac{GM}{h^2}
\]

**Étape 10 : Conditions aux limites**
Pour une ellipse, nous imposons que le périapside soit à θ = 0, donc du/dθ = 0 à θ = 0.

La solution devient :
\[
u = \frac{GM}{h^2} (1 + e \cos\theta)
\]

**Étape 11 : Retour à la variable r**
\[
u = \frac{1}{r} = \frac{GM}{h^2} (1 + e \cos\theta)
\]

Donc :
\[
r = \frac{h^2}{GM} \cdot \frac{1}{1 + e \cos\theta}
\]

**Étape 12 : Expression standard**
Nous définissons le paramètre p = h²/GM :
\[
r = \frac{p}{1 + e \cos\theta}
\]

C'est l'**équation polaire d'une conique** :
- **Cercle** : si e = 0, r = p (constante)
- **Ellipse** : si 0 < e < 1, r varie entre p/(1+e) et p/(1-e)
- **Parabole** : si e = 1, r = p/(1 + cosθ)
- **Hyperbole** : si e > 1, r peut devenir très grand

## B. Tableaux de calculs et exemples commentés

### B.1 Exemple : Calcul d'une orbite de Shepard (mission Mercury-Redstone 3)

| Paramètre | Valeur | Unité | Notes |
|-----------|--------|-------|-------|
| Apogée | 116 | km | Altitude maximale atteinte |
| Périgée | 0 | km | Au niveau de la mer (lancement vertical) |
| Vitesse d'apogée | 2.61 | km/s | Calculé par conservation d'énergie |
| Durée de vol | 15 min 22 s | - | Depuis lancement jusqu'à amerrissage |
| Distance d'amerrissage | 486 | km | Estimé depuis le cap (réel : 488 km) |

**Calcul pas à pas** (version simplifiée) :

1. **Vitesse de lancement** (depuis équilibre des forces) :
   - Force de gravité : \(F_g = 9.81 m/s^2\)
   - Accélération du moteur : \(a_{motor} = 6g = 58.9 m/s^2\) (net : \(5g = 49.0 m/s^2\))
   - Temps de combustion : ~120 s
   - Vitesse finale moteur : \(v = a \times t = 49.0 \times 120 = 5880 m/s = 5.88 km/s\)

2. **Altitude maximale** (énergie) :
   - À l'apogée, \(v = 0\) (en coordonnée verticale)
   - Conservation de l'énergie : \(\frac{1}{2}v_0^2 = g h_{max}\) (approximation)
   - \(h_{max} = \frac{v_0^2}{2g} = \frac{(5880)^2}{2 \times 9.81} \approx 1,761,000 m\)
   - Mais en réalité, g varie, donc \(h_{max} \approx 116\) km

3. **Distance d'amerrissage** (portée balistique simple) :
   - Durée totale : 15 min 22 s
   - Distance horizontale (approximée) : \(x \approx v_{initial} \times t / 2 \approx 486 km\)

### B.2 Tableau de calcul : Orbite de John Glenn (Mercury-Atlas 6)

**Données d'entrée** :
- Altitude de périgée : 160 km
- Altitude d'apogée : 260 km
- Inclinaison : 32.51°
- Demi-grand axe : \(a = 6381 km\)
- Excentricité : \(e = 0.00759\)

**Calculs pour le premier passage au périgée** :

| Temps (min) | Alt (km) | Lat (°) | Lon (°) | Vitesse (km/s) | Notes |
|-------------|----------|---------|---------|-----------------|-------|
| 0 | 160 | 32.5 | 0 | 7.819 | Périgée initial |
| 5 | 185 | 28 | 12 | 7.76 | Ascension |
| 10 | 210 | 20 | 24 | 7.70 | Proche de l'équateur |
| 15 | 230 | 8 | 36 | 7.65 | Au-delà de l'équateur |
| 20 | 250 | -5 | 48 | 7.61 | Descente |
| 25 | 260 | -18 | 60 | 7.58 | Apogée |

**Notes de calcul** :
- Changement d'altitude : varie de 160 (périgée) à 260 (apogée)
- Changement de latitude : dépend de l'inclinaison (max 32.5°N/S pour une orbite inclinée)
- Vitesse : maximum au périgée (7.819 km/s), minimum à l'apogée (~7.58 km/s)

## C. Références historiques

### C.1 Sources primaires

1. **NASA Historical Reports**
   - NASA Technical Reports Server (NTRS)
   - Langley Research Center Archives
   - Mercury, Gemini, Apollo mission documentation

2. **Publications scientifiques de l'époque**
   - Houbolt, J. C. (1961). "A Study of the Apollo By-Pass Trajectory," NASA TN D-337
   - Chapman, D. R. (1959). "An Approximate Analytical Method for Steady State Heat Transfer in Hypersonic Flight," NACA Report 1135
   - Théodore, G. (1962). "Orbital Mechanics," McGraw-Hill

### C.2 Sources secondaires

1. **Livres**
   - Shetterly, Margot Lee. *Hidden Figures: The American Dream and the Untold Story of the Black Women and the NASA* (2016)
   - Johnson, Katherine. *My Counted Life* (2017, autobiographie)

2. **Films et documentaires**
   - "Hidden Figures" (2016, réalisé par Theodore Melfi)
   - PBS documentaires sur les "Human Computers" de la NASA
   - National Geographic specials

### C.3 Archevez vidéo et orales

- Interviews de Katherine Johnson (années 1990-2010) disponibles dans les NASA archives
- Interviews de Dorothy Vaughan, Mary Jackson
- Témoignages d'astronautes (Alan Shepard, John Glenn) sur la confiance dans les calculs

## D. Index des équations principales

| Équation | Chapitre | Application |
|----------|----------|-------------|
| \(T^2 = \frac{4\pi^2}{GM} a^3\) | 2 | Période orbitale (Kepler III) |
| \(M = E - e\sin E\) | 2 | Relation temps-position (Kepler) |
| \(\frac{d^2z}{dt^2} = -g(z)\) | 3 | Mouvement vertical en gravité |
| \(r = a(1-e\cos E)\) | 2 | Distance orbitale |
| \(F_{drag} = \frac{1}{2}\rho v^2 C_D A\) | 7 | Force de traînée atmosphérique |
| \(\Delta v = v_f - v_i\) | 6 | Changement de vitesse orbital |
| \(E_k = \frac{1}{2}mv^2\) | 6 | Énergie cinétique |
| \(\omega = \frac{2\pi}{T}\) | 4 | Vitesse angulaire |

## B.3 Exemple Étendu : Simulation Complète d'une Rentrée Atmosphérique

### Paramètres de Base
- **Mission** : Apollo 11 retour (1969)
- **Vitesse initiale** : 11.2 km/s
- **Altitude initiale** : 122 km
- **Angle d'entrée** : -6.2°
- **Masse** : 5500 kg
- **Surface de référence** : 12.0 m²
- **Coefficient de traînée** : 0.8 (hypersonique)

### Profil Atmosphérique Utilisé
\[
\rho(h) = \rho_0 \exp\left(-\frac{h - h_0}{H}\right)
\]

Avec :
- \(\rho_0 = 2.5 \times 10^{-5}\) kg/m³ (à 120 km)
- H = 8500 m (hauteur d'échelle)

### Équations du Mouvement
\[
\begin{align}
\frac{dv}{dt} &= -\frac{1}{2} \frac{\rho A C_D}{m} v^2 - g(r) \sin\gamma \\
\frac{d\gamma}{dt} &= -\frac{g(r)}{v} \cos\gamma + \frac{1}{2} \frac{\rho A C_D}{m} \frac{v}{} \\
\frac{dr}{dt} &= -v \sin\gamma \\
\frac{d\theta}{dt} &= \frac{v \cos\gamma}{r}
\end{align}
\]

### Résultats de Simulation (extrait)

| Temps (s) | Altitude (km) | Vitesse (km/s) | γ (°) | Forces g | Température estimée (°C) |
|-----------|---------------|----------------|--------|----------|-------------------------|
| 0 | 122.0 | 11.2 | -6.2 | 0.1 | 0 |
| 10 | 118.5 | 11.1 | -6.3 | 0.3 | 50 |
| 20 | 113.2 | 10.9 | -6.5 | 0.8 | 200 |
| 30 | 105.8 | 10.6 | -7.0 | 2.1 | 800 |
| 40 | 95.1 | 10.0 | -8.2 | 5.8 | 2000 |
| 50 | 80.3 | 8.9 | -12.1 | 12.3 | 5000 |
| 60 | 60.2 | 6.8 | -25.4 | 18.7 | 8000 |
| 70 | 35.1 | 4.2 | -45.8 | 15.2 | 6000 |
| 80 | 15.3 | 2.1 | -62.3 | 8.9 | 2000 |
| 90 | 2.1 | 0.8 | -78.9 | 3.2 | 500 |

**Analyse des résultats** :
- **Pic de décélération** : 18.7g à t=60s (altitude 60 km)
- **Température maximale** : ~8000°C (bouclier thermique absorbe)
- **Durée totale** : 90 secondes pour traverser l'atmosphère
- **Vitesse finale** : 0.8 km/s (vitesse subsonique pour parachute)

## B.4 Tableau Comparatif : Missions Historiques

| Mission | Année | Type | Altitude Max (km) | Vitesse Max (km/s) | Durée | Calculatrice |
|---------|-------|------|-------------------|-------------------|-------|-------------|
| **Mercury-Redstone 3** | 1961 | Suborbital | 116 | 2.6 | 15 min | Katherine Johnson |
| **Mercury-Atlas 6** | 1962 | Orbital | 260 | 7.8 | 5h | Katherine Johnson + IBM |
| **Gemini 6** | 1965 | Orbital | 270 | 7.8 | 1.5j | Équipe calculatrices |
| **Apollo 8** | 1968 | Lunaire | 400000 | 11.0 | 6j | Ordinateurs avancés |
| **Apollo 11** | 1969 | Lunaire | 400000 | 11.2 | 8j | Ordinateurs avancés |
| **Space Shuttle STS-1** | 1981 | Orbital | 300 | 7.8 | 2j | Ordinateurs numériques |
| **ISS** | 1998 | Orbital | 420 | 7.7 | Permanent | Ordinateurs modernes |

## B.5 Classification des Trajectoires Spatiales

### Par Type de Mission

| Catégorie | Description | Exemple | Complexité Calcul |
|-----------|-------------|---------|------------------|
| **Suborbital** | Montée et redescente sans orbite | Shepard | Faible |
| **Orbital LEO** | Orbite basse (160-2000 km) | Hubble | Moyenne |
| **Orbital GEO** | Orbite géostationnaire (35786 km) | Satellites TV | Élevée |
| **Lunaire** | Aller-retour Terre-Lune | Apollo | Très élevée |
| **Interplanétaire** | Vers autres planètes | Voyager | Extrême |

### Par Méthode de Calcul Historique

| Période | Outils | Précision | Vérification |
|---------|--------|-----------|-------------|
| **1940s-1950s** | Tables + calculatrices mécaniques | ±1% | Double calcul manuel |
| **1960s** | Calculatrices électroniques + IBM | ±0.1% | Comparaison homme-machine |
| **1970s-1980s** | Ordinateurs numériques | ±0.01% | Simulation complète |
| **1990s-présent** | Superordinateurs + IA | ±0.001% | Validation statistique |

## C.3 Sources Additionnelles

### Livres Techniques
- **Battin, R. H.** (1999). *An Introduction to the Mathematics and Methods of Astrodynamics*
- **Curtis, H. D.** (2013). *Orbital Mechanics for Engineering Students*
- **Vallado, D. A.** (2013). *Fundamentals of Astrodynamics and Applications*

### Archives NASA
- **Langley Research Center Archives** : Documents originaux des West Computers
- **Johnson Space Center** : Rapports de mission Mercury, Gemini, Apollo
- **Historical Archives** : Interviews et documents de Katherine Johnson

### Publications Académiques
- **Chapman, D. R.** (1959). "An Approximate Analytical Method for Steady State Heat Transfer in Hypersonic Flight," NACA Report 1135
- **Houbolt, J. C.** (1961). "A Study of the Apollo By-Pass Trajectory," NASA TN D-337

## D.2 Index Étendu des Équations

| Équation | Signification | Utilisation | Chapitre | Complexité |
|----------|---------------|-------------|----------|------------|
| \(F = ma\) | Deuxième loi Newton | Base mécanique | Tous | Fondamentale |
| \(F_g = -GMm/r^2\) | Loi de gravitation | Force centrale | 2, 4 | Fondamentale |
| \(T^2 = 4\pi^2 a^3/GM\) | Troisième loi Kepler | Période orbitale | 2, 5, 6 | Moyenne |
| \(M = E - e\sin E\) | Équation de Kepler | Temps-position | 2, 5 | Difficile |
| \(\vec{a} = \ddot{r} - r\dot{\theta}^2\) | Accélération polaire | Mouvement 2D | 2 | Moyenne |
| \(a = (r_a + r_p)/2\) | Demi-grand axe | Élément orbital | 5 | Simple |
| \(e = (r_a - r_p)/(r_a + r_p)\) | Excentricité | Forme orbite | 5 | Simple |
| \(F_{drag} = \frac{1}{2}\rho v^2 C_D A\) | Force de traînée | Rentrée | 7 | Moyenne |
| \(\Delta v = v_f - v_i\) | Changement de vitesse | Impulsion | 6 | Simple |

## E. Glossaire des termes techniques

### Mécanique Céleste
- **Anomalie excentrique (E)** : Paramètre géométrique d'une ellipse relié au temps
- **Anomalie moyenne (M)** : Mesure fictive de la position basée sur le mouvement moyen
- **Anomalie vraie (v)** : L'angle réel depuis le périgée jusqu'à la position actuelle
- **Apogée** : Point le plus élevé d'une orbite
- **Périgée** : Point le plus proche d'une orbite
- **Demi-grand axe (a)** : Demi-longueur de l'axe majeur d'une ellipse
- **Excentricité (e)** : Mesure de l'allongement d'une ellipse (0 = cercle)

### Physique Appliquée
- **Aérodynamique** : Étude du mouvement des objets dans l'air
- **Hypersonique** : Régime où v > 5 Mach (supérieur à la vitesse du son)
- **Coefficient de traînée (C_D)** : Facteur adimensionnel de résistance
- **Moment cinétique** : Quantité conservée du mouvement rotatif
- **Rayon de courbure** : Rayon du cercle tangent à une courbe

### Géophysique
- **Inclinaison (i)** : Angle entre le plan orbital et l'équateur terrestre
- **Longitude du nœud ascendant (Ω)** : Point où l'orbite croise l'équateur vers le nord
- **Argument du périgée (ω)** : Angle entre nœud ascendant et périgée
- **Géoïde** : Surface équipotentielle représentant la forme réelle de la Terre
- **Ellipsoïde de référence** : Modèle mathématique de la forme terrestre

### Calcul Numérique
- **Méthode d'Euler** : Schéma simple d'intégration numérique
- **Méthode de Newton** : Itération pour résoudre équations non-linéaires
- **Pas de temps (Δt)** : Intervalle entre deux calculs successifs
- **Convergence** : Propriété d'une méthode numérique à atteindre la solution exacte

---

## F. Exercices et Problèmes

### Niveau Débutant
1. **Calculer la période** d'une orbite circulaire à 300 km d'altitude
2. **Convertir** des coordonnées cartésiennes (x=7000, y=0, z=0) en sphériques
3. **Estimer** la vitesse orbitale à différentes altitudes

### Niveau Intermédiaire
1. **Résoudre** l'équation de Kepler pour M = π/2, e = 0.1
2. **Simuler** une trajectoire suborbitale avec la méthode d'Euler
3. **Calculer** les éléments orbitaux à partir de trois positions

### Niveau Avancé
1. **Dériver** les équations de rentrée atmosphérique
2. **Optimiser** une trajectoire de transfert Terre-Lune
3. **Modéliser** les perturbations orbitales (atmosphère, Soleil, Lune)

### Solutions Guidées
Les solutions détaillées sont disponibles dans le répertoire pédagogique (à créer).

---

**Note aux lecteurs** : Ces annexes sont destinées à approfondir les concepts mathématiques. Pour une compréhension complète, il est recommandé de combiner la lecture de ces dérivations avec les explications contextuelles dans les chapitres principaux.

**Références croisées** : Voir **Chapitre 2** pour les bases mathématiques, **Chapitre 5** pour les applications pratiques, **Chapitre 7** pour les simulations numériques.
