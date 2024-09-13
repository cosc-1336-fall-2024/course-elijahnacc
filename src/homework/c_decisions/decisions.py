#divides option by total and returns result
def get_options_ratio(option, total):
    ratio = option / total
    return ratio

#checks prior ratio value and returns assigned rating
def get_faculty_rating(ratio):
    if ratio <= 0 or ratio >= 1:
        return "Invalid Value"
    elif ratio >= .9:
        return "Excellent"
    elif ratio > .8:
        return "Very Good"
    elif ratio > .7:
        return "Good"
    elif ratio > .6:
        return "Needs Improvement"
    elif ratio < .6 and ratio > 0:
        return "Unacceptable"
    else:
        return "Invalid Value"