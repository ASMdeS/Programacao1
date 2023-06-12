esconderijo = input().lower()
suspeito = input().lower()

if esconderijo == suspeito:
    print("Ahá, te encontrei e é o fim das suas férias!")
else:
    print("Carambolas, ele não está aqui. Ele continua se divertindo!")
    reteste = input()
    if reteste == esconderijo:
        print("Ahá, te encontrei e é o fim das suas férias!")
    else:
        print("Carambolas, ele não está aqui. Ele continua se divertindo!")
        reteste = input()
        if reteste == esconderijo:
            print("Ahá, te encontrei e é o fim das suas férias!")
        else:
            print("Carambolas, ele não está aqui. Ele continua se divertindo!")
            print("AAAAAAAH, ele escapou de vez!")