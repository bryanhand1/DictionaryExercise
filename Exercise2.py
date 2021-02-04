### Exercise 2 Dictionary exercises Assigment
### Create a dictionary with world series winners

### Read file and populate list of winners
WSwinners_file = open("WorldSeriesWinners.txt", "r")
WSwinners = WSwinners_file.readlines()

winners = []

for w in WSwinners:
    winners.append(w.rstrip("\n" + "\r"))


### Create a list of years from 1903-2008 without 1904 and 1994

years = [1903]

# add first set of years to list
for y in range(1905, 1994):
    years.append(y)

# add second set of years to list
for y in range(1995, 2008):
    years.append(y)

# create a dictionary with key and value from both list
# create empty list then add key and values
WSdict = {years[i]: winners[i] for i in range(len(years))}

# Ask for year
given_year = int(input("What year would you like to see the World Series Winner? "))

if given_year in WSdict.keys():
    print(
        "The World Series Winner in "
        + str(given_year)
        + " was the "
        + WSdict[given_year]
    )
else:
    print(
        "Sorry the World Series was not played in that year."
        + "\n"
        + "The World Series has been played every year from 1903 to 2008 except 1904 and 1994"
    )
