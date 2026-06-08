# 🤖 fleet-magenta-connector

> *Bridge between the SuperInstance MIDI fleet and Google Magenta AI music tools*

Google Magenta (magenta.withgoogle.com) provides state-of-the-art ML music tools. This connector bridges our ternary strategy vectors to Magenta's models.

## Architecture

```
Our MIDI → Magenta MusicVAE → Interpolate between agent states
Our patterns → Magenta Groove → Humanize fleet rhythms
Our generator → Magenta Continue → Extend agent compositions
Our ternary → Magenta Drumify → AI percussion from agent vectors
```

## Available Bridges

### MusicVAE Interpolation
Take two agent state vectors and morph between them musically:
```python
# vector_a = [1,0,-1,1] → MIDI
# vector_b = [-1,1,0,-1] → MIDI
# Magenta Interpolate: morph between the two MIDI files
```

### Groove Humanization
Add microtiming and velocity variation to fleet-generated patterns:
```python
# fleet-midi-markov produces patterns
# Magenta Groove adds human feel
```

## Ensign: Orpheus — Fleet AI Music Collaborator
Summon: `/ensign orpheus interpolate [1,0,-1,1] [-1,1,0,-1]`
