"""
given a list of tuples of movie watched times,
find how many unique minutes of the movie did the viewer watch e.g. [
(0,15),(10,25)]. The viewer watched 25 minutes of the movie.
"""


def minutes_movie_watched(tup):
    total_minutes = 0

    for i in range(len(tup) - 1):

        print(i)
        if tup[i][1] > tup[i + 1][0] and tup[i][1] > tup[i + 1][1]:
            print("1")
            total_minutes = tup[i][1] - tup[i][0]

        else:
            sub = 0
            if (tup[i][1] > tup[i + 1][0]) and (tup[i][1] <= tup[i + 1][1]):
                print("2")
                sub = tup[i][1] - tup[i + 1][0]
            else:
                print("3")
                sub = sub
            total_minutes += (tup[i][1] - tup[i][0]) + (tup[i + 1][1] - tup[i + 1][0]) - sub

    return total_minutes


print(minutes_movie_watched([(0, 15), (16, 30), (31, 45)]))

print(15+14+14)