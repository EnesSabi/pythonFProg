
Quelldatei = "C:/Users/enybo/Documents/GitHub/pythonFProg/quelldatei.html"
Zieldatei = "C:/Users/enybo/Documents/GitHub/pythonFProg/zieldatei.html"

def filterHTML(fileQuelle, fileZiel):
    with open(fileQuelle, "r") as f:
        data = f.readlines()
    with open(fileZiel, "w") as f:
        for line in data:
          print(line.strip(""))

def main():
    filterHTML(Quelldatei, Zieldatei)

if __name__ == "__main__":
    main()
