def make_dict(filename):
    """Generate sales report showing total melons each salesperson sold."""

    f = open(filename)

    melon_sellers = {}
    attributes = {}

    for line in f:
        # strip whitespace and line breaks
        line = line.rstrip()
        # split line by pipe into list of entries
        name, total, num_sold = line.split('|')

        # if name in dictionary:
        if melon_sellers.get(name, 0) == 0:
             # add each list item to nested dictionary as keys and values
            melon_sellers[name] = attributes
            melon_sellers[name]['total'] = float(total)
            melon_sellers[name]['num_sold'] = int(num_sold)
        else:
            melon_sellers[name]['total'] += float(total)
            melon_sellers[name]['num_sold'] += int(num_sold)

    return melon_sellers


def print_sales(sellers_dict):

    for name, sub_dict in sellers_dict.items():
        print(f"{name}")
        for total, num_sold in sub_dict.items():
            print(f"{total}")
            print(f"{num_sold}")
            


melon_sales = make_dict('sales-report.txt')
print_sales(melon_sales)