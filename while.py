#While loop exercise  
def run():
    LIMIT = 1000000
    counter = 0
    power_2 = 1

    while power_2 < LIMIT:
        print('2 to the ' + str(counter) +'th power equals: ' + str(power_2))
        counter += 1
        power_2 = 2 ** counter


if __name__ == '__main__':
    run()