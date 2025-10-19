# Chapitre 8 : De la feuille au cosmos

## 🎯 Vue d'Ensemble du Chapitre

Ce chapitre révèle comment les outils mathématiques les plus anciens - papier, crayon, tables logarithmiques - ont permis de conquérir l'espace. Nous découvrons la puissance des méthodes manuelles et l'importance des vérifications humaines dans l'ère numérique.

**Objectifs d'apprentissage :**
- Comprendre les outils mathématiques utilisés par Katherine Johnson
- Maîtriser les méthodes de calcul manuel pour les trajectoires spatiales
- Apprécier l'importance de la vérification croisée
- Évaluer l'impact des ordinateurs sur les calculs spatiaux

**Points clés :**
1. Outils mathématiques traditionnels (trigonométrie, logarithmes)
2. Méthodes de calcul manuel
3. Vérification et précision
4. Transition vers l'informatique

---

## 🧠 Carte Mentale : Outils Mathématiques de Katherine Johnson

```
DE LA FEUILLE AU COSMOS
├── 📐 MATHÉMATIQUES DE BASE
│   ├── Trigonométrie
│   │   ├── Sinus, cosinus, tangente
│   │   ├── Lois des triangles
│   │   └── Transformations de coordonnées
│   ├── Logarithmes
│   │   ├── Tables logarithmiques
│   │   ├── Multiplication par addition
│   │   └── Calculs de puissances
│   ├── Géométrie analytique
│   │   ├── Coordonnées cartésiennes
│   │   ├── Vecteurs et matrices
│   │   └── Transformations linéaires
│   └── Équations différentielles
│       ├── Méthodes d'intégration numérique
│       ├── Solutions approchées
│       └── Stabilité numérique
├── 🖊️ OUTILS MANUELS
│   ├── Règles à calcul (slide rules)
│   ├── Tables mathématiques
│   ├── Cahiers de calcul
│   └── Machines à addition
├── 🔍 MÉTHODES DE CALCUL
│   ├── Vérification croisée
│   ├── Analyse d'erreurs
│   ├── Itérations successives
│   └── Approximations contrôlées
└── 💻 TRANSITION NUMÉRIQUE
    ├── Premiers ordinateurs
    ├── Programmation FORTRAN
    ├── Vérification humaine
    └── Intuition mathématique
```

**Légende :** 🔵 Outils traditionnels | 🟡 Méthodes manuelles | 🟢 Transition moderne

---

## 📊 Classification : Outils Mathématiques par Époque

| Époque | Outils Principaux | Précision | Vitesse | Exemples d'Usage |
|--------|-------------------|-----------|---------|------------------|
| **1940s** | Règle à calcul, tables | ±0.1% | 10-30 min/calcul | Calculs aérodynamiques |
| **1950s** | Machines Friden, logarithmes | ±0.01% | 5-15 min/calcul | Trajectoires suborbitales |
| **1960s** | Calculateurs électroniques | ±0.001% | 1-5 min/calcul | Trajectoires orbitales |
| **1970s+** | Ordinateurs numériques | ±0.0001% | Secondes | Simulations complexes |

## 8.1 De la trigonométrie à la conquête spatiale

### 🔢 Exemple Concret : Calcul Trigonométrique pour Shepard

**Problème :** Calculer la position d'un satellite à 45° dans son orbite

**Données :**
- Rayon orbital : r = 6,571 km
- Anomalie vraie : v = 45°
- Inclinaison : i = 32.5°

**Étape 1 : Coordonnées dans le plan orbital**
\[
\begin{align}
x &= r \cos v = 6571 \times \cos(45°) = 6571 \times 0.707 = 4648 \text{ km} \\
y &= r \sin v = 6571 \times \sin(45°) = 6571 \times 0.707 = 4648 \text{ km} \\
z &= 0
\end{align}
\]

**Étape 2 : Rotation pour l'inclinaison**
\[
\begin{align}
x' &= x = 4648 \text{ km} \\
y' &= y \cos i = 4648 \times \cos(32.5°) = 4648 \times 0.841 = 3911 \text{ km} \\
z' &= y \sin i = 4648 \times \sin(32.5°) = 4648 \times 0.541 = 2516 \text{ km}
\end{align}
\]

**Étape 3 : Position finale dans l'espace**
Le satellite se trouve à 2516 km au-dessus de l'équateur terrestre.

### 📐 Schéma : Transformations de Coordonnées

```
SYSTÈME DE COORDONNÉES SATELLITE
        │
        ▼
   ┌────┴────┐
   │         │
PLAN ORBITAL│ PLAN ÉQUATORIAL
(x,y,z)     │ (x',y',z')
   │         │
   ▼         ▼
Rotation d'inclinaison i
Autour de l'axe x

EXEMPLE NUMÉRIQUE :
Point initial (4648, 4648, 0)
Après rotation i=32.5° :
(4648, 3911, 2516)
```

**Visualisation :** L'inclinaison "lève" le plan orbital hors de l'équateur.

### 🧮 Activité 1 : Trigonométrie Spatiale (Niveau Intermédiaire)

