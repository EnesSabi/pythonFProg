
def hauefigkeiten(s):
    return list(map(lambda x: x + " : " + str(s.count(x)), list(set(s))))

def main():
    print(hauefigkeiten('Erdbeere'))
    print(hauefigkeiten('Einstein'))

if __name__ == "__main__":
    main()