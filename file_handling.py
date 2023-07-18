def data_separation(path):
    fh = open(path, "r")
    return fh.read()


if __name__ == "__main__":
    path = "C:\\Users\\vishn\\OneDrive\\Desktop\\New Text Document.txt"
    result = data_separation(path)
    print(result)
    print(result)
