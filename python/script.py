import random
import string
"""
Run this file to print the flag.
"""
def main():
    print(f"GIT_KURS_{''.join(random.choice(string.ascii_letters) for _ in range(8))}")

if __name__ == "__main__":
    main()
