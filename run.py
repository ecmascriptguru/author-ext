from src.author_ext import AuthorHunter


def run():
    url = 'https://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
    hunter = AuthorHunter(url)
    print(hunter)


if __name__ == '__main__':
    run()