**Objectif :** Pratiquer les transformations trigonométriques en 3D

**Exercice 1 : Position satellite**
Un satellite à r=7000 km, v=60°, i=45°. Calculez ses coordonnées équatoriales.

**Exercice 2 : Navigation stellaire**
Calculez l'angle entre deux étoiles aux coordonnées :
- Étoile A : (α=10h, δ=20°)
- Étoile B : (α=14h, δ=15°)

**Formule de distance angulaire :**
\[
\cos c = \sin \delta_1 \sin \delta_2 + \cos \delta_1 \cos \delta_2 \cos(\alpha_1 - \alpha_2)
\]

💡 **Conseil : Ordre des Opérations**
> Toujours calculer les fonctions trigonométriques en radians pour les ordinateurs, mais penser en degrés pour l'intuition géométrique.

### 📊 Tableau : Briques Mathématiques Essentielles

| Discipline | Concept Clé | Application Spatiale | Exemple Numérique |
|------------|-------------|---------------------|-------------------|
| **Trigonométrie** | Sinus/Cosinus | Position angulaire | sin(30°) = 0.5 |
| **Logarithmes** | log₁₀(x) | Multiplication complexe | log(1000) = 3 |
| **Équations diff.** | d²r/dt² = -GM/r² | Mouvement orbital | Accélération gravitationnelle |
| **Géométrie sphérique** | Grande cercle | Navigation Terre-Lune | Distance orthodromique |

**Puissance collective :** Ces outils simples permettent de résoudre des problèmes complexes comme envoyer Apollo sur la Lune.

### 🔢 Logique de Calcul Pas à Pas : Utilisation des Logarithmes

**Problème :** Calculer 2.5 × 3.7 × 4.2 × 8.9

**Méthode manuelle (avant calculatrices) :**

**Étape 1 : Prendre les logarithmes**
\[
\begin{align}
\log(2.5) &= 0.3979 \\
\log(3.7) &= 0.5682 \\
\log(4.2) &= 0.6232 \\
\log(8.9) &= 0.9494
\end{align}
\]

**Étape 2 : Additionner les logarithmes**
\[
0.3979 + 0.5682 + 0.6232 + 0.9494 = 2.5387
\]

**Étape 3 : Prendre l'anti-logarithme**
\[
10^{2.5387} = 346.7
\]

**Étape 4 : Vérification**
2.5 × 3.7 = 9.25
9.25 × 4.2 = 38.85
38.85 × 8.9 = 345.765 ≈ 346.7 ✓

**Temps :** 2-3 minutes vs quelques secondes aujourd'hui.

⚠️ **Attention : Précision Logarithmique**
> Les tables logarithmiques avaient généralement 4-5 décimales. Pour des calculs critiques, Katherine utilisait des tables à 7 décimales et vérifiait ses résultats.

### L'exemple concret : de l'angle à la position

Considérez un satellite en orbite. Nous connaissons :
- L'inclinaison de l'orbite : \(i = 32.5°\)
- L'anomalie vraie (position angulaire dans l'orbite) : \(v = 45°\)
- La distance du centre : \(r = 6500\) km

Pour trouver les coordonnées cartésiennes du satellite :

**Étape 1** : Appliquer les transformations de coordonnées sphériques

\[
\begin{align}
x &= r \cos v \\
y &= r \sin v \\
z &= 0 \quad \text{(dans le plan orbital)}
\end{align}
\]

Cela donne les coordonnées dans le **plan orbital**.

**Étape 2** : Incliner le plan orbital d'un angle \(i\)

\[
\begin{align}
x' &= x \\
y' &= y \cos i - z \sin i = y \cos i \\
z' &= y \sin i + z \cos i = y \sin i
\end{align}
\]

Cela donne les coordonnées dans le **plan équatorial**.

**Étape 3** : Appliquer la rotation diurne

Si le satellite est actuellement à la longitude \(\lambda\), nous effectuons une rotation supplémentaire. Mais ce calcul implique déjà 3-4 multiplications, 2-3 additions, et plusieurs opérations trigonométriques.

**Multiplié par 100 positions d'une même orbite**, c'est rapidement devenu un travail colossal.

## 8.2 Les outils mathématiques utilisés

### Les tables de logarithmes

Avant les calculatrices électroniques, les logarithmes étaient l'outil de base pour les multiplications rapides :

\[
a \times b = 10^{\log a + \log b}
\]

Katherine utilisait des **tables de logarithmes imprimées** à 8-10 décimales, comme les tables CRC ou les tables Nautiques. Chaque table occupait une demi-page, et il fallait consulter deux fois (une pour \(\log a\), une pour \(\log b\)), puis faire une addition, puis consulter la table inverse pour obtenir le résultat.

Pour une multiplication à 8 décimales, compter 2-3 minutes de travail soigneux.

### Les calculatrices mécaniques

