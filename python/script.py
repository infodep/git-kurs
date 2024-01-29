import hashlib
"""
Run this file to print the flag.
"""
def main():
    print(f"GIT_KURS_{hashlib.sha256(b'Git er ganske kult!')[:8]}")

if __name__ == "__main__":
    main()
