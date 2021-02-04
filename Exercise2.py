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
    print(y)
