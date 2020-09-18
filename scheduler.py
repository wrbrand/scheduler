import sys

class Movie():
    def __init__(self, line):
        sp = line.strip().split(',')
        if len(sp) != 4: 
            return False # todo: better error to throw
        
        self.title = sp[0]
        self.year = int(sp[1])
        self.rating = sp[2].strip()
        
        (hours, minutes) = sp[3].split(':')
        
        self.duration = int(hours) * 60 + int(minutes)
        
    def __repr__(self):
        return self.title + ' - Rated ' + self.rating + ', ' + str(self.duration // 60) + ':' + ("%02d" % (self.duration % 60)) 

def parse(filename): 
    movies = []
    with open(filename, 'r') as f:
        for line in f.readlines()[1:]:
            movies.append(Movie(line))
           
    return movies
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python scheduler.py <inputFile>")
        return
       
    filename = sys.argv[1]

    movies = parse(filename)
    
if __name__ == '__main__':
    main()