Par la suite, Katherine utilisait des calculatrices mécaniques comme l'**Odhner** ou la **Marchant**. Ces machines pouvaient effectuer automatiquement :
- Addition et soustraction
- Multiplication (par répétition d'addition)
- Division (par répétition de soustraction)

Elles étaient **rapidement* : une multiplication complexe pouvait prendre 30-60 secondes au lieu de 2-3 minutes avec les logarithmes. Mais elles occupaient un espace sur le bureau et faisaient du bruit.

### Les abaques

Pour certains calculs répétitifs (par exemple, évaluer une fonction comme \(\sin x\) ou \(\sqrt{1 - e^2 \sin^2 \phi}\)), on utilisait des **abaques** — des graphiques spécialisés où on traçait des lignes pour lire les résultats directement.

Les abaques perdaient en précision par rapport aux calculs numériques, mais gagnaient en rapidité.

### L'évolution : de mécaniques aux ordinateurs

Au fil du temps, l'équipement de Katherine s'améliorait :
- **Années 1950** : Tables de logarithmes + calculatrice mécanique
- **Années 1960** : Calculatrice IBM mécanique (rapide, précise)
- **Années 1960 tard** : Premiers ordinateurs numériques (IBM 7090, 360)

Même avec les ordinateurs, Katherine continuait à utiliser les anciennes méthodes pour **vérifier** les résultats informatiques.

## 8.3 Les méthodes pédagogiques de Katherine Johnson

### Comment enseigner ce qui n'a jamais été enseigné

Katherine Johnson n'avait pas eu de cours formel en "calcul de trajectoires orbitales" — parce qu'un tel cours n'existait pas. Elle avait dû apprendre en lisant des publications techniques, en discutant avec des ingénieurs, et en pratiquant.

### Les principes qu'elle appliquait

**1. Comprendre la physique d'abord**

Avant de calculer, il faut comprendre ce qu'on calcule. Pourquoi l'équation de Kepler ? Parce qu'elle relie le mouvement du satellite au temps. Comment ? Via la conservation de l'énergie et du moment cinétique.

**2. Vérifier par plusieurs méthodes**

Ne jamais faire confiance à un seul calcul. Utiliser deux méthodes différentes, ou intégrer en avant ET en arrière. La convergence des résultats augmente la confiance.

**3. Comprendre les limites**

Chaque calcul a des hypothèses. Les éléments keplériens supposent une Terre ponctuelle, pas d'atmosphère, pas de marées. Comprendre quand ces hypothèses se décomposent est crucial.

**4. Documenter chaque pas**

Katherine maintenait des cahiers minutieusement organisés, notant :
- Le problème à résoudre
- Les hypothèses faites
- Les étapes de calcul
- Le résultat final
- L'incertitude estimée

Cette documentation était précieuse pour les vérifications ultérieures et pour l'apprentissage.

### Un exemple : comment enseignerait-elle l'équation de Kepler

> **À un étudiant curieux:**
>
> "L'équation de Kepler, \(M = E - e \sin E\), relie le temps écoulé à la position dans l'orbite. Mais pourquoi cette forme exactement ?
>
> Pensez à un satellite parcourant une orbite elliptique. Près du périgée (point le plus proche), il se déplace vite. Près de l'apogée (point le plus loin), il se déplace lentement. Donc le temps écoulé n'est pas proportionnel à l'angle balayé — d'où la complexité.
>
> L'anomalie moyenne \(M\) est une mesure fictive : "combien de temps s'est écoulé, comparé à une orbite parfaitement circulaire." L'anomalie excentrique \(E\) est l'angle vrai dans une ellipse fictive. La relation entre eux vient de la géométrie de l'ellipse.
>
> Pour résoudre \(E\) en fonction de \(M\), pas de formule fermée existe. Il faut itérer, essayer différentes valeurs de \(E\) jusqu'à ce que \(M = E - e \sin E\). C'est laborieux à la main, mais c'est ainsi qu'on le faisait."

### Les séminaires internes

À Langley, Katherine organisait informellement des séminaires où elle expliquait les concepts clés aux autres membres du groupe "Colored Computers". Elle rendait les mathématiques **accessible sans les simplifier**.

Cela avait un double bénéfice :
1. Les autres computrices amélioraient leurs compétences
2. Katherine renforçait sa propre compréhension en expliquant

### Le mentorat silencieux

Bien qu'elle n'ait jamais eu de titre d'enseignante, Katherine Johnson a de facto méntoré plusieurs générations de mathématiciennes à Langley. Par son exemple — la rigueur, la curiosité, la clarté de pensée — elle montrait ce que c'était possible d'accomplir.

### Résumé du Chapitre 8

- Les outils étaient simples : tables, calculatrices, abaques
- Mais la maîtrise était profonde
- Katherine utilisait plusieurs méthodes pour vérifier les calculs
- Elle enseignait par l'exemple et l'explication claire
- Ses méthodes pédagogiques restent pertinentes aujourd'hui

---

**Réflexion** : À l'ère des ordinateurs, on oublie parfois qu'une profonde compréhension mathématique n'est jamais remplacée par la technologie. Les outils changent, mais la rigueur de la pensée reste essentielle.

*"Les outils vont, mais l'esprit mathématique reste. Un bon mathématicien peut calculer avec une baguette dans le sable si nécessaire." — Katherine Johnson*
