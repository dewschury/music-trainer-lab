from notes import note_to_freq

def test_la_440():
    assert note_to_freq(0) == 440.0