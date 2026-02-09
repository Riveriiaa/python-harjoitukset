import mysql.connector


def main():
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="password",
        autocommit=True
    )

    cursor = connection.cursor()

    icao = input("Enter the ICAO code of an airport: ").upper()

    sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
    """

    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        name = result[0]
        city = result[1]

        print(f"Airport name: {name}")
        print(f"Location: {city}")
    else:
        print(f"No airport found with ICAO code {icao}")


    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()