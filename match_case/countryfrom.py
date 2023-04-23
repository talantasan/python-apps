while True:
    country = input('Enter your country: ')
    country = country.lower()
    match country:
        case 'germany':
            print('Hallo')
        case 'usa':
            print('Hello')
        case 'india':
            print('Namaste')
        case _:
            print('Wrong country entry')