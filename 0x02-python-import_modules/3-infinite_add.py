#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    args = len(sys.argv) - 1

    for i in range(args):
        result = sys.argv[i]++
