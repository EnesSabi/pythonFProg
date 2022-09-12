menners = ["Raphael", "Konstantin", "Enes", "Leon"]
damen = ["Sedef", "Rukiye", "Özge", "Helena"]
tanzlehrer = ["Jürgen"]

def tl_mit_jedem():
    parchen = []
    gesamt = menners + damen
    for x in gesamt:
        paar = x + "&" + tanzlehrer[0]
        parchen.append(paar)
    return parchen

def jeder_mit_jedem():
    parchen = []
    
    for x in menners:
        for y in damen:
            paar = x + "&" + y
            parchen.append(paar)
    return parchen

def main():
    x = tl_mit_jedem()
    y = jeder_mit_jedem()
    print(x + y)

if __name__ == "__main__":
    main()