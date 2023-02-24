import search as s


if __name__ == '__main__':
    print("Welcome to the Youtube Keyword Video Generator!! ")
    while True:
        title = input("What's the keyword? ")
        maxx = int(input("How many videos? "))
        print('')
        s.search(title, maxx, "link")
