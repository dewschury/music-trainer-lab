# notes.py - Día 1: Escala cromática y frecuencias
# Este script imprime las 12 notas de una octava y su frecuencia en Hz.

def note_to_freq(note_index, a4_freq=440.0):
    """Convierte un índice de nota (0 = La) a su frecuencia en Hz."""
    # Fórmula: f = 440 * 2^(n/12)
    return a4_freq * (2 ** (note_index / 12))

notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

for i, note in enumerate(notes):
    freq = note_to_freq(i)
    print(f"{note:>2} : {freq:.2f} Hz")