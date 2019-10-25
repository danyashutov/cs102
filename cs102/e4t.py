class grid:
    def __init__(self, n=3):
        """Generation of the base table"""
        self.n = n
        self.table = [[((i * n + i / n + j) % (n * n) + 1) for j in range(n * n)] for i in range(n * n)]
        print
        "The base table is ready!"

    def __del__(self):
        pass

    def show(self):
        for i in range(self.n * self.n):
            print
            self.table[i]