# Introduction

This document is my attempt to write the brief introduction to music theory I wish I had.
I try to motivate from first principles why music has the structure it has
and what the palette of options are.

The initial goal is to introduce the concept of a mode in music theory,
and to focus on the major and minor modes as examples.
The final target is to introduce chord progressions.
What does it take to make a song?


# Modes

In *diatonic* music there are seven notes in a scale before coming to the *octave* which has double the frequency of the original root note.

Example C-major and A-minor scales are:

\lilypondfile{c-major-scale.ly}

where 1 and 2 denote that a note is a half step (1 semitone) or a whole step (2 semitones) above the previous note.

The sequence 2212221 defines the *major mode*.
The major mode notes naturally occur on the white keys of a piano (no accents) in the key of C major (*i.e.* when C is the root).
The sequence 2122122 defines the *minor mode*.
The minor mode notes naturally occur on the white keys in the key of A minor.
There are seven modes in total in diatonic music that all use the same seven notes,
just starting from different positions for the root note.

Table: All the diatonic modes in 12-tone music. {#tbl:modes}

| Mode             | Interval pattern | Root for all white  | Notes for C root             | Character              |
|:-----------------|:-----------------|:--------------------|:-----------------------------|:-----------------------|
| Ionian (major)   | 2212221          | C                   | C D E F G A B                | Bright, happy          |
| Dorian           | 2122212          | D                   | C D E$\flat$ F G A B$\flat$  | Minor, raised 6th  |
| Phrygian         | 1222122          | E                   | C D$\flat$ E$\flat$ F G A$\flat$ B$\flat$   | Dark, Spanish sound    |
| Lydian           | 2221221          | F                   | C D E F$\sharp$ G A B        | Dreamy, raised 4th     |
| Mixolydian       | 2212212          | G                   | C D E F G A B$\flat$         | Major, flat 7th    |
| Aeolian (minor)  | 2122122          | A                   | C D E$\flat$ F G A$\flat$ B$\flat$    | Sad, melancholic       |
| Locrian          | 1221222          | B                   | C D$\flat$ E$\flat$ F G$\flat$ A$\flat$ B$\flat$   | Unstable, diminished   |

Western music tends to focus on using the major and minor modes, but there are exceptions.


# Intervals

Now we introduce *polyphony*, playing more than one note at a time.
An *interval* is the gap in pitch (frequency) between two notes.
Each interval has a name as listed in Table&nbsp;\ref{tbl:intervals}.
We will use notes of different intervals together to build chords.

\lilypondfile{intervals.ly}

Table: All the two-note intervals in 12-tone music. {#tbl:intervals}

| Interval | Name           | Semitones |     Frequency ratio (pure tuning) | Frequency ratio (equal temperament) |
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

That certain intervals have simple mathematical ratios for the ratios of
their frequencies is a rough start at the answer to:
Why does music sound like that?
Why certain tunings?
Why 12 in 12-tone music?

In *just intonation* (or *pure tuning*), intervals use simple integer frequency ratios like 3:2 for a perfect fifth.
These ratios produce the most consonant, pure-sounding intervals because the overtones align perfectly.
However, just intonation creates problems when changing keys or playing complex harmony.
*Equal temperament* solves this by dividing the octave into 12 equal semitones, where each semitone has a frequency ratio of $2^{1/12} \approx 1.0595$.
This means a perfect fifth has a ratio of $2^{7/12} \approx 1.4983$ instead of exactly 3:2 = 1.5.
While equal temperament makes most intervals slightly out of tune compared to their pure versions,
it allows music to be played in any key with the same relative tuning,
making it the standard tuning system for Western music since the 18th century.


# Trichords

The scaffolding on which we will build chords are trichords, consisting of scale degrees 1-3-5 (root, third, fifth).
The minor or major quality of the chord is determined by the 3rd interval being major or minor.
Here are C-major and C-minor chords, and their first and second inversions, derived by rotating the bottom note to an octave higher.
Following that are augmented and diminished versions of a C chord, where the 5th is raised or lowered a half step, respectively.

\lilypondfile{trichords.ly}


# Seventh chords and beyond

Adding a fourth note to a trichord creates richer, more complex harmonies.
The most common extension is adding a 7th above the root.

A dominant seventh chord (C7) is a major trichord with an additional minor 7th interval added.
A major seventh chord (CM7 or Cmaj7)  is a major trichord with an additional major 7th interval added.
A minor seventh chord (Cm7)  is a minor trichord with an additional minor 7th interval added.
There exist augmented and diminished versions of seventh chords that raise/lower the 5th and/or the 7th intervals.

\lilypondfile{sevenchords.ly}

Extensions can continue beyond the 7th to create 9th, 11th, and 13th chords, which are common in jazz.

These are Cmaj7 and its inversions, followed by variants of Em11:

\lilypondfile{c-maj-7-invesions.ly}


# Chord progressions

Now we have introduced enough topics to ask a natural question:

If one wants to stay within a certain key in given mode, what chords are allowed?

For the major and minor modes, the answer turns out to be,
in roman numeral notation where major chords are written in capital letters
and minor chords are written in lowercase letters

Major: I ii iii IV V vi vii${}^{\circ}$     
Minor: i ii${}^{\circ}$ III iv v VI VII        

To step through why this is the case, consider the C-major key as an example.
The 1st trichord is clearly a C-major chord: C-E-G.
The 2nd trichord beginning with D as the root is D-F-A,
where note that since D-F is a minor 3rd this trichord is minor.
Therefore the second chord in the key of C major is Dm.
The third chord is E-G-B, which is Em, and so on.
One can tell which notes are allowed in each chord by remembering that
we always pick only from the white piano keys in the key of C major.

\lilypondfile{c-major-chords.ly}

The chords that are allowed naturally in each mode are summarized in Table&nbsp;\ref{tbl:chords-for-modes}.

Table: Chords that are natural for each mode. {#tbl:chords-for-modes}

| Mode \\ Chord   | 1       | 2         | 3         | 4       | 5       | 6         | 7           |
|:----------------|:--------|:----------|:----------|:--------|:--------|:----------|:------------|
| Ionian (major)  | I       | ii        | iii       | IV      | V       | vi        | vii${}^{\circ}$ |
| Aeolian (minor) | i       | ii${}^{\circ}$ | III       | iv      | v       | VI        | VII         |
| Dorian          | i       | ii        | III       | IV      | v       | vi${}^{\circ}$ | VII         |
| Phrygian        | i       | II        | III       | iv      | v${}^{\circ}$ | VI        | vii         |
| Lydian          | I       | II        | iii       | iv${}^{\circ}$ | V       | vi        | vii         |
| Mixolydian      | I       | ii        | iii${}^{\circ}$ | IV      | v       | vi        | VII         |
| Locrian         | i${}^{\circ}$ | II        | iii       | iv      | V       | VI        | vii         |

Note that the major chords that are allowed in a major mode key are I, IV, and V.
Many pop songs have been written that utilize or focus on only these chords,
perhaps throwing in a vi chord.
Common chord progressions in Western pop music are listed in
Table&nbsp;\ref{tbl:pop-major-progressions}
and Table&nbsp;\ref{tbl:pop-minor-progressions}.

Table: Common chord progressions in Western pop music in major keys. {#tbl:pop-major-progressions}

| Name/Description          | Progression           | Example in C major  | Notable songs                                           |
|:--------------------------|:----------------------|:--------------------|:--------------------------------------------------------|
| Pop-punk progression      | I-V-vi-IV             | C-G-Am-F            | "Let It Be", "Don't Stop Believin", "Someone Like You", "Glycerine", "What's My Age Again?" |
| '50s, doo-wop progression | I-vi-IV-V             | C-Am-F-G            | "Stand By Me", "Blue Moon", "Every Breath You Take"     |
| Sensitive female progression | vi-IV-I-V          | Am-F-C-G            | "Zombie", "Apologize"                                   |
| Three-chord rock          | I-IV-V                | C-F-G               | "La Bamba", "Twist and Shout", "Wild Thing"             |
| Canon progression         | I-V-vi-iii-IV-I-IV-V  | C-G-Am-Em-F-C-F-G   | "Pachelbel's Canon" progression                         |
| Jazz turnaround           | ii-V-I                | Dm-G-C              | Jazz standard turnaround                                |
| Circle progression        | I-vi-ii-V             | C-Am-Dm-G           | "Heart and Soul", "Blue Moon" (variation)               |
| Singer-songwriter         | I-IV-vi-V             | C-F-Am-G            | "Self Esteem", "What's Up"                              |
| Rock ballad               | vi-V-IV-V             | Am-G-F-G            | Common in rock music                                    |
| Mixolydian vamp           | I-VII$\flat$-IV       | C-B$\flat$-F        | "Sweet Child O' Mine", modal mixture                    |

Table: Common chord progressions in Western pop music in minor keys. {#tbl:pop-minor-progressions}

| Name/Description          | Progression           | Example in A minor  | Notable songs                                           |
|:--------------------------|:----------------------|:--------------------|:--------------------------------------------------------|
| Aeolian vamp              | i-VI-III-VII          | Am-F-C-G            | "All Along the Watchtower", "Stairway to Heaven" intro  |
| Minor three-chord         | i-iv-v                | Am-Dm-Em            | "Summertime", basic minor progression                   |
| Andalusian cadence        | i-VI-VII              | Am-F-G              | "House of the Rising Sun", Andalusian cadence variant   |
| Descending minor          | i-VII-VI-V            | Am-G-F-E            | Descending progression, common in minor keys            |

