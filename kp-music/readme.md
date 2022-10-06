## Music of solar wind (Kp music)

Our Raspberry Pi Python program produces a piece of “music” with downloaded Kp-index values (planetary geomagnetic disturbance data) and plays it with a Bluetooth speaker.

In Geosciences, Kp data are displayed graphically as an aid for scientists, and the graphical notation looks like a musical score. It is often called "Bartels musical diagrams," after the inventor of Kp-index, [Julius Bartels](https://en.wikipedia.org/wiki/Julius_Bartels).

<p align="center">
<img src="../images/bartels-diagram.png" width="350">
</p>

This motivated us to map a sequence of Kp values to musical elements. Our current mapping algorithm does:

28 Kp values (0, 0+, 1-, 1, 1+, 2-, ... , 9)
-

eighth note 


a scale

major and minor scales


 considering 3 properties of sound: pitch, duration and intensity.


Heptatonic (7 notes per octave):
Octatonic (8 notes per octave): u
Pentatonic (5 notes per octave): t


We also used the concepts of triads (chords), key signatures and musical scales in the mapping.



LED panel viewers can listen to the "music of solar wind" and feel how solar wind sing. They can also vary it into different vibes by changing key signatures/scales.
