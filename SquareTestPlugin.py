class SquareTestPlugin:
    def input(self, infile):
        self.myfile = open(infile, 'r')

    def run(self):
        pass

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        for line in self.myfile:
            line = line.strip()
            line = line[1:len(line)-1]
            line = (float(x) for x in line.split(','))
            outfile.write(str(list(x**2 for x in line)))
            outfile.write("\n")
