# Chapitre 2 : Le langage des trajectoires

## 2.1 Les coordonnées sphériques et les bases de la navigation spatiale

### De Ptolémée à Kepler : une brève histoire

Pour comprendre comment Katherine Johnson calculait les trajectoires orbitales, nous devons d'abord établir le **langage mathématique** des mouvements célestes.

Pendant des millénaires, les astronomes ont essayé de décrire les mouvements des planètes. Ptolémée croyait que la Terre était au centre de l'univers. Copernic plaça le Soleil au centre. Mais c'est **Johannes Kepler** (1571-1630) qui, en utilisant les observations précises de Tycho Brahe, découvrit les trois lois qui gouvernent les orbites.

Ces trois lois sont **la fondation mathématique de tout calcul de trajectoire**, y compris ceux que Katherine Johnson effectuait.

### Les coordonnées cartésiennes et sphériques

#### Coordonnées cartésiennes (x, y, z)

La façon la plus simple de localiser un point dans l'espace tridimensionnel est d'utiliser trois coordonnées orthogonales. Le **vecteur position** \(\vec{r}\) d'un point \((x, y, z)\) peut s'écrire de plusieurs manières équivalentes :

**Notation avec chapeau (hat notation)** :
\[
\vec{r} = x\hat{x} + y\hat{y} + z\hat{z}
\]

**Notation classique** (très utilisée en physique) :
\[
\vec{r} = x\vec{i} + y\vec{j} + z\vec{k}
\]

**Notation avec indices** (courante en mécanique) :
\[
\vec{r} = x\vec{e}_x + y\vec{e}_y + z\vec{e}_z
\]

**Notation matricielle** (utile pour les calculs) :
\[
\vec{r} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}
\]

> **Note** : Dans toutes ces notations, les vecteurs unitaires (\(\hat{x}, \hat{y}, \hat{z}\) ou \(\vec{i}, \vec{j}, \vec{k}\) ou \(\vec{e}_x, \vec{e}_y, \vec{e}_z\)) représentent les **vecteurs de base orthonormés** :
> - Ils sont **perpendiculaires** entre eux (orthogonaux)
> - Ils ont une **longueur unitaire** (norme = 1)
> - Ils pointent le long des axes positifs x, y, et z respectivement

**Interprétation physique** : L'équation \(\vec{r} = x\hat{x} + y\hat{y} + z\hat{z}\) indique que le vecteur position \(\vec{r}\) est composé d'une magnitude \(x\) dans la direction \(\hat{x}\), d'une magnitude \(y\) dans la direction \(\hat{y}\), et d'une magnitude \(z\) dans la direction \(\hat{z}\).

