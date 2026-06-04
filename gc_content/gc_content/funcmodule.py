from collections import deque

import matplotlib.pyplot as plt

def gc_content_strict(seq):
    cont = (seq.count("G") + seq.count("C"))*100/len(seq)
    if seq.count("N") != 0:
        print("This sequence has mistakes.")
    return cont

def gc_window(genome: str, window_size: int):
    window = deque(maxlen = window_size)
    gc_count = 0
    gc_fin = 0
    result = []
    
    for i, base in enumerate(genome):
        window.append(base)
        if base.upper() == "G" or base.upper() == "C":
            gc_count += 1
        if len(window) == window_size:
            gc_fin = gc_count * 100 / window_size
            result.append(gc_fin)
            if genome[i - window_size + 1].upper() == "G" or genome[i - window_size + 1].upper() == "C":
                gc_count -= 1

                
    plt.bar(range(0, len(result)), result)
    plt.title("GC-content")
    plt.xlabel("Window")
    plt.ylabel("GC-content")
    plt.show(block=True)
