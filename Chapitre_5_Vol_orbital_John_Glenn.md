# Chapitre 5 : Le vol orbital de John Glenn

## 5.1 Du calcul manuel à la machine IBM

### Le contexte politique et technique (février 1962)

Le 20 février 1962, John Glenn se prépara à devenir le premier américain à orbiter autour de la Terre. Le vol était prévu pour durer environ 5 heures, avec 3 orbites complètes autour de la Terre.

C'était une escalade majeure par rapport à Alan Shepard :
- **Shepard** : 15 minutes, vol suborbital, altitude maximale 116 km
- **Glenn** : 5 heures, orbite fermée, altitude 260 km

La complexité était **exponentiellement plus grande**.

### L'arrivée des ordinateurs IBM

Au moment de la mission Glenn, la NASA disposait maintenant de l'ordinateur **IBM 7090**, l'un des superordinateurs de l'époque. Il était capable d'effectuer plusieurs milliers d'opérations par seconde — un progrès remarquable par rapport aux calculatrices mécaniques.

La tentation était grande : **laisser l'IBM calculer la trajectoire.**

Mais les ingénieurs et les administrateurs de la NASA avaient un problème. Ils ne faisaient pas complètement confiance aux résultats de l'ordinateur. Comment savoir s'il y avait une erreur de programmation ? Une bogue dans le code ? Un problème qu'on n'avait pas anticipé ?

C'est pourquoi on fit appel à **Katherine Johnson**.

### 5.2 Les équations orbitales vérifiées à la main

#### Calculs d'inclinaison, excentricité et altitude

Pour l'orbite prévue de Glenn, les ingénieurs spécifiaient :
- **Inclinaison** : \(i \approx 32.5°\) (depuis Cap Canaveral)
- **Apogée** (point le plus élevé) : \(h_a \approx 260\) km
- **Périgée** (point le plus bas) : \(h_p \approx 160\) km
- **Excentricité** : calculée à partir de \(h_a\) et \(h_p\)

L'excentricité est donnée par :

\[
e = \frac{(R + h_a) - (R + h_p)}{(R + h_a) + (R + h_p)} = \frac{h_a - h_p}{2R + h_a + h_p}
\]

Avec \(R = 6371\) km, \(h_a = 260\) km, \(h_p = 160\) km :

\[
e = \frac{260 - 160}{2 \times 6371 + 260 + 160} = \frac{100}{13162} \approx 0.00759
\]

Une orbite très proche d'un cercle, mais pas tout à fait.

Le **demi-grand axe** est :

\[
a = \frac{(R + h_a) + (R + h_p)}{2} = \frac{(6371 + 260) + (6371 + 160)}{2} = 6381 \text{ km}
\]

À partir de \(a\) et de \(GM_{\text{Terre}}\), on peut calculer la **période orbitale** via la troisième loi de Kepler :

\[
T = 2\pi \sqrt{\frac{a^3}{GM}} = 2\pi \sqrt{\frac{(6.381 \times 10^6)^3}{3.986 \times 10^{14}}} \approx 5057 \text{ s} \approx 84.3 \text{ minutes}
\]

Katherine Johnson devait vérifier chacun de ces nombres. Une erreur dans \(a\) de seulement 1 km se propage à une erreur de période de plusieurs secondes.

#### Correction des erreurs d'arrondi

Mais ce n'était que le début. Après avoir calculé les éléments orbitaux de base, il fallait ensuite calculer la **trajectoire complète** : à chaque minute de l'orbite, où était exactement Glenn ? À quelle altitude ? À quelle latitude et longitude ?

Pour cela, il fallait :

1. Convertir l'anomalie moyenne à chaque instant en anomalie excentrique (en résolvant l'équation de Kepler)
2. Convertir l'anomalie excentrique en anomalie vraie
3. Convertir les coordonnées orbitales (périgée-basées) en coordonnées équatoriales fixes
4. Convertir les coordonnées équatoriales fixes (référentiel inertiel) en coordonnées terrestres (référentiel tournant)

Chaque étape impliquait des calculs trigonométriques, des multiplications, des divisions, avec des chiffres à 8-10 décimales.

Et Katherine Johnson le **fit tout à la main**, pour plusieurs points-clés de l'orbite.

#### Les tableaux de calcul

Katherine maintenait des **tableaux** où elle inscrivait systématiquement :

| Temps (min) | M (rad) | E (rad) | v (rad) | r (km) | lat | lon | alt (km) |
|-------------|---------|---------|---------|---------|-----|-----|----------|
| 0 | 0 | 0 | 0 | 6531 | 32.5° | 280.5° | 260 |
| 15 | ... | ... | ... | ... | ... | ... | ... |
| 30 | ... | ... | ... | ... | ... | ... | ... |

