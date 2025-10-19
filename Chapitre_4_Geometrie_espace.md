# Chapitre 4 : La géométrie de l'espace

## 🎯 Vue d'Ensemble du Chapitre

Ce chapitre explore les subtilités géométriques et physiques qui rendent le "vide" spatial bien plus complexe qu'il n'y paraît. De la forme légèrement aplatie de la Terre aux effets de sa rotation, nous découvrons pourquoi les calculs de trajectoire nécessitent des corrections sophistiquées.

**Objectifs d'apprentissage :**
- Comprendre que la Terre n'est pas une sphère parfaite
- Maîtriser les systèmes de coordonnées utilisés en astronautique
- Analyser les effets de la rotation terrestre sur les trajectoires
- Évaluer l'importance des corrections physiques dans les calculs précis

**Points clés :**
1. Ellipsoïde de référence WGS84
2. Rotation terrestre et force de Coriolis
3. Corrections relativistes et gravitationnelles
4. Applications aux missions spatiales

---

## 🧠 Carte Mentale : Géométrie Spatiale

```
GÉOMÉTRIE DE L'ESPACE
├── 🌍 FORME DE LA TERRE
│   ├── Sphère parfaite (approximation)
│   ├── Ellipsoïde aplati (réalité)
│   └── Géoïde irrégulier (précision ultime)
├── 📐 SYSTÈMES DE COORDONNÉES
│   ├── Cartésiennes (x,y,z)
│   ├── Sphériques (r,θ,φ)
│   ├── Orbitales (éléments keplériens)
│   └── Géodésiques (lat,lon,h)
├── 🌪️ EFFETS DYNAMIQUES
│   ├── Rotation terrestre
│   ├── Force de Coriolis
│   ├── Marées gravitationnelles
│   └── Pression de radiation
└── 🔬 CORRECTIONS PHYSIQUES
    ├── Potentiel gravitationnel
    ├── Atmosphère résiduelle
    ├── Effets relativistes
    └── Précision requise
```

**Légende :** 🔵 Concepts fondamentaux | 🟡 Corrections importantes | 🟢 Applications pratiques

---

## 📊 Classification : Niveaux de Précision Géodésique

| Niveau | Modèle | Précision | Applications | Exemple d'Erreur |
|--------|--------|-----------|-------------|------------------|
| **1 - Sphère** | Rayon constant | ±100 km | Calculs préliminaires | Trajectoire approximative |
| **2 - Ellipsoïde** | Aplatissement polaire | ±1 km | Navigation GPS | Point d'atterrissage |
| **3 - Géoïde** | Surface équipotentielle | ±10 m | Cartographie précise | Topographie détaillée |
| **4 - Géodésie moderne** | Variations locales | ±1 cm | Missions spatiales | Corrections orbitales |

## 4.1 La Terre n'est pas une sphère parfaite : l'ellipsoïde de référence

### L'hypothèse simplifiante

Dans les chapitres précédents, nous avons traité la Terre comme une sphère parfaite de rayon \(R = 6371\) km, avec une masse uniformément distribuée.

**C'est une hypothèse qui, bien que utile pour les calculs préliminaires, n'est pas précise.**

En réalité, la Terre est légèrement aplatie aux pôles et bombée à l'équateur. Elle ressemble plus à un **ellipsoïde oblate** (ou plus techniquement, un **géoïde**).

### L'ellipsoïde de référence WGS84

Pour les calculs de trajectoires précises, les astronomes et les ingénieurs utilisent un modèle standard appelé l'**ellipsoïde de référence WGS84** (World Geodetic System 1984).

Ses paramètres clés sont :
- **Rayon équatorial** \(a = 6378.137\) km
- **Rayon polaire** \(b = 6356.752\) km
- **Aplatissement** \(f = (a - b) / a \approx 0.003353\)

Cela signifie que le rayon équatorial est d'environ 21 km plus grand que le rayon polaire. Ce n'est pas énorme, mais c'est suffisant pour affecter les calculs de trajectoires orbites.

### Coordonnées géodésiques

