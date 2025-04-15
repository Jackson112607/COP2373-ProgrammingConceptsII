# This program creates a database that includes the population in 2023 of 10 cities in Florida. The program then asks the
# user which city they'd like to see population data for. It displays the population of that city and its growth for the
# next 20 years at a 2% growth rate in a graph.

# Import SQL and matplotlib.
import sqlite3
import matplotlib.pyplot as plt

# Create the database for each city's population.
def create_database_and_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Insert the city names and populations for 2023 into the database.
def insert_initial_data(db_name):
    cities = [
        "Miami", "Jacksonville", "Tampa", "Orlando", "St. Petersburg",
        "Hialeah", "Tallahassee", "Fort Lauderdale", "Cape Coral", "Pembroke Pines"
    ]
    populations_2023 = [467963, 954614, 418245, 307573, 258308, 220998, 201735, 182595, 204952, 170185]

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for city, population in zip(cities, populations_2023):
        cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city, 2023, population))
    conn.commit()
    conn.close()

# Applies the 2% growth rate to populations for the next 20 years.
def simulate_population_growth(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT city FROM population WHERE year = 2023")
    cities = [row[0] for row in cursor.fetchall()]

    for city in cities:
        cursor.execute("SELECT population FROM population WHERE city = ? AND year = 2023", (city,))
        population = cursor.fetchone()[0]
        for year in range(2024, 2044):
            population = int(population * 1.02)
            cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city, year, population))
    conn.commit()
    conn.close()

# Display the population growth in a graph.
def show_population_growth(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT city FROM population WHERE year = 2023")
    cities = [row[0] for row in cursor.fetchall()]

    print("Available cities:")
    for i, city in enumerate(cities):
        print(f"{i+1}. {city}")
    city_index = int(input("Enter the number of the city to show population growth: ")) - 1
    selected_city = cities[city_index]
    cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (selected_city,))
    data = cursor.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.plot(years, populations)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title(f"Population Growth for {selected_city}")
    plt.grid(True)
    plt.show()

# Run the program.
def main():
    db_name = "population_jh.db"
    create_database_and_table(db_name)
    insert_initial_data(db_name)
    simulate_population_growth(db_name)
    show_population_growth(db_name)

# Call main.
main()