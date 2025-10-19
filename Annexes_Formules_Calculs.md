# Annexes : Formules et Calculs Détaillés

## 📐 ANNEXE A : Formules Fondamentales des Mathématiques Spatiales

### A.1 Lois de Kepler et Mécanique Céleste

#### Loi des aires (Deuxième loi de Kepler)
\[
\frac{dA}{dt} = \frac{1}{2} r^2 \dot{\theta} = \frac{\sqrt{\mu p}}{2}
\]
Où :
- \(A\) = aire balayée
- \(r, \theta\) = coordonnées polaires
- \(\mu = GM\) = paramètre gravitationnel
- \(p\) = paramètre orbital

#### Loi des périodes (Troisième loi de Kepler)
\[
T^2 = \frac{4\pi^2}{GM} a^3
\]
**Dérivation pas à pas :**

**Étape 1 :** De la loi des aires, aire totale d'une orbite circulaire :
\[
A = \pi a^2
\]

**Étape 2 :** Vitesse aréolaire constante :
\[
\frac{dA}{dt} = \frac{\sqrt{\mu p}}{2} = \frac{\sqrt{\mu a}}{2} \quad (\text{car } p = a \text{ pour cercle})
\]

**Étape 3 :** Aire totale :
\[
A = \frac{\sqrt{\mu a}}{2} \times T
\]

**Étape 4 :** Substitution :
\[
\pi a^2 = \frac{\sqrt{\mu a}}{2} T
\]

**Étape 5 :** Résolution pour T² :
\[
T^2 = \frac{4\pi^2 a^3}{\mu}
\]

#### Équation de Kepler (orbites elliptiques)
\[
M = E - e \sin E
\]
Où :
- \(M\) = anomalie moyenne
- \(E\) = anomalie excentrique
- \(e\) = excentricité

**Résolution itérative (méthode de Newton) :**

**Étape 1 :** Estimation initiale \(E_0 = M\)

**Étape 2 :** Itération :
\[
E_{n+1} = E_n - \frac{E_n - e \sin E_n - M}{1 - e \cos E_n}
\]

**Étape 3 :** Convergence : |E_{n+1} - E_n| < 10^{-8}

### A.2 Systèmes de Coordonnées Spatiales

#### Transformation cartésien → sphérique
\[
\begin{align}
r &= \sqrt{x^2 + y^2 + z^2} \\
\theta &= \cos^{-1}\left(\frac{z}{r}\right) \\
\phi &= \tan^{-1}\left(\frac{y}{x}\right)
\end{align}
\]

#### Coordonnées orbitales (éléments kepleriens)
\[
\begin{align}
a &= \text{demi-grand axe} \\
e &= \text{excentricité} \\
i &= \text{inclinaison} \\
\Omega &= \text{longitude du nœud ascendant} \\
\omega &= \text{argument du périastre} \\
\nu &= \text{anomalie vraie}
\end{align}
\]

### A.3 Équations du Mouvement Orbital

#### Équation de Lagrange (forme polaire)
\[
\frac{d^2 u}{d\theta^2} + u = -\frac{\mu}{h^2}
\]
Où :
- \(u = 1/r\) = variable auxiliaire
- \(h\) = moment cinétique spécifique

#### Équation de trajectoire en coordonnées polaires
\[
\frac{d^2}{dr^2}\left(\frac{1}{r}\right) + \frac{1}{r} = -\frac{\mu}{h^2}
\]

## 🔢 ANNEXE B : Calculs Numériques Détaillés

### B.1 Méthode d'Euler pour l'Intégration Numérique

**Problème :** Résoudre \(\frac{dv}{dt} = a(t)\) avec v(0) = v₀

**Algorithme pas à pas :**

**Étape 1 :** Initialisation
- t = 0, v = v₀
- Δt = pas de temps (typiquement 0.1-1.0 s)

**Étape 2 :** Calcul de l'accélération
- a = f(t, v) [loi de Newton, gravitation, etc.]

**Étape 3 :** Mise à jour de la vitesse
\[
v_{n+1} = v_n + a_n \Delta t
\]

**Étape 4 :** Mise à jour de la position
\[
x_{n+1} = x_n + v_n \Delta t
\]

**Étape 5 :** Incrémentation du temps
- t = t + Δt

