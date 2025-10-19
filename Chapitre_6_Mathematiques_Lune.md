# Chapitre 6 : Les mathématiques de la Lune

## 🎯 Vue d'Ensemble du Chapitre

Ce chapitre explore les mathématiques complexes des missions lunaires, de l'insertion dans la trajectoire lunaire jusqu'au retour sur Terre. Nous découvrons comment les calculs deviennent exponentiellement plus difficiles quand on sort de l'orbite terrestre.

**Objectifs d'apprentissage :**
- Comprendre les transferts orbitaux Terre-Lune (trajectoires de Hohmann)
- Maîtriser les calculs d'impulsion et de timing pour les missions spatiales
- Analyser les défis des voyages interplanétaires
- Évaluer l'importance de la précision dans les missions lunaires

**Points clés :**
1. Trajectoires de Hohmann et variantes
2. Calculs d'impulsion (Δv)
3. Dynamique à trois corps (Terre-Lune-Vaisseau)
4. Précision temporelle et énergétique

---

## 🧠 Carte Mentale : Mathématiques Lunaires

```
MATHÉMATIQUES DE LA LUNE
├── 🚀 INSERTION LUNAIRE
│   ├── Orbite de stationnement terrestre
│   ├── Calcul Δv pour transfert
│   ├── Fenêtre de lancement optimale
│   └── Trajectoire balistique initiale
├── 🌓 TRANSFERTS ORBITAUX
│   ├── Trajectoire de Hohmann classique
│   │   ├── Demi-grand axe de transfert
│   │   ├── Vitesses aux points de transfert
│   │   └── Temps de transit (3 jours)
│   ├── Variantes optimisées
│   │   ├── Trajectoires plus rapides
│   │   ├── Transferts à économie d'énergie
│   │   └── Corrections en cours de route
│   └── Dynamique à trois corps
│       ├── Influence gravitationnelle Lune
│       ├── Perturbations orbitales
│       └── Corrections de trajectoire
└── 🌍 RETOUR VERS LA TERRE
    ├── Insertion en orbite lunaire
    ├── Calcul du retour (Δv lunaire)
    ├── Rentrée atmosphérique terrestre
    └── Précision d'amerrissage
```

**Légende :** 🔵 Concepts fondamentaux | 🟡 Calculs complexes | 🟢 Applications pratiques

---

## 📊 Classification : Types de Trajectoires Lunaire

| Type de Trajectoire | Temps de Transit | Δv Total (km/s) | Avantages | Inconvénients | Exemples |
|---------------------|------------------|----------------|-----------|---------------|----------|
| **Hohmann classique** | 3 jours | ~3.2 | Économe en énergie | Lent, sensible aux erreurs | Apollo 8, 10, 11 |
| **Transfert rapide** | 2-2.5 jours | ~3.5-4.0 | Plus rapide | Consomme plus de carburant | Soyouz lunaire |
| **Transfert direct** | 1-2 jours | ~4.5+ | Très rapide | Très énergivore | Missions d'urgence |
| **Transfert libre-retour** | Variable | ~3.0 | Sécurité assurée | Limité à certaines fenêtres | Apollo 13 (planifié) |
| **Transfert bi-elliptique** | 3.5-4 jours | ~3.1 | Parfois plus efficace | Plus complexe | Optimisations modernes |

## 6.1 Les équations d'insertion lunaire

### 🌙 Exemple Concret : Calcul pour Apollo 11

**Données de mission :**
- Orbite terrestre : 190 km d'altitude (rayon = 6571 km)
- Distance Terre-Lune : 384,400 km (moyenne)
- Vitesse orbitale terrestre : 7.79 km/s
- Masse de la Lune : 7.34 × 10²² kg

**Étape 1 : Calcul de la vitesse de transfert requise**
La vitesse pour atteindre la Lune depuis l'orbite terrestre :

\[
v_{\text{transfert}} = \sqrt{GM_{\oplus} \left( \frac{2}{r_{\oplus}} - \frac{1}{a_t} \right)}
\]

Où :
- \(r_{\oplus} = 6571\) km (rayon orbite terrestre)
- \(a_t = \frac{r_{\oplus} + r_{\text{Lune}}}{2} = \frac{6571 + 384400}{2} = 195485.5\) km

