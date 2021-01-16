"""Generate sales report showing total melons each salesperson sold."""

# create empty lists # !! create empty dictionary
salespeople = []
melons_sold = []

f = open('sales-report.txt')
# loop through file
for line in f:
    # strip whitespace and line breaks
    line = line.rstrip()
    # split line by pipe into list of entries
    entries = line.split('|') # !! instead of making this a list, unpack here into 3 variables with

    # name first item of entries list 
    salesperson = entries[0] # !! assign variables as values, change to int and float
    # name last item of entries list
    melons = int(entries[2])

    # if the salesperson already has an entry
    if salesperson in salespeople: # !! reference and update by key - use dict.get? should cover this whole block
        # give the salesperson a position based on their index
        position = salespeople.index(salesperson)
        # add the corresponding number of melons to the melons_sold list based on salesperson position
        melons_sold[position] += melons
    # if salesperson isn't already in salespeople,
    else:
        # add them
        salespeople.append(salesperson)
        # add their melons to the melons_sold list
        melons_sold.append(melons)

# for each salesperson, print their name and their melons sold
for i in range(len(salespeople)): # !! print using .items?
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')