**Étape 6 :** Répétition jusqu'à t_final

**Erreur d'approximation :** O(Δt) - diminue avec Δt plus petit

### B.2 Calcul du Δv pour Transferts Orbitaux

**Exemple : Apollo 11 (Terre → Lune)**

**Données :**
- r₁ = 6,571 km (orbite terrestre basse)
- r₂ = 384,400 km (orbite lunaire)
- μ = 3.986 × 10¹⁴ m³/s²

**Calcul du demi-grand axe de transfert :**
\[
a_t = \frac{r_1 + r_2}{2} = \frac{6571000 + 384400000}{2} = 195485500 \text{ m}
\]

**Vitesses de transfert :**
\[
\begin{align}
v_1 &= \sqrt{\mu \left( \frac{2}{r_1} - \frac{1}{a_t} \right)} = \sqrt{3.986e14 \left( \frac{2}{6.571e6} - \frac{1}{1.954855e8} \right)} = 10840 \text{ m/s} \\
v_2 &= \sqrt{\mu \left( \frac{2}{r_2} - \frac{1}{a_t} \right)} = \sqrt{3.986e14 \left( \frac{2}{3.844e8} - \frac{1}{1.954855e8} \right)} = 2380 \text{ m/s}
\end{align}
\]

**Δv total :**
\[
\Delta v = |v_1 - v_{\text{circulaire TE}}| + |v_2 - v_{\text{circulaire Lune}}| \approx 3150 \text{ m/s}
\]

### B.3 Correction pour la Rotation Terrestre

**Effet Coriolis sur une trajectoire :**

**Force de Coriolis :**
\[
\vec{F}_c = -2m \vec{\omega} \times \vec{v}
\]

**Déviation latérale pour un missile :**
\[
\Delta x = \frac{1}{2} \omega \cos \phi \ t^2 \ v
\]

**Exemple numérique :**
- ω = 7.29 × 10^{-5} rad/s
- φ = 28.5° (Cap Canaveral)
- v = 2500 m/s (vitesse missile)
- t = 300 s (durée de vol)

**Calcul :**
\[
\Delta x = \frac{1}{2} \times 7.29e-5 \times \cos(28.5°) \times 300^2 \times 2500 \approx 520 \text{ m}
\]

## 📊 ANNEXE C : Tables de Données et Constantes

### C.1 Constantes Physiques Utiles

| Constante | Valeur | Unité | Utilisation |
|-----------|--------|-------|-------------|
| **G** | 6.67430 × 10^{-11} | m³ kg⁻¹ s⁻² | Constante gravitationnelle |
| **M_⊕** | 5.972 × 10^{24} | kg | Masse de la Terre |
| **R_⊕** | 6.371 × 10^6 | m | Rayon terrestre équatorial |
| **ω_⊕** | 7.292 × 10^{-5} | rad/s | Vitesse angulaire terrestre |
| **μ_⊕** | 3.986 × 10^{14} | m³/s² | Paramètre gravitationnel terrestre |

### C.2 Données Orbitales des Missions Historiques

| Mission | Altitude (km) | Période (min) | Vitesse (km/s) | Δv (m/s) |
|---------|---------------|---------------|----------------|-----------|
| **Mercury-Redstone 3** (Shepard) | 190 | 90.2 | 7.79 | 0 |
| **Mercury-Atlas 6** (Glenn) | 260 | 88.5 | 7.84 | 50 |
| **Apollo 11** (Lune) | 190 → 384400 | 90.2 → 64800 | 7.79 → 0.97 | 3150 |
| **ISS** | 408 | 92.6 | 7.66 | 0 |

### C.3 Exemples d'Orbites Elliptiques

| Satellite | a (km) | e | Période | Périgée (km) | Apogée (km) |
|-----------|--------|---|---------|--------------|-------------|
| **GPS** | 26560 | 0.01 | 12h | 20180 | 32940 |
| **Hubble** | 6930 | 0.0002 | 97 min | 586 | 620 |
| **Molniya** | 26554 | 0.74 | 12h | 508 | 39787 |

## 🧩 ANNEXE D : Exercices et Problèmes Résolus

### D.1 Exercices de Niveau Débutant

**Exercice 1 : Calcul de vitesse orbitale**
Une station spatiale orbite à 400 km d'altitude. Calculez sa vitesse.

