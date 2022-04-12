def add_time(start, duration):
    start_time = start.replace(":", " ").split()

    duration_time = duration.replace(":", " ").split()
    duration_hour = int(duration_time[0])
    duration_minutes = int(duration_time[1])

    starting_hour = int(start_time[0])
    starting_minutes = int(start_time[1])
    starting_day_time = start_time[2]
    day = ''  # next day, 2 days after and so on
    # week_days = {'monday': 1,
    #              'tuesday': 2,
    #              'wednesday': 3,
    #              'thursday': 4,
    #              'friday': 5,
    #              'saturday': 6,
    #              'sunday': 7
    #              }.get(value)

    minutes = duration_minutes + starting_minutes
    hour = duration_hour + starting_hour
    if minutes > 60:
        minutes -= 60
        hour += 1
        
    print(minutes)
    print(hour)


add_time("12:40 PM", "200:32")
