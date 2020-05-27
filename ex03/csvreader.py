from pprint import pprint


class CsvReader():
    def __init__(self, filename=None, sep=',',
                 header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()
        return isinstance(value, TypeError)

    def getdata(self):
        data = self.file.seek(0)
        data = self.file.read()
        arr = data.split("\n")
        csv = []
        if not self.header:
            arr = arr[1:len(csv)-1]
        for x in arr[self.skip_top:len(arr)-self.skip_bottom]:
            st = x.split(self.sep)
            i = 0
            for y in st:
                st[i] = y.strip()
                i += 1
            csv.append(st)
        return csv

    def getheader(self):
        data = self.file.seek(0)
        data = self.file.readline()
        arr = data.split("\n")
        csv = []
        for x in arr[:1]:
            st = x.split(self.sep)
            i = 0
            for y in st:
                st[i] = y.strip()
                i += 1
            csv.append(st)
        return csv[0]


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        pprint(data)
        pprint(header)
