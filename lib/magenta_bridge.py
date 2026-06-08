"""Magenta bridge — fleet MIDI ↔ Google Magenta AI tools."""
import json
def check(): return False  # pip install magenta to enable
def interpolate(a,b,out="/tmp/interpolated.mid"):
    import music21
    s1,s2=music21.converter.parse(a),music21.converter.parse(b)
    bl=music21.stream.Score()
    for i,(p1,p2) in enumerate(zip(s1.parts,s2.parts)):
        np=music21.stream.Part()
        for n1,n2 in zip(p1.flatten().notes,p2.flatten().notes):
            if hasattr(n1,"pitch")and hasattr(n2,"pitch"):
                avg=(n1.pitch.midi+n2.pitch.midi)//2
                n=music21.note.Note(avg);n.duration=n1.duration;np.append(n)
        bl.append(np)
    bl.write("midi",fp=out);return out
