import webbrowser


def get_websites(filename):
    """
    take in a .txt file and return each line of text in a list
    """
    with open(filename) as f:
        read_data = f.read()
        return read_data.split('\n')


def openWebsites(websites):
    """
    opening the websites
    """
    for website in websites:
        if website:
            webbrowser.open_new(website)


def main():
        # get websites from txt file first
    websites = get_websites('websites.txt')

    # open websites
    openWebsites(websites)


if __name__ == "__main__":
    main()
