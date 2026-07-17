#!/usr/bin/env python3
"""Synthesize an original instrumental bed for the CléAvenir cinematic film.
No samples, no external assets — additive sine/triangle synthesis with simple
ADSR envelopes, matching the piece's emotional arc section by section.
"""
import numpy as np
import soundfile as sf

SR = 44100
TOTAL = 51.0

def note(freq, t0, dur, amp=0.18, wave="sine", attack=0.4, release=0.8, vibrato=0.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    if vibrato > 0:
        freq_t = freq * (1 + vibrato * np.sin(2 * np.pi * 4.5 * t))
    else:
        freq_t = freq
    phase = 2 * np.pi * np.cumsum(np.full(n, freq_t / SR)) if vibrato > 0 else 2 * np.pi * freq * t
    if wave == "sine":
        sig = np.sin(phase)
    elif wave == "triangle":
        sig = 2 / np.pi * np.arcsin(np.sin(phase))
    else:
        sig = np.sin(phase)
    env = np.ones(n)
    a = min(int(attack * SR), n // 2)
    r = min(int(release * SR), n - a)
    if a > 0:
        env[:a] = np.linspace(0, 1, a) ** 1.5
    if r > 0:
        env[-r:] *= np.linspace(1, 0, r) ** 1.5
    return sig * env * amp

def place(buf, sig, t0):
    i0 = int(t0 * SR)
    i1 = min(i0 + len(sig), len(buf))
    if i1 > i0:
        buf[i0:i1] += sig[: i1 - i0]

buf = np.zeros(int(TOTAL * SR) + SR)

def pad(chord, t0, dur, amp=0.09):
    for f in chord:
        place(buf, note(f, t0, dur, amp=amp, wave="sine", attack=dur * 0.35, release=dur * 0.5), t0)
        place(buf, note(f * 2, t0, dur, amp=amp * 0.25, wave="sine", attack=dur * 0.4, release=dur * 0.5), t0)

def pluck(freq, t0, dur=0.9, amp=0.1):
    place(buf, note(freq, t0, dur, amp=amp, wave="triangle", attack=0.01, release=dur * 0.9), t0)

A3, C4, E4, F3, G3, A4, C5, E5, F4, G4 = 220.00, 261.63, 329.63, 174.61, 196.00, 440.00, 523.25, 659.25, 349.23, 392.00

# --- Section 1 (0-14s): Le poids du choix / le doute — sparse minor pad, tension ---
pad([A3, C4, E4], 0, 14, amp=0.075)
for t, f in [(2.4, A4), (5.6, C5), (8.8, E4 * 2), (11.6, A4)]:
    pluck(f, t, dur=1.6, amp=0.055)

# --- Section 2 (14-22s): La rencontre — brightening swell ---
pad([F3, A3, C4], 14, 8, amp=0.11)
pad([F3, A3, C4, F4], 19, 6, amp=0.07)
for t, f in [(15.0, C5), (16.6, E5), (18.2, F4 * 2), (20.0, A4)]:
    pluck(f, t, dur=1.4, amp=0.06)

# --- Section 3 (22-36s): La transformation — rhythmic arpeggio, ~100bpm ---
prog = [
    (22.0, [A3, C4, E4]), (25.5, [F3, A3, C4]),
    (29.0, [C4, E4, G4]), (32.5, [F3, A3, C4]),
]
for t0, chord in prog:
    pad(chord, t0, 4.4, amp=0.06)
step = 0.3
seq = [A4, C5, E5, C5, A4, E4 * 2, C5, E5] * 6
tt = 22.3
for f in seq:
    if tt > 35.6:
        break
    pluck(f, tt, dur=0.5, amp=0.05)
    tt += step

# --- Section 4 (36-45s): Le nouveau chemin — warm major pad ---
pad([F3, A3, C4], 36, 5, amp=0.1)
pad([C4, E4, G4], 41, 4.5, amp=0.11)
for t, f in [(37.2, C5), (39.4, E5), (41.8, G4 * 2), (43.4, C5)]:
    pluck(f, t, dur=1.5, amp=0.055)

# --- Section 5 (45-51s): CTA — sustained resolve, fade out ---
pad([C4, E4, G4, C5], 45, 6, amp=0.1)
pluck(E5, 46.2, dur=2.0, amp=0.05)
pluck(G4 * 2, 47.6, dur=2.0, amp=0.045)

# gentle overall fade-out in the last 1.5s
tail = int(1.5 * SR)
buf[-tail - SR:-SR] *= np.linspace(1, 0, tail)
buf[-SR:] = 0

buf = buf[: int(TOTAL * SR)]
peak = np.max(np.abs(buf))
if peak > 0:
    buf = buf / peak * 0.72

stereo = np.stack([buf, buf], axis=1).astype(np.float32)
sf.write("assets/music.wav", stereo, SR)
print("wrote assets/music.wav", len(buf) / SR, "s")
