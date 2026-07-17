# HANDOFF — CléAvenir · L'histoire de Cléo

## État actuel
- **Durée**: 50 secondes, 30fps, 1920×1080
- **Scènes**: 6 (S01–S06)
- **Structure**: index.html (root) + 6 sub-compositions dans compositions/
- Projet compagnon de `cleavenir-launch` (ne le modifie pas) — même identité
  de marque, registre plus cinématique / narratif.

## Architecture
```
index.html          Root: 50s, 6 slots, flash-cuts, resolve-to-navy, audio
compositions/
  s01-le-poids-du-choix.html    … s06-cta.html
assets/
  music.wav          Placeholder silencieux 50s — à remplacer par une vraie musique
  fonts/              Syne-800.ttf, SpaceGrotesk-700.ttf (auto-hébergées pour un
                       rendu déterministe hors-ligne — Inter est pré-embarquée par
                       le compilateur HyperFrames)
meta.json            Métadonnées du projet
BRIEF.md             Brief confirmé (intent layer)
SCRIPT.md            Script voix-off (6 scènes, FR)
STORYBOARD.md        Direction visuelle scène par scène
HANDOFF.md           Ce fichier
```

## Fonts
- **Syne** 800 — titres (auto-hébergée dans assets/fonts, cohérence avec la marque)
- **Inter** 300/400/500 — corps, UI (pré-embarquée par HyperFrames)
- **Space Grotesk** 700 — badges (auto-hébergée dans assets/fonts)

## Cinématiques avancées mises en œuvre
- Push-in caméra continu (scale) sur S01 et S04
- Portail lumineux radial + anneaux concentriques (S02→S03)
- Orbe IA à nœuds orbitaux animés (S03)
- Montage à flashs de coupe rythmés, fond parallax en rotation lente (S04)
- Tracé SVG animé + personnage progressant le long du chemin (S05)
- Éclats géométriques rotatifs + logo assemblé (S06)
- Vignettes dramatiques et grain filmique sur les scènes sombres

## Audio
- `assets/music.wav` : placeholder silencieux 50s
- → **TODO** : remplacer par une vraie musique (montée émotionnelle, résolution
  confiante) et une voix-off (script dans SCRIPT.md)

## Ce qui reste à faire
- [ ] Ajouter une vraie voix-off (script dans SCRIPT.md)
- [ ] Remplacer music.wav par une vraie musique
- [ ] Vérifier les durées exactes des scènes après render final
- [ ] Envisager `hyperframes cloud` / rendu `--quality high` pour la livraison finale

## Rendu
```bash
cd /home/user/hyperframes/cleavenir-cleo-histoire
npx hyperframes lint
npx hyperframes check
npx hyperframes render --output renders/cleavenir-cleo-histoire.mp4 --quality draft
npx hyperframes render --output renders/cleavenir-cleo-histoire-hq.mp4 --quality high
```

## Note d'environnement
Ce projet a été construit dans un environnement d'exécution isolé sans accès
réseau depuis Chrome headless : gsap est installé en local (`node_modules/`,
déclaré dans `package.json`) plutôt que chargé depuis un CDN, et les polices
non pré-embarquées (Syne, Space Grotesk) sont auto-hébergées dans
`assets/fonts/`. C'est aussi la configuration la plus robuste pour des rendus
reproductibles — à conserver même dans un environnement avec accès réseau complet.
