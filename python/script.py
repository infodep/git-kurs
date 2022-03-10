"""
Test file, please ignore
"""

def main(tom_liste = []):
    assert tom_liste == []
    tom_liste.append(10)
    assert tom_liste[0] == 10

if __name__ == "__main__":
    main()
    main() # hvorfor krasjer programmet her? 
