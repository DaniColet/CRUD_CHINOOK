# Daniel Colet Ayllo
# 11/04/25
# Activitat 1: CRUD amb la base de dades CHINOOK

#Llibreries
import psycopg

#Definició que ens permet connectar-nos al PostgresSQL
def connection():
    connexio= """
        dbname = chinook_v2
        user = postgres
        password = pirineus
        host = localhost
        port = 5432
    """
    return psycopg.connect(connexio)

# Mostra el menú d'opcions per pantalla
def printar_menu():
    print("\nMenú Principal")
    print("1 - Consultar tots els artistes")
    print("2 - Consultar artistes pel seu nom")
    print("3 - Consultar els 5 primers àlbums pel nom de l'artista")
    print("4 - Afegir un artista")
    print("5 - Modificar el nom d'un artista")
    print("6 - Borrar un artista")
    print("7 - Sortir")

# Opció 1 - Definició per consultar i mostrar tots els artistes
def consultar_artistes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM artist ORDER BY artist_id;")
    resultat = cursor.fetchall()
    if resultat:
        for fila in resultat:
            print(f"ID: {fila[0]}, NOM: {fila[1]}")
    else:
        print("No hi ha resultats per aquesta consulta.")

# Opció 2 - Definició per fer una consulta per nom
def consultar_artistes_nom(conn):
    nom = input("Introdueix el nom de l'artista: ")
    if len(nom) < 2:
        print("Has d'introduir almenys 2 caràcters")
        return
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM artist WHERE Name ILIKE %s;", ('%' + nom + '%',))
    resultat = cursor.fetchall()
    if resultat:
        for fila in resultat:
            print(f"ID: {fila[0]}, NOM: {fila[1]}")
    else:
        print("No hi ha resultats per aquesta consulta.")

# Opció 3 - Definició per mostrar els 5 primers àlbums d’un artista pel nom
def consultar_5_pri_albums_artista(conn):
    nom = input("Nom de l'artista: ")
    if len(nom) < 2:
        print("Has d'introduir almenys 2 caràcters")
        return
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.album_id, a.title, art.name
        FROM album a
        JOIN artist art ON a.artist_id = art.artist_id
        WHERE art.name ILIKE %s
        ORDER BY a.album_id
        LIMIT 5;
    """, (nom + '%',))
    resultat = cursor.fetchall()

    if resultat:
        for fila in resultat:
            print(f"ID_ALBUM: {fila[0]}, NOM_ALBUM: {fila[1]}, NOM_ARTISTA: {fila[2]}")
    else:
        print("No hi ha resultats per aquesta consulta.")

# Opció 4 - Definició per afegir un artista nou
def afegir_artista(conn):
    nom = input("Nom del nou artista: ")
    if len(nom) < 3:
        print("Has d'introduir almenys 3 caràcters")
        return
    cursor = conn.cursor()
    cursor.execute("INSERT INTO artist(name) VALUES (%s);", (nom,))
    conn.commit()
    print("L’artista s’ha afegit correctament")

# Opció 5 - Definició per modificar el nom d’un artista existent
def modificar_artista(conn):
    id = input("ID de l'artista a modificar: ")
    nou_nom = input("Nou nom: ")
    if len(nou_nom) < 3:
        print("Has d'introduir almenys 3 caràcters")
        return
    cursor = conn.cursor()
    cursor.execute("UPDATE artist SET name = %s WHERE artist_id = %s;", (nou_nom, id))
    if cursor.rowcount == 0:
        print("No s'ha trobat cap artista amb aquesta ID.")
    else:
        conn.commit()
        print("L’artista s’ha modificat correctament")

# Opció 6 - Definició per eliminar un artista per ID com a paràmetre
def borrar_artista(conn):
    id = input("ID de l'artista a esborrar: ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM artist WHERE artist_id = %s;", (id,))
    if cursor.rowcount == 0:
        print("No s'ha trobat cap artista amb aquesta ID.")
    else:
        conn.commit()
        print("L’artista s’ha borrat correctament")

# Controlador del menú i accions amb les que interactua l'usuari
def menu():
    conn = connection()
    opcio = 0
    while opcio != 7:
        printar_menu()
        opcio_input = input("Selecciona una opció: ")

        if opcio_input.isdigit():
            opcio = int(opcio_input)
        else:
            print("Opció no vàlida, afegeix una opció correcte")
            opcio = 0  # Assignem un valor no vàlid per continuar el bucle

        if opcio == 1:
            consultar_artistes(conn)
        elif opcio == 2:
            consultar_artistes_nom(conn)
        elif opcio == 3:
            consultar_5_pri_albums_artista(conn)
        elif opcio == 4:
            afegir_artista(conn)
        elif opcio == 5:
            modificar_artista(conn)
        elif opcio == 6:
            borrar_artista(conn)
        elif opcio == 7:
            print("Sortint del programa...")
            conn.close()
        else:
            print("Opció no vàlida, afegeix una opció correcte")
    return conn

# Punt d'entrada i de sortida del programa
if __name__ == "__main__":
    conn = menu()
    conn.close()
    print("Connexió tancada.")