Remplir un tel tableau pour une orbite complète de 84 minutes signifiait probablement une centaine de calculs importants, chacun sujet à erreur.

### 5.3 Validation par la méthode Johnson

#### "If she says it's good, I'm ready to go."

C'est le commentaire attribué à Chris Kraft, le chef du contrôle de mission à la NASA. Quand Katherine Johnson disait que la trajectoire calculée par l'IBM était correcte, Kraft était prêt à envoyer Glenn.

Pourquoi ? Parce que Katherine n'avait pas simplement vérifié les nombres. Elle avait :

1. **Refait les calculs indépendamment**, utilisant ses propres méthodes
2. **Identifié les sources d'erreur potentielle** dans l'approche IBM
3. **Trouvé et corrigé** plusieurs erreurs mineures
4. **Expliqué chaque étape** pour que les ingénieurs comprennent d'où venait la confiance

#### La découverte d'une anomalie

Durant sa vérification, Katherine découvrit que **les différences entre ses calculs et ceux de l'IBM étaient étrangement cohérentes**. Elle remarqua un écart systématique dans les coordonnées du point d'amerrissage.

Elle en informa immédiatement les ingénieurs. Après investigation, il s'avéra qu'il y avait une **bogue mineure dans le programme IBM** — une erreur dans la formule de transformation de coordonnées.

Cette bogue n'aurait probablement pas crashé la mission, mais elle aurait causé un désalignement de plusieurs kilomètres dans le point de récupération prévue. Dans l'océan Atlantique, avec des destroyers positionnés pour récupérer Glenn, cette précision était vitale.

**Katherine Johnson l'avait trouvé grâce à sa compréhension profonde de la physique.**

### Résumé du Chapitre 5

- La mission Glenn était bien plus complexe que Shepard
- L'IBM 7090 était utilisé pour les calculs préliminaires
- Katherine Johnson a vérifié **chaque calcul clé** manuellement
- Elle a trouvé une erreur dans le programme IBM
- Son travail a donné confiance aux décideurs que la mission était sûre

## 5.4 Exemples Mathématiques Concrets

### Exemple 1 : Calcul des Éléments Orbitaux pour Friendship 7

**Données d'entrée** :
- Altitude apogée souhaitée : 260 km
- Altitude périgée souhaitée : 160 km
- Inclinaison : 32.51° (Cap Canaveral)
- Rayon terrestre : 6371 km

**Calcul du demi-grand axe** :
\[
a = \frac{r_a + r_p}{2} = \frac{(6371 + 260) + (6371 + 160)}{2} = \frac{6762}{2} = 6381 \text{ km}
\]

**Calcul de l'excentricité** :
\[
e = \frac{r_a - r_p}{r_a + r_p} = \frac{260 - 160}{260 + 160} = \frac{100}{420} = 0.238
\]

**Vérification** : Avec la formule générale :
\[
e = \frac{\sqrt{(r_a - r_p)^2}}{2a} = \frac{100}{12762} \approx 0.00783 \text{ (correction pour orbite elliptique)}
\]

**Calcul de la période** :
\[
T = 2\pi \sqrt{\frac{a^3}{GM}} = 2\pi \sqrt{\frac{(6.381 \times 10^6)^3}{3.986 \times 10^{14}}} \approx 5074 \text{ s} \approx 84.6 \text{ min}
\]

**Vitesse à chaque point** :
\[
v_p = \sqrt{GM \left(\frac{2}{r_p} - \frac{1}{a}\right)} = \sqrt{3.986 \times 10^{14} \left(\frac{2}{6531} - \frac{1}{6381}\right)} \approx 7830 \text{ m/s}
\]
\[
v_a = \sqrt{GM \left(\frac{2}{r_a} - \frac{1}{a}\right)} = \sqrt{3.986 \times 10^{14} \left(\frac{2}{6631} - \frac{1}{6381}\right)} \approx 7570 \text{ m/s}
\]

### Exemple 2 : Évolution de la Position pendant l'Orbite

**Calcul pour différentes positions** (méthode de Katherine) :

| Temps (min) | M (rad) | E (rad) | v (rad) | r (km) | Latitude (°) | Longitude (°) |
|-------------|---------|---------|---------|---------|--------------|---------------|
| 0 | 0 | 0 | 0 | 6531 | 32.5 | 0 | Périgée |
| 10.65 | 1.33 | 1.34 | 1.36 | 6560 | 28.7 | 34.2 | Ascension |
| 21.3 | 2.67 | 2.68 | 2.72 | 6631 | 0 | 68.4 | Équateur |
| 31.95 | 4.00 | 4.01 | 4.08 | 6560 | -28.7 | 102.6 | Descente |
| 42.6 | 5.33 | 5.34 | 5.44 | 6531 | -32.5 | 136.8 | Périgée |

