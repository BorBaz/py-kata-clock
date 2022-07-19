# My case
def past(hours, minutes, seconds):
    # Convert hours to seconds
    hour_to_seconds = hours * 3600

    # Convert minutes to seconds
    minutes_to_seconds = minutes * 60

    seconds = hour_to_seconds + minutes_to_seconds + seconds

    return seconds * 1000

# Best case
def past_bc(h, m, s):
    return (3600*h + 60*m + s) * 1000


print(past(0,1,1))
