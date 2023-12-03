from read_file import read_file
import csv


def parse_data():
    data = read_file('day2.txt')
    data = data.split('\n')

    colors = ['green', 'blue', 'red']
    
    csv_file_lines = []
    for line in data:
        line = line.split(':')
        game = line[0]
        game_number = int(game.split(' ')[1])

        results = line[1]
        results = [i.split(',') for i in results.split(';')]

        for game_set in results:

            set_results = {'game':game_number,
                        'green':None,
                        'blue':None,
                        'red':None}
            
            for cubes in game_set:
                for color in colors:
                    if color in cubes:
                        number_cubes = cubes.split(' ')
                        set_results[color] = int(number_cubes[1])

            csv_file_lines.append(set_results)
    
    with open('data/day2_parsed.csv', 'w', newline='') as f:
        fieldnames = ['game', 'green', 'blue', 'red']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in csv_file_lines:
            csv_writer.writerow(row)
    

if __name__ == "__main__":
    parse_data()