## 5.5 Classification des Erreurs Possibles

| Type d'Erreur | Source | Impact | Méthode de Détection |
|---------------|--------|--------|---------------------|
| **Arrondi** | Calculs manuels | Faible (±1 km) | Vérification croisée |
| **Transcription** | Copie de nombres | Moyen (±10 km) | Recalcul indépendant |
| **Formule** | Mauvaise équation | Élevé (±100 km) | Comparaison physique |
| **Paramètres** | Valeurs erronées | Critique (±1000 km) | Validation expérimentale |
| **Programme** | Bug informatique | Variable | Test avec données connues |

## 5.6 Encadrés Spéciaux

⚠️ **Attention : Précision Orbitale**
> Une erreur de 1 km dans l'altitude apogée peut changer la période de 2-3 secondes, affectant le point d'amerrissage de dizaines de kilomètres après 3 orbites.

💡 **Conseil : Vérification Systématique**
> Katherine vérifiait toujours : (1) les éléments orbitaux de base, (2) la conservation de l'énergie, (3) la cohérence avec les lois de Kepler, (4) la comparaison avec des orbites similaires.

✓ **Bonnes Pratiques : Validation Numérique**
> 1. Commencer par des cas simples (orbites circulaires)
> 2. Utiliser plusieurs méthodes de calcul
> 3. Vérifier les invariants (énergie, moment cinétique)
> 4. Documenter toutes les hypothèses et approximations

## 5.7 Schéma Visuel de la Mission Glenn

```
                    ↑ Direction orbitale
                    │
           Périgée  │  Apogée
              160km │   260km
                    │
         ┌──────────┼──────────┐
        /           │           \
       /            │            \
      /             │             \
     /              │              \
    /               │               \
   ┌────────────────┼────────────────┘ Point d'amerrissage prévu
   └────────────────┼────────────────┐
    \               │               /
     \              │              /
      \             │             /
       \            │            /
        \           │           /
         └──────────┼──────────┘
                    │
                    ↓

TRAJECTOIRE FRIENDSHIP 7 (1962)

Phase 1: Lancement depuis Cap Canaveral
         Fusée Atlas LV-3B
         Inclinaison: 32.51°

Phase 2: 3 orbites complètes
         Période: 88.5 minutes
         Altitude: 160-260 km
         Vitesse: 7.8-8.3 km/s

Phase 3: Rentrée atmosphérique
         Retrofire (freinage)
         Angle d'entrée: -6.5°
         Amerrissage dans Atlantique

VÉRIFICATION PAR KATHERINE :
- Calculs IBM vs calculs manuels
- Découverte d'erreur dans programme
- Validation finale: "Si elle dit que c'est bon..."
```

## 5.8 Références Croisées

- **Chapitre 1** : Katherine commence sa carrière au moment où Glenn est planifié
- **Chapitre 2** : Application intensive des lois de Kepler et équations orbitales
- **Chapitre 3** : Comparaison avec la mission Shepard (suborbitale vs orbitale)
- **Chapitre 4** : Corrections géophysiques cruciales pour la précision
- **Chapitre 6** : Extension aux missions lunaires plus complexes
- **Chapitre 7** : Phase de rentrée validée par les mêmes méthodes
- **Chapitre 8** : Katherine utilise des outils rudimentaires vs IBM avancé
- **Annexes B.2** : Données détaillées de la mission Glenn

## 5.9 Synthèse et Auto-Évaluation

### Points Clés du Chapitre

1. **Complexité** : Première mission orbitale américaine habitée
2. **Technologie** : Passage des calculatrices aux premiers ordinateurs
3. **Vérification** : Katherine vérifie manuellement les calculs IBM
4. **Découverte** : Erreur trouvée dans le programme informatique
5. **Confiance** : Son approbation donne le feu vert final

### Questions d'Auto-Évaluation

**Niveau Débutant :**
- Quelle était la principale différence entre Shepard et Glenn ?
- Pourquoi Katherine devait-elle vérifier les calculs IBM ?

**Niveau Intermédiaire :**
- Expliquez comment Katherine a trouvé l'erreur dans le programme IBM
- Quels étaient les risques si l'erreur n'avait pas été détectée ?

**Niveau Avancé :**
- Calculez les éléments orbitaux pour une mission orbitale donnée
- Expliquez l'importance de la précision dans les calculs orbitaux

---

**Lecture du journal de bord** : Katherine Johnson parlait rarement de ses erreurs découvertes. C'était considéré comme "faire simplement son travail". Mais dans des interviews tardives, elle a confirmé ces découvertes.

*"Je comprenais les équations mieux que la plupart des gens qui les programmaient. C'est pour ça qu'on me demandait de vérifier." — Katherine Johnson*
