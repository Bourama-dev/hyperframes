# HANDOFF — CléAvenir Launch Video v3.0

## État actuel
- **Durée**: 100 secondes, 30fps, 1920×1080
- **Scènes**: 16 (numérotées S01–S16)
- **Structure**: index.html (root) + 16 sub-compositions dans compositions/

## Architecture
```
index.html          Root: 100s, 16 slots, overlays de transition, audio
compositions/
  s01-logo-reveal.html   … s16-cta.html
  components/            Plugins HyperFrames installés
assets/
  music.mp3         Placeholder silencieux 100s — à remplacer
meta.json           Métadonnées du projet
SCRIPT.md           Script voix-off (16 scènes, FR)
STORYBOARD.md       Direction visuelle scène par scène
HANDOFF.md          Ce fichier
```

## Fonts (Google Fonts, cachées par HyperFrames)
- **Syne** 600/700/800 — titres
- **Inter** 300/400/500/600/700 — corps, UI
- **Space Grotesk** 500/600/700 — badges, eyebrows

## Plugins installés
- `caption-clip-wipe` · `caption-editorial-emphasis` · `caption-gradient-fill`
- `caption-kinetic-slam` · `vfx-iphone-device` · `vfx-liquid-background`
- `vfx-portal` · `vfx-shatter` · `transitions-cover`
- `grid-pixelate-wipe` · `vignette` · `flowchart` · `logo-outro`

## Transitions implémentées
- **Flash blanc** (0.08s) : coupes rapides entre scènes rapprochées
- **Grid pixelate** (0.6s) : coupes dramatiques aux points clés (S04→S05, S08→S09, S12→S13)
- **Fade to white** (2s) : résolution finale 98–100s

## Audio
- `assets/music.mp3` : placeholder silencieux 100s
- → **TODO** : remplacer par une musique upbeat/inspirante (genre : SaaS launch, électronique douce)

## Ce qui reste à faire
- [ ] Ajouter une vraie voix-off (script dans SCRIPT.md)
- [ ] Remplacer music.mp3 par une vraie musique
- [ ] Vérifier les durées exactes des scènes après render final
- [ ] Ajuster les timings si certaines scènes semblent trop longues

## Rendu
```bash
cd /home/user/mes-videos/cleavenir-launch
npx hyperframes lint
npx hyperframes render --output renders/cleavenir-v3.mp4 --quality draft
npx hyperframes render --output renders/cleavenir-v3-hq.mp4 --quality high
```
