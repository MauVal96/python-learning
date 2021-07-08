# Dictionary exercises
def run():
    my_dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
    }

    print(my_dictionary['key1'])
    print(my_dictionary['key2'])
    print(my_dictionary['key3'])

    country_population = {
        'Argentina': 44938712,
        'Brazil': 210147125,
        'Colombia': 50372424
    }

    # Keys
    for country in country_population.keys():
        print(country)

    # Values
    for country in country_population.values():
        print(country)

    # Items key-value
    for country, population in country_population.items():
        print(country + ' has : ' + str(population) + ' habitants')


if __name__ == '__main__':
    run()