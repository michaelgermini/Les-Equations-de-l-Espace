# Contribuer à "Les Équations de l'Espace"

Merci de votre intérêt pour contribuer à ce projet ! Ce document explique comment vous pouvez nous aider.

---

## 📋 Types de Contributions Bienvenues

### 1. **Corrections et clarifications**
- Erreurs de typage, grammaire ou orthographe
- Équations incorrectes
- Explications confuses
- Références manquantes

**Comment contribuer** :
1. Ouvrez une "Issue" décrivant l'erreur
2. Proposez une correction (optionnel)
3. Indiquez précisément l'emplacement (chapitre, section)

### 2. **Améliorations du contenu**
- Ajouter des exemples numériques supplémentaires
- Clarifier des concepts difficiles
- Ajouter des diagrammes ou visualisations (description textuelle)
- Enrichir les annexes

**Comment contribuer** :
1. Proposez d'abord une "Issue" avec votre idée
2. Attendez le feedback
3. Si approuvé, soumettez votre contribution

### 3. **Traductions**
- Traduire des chapitres en d'autres langues
- Adapter le contenu pour d'autres contextes géographiques

**Comment contribuer** :
1. Créez un nouveau répertoire (ex: `/fr/`, `/en/`, `/es/`)
2. Traduisez fidèlement
3. Maintient la structure et les références

### 4. **Compléments pédagogiques**
- Solutions d'exercices
- Projets de programmation complets
- Fiches de révision
- Questions de compréhension

**Comment contribuer** :
1. Créez un répertoire `/ressources_pedagogiques/`
2. Organisez par chapitre ou sujet
3. Incluez les solutions avec explications

### 5. **Ressources historiques**
- Archivage de photos/images de Katherine Johnson
- Citations supplémentaires
- Interviews transcript
- Données de missions (NASA archives)

**Comment contribuer** :
1. Localisez la source
2. Demandez la permission (droits d'auteur)
3. Proposez l'intégration

---

## 🛠️ Guide Pratique de Contribution

### Avant de Commencer

1. **Lisez le projet entier** pour comprendre le ton et le style
2. **Consultez l'INDEX** pour voir comment les concepts sont interconnectés
3. **Vérifiez les Issues existantes** pour éviter les doublons

### Format et Style

#### Ton
- **Clair et accessible** : Expliquez comme vous expliqueriez à un collègue
- **Rigoureux** : Les faits doivent être vérifiés
- **Inclusif** : Évitez le jargon gratuit ; définissez les termes
- **Honnête** : Admettez les incertitudes

#### Texte
```markdown
# Titre de Section
## Sous-section
### Sous-sous-section (éviter de descendre plus bas)

Paragraphe principal : commencez par une idée claire.
Puis développez avec des détails.

- Point 1
- Point 2
- Point 3

**Gras** pour l'importance, *italique* pour l'emphase.
```

#### Équations
Utilisez LaTeX avec délimiteurs `\(...\)` pour inline et `\[...\]` pour display :

```
La vitesse orbitale est \(v = \sqrt{\frac{GM}{r}}\).

L'équation de Kepler est :

\[
M = E - e\sin E
\]
```

#### Citations
Format : *"Citation texte." — Auteur, année*

```
*"Je croyais que c'était mon travail." — Katherine Johnson, 2010*
```

#### Références
- Incluez titre, auteur, année, URL si disponible
- Groupez les références par type (livres, articles, vidéos)

### Processus de Contribution

#### Étape 1 : Créer une Issue
```
Titre : Description brève
Description :
- Quelle est l'amélioration proposée ?
- Où dans le projet ?
- Pourquoi c'est important ?
- Avez-vous une approche suggérée ?
```

#### Étape 2 : Attendre le Feedback
Les mainteneurs évalueront :
- Cohérence avec le projet
- Qualité et rigueur
- Impact sur l'expérience lecteur

#### Étape 3 : Soumettre la Contribution
1. Créez une branche : `git checkout -b fix/correction-nom`
2. Faites vos modifications
3. Testez la cohérence (vérifiez liens, équations, références)
4. Soumettez une "Pull Request"

#### Étape 4 : Révision
Les mainteneurs examineront et proposeront des modifications si nécessaire.

---

## 📚 Normes Éditoriales

### Vérification des Faits
- **Équations** : Vérifiez auprès de sources académiques reconnues
- **Dates et faits historiques** : Consultez les archives NASA ou sources primaires
- **Biographie de Katherine** : Référencez "Hidden Figures" ou interviews
- **Données de missions** : Utilisez les rapports officiels NASA

### Structure de Chapitre
Chaque chapitre devrait suivre cette structure :

```
# Chapitre N : Titre

## Section Principale
### Sous-section avec contexte
#### Point spécifique

- Contexte historique / scientifique
- Développement du concept
- Équations si pertinent
- Exemple pratique ou application

### Résumé du Chapitre
- Point 1
- Point 2
- Point 3
```

### Longueur Recommandée
- Chapitres : 2000-4000 mots
- Sections : 400-800 mots
- Annexes : Flexible, mais organisé

---

## 🔍 Checklist Avant de Soumettre

- [ ] Relecture complète (grammaire, orthographe)
- [ ] Vérification des liens internes
- [ ] Les équations s'affichent correctement
- [ ] Les références sont complètes
- [ ] Le ton est cohérent avec le reste du projet
- [ ] Les faits sont vérifiés
- [ ] Pas de plagiat (paraphrasez ou citez)
- [ ] L'INDEX a été mis à jour si nécessaire

---

## 💡 Domaines Prioritaires pour Contributions

### Haute Priorité
1. **Diagrammes et visualisations** : Des descriptions ASCII ou des suggestions de diagrammes
2. **Solutions d'exercices** : Pour les exemples numériques
3. **Compléments historiques** : Plus d'interviews ou de citations
4. **Traductions** : Rendre le projet multilingue

### Moyenne Priorité
1. **Correction d'équations** : Si vous trouvez des erreurs
2. **Clarifications pédagogiques** : Si un concept est confus
3. **Ressources complémentaires** : Liens vers autre matériel

### Basse Priorité
1. **Reformulation complète** : Seulement si vraiment nécessaire
2. **Changements de structure** : À discuter d'abord
3. **Ajouts spéculatifs** : Qui ne sont pas vérifiables

---

## 📞 Contact et Questions

- **Questions générales** : Ouvrez une Issue avec le label `question`
- **Suggestions futures** : Ouvrez une Issue avec le label `enhancement`
- **Erreurs** : Ouvrez une Issue avec le label `bug`

---

## 📜 Licence et Attribution

En contribuant, vous acceptez que votre travail soit distribué sous la même licence que le projet.

Vous serez crédité(e) comme contributeur dans :
- Les fichiers modifiés
- Un fichier `CONTRIBUTORS.md` (à créer)
- Les remerciements du projet

---

## 🎯 Philosophie de Contribution

Ce projet honore Katherine Johnson en cherchant :

1. **Rigueur** : Les faits doivent être justes
2. **Accessibilité** : Les concepts doivent être compris par tous
3. **Clarté** : Pas de jargon inutile
4. **Inclusivité** : Perspectives diverses les bienvenues
5. **Respect** : De Katherine et de tous les contributeurs

---

## 🙏 Merci !

Votre contribution, quelle qu'elle soit, est précieuse pour maintenir et améliorer ce projet. 

Ensemble, nous honorons l'héritage de Katherine Johnson et rendons la science plus accessible. ✨

---

**Besoin d'aide ?** Ouvrez une Issue — nous sommes là pour vous !