**Solution :**
\[
\begin{align}
r &= 6371 + 400 = 6771 \text{ km} = 6.771 \times 10^6 \text{ m} \\
v &= \sqrt{\frac{GM}{r}} = \sqrt{\frac{3.986 \times 10^{14}}{6.771 \times 10^6}} = 7660 \text{ m/s} = 7.66 \text{ km/s}
\end{align}
\]

**Exercice 2 : Période orbitale**
Calculez la période d'un satellite à 2000 km d'altitude.

**Solution :**
\[
\begin{align}
r &= 6371 + 2000 = 8371 \text{ km} = 8.371 \times 10^6 \text{ m} \\
T &= 2\pi \sqrt{\frac{r^3}{GM}} = 2\pi \sqrt{\frac{(8.371e6)^3}{3.986e14}} = 7640 \text{ s} = 127 \text{ min}
\end{align}
\]

### D.2 Exercices de Niveau Intermédiaire

**Exercice 3 : Transfert de Hohmann**
Calculez le Δv nécessaire pour aller de l'orbite terrestre basse (200 km) à l'orbite géostationnaire (35786 km).

**Solution :**
\[
\begin{align}
r_1 &= 6371 + 200 = 6571 \text{ km} \\
r_2 &= 42164 \text{ km} \\
a_t &= \frac{6571 + 42164}{2} = 24367.5 \text{ km} \\
v_1 &= \sqrt{3.986e14 \left( \frac{2}{6.571e6} - \frac{1}{2.43675e7} \right)} = 7790 \text{ m/s} \\
v_{\text{circ1}} &= \sqrt{\frac{3.986e14}{6.571e6}} = 7790 \text{ m/s} \\
v_2 &= \sqrt{3.986e14 \left( \frac{2}{4.2164e7} - \frac{1}{2.43675e7} \right)} = 1920 \text{ m/s} \\
v_{\text{circ2}} &= \sqrt{\frac{3.986e14}{4.2164e7}} = 3070 \text{ m/s} \\
\Delta v &= |v_1 - v_{\text{circ1}}| + |v_2 - v_{\text{circ2}}| = 0 + 1150 = 1150 \text{ m/s}
\end{align}
\]

### D.3 Exercices de Niveau Avancé

**Exercice 4 : Équation de Kepler**
Résolvez M = 2.5 rad pour une orbite d'excentricité e = 0.1.

**Solution itérative :**
\[
\begin{align}
E_0 &= 2.5 \\
E_1 &= 2.5 - \frac{2.5 - 0.1 \sin 2.5 - 2.5}{1 - 0.1 \cos 2.5} = 2.5 - \frac{0}{0.884} = 2.5 \\
E_2 &= 2.5 \text{ (convergé)}
\end{align}
\]

**Exercice 5 : Rentrée atmosphérique**
Calculez la décélération maximale lors de la rentrée Apollo.

**Données :** v = 11 km/s, ρ = 0.001 kg/m³, C_d = 1.5, A = 12 m², m = 5500 kg

**Solution :**
\[
\begin{align}
F_d &= \frac{1}{2} \rho v^2 C_d A = \frac{1}{2} \times 0.001 \times 121000000 \times 1.5 \times 12 = 1,089,000 \text{ N} \\
a &= \frac{F_d}{m} = \frac{1,089,000}{5500} = 198 \text{ m/s}^2 = 20.2g
\end{align}
\]

## 📈 ANNEXE E : Index des Équations par Complexité

| Complexité | Équation | Chapitre | Utilisation |
|------------|----------|----------|-------------|
| **Basique** | \(v = \sqrt{GM/r}\) | 2 | Vitesse orbitale circulaire |
| **Intermédiaire** | \(T = 2\pi \sqrt{a^3/GM}\) | 2 | Loi des périodes |
| **Avancée** | \(M = E - e \sin E\) | 2 | Équation de Kepler |
| **Expert** | \(\vec{a} = -\frac{GM}{r^2} \hat{r} + \vec{a}_{ext}\) | 3 | Équation du mouvement 3D |

**Légende de complexité :**
- **Basique** : Algèbre simple
- **Intermédiaire** : Trigonométrie, logarithmes
- **Avancée** : Équations différentielles
- **Expert** : Systèmes vectoriels, calcul tensoriel
