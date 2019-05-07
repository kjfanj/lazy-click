import webbrowser

# url = 'http://www.python.org/'

# # Open URL in a new tab, if a browser window is already open.
# webbrowser.open_new_tab(url + 'doc/')

# # Open URL in new window, raising the window if possible.
# webbrowser.open_new(url)


def get_websites(filename):
    with open(filename) as f:
        read_data = f.read()
        print(read_data)
        return read_data.split('\n')


def main():
    # run everything here
    websites = get_websites('websites.txt')
    print(websites)


if __name__ == "__main__":
    main()
