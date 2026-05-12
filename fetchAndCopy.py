import fetch_book
import sys
import os

def printUsage():
    print("Wrong number of arguments.\nUsage :\n   fetchAndCopy.py url_of_story number_of_chapters name_of_book")


if __name__ == "__main__":
    args = sys.argv[1:]
    if(len(args) != 3):
        printUsage()
        exit()

    next_url = args[0]
    nb_chapters = int(args[1])
    name_of_book = args[2]

    print("---------Fetch from royalroad------")
    fetch_book.main(next_url,nb_chapters,"{0}.html".format(name_of_book))

    os.chdir("Calibre")
    print("---------Conversion from htlml to azw3 (kindle compatibility)------")
    os.system("ebook-convert ../{0}.html ../{0}.azw3".format(name_of_book))
    print("---------Transferring to the device------")
    os.system("ebook-device cp --force ../{0}.azw3 dev:/documents/{0}.azw3".format(name_of_book))
    print("----------Erasing temp files--------")
    os.chdir("..")
    os.remove("{0}.azw3".format(name_of_book))
    os.remove("{0}.html".format(name_of_book))
    print("----------Done!-------------")


