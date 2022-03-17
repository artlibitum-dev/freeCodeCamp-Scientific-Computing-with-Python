def add_time(start, duration, *args):

    new_time = ""
    days = 0
    days_of_week = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'   
    ]

    startTime = start.split(' ')

    startHours, startMinutes = startTime[0].split(':')
    dayTime = startTime[1]

    durationHours, durationMinutes = duration.split(':')
    startHours24 = int(startHours) if dayTime == "AM" else int(startHours) + 12
    
    endMinutes = int(startMinutes) + int(durationMinutes)
    
    if endMinutes >= 60:
        durationHours = int(durationHours) + 1
        endMinutes = endMinutes - 60

    endHours = int(startHours24) + int(durationHours)

    if endHours > 24:
        days = endHours // 24
        endHours = endHours % 24

    if endHours >= 12 :
        dayTime = 'PM'            
        if endHours != 0 and endHours % 12 != 0: endHours -= 12
    else: 
        dayTime = 'AM'

    if endHours == 0: endHours = 12

    new_time = f'{endHours}:{endMinutes:02} {dayTime}'

    if args:
        day_index = int(days_of_week.index(args[0].capitalize())) + days
        new_time += f', {days_of_week[day_index % 7]}'
    
    if days == 1:
        new_time += f' (next day)'
    elif days > 1: 
        new_time += f' ({days} days later)'

    return new_time