\[
v_{\text{transfert}} = \sqrt{3.986 \times 10^{14} \left( \frac{2}{6.571 \times 10^6} - \frac{1}{1.954855 \times 10^8} \right)} = 10.84 \text{ km/s}
\]

**Étape 2 : Calcul du Δv requis**
\[
\Delta v = v_{\text{transfert}} - v_{\text{orbitale}} = 10.84 - 7.79 = 3.05 \text{ km/s}
\]

**Étape 3 : Temps de transit (loi de Kepler)**
\[
T = \pi \sqrt{\frac{a_t^3}{GM_{\oplus}}} = 3.1416 \times \sqrt{\frac{(1.954855 \times 10^8)^3}{3.986 \times 10^{14}}} = 2,592,000 \text{ s} \approx 3.0 \text{ jours}
\]

### 📈 Schéma : Profil de Vitesse Apollo

```
PROFIL DE VITESSE APOLLO 11
     │
12.0 │                ┌── Décollage Terre
     │               /
11.0 │              ├─ Insertion orbite terrestre
     │             /
10.0 │            ├─ Transfert vers Lune (vitesse max)
     │           /
 9.0 │          ├─ Arrivée Lune
     │         /
 8.0 │        ├─ Insertion orbite lunaire
     │       /
 7.0 │      ├─ Décollage Lune
     │     /
 6.0 │    ├─ Transfert vers Terre
     │   /
 5.0 │  ├─ Rentrée atmosphère
     │ /
 4.0 │ ├─ Amerrissage
     │
     └─────────────────────────
       Décollage  Insertion   Arrivée   Décollage  Rentrée
       Terre      transfert   Lune      Lune       Terre
```

**Analyse :** 5 changements majeurs de vitesse, total Δv ≈ 6.5 km/s pour mission aller-retour.

### 🧮 Activité 1 : Calcul de Fenêtre de Lancement (Niveau Intermédiaire)

**Objectif :** Comprendre les contraintes temporelles des missions lunaires

**Problème :** La Lune s'éloigne de la Terre à une vitesse d'environ 1 km/s. Calculez combien de temps une fenêtre de lancement reste ouverte.

**Données :**
- Distance Terre-Lune : 384,400 km
- Vitesse orbitale de la Lune autour de la Terre : ~1.02 km/s
- Tolérance de précision : ±50 km sur le point d'insertion lunaire

**Calcul :**
1. Temps pour que la Lune se déplace de 50 km : t = distance/vitesse = 50/1.02 ≈ 49 secondes
2. Fenêtre de lancement : ±24.5 secondes autour du moment optimal

**Discussion :**
- Pourquoi les lancements lunaires doivent être si précis ?
- Quels facteurs limitent la taille de la fenêtre de lancement ?
- Comment les ingénieurs compensent-ils les imprécisions ?

💡 **Conseil : Synchronisation Orbitale**
> Les missions lunaires doivent synchroniser trois orbites : vaisseau autour de Terre, Lune autour de Terre, et vaisseau autour de Lune. Cette "danse cosmique" nécessite une précision de l'ordre de la seconde.

### Du chemin terrestre vers la Lune

Une mission lunaire est exponentiellement plus complexe qu'une orbite terrestre. Non seulement la capsule doit quitter l'orbite terrestre, mais elle doit le faire avec une trajectoire très précise pour :
1. Quitter l'orbite terrestre
2. Traverser l'espace interplanétaire
3. Entrer en orbite lunaire
4. Revenir à la Terre

### 🏞️ Activité 2 : Orbite de Stationnement (Niveau Débutant)

**Objectif :** Comprendre l'importance de l'orbite de parking dans les missions lunaires

**Calcul simple :**
Une orbite circulaire à 190 km d'altitude a un rayon de 6,571 km. Calculez la vitesse orbitale.

**Formule :**
\[
v = \sqrt{\frac{GM}{r}} = \sqrt{\frac{3.986 \times 10^{14}}{6.571 \times 10^6}} = 7.79 \text{ km/s}
\]

**Questions :**
1. Pourquoi utiliser une orbite de stationnement plutôt que lancer directement vers la Lune ?
2. Quel avantage offre cette orbite pour les calculs de trajectoire ?
3. Comment Katherine Johnson calculait-elle ces orbites de parking ?

⚠️ **Attention : Stabilité Orbitale**
> Une orbite de stationnement n'est pas permanente. L'atmosphère résiduelle à 190 km cause une décélération lente (drag atmosphérique) qui nécessite des corrections périodiques.

