def median():
    Liste = [7,3,2,5,9]
    Mitte = int(len(Liste)/2)
    Liste.sort()
    print(Liste[Mitte])

def main():
    median()

if __name__ == "__main__":
    main()