def add_time(a, b):
    start = a.split()
    start_h, start_m = [int(val) for val in start[0].split(':')]
    start_app = start[1]
    dur_h, dur_m = [int(val) for val in b.split(':')]

    end_m = start_m+dur_m
    end_h = end_m//60
    end_m %= 60
    end_h += start_h+dur_h

    if (end_h//12) % 2 == 0:
        end_app = start_app
    else:
        end_app = 'AM' if start_app == 'PM' else 'PM'

    return f'{end_h:02}:{end_m:02} {end_app}'


print(add_time("11:43 PM", "24:20"),
      'Returns: 12:03 AM')