### 📊 Tableau : Comparaison Orbites de Stationnement

| Altitude (km) | Rayon (km) | Vitesse (km/s) | Période (min) | Durée viable | Utilisation |
|---------------|------------|----------------|---------------|--------------|-------------|
| **160** | 6531 | 7.84 | 88.5 | 2-3 jours | Stationnement court |
| **190** | 6571 | 7.79 | 90.2 | 1-2 semaines | Apollo standard |
| **300** | 6681 | 7.73 | 92.6 | Plusieurs mois | Station spatiale |
| **400** | 6781 | 7.67 | 94.7 | Années | Orbites opérationnelles |

**Observation :** Plus l'altitude est élevée, plus l'orbite est stable mais plus le Δv pour atteindre la Lune est important.

### 🌙 Logique de Calcul Pas à Pas : Δv pour Transfert Lunaire

**Étape 1 : Définir les orbites**
- Orbite initiale : r₁ = rayon orbite terrestre = 6,571 km
- Orbite finale : r₂ = distance Terre-Lune = 384,400 km

**Étape 2 : Calculer le demi-grand axe de transfert**
\[
a_t = \frac{r_1 + r_2}{2} = \frac{6571 + 384400}{2} = 195,485.5 \text{ km}
\]

**Étape 3 : Vitesse à l'apogée (point de départ)**
\[
v_1 = \sqrt{GM \left( \frac{2}{r_1} - \frac{1}{a_t} \right)} = \sqrt{3.986e14 \left( \frac{2}{6571000} - \frac{1}{195485500} \right)} = 10.84 \text{ km/s}
\]

**Étape 4 : Vitesse orbitale actuelle**
\[
v_{\text{orbit}} = \sqrt{\frac{GM}{r_1}} = 7.79 \text{ km/s}
\]

**Étape 5 : Δv requis**
\[
\Delta v = v_1 - v_{\text{orbit}} = 10.84 - 7.79 = 3.05 \text{ km/s}
\]

**Étape 6 : Vérification énergétique**
Cette impulsion correspond à environ 25 tonnes de carburant pour Apollo (masse ~45 tonnes).

✓ **Bonne Pratique : Vérification Croisée**
> Katherine Johnson vérifiait toujours ses calculs Δv de trois manières différentes : algébrique, géométrique, et numérique. Cela réduisait les erreurs à moins de 0.01%.

### 6.2 Les transferts orbitaux de Hohmann et leurs variantes

#### La trajectoire de Hohmann classique

En 1925, Walter Hohmann découvrit une trajectoire économe en énergie pour transférer entre deux orbites circulaires. Pour un transfert Terre-Lune :

**Conditions** :
- Orbite initiale autour de la Terre : rayon \(r_1\)
- Orbite finale (orbite autour de la Lune) : rayon \(r_2\)
- Orbite de transfert (ellipse) : périgée à \(r_1\), apogée à \(r_2\)

**Les calculs** :

Le demi-grand axe de l'ellipse de transfert est :

\[
a_t = \frac{r_1 + r_2}{2}
\]

Les vitesses requises aux deux points sont calculées par :

\[
v_1 = \sqrt{GM \left( \frac{2}{r_1} - \frac{1}{a_t} \right)}
\]

\[
v_2 = \sqrt{GM \left( \frac{2}{r_2} - \frac{1}{a_t} \right)}
\]

Les impulsions (changements de vitesse) sont alors :

\[
\Delta v_1 = v_1 - v_{\text{orbital, 1}}
\]

\[
\Delta v_2 = v_{\text{orbital, 2}} - v_2
\]

#### Le temps de transfert

Le temps pour parcourir la trajectoire de Hohmann (demi-ellipse) est donné par la troisième loi de Kepler :

\[
T = \pi \sqrt{\frac{a_t^3}{GM}}
\]

Pour un transfert Terre-Lune, cela donne typiquement environ **3 jours**.

#### Variantes et optimisations

La trajectoire de Hohmann n'est pas toujours optimale pour les missions Apollo, car elle prend 3 jours. Les missions réelles utilisaient souvent des variantes :

- **Trajectoires plus rapides** : utiliser plus de carburant pour traverser en 2-2.5 jours
- **Trajectoires d'insertion directe** : commencer la correction de cap dès le lancement, plutôt que depuis une orbite de stationnement

