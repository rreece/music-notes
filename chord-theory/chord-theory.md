# Introduction

Lorem ipsum dolor sit amet, duo ut putant verear, nam ut brute utroque. Officiis qualisque conceptam te duo, eu vim soluta numquam, has ut aliquip accusamus. Probo aliquam pri id. Mutat singulis ad vis, eam euismod pertinax an, ea tale volumus vel. At porro soleat est. Debet facilis admodum an sed, at falli feugiat est.

## Modes

The initial goal is to introduce the concept of a *mode* in music theory, and the major and minor modes as examples.

A C-major and A-minor scales are:

\lilypondfile{c-major-scale.ly}

where 1 and 2 denote that a note is a half step (1 semitone) or a whole step (2 semitones) above the previous note.

The sequence 2212221 defines the major mode.
The major mode notes naturally occur on the white keys in the key of C.
The sequence 2122212 defines the minor mode.
The minor mode notes naturally occur on the white keys in the key of A.

## Intervals

Lorem ipsum dolor sit amet, duo ut putant verear, nam ut brute utroque. Officiis qualisque conceptam te duo, eu vim soluta numquam, has ut aliquip accusamus. Probo aliquam pri id. Mutat singulis ad vis, eam euismod pertinax an, ea tale volumus vel. At porro soleat est. Debet facilis admodum an sed, at falli feugiat est.

\lilypondfile{intervals.ly}

Table: All the two-note intervals in 12-tone music. {#tbl:intervals}

| Interval | Name           | Semitones |     Frequency ratio (just/pure) | Frequency ratio (equal temperament) |
|:---------|:---------------|----------:|--------------------------------:|------------------------------------:|
| m2       | Minor second   |         1 |                           16:15 |           $2^{1/12} \approx 1.0595$ |
| M2       | Major second   |         2 |                             9:8 |           $2^{2/12} \approx 1.1225$ |
| m3       | Minor third    |         3 |                             6:5 |           $2^{3/12} \approx 1.1892$ |
| M3       | Major third    |         4 |                             5:4 |           $2^{4/12} \approx 1.2599$ |
| P4       | Perfect fourth |         5 |                             4:3 |           $2^{5/12} \approx 1.3348$ |
| A4/d5    | Tritone        |         6 |  45:32 or 64:45 or $\sqrt{2}$:1 |           $2^{6/12} \approx 1.4142$ |
| P5       | Perfect fifth  |         7 |                             3:2 |           $2^{7/12} \approx 1.4983$ |
| m6       | Minor sixth    |         8 |                             8:5 |           $2^{8/12} \approx 1.5874$ |
| M6       | Major sixth    |         9 |                             5:3 |           $2^{9/12} \approx 1.6818$ |
| m7       | Minor seventh  |        10 |                     16:9 or 9:5 |          $2^{10/12} \approx 1.7818$ |
| M7       | Major seventh  |        11 |                            15:8 |          $2^{11/12} \approx 1.8877$ |
| O        | Octave         |        12 |                             2:1 |                $2^{12/12} = 2.0000$ |

The tritone is also called an augmented fourth or a diminished fifth (A4/d5).

## Trichords

The scafolding on which we will build chords are trichords: 1-3-5, a perfect 5th, and then the minor or major color of the chord is determined by the 3rd.

\lilypondfile{trichords.ly}

## Seven-chords

A dominant seventh chord (C7) is a major trichord with an additional minor 7th interval added.
A major seventh chord (CM7 or Cmaj7)  is a major trichord with an additional major 7th interval added.
A minor seventh chord (Cm7)  is a minor trichord with an additional minor 7th interval added.
There exist augmented and diminished versions of seventh chords that raise/lower the 5th and/or the 7th intervals.

\lilypondfile{sevenchords.ly}

All these are inversions of Cmaj7:

\lilypondfile{c-maj-7-invesions.ly}

