days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


def add_time(start, duration, day_of_week = ''):
    #Hours and minutes to add to the start time
    time_to_add = duration.split(':')
    hours_to_add = time_to_add[0]
    minutes_to_add = time_to_add[1]
    
    #Time period, hour and minute from the start time
    splitted_time = start.split(" ")
    time_selected = splitted_time[0]
    time_period = splitted_time[1]
    star_hour = time_selected.split(':')[0]
    start_minutes = time_selected.split(':')[1]
    days_later = 0
    add_addiotal_hour = 0
    sum_of_hour = 0

    final_minute = int(start_minutes) + int(minutes_to_add)  
    if final_minute >= 60:
        final_minute -= 60
        add_addiotal_hour += 1
        
    
    if int(hours_to_add)//24 >= 1:
        days_later += int(hours_to_add)//24
        add_addiotal_hour += int(hours_to_add)%24
    else:
        sum_of_hour +=  int(hours_to_add)
        
    sum_of_hour += int(star_hour) + add_addiotal_hour
    
    if sum_of_hour >= 12:
        final_hour = "12" if sum_of_hour - 12 == 0 else sum_of_hour - 12
        if time_period == 'PM':
            time_period = 'AM'
            days_later += 1
        else:
            time_period = 'PM'
    else:
        final_hour = sum_of_hour
        
    result =  str(final_hour) + ':' + "{:02}".format(final_minute) + ' ' + time_period
    
    if day_of_week:
        days_lower_case = [day.lower() for day in days_of_the_week]
        index_of_day = days_lower_case.index(day_of_week.lower())
        days_ahead = days_later%7
        final_index = index_of_day
        
        while days_ahead > 0:
            index_of_day += 1       
            if index_of_day > 6:
                index_of_day = 0
            days_ahead -= 1

                
        
        result += ', ' + days_of_the_week[index_of_day]
  
    
    if days_later > 0:
        result += ' ' + '(next day)' if days_later == 1 else f' ({days_later} days later)'
    
    return result
    
add_time('8:16 PM', '466:02', 'tuesday')