Pour une orbite autour de la Terre, nous plaçons généralement l'origine au centre terrestre, l'axe \(z\) pointant vers le pôle nord, et l'axe \(x\) pointant vers un point de référence dans l'espace (par convention, l'équinoxe de printemps).

#### Coordonnées sphériques (r, θ, φ)

Les coordonnées sphériques sont souvent plus naturelles pour les orbites. Un point est décrit par :
- **r** : distance du centre
- **θ** (thêta) : angle polaire (0 au pôle nord, π/2 à l'équateur, π au pôle sud)
- **φ** (phi) : angle azimutal (0 à 2π)

La transformation est :

\[
\begin{align}
x &= r \sin\theta \cos\phi \\
y &= r \sin\theta \sin\phi \\
z &= r \cos\theta
\end{align}
\]

### Les coordonnées orbitales : un système spécialisé

Pour décrire une orbite, les astronomes et les ingénieurs utilisent un système de coordonnées spécialisé basé sur les **éléments orbitaux** (orbital elements).

Plutôt que (x, y, z) ou (r, θ, φ), une orbite est complètement décrite par six nombres :

1. **a** : demi-grand axe (taille de l'orbite)
2. **e** : excentricité (forme de l'orbite : 0 = cercle, proche de 1 = ellipse très allongée)
3. **i** : inclinaison (angle avec l'équateur terrestre)
4. **Ω** (Oméga capital) : longitude du nœud ascendant (où l'orbite croise l'équateur en montant)
5. **ω** (oméga minuscule) : argument du périgée (orientation de l'ellipse dans le plan orbital)
6. **M** : anomalie moyenne (position actuelle dans l'orbite)

Ces six nombres, appelés les **éléments keplériens**, sont suffisants pour reconstruire complètement la position et la vitesse d'un engin spatial à tout moment.

> **Note technique** : Le problème de passer des 6 éléments keplériens à la position cartésienne \((x, y, z)\) ou vice-versa est un problème central que Katherine Johnson devait résoudre constamment. Ce n'est pas trivial — cela implique des équations transcendantes qu'on ne peut pas résoudre analytiquement.

### 2.2 Équations du mouvement orbital

#### Dérivation à partir des lois de Kepler

**Première loi de Kepler** : *Les orbites sont des ellipses, avec le corps central à l'un des foyers.*

Cette loi nous dit la **forme** de l'orbite, mais pas comment l'objet se déplace le long de l'orbite.

**Deuxième loi de Kepler** : *Le rayon-vecteur balaie des aires égales en des temps égaux.*

Mathématiquement, cela signifie que le **moment cinétique** est conservé :

\[
\vec{L} = \vec{r} \times m\vec{v} = \text{constant}
\]

**Troisième loi de Kepler** : *Le carré de la période est proportionnel au cube du demi-grand axe.*

\[
T^2 = \frac{4\pi^2}{GM} a^3
\]

Où \(G\) est la constante gravitationnelle, \(M\) est la masse du corps central, et \(a\) est le demi-grand axe.

#### La dérivation newtonienne

Les trois lois de Kepler peuvent être dérivées de la **deuxième loi de Newton** appliquée à une force gravitationnelle centrale :

\[
\vec{F} = -\frac{GMm}{r^2} \hat{r}
\]

En substituant dans \(\vec{F} = m\vec{a}\) :

\[
\vec{a} = -\frac{GM}{r^2} \hat{r}
\]

C'est une équation différentielle vectorielle qui gouverne toute orbite. **Résoudre cette équation est le cœur du problème de la trajectoire.**

#### Transformation en coordonnées polaires

Pour une orbite dans un plan (mouvement 2D), il est utile de convertir l'équation vectorielle en coordonnées polaires \((r, \theta)\).

**Étape 1 : Rappel des coordonnées polaires**
- \(r\) : distance du centre
- \(\theta\) : angle par rapport à l'axe de référence
- Les dérivées : \(\dot{r} = dr/dt\), \(\ddot{r} = d²r/dt²\), etc.

**Étape 2 : Expression de l'accélération en polaire**

L'accélération en coordonnées polaires se décompose en deux termes :

\[
\vec{a} = \left(\ddot{r} - r\dot{\theta}^2\right) \hat{r} + (r\ddot{\theta} + 2\dot{r}\dot{\theta}) \hat{\theta}
\]

**Explication des termes :**
- \(\ddot{r}\) : accélération radiale (vers l'extérieur/intérieur)
- \(-r\dot{\theta}^2\) : accélération centrifuge (due à la rotation)
- \(r\ddot{\theta}\) : accélération angulaire normale
- \(2\dot{r}\dot{\theta}\) : accélération angulaire due au mouvement radial

**Étape 3 : Application de la loi de Newton**

La force gravitationnelle n'agit que dans la direction radiale (vers le centre), donc l'équation dans la direction \(\hat{\theta}\) est nulle :

**Équation radiale (direction \(\hat{r}\))** :
\[
\ddot{r} - r\dot{\theta}^2 = -\frac{GM}{r^2}
\]

**Pourquoi cette forme ?**
- Terme de gauche : accélération totale dans la direction radiale
- Terme de droite : force gravitationnelle par unité de masse (loi de Newton)

**Équation angulaire (direction \(\hat{\theta}\))** :
\[
r\ddot{\theta} + 2\dot{r}\dot{\theta} = 0
\]

**Étape 4 : Conservation du moment cinétique**

Réécrivons la deuxième équation :

\[
r\ddot{\theta} + 2\dot{r}\dot{\theta} = 0
\]

\[
\ddot{\theta} + \frac{2\dot{r}}{r}\dot{\theta} = 0
\]

Cette équation ressemble à une dérivée. En effet :

\[
\frac{d}{dt}(r^2 \dot{\theta}) = r^2 \ddot{\theta} + 2r\dot{r}\dot{\theta} = r \cdot r\ddot{\theta} + 2r\dot{r}\dot{\theta} = r(r\ddot{\theta} + 2\dot{r}\dot{\theta})
\]

Donc l'équation devient :

\[
\frac{d}{dt}(r^2 \dot{\theta}) = 0
\]

**Conclusion :** Le moment cinétique par unité de masse \(h = r^2\dot{\theta}\) est constant.

**Signification physique :** Cette constante représente la vitesse angulaire effective de l'orbite et détermine sa "forme" globale.

### 2.3 L'intégration du temps dans la mécanique orbitale

#### Le problème de Kepler

Supposons que nous connaissons les éléments orbitaux : \(a\), \(e\), \(i\), etc. Nous voulons connaître la position du satellite **à un moment spécifique** \(t\).

Le problème est que la relation entre le temps et la position dans l'orbite n'est pas linéaire. Près du périgée (point le plus proche), le satellite se déplace rapidement. Près de l'apogée (point le plus lointain), il se déplace lentement.

#### L'anomalie excentrique

Pour résoudre ce problème, les astronomes définissent une variable intermédiaire appelée l'**anomalie excentrique** \(E\).

L'ellipse peut être paramétrée par :

\[
\begin{align}
r &= a(1 - e\cos E) \\
v &= r\theta = a(1-e^2) / (1 + e\cos v)
\end{align}
\]

Où \(v\) est l'**anomalie vraie** (l'angle réel dans l'orbite, mesuré depuis le périgée).

#### L'équation de Kepler

La relation entre le temps et l'anomalie excentrique est donnée par l'**équation de Kepler** :

\[
M = E - e\sin E
\]

**Étape 1 : Comprendre les variables**

- \(M\) : **Anomalie moyenne** = angle fictif que le satellite aurait si l'orbite était circulaire
- \(E\) : **Anomalie excentrique** = angle dans l'ellipse fictive centrée sur le foyer
- \(e\) : **Excentricité** de l'orbite

**Étape 2 : Calcul de l'anomalie moyenne**

\[
M = n(t - t_p)
\]

Où :
- \(n = \sqrt{GM/a^3}\) est le **mouvement moyen** (rad/s)
- \(t\) est le temps actuel
- \(t_p\) est le temps du dernier passage au périgée

**Explication :** Pour une orbite circulaire, l'angle parcouru serait simplement \(M = n(t - t_p)\). Pour une ellipse, c'est plus complexe.

**Étape 3 : Dérivation de l'équation de Kepler**

L'équation \(M = E - e\sin E\) vient de la géométrie de l'ellipse :

1. **Ellipse centrée :** Dans un système où l'ellipse est centrée sur le foyer, on utilise l'anomalie excentrique \(E\).

2. **Relation trigonométrique :** La distance du centre à un point de l'ellipse est donnée par :
   \[
   r = a(1 - e\cos E)
   \]

3. **Conservation des aires :** La deuxième loi de Kepler donne :
   \[
   r^2 \dot{\theta} = h
   \]

4. **Intégration temporelle :** En intégrant cette équation, on obtient la relation entre \(M\) et \(E\).

**Étape 4 : Résolution numérique**

**C'est ici que les calculs deviennent difficiles.** Il n'y a pas de solution analytique fermée pour \(E\) en fonction de \(M\). Il faut utiliser des **méthodes numériques itératives**.

**Méthode de Newton-Raphson :**

**Étape 4.1 :** Reformuler comme problème de zéro de fonction :
\[
f(E) = E - e\sin E - M = 0
\]

**Étape 4.2 :** Itération avec la dérivée :
\[
f'(E) = 1 - e\cos E
\]

**Étape 4.3 :** Formule d'itération :
\[
E_{n+1} = E_n - \frac{E_n - e\sin E_n - M}{1 - e\cos E_n}
\]

**Étape 4.4 :** Condition d'arrêt :
\[
|E_{n+1} - E_n| < \epsilon \quad (\epsilon \approx 10^{-8} \text{ rad})
\]

**Étape 4.5 :** Valeur initiale intelligente :
\[
E_0 = M + e\sin M \quad (\text{pour } e < 0.3)
\]

**Exemple numérique :**
- Données : \(M = 1.2\) rad, \(e = 0.1\)
- \(E_0 = 1.2 + 0.1\sin(1.2) = 1.298\)
- Après 2 itérations : \(E \approx 1.309\) rad

**Pourquoi c'est difficile :** L'équation est transcendante - elle contient à la fois \(E\) et \(\sin E\), donc pas de solution algébrique simple.

### Résumé : du temps à la position

Pour trouver la position d'un satellite à un temps \(t\) donné :

1. Calculer l'anomalie moyenne : \(M = n(t - t_p)\)
2. Résoudre l'équation de Kepler pour trouver \(E\) (itérativement, c'est le travail difficile)
3. Convertir à l'anomalie vraie : \(\tan(v/2) = \sqrt{(1+e)/(1-e)} \tan(E/2)\)
4. Calculer la distance : \(r = a(1 - e\cos E)\)
5. Calculer les coordonnées cartésiennes : \(x\), \(y\), \(z\)

Katherine Johnson **effectuait ces calculs quotidiennement**, souvent pour plusieurs positions d'une même orbite, et elle le faisait à la main ou avec une calculatrice mécanique.

## 2.4 Exemples Mathématiques Concrets

### Exemple 1 : Calcul de l'Orbite de la Station Spatiale Internationale

**Paramètres donnés** :
- Demi-grand axe : \(a = 6778\) km
- Excentricité : \(e = 0.0005\) (orbite quasi-circulaire)
- Inclinaison : \(i = 51.6°\)
- Période orbitale : \(T = 92.5\) minutes

**Calcul de la vitesse orbitale** :
\[
v = \sqrt{GM_{\oplus}/r} = \sqrt{3.986 \times 10^{14} / 6.778 \times 10^6} = 7676 \text{ m/s} \approx 7.68 \text{ km/s}
\]

**Calcul du mouvement moyen** :
\[
n = \frac{2\pi}{T} = \frac{2\pi}{5570 \text{ s}} = 0.001127 \text{ rad/s}
\]

**Résolution de l'équation de Kepler** (pour t = 30 min = 1800 s) :
\[
M = n(t - t_p) = 0.001127 \times 1800 = 2.0286 \text{ rad}
\]

Itération pour trouver \(E\) :
- \(E_0 = M = 2.0286\)
- \(E_1 = 2.0286 + 0.0005 \sin(2.0286) = 2.0296\)
- \(E_2 \approx 2.0296\) (convergence rapide car e petit)

**Position finale** :
\[
r = a(1 - e\cos E) = 6778(1 - 0.0005 \times 0.499) = 6775.3 \text{ km}
\]

### Exemple 2 : Comparaison Orbites Circulaire vs Elliptique

| Paramètre | Orbite Circulaire | Orbite Elliptique (e=0.1) |
|-----------|------------------|---------------------------|
| **a** | 7000 km | 7000 km |
| **r_apogée** | 7000 km | 7700 km |
| **r_périgée** | 7000 km | 6300 km |
| **v_apogée** | 7520 m/s | 7130 m/s |
| **v_périgée** | 7520 m/s | 7910 m/s |
| **Période** | 98.0 min | 98.0 min |
| **Temps périgée** | 24.5 min | 21.8 min |
| **Temps apogée** | 24.5 min | 27.2 min |

## 2.5 Classification des Systèmes de Coordonnées

| Système | Dimensions | Utilisation | Avantages | Inconvénients |
|---------|------------|-------------|-----------|-------------|
| **Cartésien** | 3D (x,y,z) | Position absolue | Simple, intuitif | Pas adapté aux orbites |
| **Sphérique** | r, θ, φ | Position relative | Naturel pour champs radiaux | Complexe pour mouvements |
| **Orbital** | 6 éléments | Description complète | Compact, standard | Nécessite conversions |
| **Polaire** | r, θ | Mouvement planaire | Simple dérivation | Limité à 2D |
| **Géodésique** | φ, λ, h | Surface terrestre | Compatible GPS | Nécessite ellipsoïde |

## 2.6 Encadrés Spéciaux

⚠️ **Attention : Convergence de l'Équation de Kepler**
> Pour les orbites très elliptiques (e > 0.8), l'itération peut diverger. Utilisez toujours des valeurs initiales intelligentes et surveillez la convergence.

💡 **Conseil : Ordres de Grandeur**
> Une orbite terrestre basse a généralement :
> - a ≈ 6500-7000 km
> - e < 0.1 (circulaire)
> - T ≈ 90-100 minutes
> - v ≈ 7.5-8 km/s

✓ **Bonnes Pratiques : Conversion de Coordonnées**
> 1. Toujours vérifier que r > 0 et |e| < 1
> 2. Utiliser des angles en radians pour les calculs
> 3. Vérifier la conservation de l'énergie entre conversions
> 4. Documenter l'origine des systèmes de coordonnées

## 2.7 Schéma Visuel des Coordonnées Orbitales

```
                    ↑ Direction du mouvement
                    │
                    │
            ┌───────┼───────┐ Apogée (point le plus éloigné)
           /        │        \
          /         │         \
         /          │          \
        /           │           \
       /            │            \
Apogée ┌────────────┼────────────┘ Périgée (point le plus proche)
       └────────────┼────────────┐
        \           │           /
         \          │          /
          \         │         /
           \        │        /
            └───────┼───────┘
                    │
                    ↓

ÉLÉMENTS ORBITAUX :

a = Demi-grand axe (taille moyenne)
e = Excentricité (forme : 0=circulaire)
i = Inclinaison (angle avec équateur)
Ω = Longitude du nœud ascendant
ω = Argument du périgée
M = Anomalie moyenne (position)

COORDONNÉES AU POINT ACTUEL :
r = Distance du centre (varie)
v = Anomalie vraie (angle actuel)
θ = Angle polaire
```

## 2.8 Références Croisées

- **Chapitre 1** : Katherine découvre ces concepts autodidacte à Langley
- **Chapitre 3** : Application aux trajectoires suborbitales (cas limite)
- **Chapitre 4** : Corrections nécessaires pour la précision réelle
- **Chapitre 5** : Utilisation intensive pour la mission Glenn
- **Chapitre 6** : Extension aux transferts Terre-Lune
- **Chapitre 8** : Katherine maîtrisait ces calculs avec des outils rudimentaires
- **Annexes A.1-A.3** : Dérivations complètes des équations présentées

## 2.9 Synthèse et Auto-Évaluation

### Points Clés du Chapitre

1. **Kepler** : Trois lois décrivent le mouvement orbital
2. **Coordonnées** : Plusieurs systèmes pour différentes utilisations
3. **Équation de Kepler** : Le défi central de résolution temporelle
4. **Mécanique newtonienne** : Fondement physique des orbites
5. **Pratique** : Katherine appliquait ces concepts quotidiennement

### Questions d'Auto-Évaluation

**Niveau Débutant :**
- Quelles sont les trois lois de Kepler ?
- Quelle est la différence entre anomalie vraie et anomalie moyenne ?

**Niveau Intermédiaire :**
- Expliquez pourquoi l'équation de Kepler nécessite une résolution itérative
- Comparez les avantages des coordonnées orbitales vs cartésiennes

**Niveau Avancé :**
- Dérivez les équations du mouvement polaire à partir de la mécanique newtonienne
- Expliquez comment les éléments keplériens sont déterminés à partir d'observations

---

**Lectures complémentaires** :
- Vallado, D. A. (2013). *Fundamentals of Astrodynamics and Applications*
- Curtis, H. D. (2013). *Orbital Mechanics for Engineering Students*

*"La beauté de ces équations, c'est qu'elles décrivent avec une précision remarquable comment les objets se déplacent dans l'espace." — Katherine Johnson*
