# Simple Dictionary Maker from another Dictionary by WildZarek
# This script is for educational purposes only
# Developed in the Piscine Discovery Ciberseguridad - Enero/2025

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]}.py <file>")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        filename, _ = os.path.splitext(input_file)
        extension = input_file.split(".")[-1]
        with open(input_file, "r") as fd1:
            words = fd1.read().splitlines()
            with open(f"{filename}_new.{extension}", "w") as fd2:
                for word1 in words:
                    for word2 in words:
                        fd2.write(f"{word1}{word2}\n")