Avec l'ellipsoïde WGS84, un point à la surface terrestre est décrit par trois coordonnées :
- **φ** (phi) : latitude géodésique
- **λ** (lambda) : longitude
- **h** : altitude (hauteur au-dessus de l'ellipsoïde)

La transformation entre les coordonnées géodésiques et les coordonnées cartésiennes ECEF (Earth-Centered, Earth-Fixed) est plus complexe qu'avec une sphère :

\[
\begin{align}
x &= (N(\phi) + h) \cos\phi \cos\lambda \\
y &= (N(\phi) + h) \cos\phi \sin\lambda \\
z &= (N(\phi) (1 - e^2) + h) \sin\phi
\end{align}
\]

Où \(N(\phi) = \frac{a}{\sqrt{1 - e^2 \sin^2\phi}}\) est le **rayon de courbure**, et \(e^2 = 2f - f^2\) est l'excentricité au carré.

### 🌍 Exemple Concret : Calcul d'Altitude Géodésique

**Données :**
- Latitude : φ = 45° (Paris)
- Longitude : λ = 2.35° (Paris)
- Altitude ellipsoïdale : h = 0 m (niveau mer)

**Calcul du rayon de courbure N(φ) :**
- a = 6378.137 km (rayon équatorial)
- e² = 0.00669438 (excentricité carrée)
- φ = 45° = π/4 radians

\[
N(\phi) = \frac{6378.137}{\sqrt{1 - 0.00669438 \sin^2(45°)}} = \frac{6378.137}{\sqrt{1 - 0.00669438 \times 0.5}} = \frac{6378.137}{\sqrt{1 - 0.00334719}} = \frac{6378.137}{\sqrt{0.99665281}} \approx \frac{6378.137}{0.998325} \approx 6388.8 \text{ km}
\]

**Coordonnées cartésiennes :**
\[
\begin{align}
x &= (6388.8 + 0) \cos(45°) \cos(2.35°) \approx 6388.8 \times 0.707 \times 0.999 \approx 4518 \text{ km} \\
y &= (6388.8 + 0) \cos(45°) \sin(2.35°) \approx 6388.8 \times 0.707 \times 0.041 \approx 185 \text{ km} \\
z &= (6388.8 \times (1 - 0.00669438) + 0) \sin(45°) \approx 6388.8 \times 0.9933 \times 0.707 \approx 4485 \text{ km}
\end{align}
\]

**Interprétation :** Ces coordonnées placent Paris dans le système de référence terrestre centré.

### 📐 Activité 1 : Conversion de Coordonnées (Niveau Intermédiaire)

**Objectif :** Pratiquer la conversion entre systèmes de coordonnées

**Exercice 1 : Sphérique → Cartésien**
Point : r = 6371 km, θ = 30°, φ = 45°
Calculez x, y, z.

**Exercice 2 : Géodésique → Cartésien**
Point : φ = 0° (équateur), λ = 0° (Greenwich), h = 100 km
Calculez x, y, z.

**Exercice 3 : Comparaison**
Quelle est la différence de distance au centre entre :
- Un point à l'équateur (h = 0)
- Un point au pôle nord (h = 0)
- Expliquez pourquoi.

💡 **Conseil : Ordre des opérations**
> Toujours convertir en radians d'abord ! Les fonctions trigonométriques des langages de programmation utilisent des radians, pas des degrés.

### 4.2 Calculs de correction dus à la rotation terrestre

#### La Terre tourne

Lorsqu'on calcule une trajectoire spatiale, il faut choisir un système de référence. Il existe deux choix naturels :

1. **Référentiel inertiel** : fixe par rapport aux étoiles (ne tourne pas avec la Terre)
2. **Référentiel terrestre** : fixé à la Terre et tournant avec elle

Pour les calculs de trajectoire, les équations de mouvement sont plus simples dans le référentiel inertiel. Mais les paramètres géographiques (latitude, longitude) sont définis dans le référentiel terrestre.

#### Conversion entre référentiels

La Terre effectue une rotation complète en 1 jour sidéral = 86164.0905 secondes.

La vitesse angulaire est donc :

\[
\omega_\oplus = \frac{2\pi}{86164.0905 \text{ s}} = 7.292115 \times 10^{-5} \text{ rad/s}
\]

Lorsqu'on passe d'un référentiel à l'autre, on doit appliquer une rotation de l'angle \(\theta = \omega_\oplus \cdot t\) autour de l'axe polaire.

#### L'effet Coriolis

Dans le référentiel tournant de la Terre, il existe une **force fictive** appelée la **force de Coriolis** :

\[
\vec{F}_{\text{Coriolis}} = -2m \vec{\omega}_\oplus \times \vec{v}
\]

Pour une trajectoire de vol suborbital, cet effet est généralement petit mais mesurable. Katherine Johnson devait le considérer dans ses calculs.

### 🌪️ Exemple Numérique : Effet Coriolis sur Shepard

**Contexte :** Mission Mercury-Redstone 3, lancement depuis Cap Canaveral (φ = 28.5°)

**Paramètres :**
- ω_⊕ = 7.292 × 10⁻⁵ rad/s (vitesse angulaire terrestre)
- v = 2.6 km/s (vitesse maximale de Shepard)
- φ = 28.5° (latitude de lancement)

**Calcul de la force de Coriolis :**
\[
F_{\text{Coriolis}} = 2m \omega_\oplus v \sin\phi
\]

\[
\sin(28.5°) = 0.478
\]

\[
F_{\text{Coriolis}} = 2 \times m \times 7.292 \times 10^{-5} \times 2600 \times 0.478 \approx 4.6 \times 10^{-2} m \text{ N}
\]

**Impact sur la trajectoire :**
- Déviation latérale d'environ 0.5 km sur la portée de 486 km
- Nécessite correction dans les calculs de point d'atterrissage

### 📊 Schéma : Effets de la Rotation Terrestre

```
EFFETS DE LA ROTATION TERRESTRE
        │
        ▼
   ┌────┴────┐
   │         │
CENTRI-     │ CORIOLIS
FUGE        │
   │         │
   ▼         ▼
Accélération  Force apparente
centrifuge    qui dévie les
(radiale)     objets en
              mouvement

EXEMPLE : MISSILE BALISTIQUE
├── Sans Coriolis : Trajectoire symétrique
├── Avec Coriolis : Déviation vers l'est (hémisphère nord)
└── Impact : Correction de 0.1-1° dans l'azimut de lancement
```

**Pourquoi important :** La Terre tourne sous le missile pendant son vol, changeant le point de référence.

### 🧮 Activité 2 : Calculs de Rotation (Niveau Avancé)

**Objectif :** Calculer l'impact de la rotation terrestre sur une trajectoire

**Problème :** Un missile lancé verticalement à Paris (φ = 48.8°N) atteint 1000 km d'altitude en 5 minutes.

**Questions :**
1. De combien la Terre a-t-elle tourné pendant ce temps ?
2. Quelle distance latérale cela représente-t-il ?
3. Comment corriger la trajectoire de rentrée ?

**Données utiles :**
- Circonférence terrestre : 40,075 km
- Période de rotation : 24 heures = 86,400 secondes

⚠️ **Attention : Direction de la Coriolis**
> Dans l'hémisphère nord, la force de Coriolis dévie vers la droite par rapport au mouvement. Dans l'hémisphère sud, c'est vers la gauche. Aux pôles, elle est nulle ; à l'équateur, elle est maximale.

### 4.3 Effets relativistes et précision des trajectoires

#### La relativité générale

Vous vous demandez peut-être : est-ce qu'on doit considérer la **relativité générale** pour les trajectoires spatiales ?

**Techniquement, oui. Pratiquement, c'est plus subtil.**

La relativité générale dit que la gravité n'est pas une force, mais une courbure de l'espace-temps. Pour les applications pratiques de la NASA dans les années 1960, l'effet relativiste était déjà mesurable, mais très petit.

#### Corrections relativistes

Le principal effet relativiste pour une orbite terrestre basse est l'**aberration relativiste** et la **correction de temps**. Mais les plus importants effets étaient dus à des facteurs classiques négligés, comme :

1. **Le potentiel gravitationnel non-sphérique** : la Terre n'a pas une distribution de masse uniforme
2. **Les marées lunaires et solaires** : autres corps célestes génèrent des forces perturbatrices
3. **La pression de radiation solaire** : pour les engins spatiaux légers
4. **La traînée atmosphérique** : pour les orbites basses

#### L'exemple de John Glenn

Pour la mission de John Glenn en 1962 (que nous couvrirons au Chapitre 5), ces corrections étaient **cruciales**. Glenn orbiterait à une altitude d'environ 260 km, où la traînée atmosphérique était mesurable.

Les corrections dues à la traînée atmosphérique, au non-sphéricité de la Terre, et aux marées devaient être incluses dans les calculs de trajectoire pour prédire correctement :
- La durée de chaque orbite
- Le point d'amarrissage après que la capsule amorce sa descente
- La vitesse de rentrée

### ⚛️ Exemple : Corrections Relativistes pour GPS

**Contexte :** Les satellites GPS orbitent à 20,200 km d'altitude

**Effets relativistes principaux :**
1. **Dilatation temporelle** (effet gravitationnel) : Δt/t ≈ -GM/(c²r) ≈ -4.5 × 10⁻¹⁰
2. **Effet de vitesse** (relativité restreinte) : Δt/t ≈ -v²/(2c²) ≈ -7.8 × 10⁻¹¹

**Impact total :** Les horloges des satellites avancent d'environ 38 microsecondes par jour !

**Conséquence :** Sans correction relativiste, le GPS aurait une erreur de position de 10 km par jour.

### 📈 Diagramme : Hiérarchie des Corrections

```
CORRECTIONS DE TRAJECTOIRE
        │
        ▼
   ┌────┴────┐
   │         │
BASIQUE     │ AVANCÉ
(sphère)    │ (ellipsoïde)
   │         │
   ▼         ▼
Gravité      Rotation terrestre
uniforme      Coriolis
   │         │
   ▼         ▼
   ┌────┴────┴────┐
   │             │
MODERNE        │ ULTRA-PRÉCIS
(géoïde)       │ (relativité)
   │             │
   ▼             ▼
Marées          Effets quantiques
Atmosphère      Théorie des cordes
résiduelle      (futur)
```

**Leçon :** Chaque niveau de précision révèle de nouveaux effets qui étaient auparavant négligeables.

### 🔬 Activité 3 : Évaluation des Corrections (Niveau Expert)

**Objectif :** Hiérarchiser l'importance des corrections selon le type de mission

| Correction | Impact Suborbital | Impact Orbital LEO | Impact Géostationnaire |
|------------|-------------------|-------------------|----------------------|
| **Aplatissement** | Faible (±100m) | Moyen (±1km) | Important (±10km) |
| **Coriolis** | Moyen (±500m) | Faible (±100m) | Négligeable |
| **Atmosphère** | Crucial (±50km) | Important (±5km) | Négligeable |
| **Marées** | Faible | Moyen (±500m) | Important (±2km) |
| **Relativité** | Négligeable | Faible (±10m) | Moyen (±100m) |

**Discussion :**
1. Pourquoi les corrections atmosphériques sont-elles cruciales pour les missions suborbitales ?
2. Quelles corrections deviennent importantes pour les missions interplanétaires ?
3. Comment Katherine Johnson priorisait-elle ces corrections dans ses calculs ?

✓ **Bonne Pratique : Approche Hiérarchique**
> Commencez toujours par les corrections les plus importantes pour votre mission, puis ajoutez les effets secondaires. Cette approche "par couches" permet de contrôler la précision tout en gérant la complexité.

### Résumé des corrections nécessaires

Pour un calcul de trajectoire vraiment précis, Katherine Johnson devait tenir compte de :

| Facteur | Magnitude | Importance |
|---------|-----------|-----------|
| Non-sphéricité terrestre | ~21 km d'aplatissement | Haute |
| Rotation terrestre | 1 rotation par jour | Haute |
| Traînée atmosphérique | Varie avec altitude | Moyenne-Haute |
| Marées lunaires | ~0.3 m/s² à ~60000 km | Basse (pour LEO) |
| Effets relativistes | ~10 mm/jour pour LEO | Très basse |
| Pression de radiation solaire | ~10⁻⁶ m/s² | Très basse |

Pour une mission suborbitalecourte (Shepard), les facteurs "Haute" étaient essentiels.
Pour une mission orbitale (Glenn), tous les facteurs "Haute" et "Moyenne" étaient nécessaires.

## 📚 Synthèse et Évaluation du Chapitre 4

### 🎯 Points Clés Acquis

1. **Forme terrestre** : La Terre n'est pas sphérique mais ellipsoïdale, nécessitant le modèle WGS84
2. **Systèmes de coordonnées** : Multiples systèmes (cartésien, sphérique, orbital, géodésique) pour différents usages
3. **Rotation terrestre** : Effets Coriolis et centrifuge qui déforment les trajectoires
4. **Corrections physiques** : Atmosphère, marées, relativité ajoutent de la précision
5. **Approche hiérarchique** : Différents niveaux de précision selon les besoins de mission

### 📊 Évaluation par Niveau

#### **Niveau Débutant** (Acquisition des bases)
- **Objectif atteint** : Comprendre que l'espace n'est pas vide et uniforme
- **Compétences développées** : Notion de corrections géophysiques, systèmes de coordonnées
- **Évaluation** : Capacité à expliquer pourquoi la Terre n'est pas sphérique

#### **Niveau Intermédiaire** (Analyse technique)
- **Objectif atteint** : Appliquer les corrections de base aux calculs de trajectoire
- **Compétences développées** : Conversion de coordonnées, évaluation d'effets dynamiques
- **Évaluation** : Capacité à calculer l'impact de la rotation terrestre sur une trajectoire

#### **Niveau Avancé** (Maîtrise experte)
- **Objectif atteint** : Hiérarchiser et appliquer les corrections selon le contexte
- **Compétences développées** : Analyse critique des approximations, optimisation de précision
- **Évaluation** : Capacité à concevoir un modèle de trajectoire incluant toutes les corrections pertinentes

### 🧩 Exercices Progressifs

#### **Exercice 1 : Coordonnées de Base (Débutant)**
Convertissez les coordonnées sphériques suivantes en cartésiennes :
- Point A : r = 6371 km, θ = 90°, φ = 0°
- Point B : r = 6671 km, θ = 45°, φ = 90°

#### **Exercice 2 : Effets de Rotation (Intermédiaire)**
Un satellite en orbite circulaire à 600 km d'altitude passe au-dessus de l'équateur à vitesse 7.5 km/s.
Calculez l'effet Coriolis maximal en magnitude et direction.

#### **Exercice 3 : Hiérarchie de Corrections (Avancé)**
Pour une mission de satellite géostationnaire, listez et justifiez l'ordre d'importance des corrections suivantes :
- Aplatissement terrestre
- Marées lunaires
- Atmosphère résiduelle
- Effets relativistes

### 🔍 Questions d'Auto-Évaluation

**Après avoir lu ce chapitre, pouvez-vous :**
1. Expliquer pourquoi nous utilisons l'ellipsoïde WGS84 plutôt qu'une sphère ?
2. Décrire les différences entre les systèmes de coordonnées cartésien, sphérique et géodésique ?
3. Calculer l'impact de l'effet Coriolis sur une trajectoire balistique ?
4. Hiérarchiser les corrections physiques selon leur importance pour différents types de mission ?
5. Expliquer pourquoi la relativité générale affecte les horloges des satellites GPS ?

### 📈 Indicateurs de Maîtrise

- **Niveau 1** : Vous comprenez que l'espace nécessite des corrections complexes
- **Niveau 2** : Vous pouvez appliquer les corrections de base aux calculs
- **Niveau 3** : Vous maîtrisez l'approche hiérarchique pour optimiser la précision

### 🔗 Références Croisées

- **Chapitre 2** : Fondements mathématiques utilisés ici
- **Chapitre 3** : Corrections appliquées aux trajectoires suborbitales
- **Chapitre 5** : Corrections cruciales pour Glenn (atmosphère + rotation)
- **Chapitre 6** : Extensions aux distances lunaires
- **Chapitre 7** : Corrections essentielles pour la rentrée atmosphérique

---

**Résumé du Chapitre 4**

La géométrie de l'espace révèle que le "vide" spatial est en réalité un environnement complexe régi par :
- Une Terre non sphérique (ellipsoïde WGS84)
- Des systèmes de coordonnées multiples pour différents besoins
- Des effets dynamiques (rotation, Coriolis, relativité)
- Une hiérarchie de corrections selon la précision requise

Katherine Johnson maîtrisait ces subtilités pour assurer la précision des trajectoires spatiales.

---

**Lectures complémentaires** :
- NIMA Technical Report TR8350.2 (WGS84 Standard)
- Vallado et al., *Fundamentals of Astrodynamics and Applications*

*"La géométrie du monde réel était bien plus complexe que les équations de nos manuels." — Katherine Johnson*