Katherine Johnson et ses collègues devaient calculer ces variantes pour évaluer les compromis entre temps de vol et consommation de carburant.

### 6.3 Calcul du retour atmosphérique

#### Les enjeux

Le retour depuis la Lune est plus complexe que l'insertion, car le vaisseau arrive à une vitesse très élevée — environ **11 km/s** — qui est beaucoup plus rapide que la vitesse orbitale terrestre (7.8 km/s).

L'énergie cinétique qu'il faut dissiper est énorme :

\[
E_k = \frac{1}{2} m v^2 = \frac{1}{2} m (11 \text{ km/s})^2 = 60.5 \, m \, (\text{km/s})^2
\]

Comparé à une rentrée de capsule Mercury ou Gemini, qui arrivait à environ 8 km/s, cette énergie supplémentaire pose des défis thermiques et aérodynamiques majeurs.

#### Angle d'entrée optimal

L'angle avec lequel la capsule entre dans l'atmosphère est critique. Trop raide, et elle se désintègre sous la chaleur. Pas assez raide, et elle peut rebondir dans l'espace comme une pierre sur l'eau.

L'angle d'entrée \(\gamma\) (gamma, mesuré par rapport à l'horizontale) doit généralement être entre **-5°** et **-7°** pour une rentrée Apollo.

Le calcul de cet angle implique de résoudre des équations couplées :
- Équations du mouvement en 3D
- Modèle d'atmosphère varié
- Modèle de friction thermique
- Équations thermiques du bouclier thermique

#### Friction et perte d'énergie

Une fois dans l'atmosphère, la capsule expérimente une force de traînée énorme. Cette traînée est modélisée par :

\[
F_{\text{drag}} = \frac{1}{2} \rho v^2 C_D A
\]

Où :
- \(\rho\) est la densité de l'air (qui change rapidement avec l'altitude)
- \(v\) est la vitesse
- \(C_D\) est le coefficient de traînée (qui dépend de la forme et du flux)
- \(A\) est la section transversale

La densité de l'air varie de façon exponentielle avec l'altitude (jusqu'à environ 80 km), puis à pente plus douce au-delà. Katherine Johnson devait utiliser des modèles d'atmosphère standard (comme le modèle COSPAR) et intégrer numériquement les équations du mouvement pour prédire :
- L'altitude et la vitesse à chaque instant
- La force g subie par l'astronaute
- La trajectoire finale

#### Dissipation de chaleur

L'énergie cinétique énorme est convertie en chaleur à deux endroits :
1. **Sur le bouclier thermique** : la plupart de l'énergie est dissipée ici
2. **Dans l'atmosphère** : crée un plasma lumineux autour de la capsule

Le calcul de la température du bouclier thermique requiert de résoudre l'équation de la chaleur en 3D, ce qui était au-delà des capacités computationnelles de l'époque. Pour ce qui était utilisable pour les missions Apollo, on employait des modèles simplifiés et semi-empiriques basés sur des tests d'hypersonique en laboratoire.

### Résumé du Chapitre 6

- Les missions lunaires impliquent des transferts orbitaux complexes
- Les trajectoires de Hohmann sont les plus économes en énergie, mais pas toujours optimales
- Le retour atmosphérique est un défi thermique et aérodynamique majeur
- Le calcul de la trajectoire de retour implique intégration numérique complexe et modèles d'atmosphère

## 6.4 Références Croisées

- **Chapitre 2** : Lois de Kepler appliquées aux transferts multi-corps
- **Chapitre 4** : Corrections géophysiques étendues aux distances lunaires
- **Chapitre 5** : Comparaison avec les orbites terrestres (complexité accrue)
- **Chapitre 7** : Rentrée lunaire vs rentrée terrestre (vitesses plus élevées)
- **Chapitre 8** : Katherine travaille sur ces calculs avec ordinateurs avancés
- **Annexes A.3** : Dérivations des équations orbitales utilisées

---

**Lectures complémentaires** :
- NASA Apollo Technical Documentation
- Vallado & Curtis, *Orbital Mechanics for Engineering Students* (Chapitre sur Hohmann transfers)

*"Les équations de retour étaient parmi les plus complexes que nous ayons jamais résolues. Une erreur signifiait que l'astronaute ne rentrerait pas vivant." — Katherine Johnson*
