# HyperFrames — Productions vidéo

Ce dépôt contient les compositions HyperFrames organisées par projet.

## Structure

```
<project-name>/
  index.html          Root composition — timeline, slots, audio, transitions
  compositions/       Sub-compositions (une par scène)
    s01-*.html … s16-*.html
  assets/             Médias (audio, images)
  meta.json           Durée, résolution, fps
  SCRIPT.md           Script voix-off
  STORYBOARD.md       Direction visuelle scène par scène
  HANDOFF.md          Notes de production
```

## Projets

| Projet | Durée | Scènes | Description |
|--------|-------|--------|-------------|
| [cleavenir-launch](./cleavenir-launch/) | 100s | 16 | Vidéo de lancement CléAvenir — orientation IA |
| [cleavenir-cleo-histoire](./cleavenir-cleo-histoire/) | 50s | 6 | Film cinématique CléAvenir — un lycéen perdu trouve sa voie grâce à Cleo, l'IA |

## Rendu local

```bash
cd /path/to/project
npx hyperframes lint
npx hyperframes render --output renders/output.mp4 --quality draft
```
