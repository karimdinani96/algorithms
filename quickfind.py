class QuickFind:

    ids = []

    def __init__(self, n):
        for i in range(0, n):
            self.ids.insert(i, i)

    def connected(self, p, q):
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        pid = self.ids[p]
        qid = self.ids[q]
        for i in range(0, len(id)):
            if self.ids[i] == pid:
                self.ids[i] = qid


def main():
    qf = QuickFind(10)


if __name__ == '__main__':
    print("this is a demo for quickfind algorithm")
    main()
