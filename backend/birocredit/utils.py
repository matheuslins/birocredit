

def parser_choice(choosed, choices):
    item = list(filter(lambda x: x[0].startswith(str(choosed)), choices))
    if item:
        return item[0][1]
