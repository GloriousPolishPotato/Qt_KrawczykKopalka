# Main demonstrujacy i testujacy mozliwosci klas Shelf i Product
#
#  Autorzy: Szymon Krawczyk, Michal Kopałka
#   Data utworzenia: 31.10.2020

import Shelf

def main():
    anime_shelf = Shelf.Shelf()


    try:
        anime_shelf.new_product("Megumin figurine", 99.98, 7)
        anime_shelf.new_product("HEJ", "asd", 123)


    except Shelf.Product.WrongTypeOfVariableInPriceError:
        print("fsdsafwef")


    #anime_shelf.new_product("Megumin figurine", 99.98, 7)
    #anime_shelf.new_product("Holo sticker", 5.55, 17)
    #anime_shelf.new_product(112, 123, 123)
    #anime_shelf.new_product("HEJ", "asd", 123)
    print(anime_shelf)

    anime_shelf.change_name("MegumiN figurine", "Megumin figure")
    anime_shelf.set_amount("megumin figure", 2)
    anime_shelf.set_price("megumin figure", 130.49)
    print(anime_shelf)

    anime_shelf.remove_product("megumin figure")
    anime_shelf.change_amount("HoLo StIcKeR", 25)
    print(anime_shelf)


if __name__ == '__main__':
    main()

# TODO rozbudowac