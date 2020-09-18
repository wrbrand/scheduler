import sys
import datetime

OPENING_HOURS = [
    (datetime.timedelta(hours=8), datetime.timedelta(hours=23)),
    (datetime.timedelta(hours=10, minutes=30), datetime.timedelta(hours=23, minutes=30))
]

DAY_OF_WEEK_TO_HOURS = {
    0: 0, 
    1: 0, 
    2: 0,
    3: 0,
    4: 1,
    5: 1,
    6: 1
}

CLEANING_TIME = 35

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

def roundShowtime(t):
    return datetime.timedelta(minutes=((t.total_seconds() // 60) // 5) * 5)
    
def output(showings, movies):
    day_of_week = datetime.date.today().weekday()
    
    hours = OPENING_HOURS[DAY_OF_WEEK_TO_HOURS[day_of_week]]

    print(datetime.date.today().strftime("%A %m/%d/%Y"))
    for m in movies:
        print('\n', m)
        for (hour, minute) in showings[DAY_OF_WEEK_TO_HOURS[day_of_week]][m.title][::-1]:
            start = datetime.time(hour=int(hour), minute=int(minute))
            end = datetime.time(hour=int(hour + (m.duration // 60)), minute=int((minute + m.duration) % 60))
            print('\t', start, '-', end)
   
def main():
    if len(sys.argv) < 2:
        print("Usage: python scheduler.py <inputFile>")
        return
       
    filename = sys.argv[1]

    movies = parse(filename)
    
    showings = {}
    
    for i in range(len(OPENING_HOURS)):
        (opening, closing) = OPENING_HOURS[i]
        
        showings[i] = {}
        
        for movie in movies:
            shows = []
            
            startTime = closing - datetime.timedelta(minutes=movie.duration)
            startTime = roundShowtime(startTime)
            while startTime > opening:
                hours = startTime.total_seconds() // (60*60)
                minutes = (startTime.total_seconds() // 60) - (hours * 60)
                shows.append((hours, minutes))
                startTime -= datetime.timedelta(minutes=CLEANING_TIME)
                startTime -= datetime.timedelta(minutes=movie.duration)
                
                startTime = roundShowtime(startTime)
                
            showings[i][movie.title] = shows
       
    output(showings, movies)        
    
    
if __name__ == '__main__':
    main()