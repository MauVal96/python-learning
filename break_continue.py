# Break and continue statements
def run():
    # Continue
    for counter in range (1000):
        if counter %2 != 0:
            continue
        else: 
            print(counter)
    
    # # Break 1
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    
    # # Break 2
    # text = input('Input a text: ')
    # for letter in text:
    #     if letter == 'o':
    #         break
    #     print(letter)


if __name__ == '__main__':
    run()
