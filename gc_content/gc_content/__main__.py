import sys
from gc_content.funcmodule import gc_content_strict
from gc_content.funcmodule import gc_window

def main():
    file_name = sys.argv[1]
    window = int(sys.argv[2])
    with open(file_name) as f:
        sequence = f.readline().strip()
        
    gc_content_strict(sequence)
    gc_window(sequence, window)

if __name__ == "__main__":
    main()
