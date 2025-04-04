#Daniel Colet Ayllo
#04/04/25
#Activitat 1: CRUD amb la base de dades CHINOOK


#LLibreries
import psycopg

#Creem la connexio a la base de dades
def connection():
    connexio = """         
        dbname = chinook_v2
        user = postgres
        password = pirineus
        host = localhost
        port = 5432
    """

    conn = psycopg.connect(connexio) #Ens connectem a la base de dades
    curs = conn.cursor()
    return curs

#Mostar opcions del menú per consolo
def printar_menu():
    print("\nMenú Principal")
    print("1 - Consultar tots els artistes")
    print("2 - Consultar artistes pel seu nom")
    print("3 - Consultar els 5 primers àlbums pel nom de l'artista")
    print("4 - Afegir un artista")
    print("5 - Modificar el nom d'un artista")
    print("6 - Borrar un artista")
    print("7 - Sortir")

#Definició per demanar una opció a l'usuari per executar la definició que correspon
def escollir_opcio(cursor):
    opcio = int(input("Escolliu una opció: "))
    if opcio == 1:
        consultar_artistes(cursor)
    elif opcio == 2:
        consultar_artistes_nom()
    elif opcio == 3:
        consultar_5_pri_alm()
    elif opcio == 4:
        afegir_artista()
    elif opcio == 5:
        modificar_artista()
    elif opcio == 6:
        borrar_artista()
    elif opcio == 7:
        print("Sortint...")
        exit()
    else:
        print("Opció no vàlida. Torna a intentar-ho.")
    return opcio

def menu():
    cursor = connection()
    while opcio != 7:
        printar_menu()
        opcio = escollir_opcio(cursor)


#Main
def main():
    menu()

if __name__ == "__main__":
    main()