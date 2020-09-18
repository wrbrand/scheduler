import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python scheduler.py <inputFile>")
        return
       
    filename = sys.argv[1]

    movies = []
    with open(filename, 'r') as f:
        movies = f.readlines()[1:]
        
    print(movies)
    
if __name__ == '__main__':
    main()