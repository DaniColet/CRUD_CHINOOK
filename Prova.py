# Daniel Colet Ayllo
# 04/04/25
# Activitat 1: CRUD amb la base de dades CHINOOK

# Llibreries
import psycopg

# Connexió a la base de dades
def connection():
    conn = psycopg.connect(
        dbname="chinook_v2",
        user="postgres",
        password="pirineus",
        host="localhost",
        port="5432"
    )
    curs = conn.cursor()
    return conn, curs

# Mostra el menú d'opcions
def printar_menu():
    print("\nMenú Principal")
    print("1 - Consultar tots els artistes")
    print("2 - Consultar artistes pel seu nom")
    print("3 - Consultar els 5 primers àlbums pel nom de l'artista")
    print("4 - Afegir un artista")
    print("5 - Modificar el nom d'un artista")
    print("6 - Borrar un artista")
    print("7 - Sortir")

# Opció 1 - Consultar tots els artistes
def consultar_artistes(cursor):
    cursor.execute("SELECT * FROM Artist ORDER BY ArtistId;")
    resultat = cursor.fetchall()
    for fila in resultat:
        print(f"{fila[0]} - {fila[1]}")

# Opció 2 - Consultar artistes pel nom
def consultar_artistes_nom(cursor):
    nom_artista = input("Introdueix el nom de l'artista: ")
    cursor.execute("SELECT * FROM Artist WHERE Name ILIKE %s;", ('%' + nom_artista + '%',))
    resultat = cursor.fetchall()
    for fila in resultat:
        print(f"{fila[0]} - {fila[1]}")

# Opció 3 - Mostrar 5 primers àlbums d’un artista pel nom
def consultar_5_pri_alm(cursor):
    nom_artista = input("Nom de l'artista: ")
    cursor.execute("""
        SELECT Album.Title
        FROM Album
        JOIN Artist ON Album.ArtistId = Artist.ArtistId
        WHERE Artist.Name ILIKE %s
        ORDER BY Album.AlbumId
        LIMIT 5;
    """, ('%' + nom_artista + '%',))
    resultat = cursor.fetchall()
    for fila in resultat:
        print(f"- {fila[0]}")

# Opció 4 - Afegir un artista
def afegir_artista(conn, cursor):
    nom_nou_artista = input("Nom del nou artista: ")
    cursor.execute("INSERT INTO Artist(Name) VALUES (%s);", (nom_nou_artista,))
    conn.commit()
    print("Artista afegit correctament.")

# Opció 5 - Modificar el nom d’un artista
def modificar_artista(conn, cursor):
    id_artista = input("ID de l'artista a modificar: ")
    nom_artista_modificat = input("Nou nom: ")
    cursor.execute("UPDATE Artist SET Name = %s WHERE ArtistId = %s;", (nom_artista_modificat, id_artista))
    conn.commit()
    print("Artista modificat correctament.")

# Opció 6 - Esborrar un artista
def borrar_artista(conn, cursor):
    id = input("ID de l'artista a esborrar: ")
    cursor.execute("DELETE FROM Artist WHERE ArtistId = %s;", (id,))
    conn.commit()
    print("Artista esborrat correctament.")

# Gestió d'opcions del menú
def escollir_opcio(conn, cursor):
    opcio = int(input("Escull una opció: "))
    if opcio == 1:
        consultar_artistes(cursor)
    elif opcio == 2:
        consultar_artistes_nom(cursor)
    elif opcio == 3:
        consultar_5_pri_alm(cursor)
    elif opcio == 4:
        afegir_artista(conn, cursor)
    elif opcio == 5:
        modificar_artista(conn, cursor)
    elif opcio == 6:
        borrar_artista(conn, cursor)
    elif opcio == 7:
        print("Sortint del programa...")
        conn.close()
        exit()
    else:
        print("Opció no vàlida. Torna-ho a intentar.")
    return opcio

# Bucle principal
def menu():
    conn, cursor = connection()
    opcio = 0
    while opcio != 7:
        printar_menu()
        opcio = escollir_opcio(conn, cursor)

# Main
def main():
    menu()

if __name__ == "__main__":
    main()