"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

# These date below will not change often so we can pre-calculate them.
speed_interval = [200, 400, 600, 1000]

speed_table = {speed_interval[0]: [15, 34],
               speed_interval[1]: [15, 32],
               speed_interval[2]: [15, 30],
               speed_interval[3]: [11.428, 28]}

finish_time = {200: [5.88, 13.5],
               300: [9.0, 20.0],
               400: [12.13, 27.0],
               600: [18.799, 40.0],
               1000: [33.08, 75.0]}

exceed_number = 1.1


#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.

#  Overall closing time limits vary for each brevet according to the distance.
#  These are: (in hours and minutes, HH:MM) 13:30 for 200 KM,
#                                           20:00 for 300 KM,
#                                           27:00 for 400 KM,
#                                           40:00 for 600 KM,
#                                           75:00 for 1000 KM.
#  The last control distance should be between the brevet distance and
#  that distance plus 10% and return the value according ot the time limits of distance

def get_hour_min_day(hour):
    """
    Args:
        hour: a float number of hours after computing
    return:
        a set of hours and time
    """
    total_minutes = hour * 60
    days = int(hour // 24)
    hours = int((total_minutes // 60) % 24)
    minutes = int(round(total_minutes % 60))
    return days, hours, minutes


def determine_interval(distance):
    """
    Args:
        distance: number, the control distance in kilometers
    Returns:
         interval, the index of speed_interval.
    """
    index = 0
    for i in range(0, len(speed_interval)):
        if distance > speed_interval[i]:
            index += 1
    return index


def compute_time(distance, interval, speed_type):
    """
    Args:
        distance: number, the control distance in kilometers
        interval: number, the interval of distance
        speed_type: boolean, 1 means max speed, and 0 means min speed
    """
    time = 0
    while interval >= 0:
        if interval == 0:
            # distance is smaller than or equal to 200
            time += distance / speed_table[speed_interval[0]][speed_type]
        else:
            # distance is greater than 200
            extra_distance = distance - speed_interval[interval-1]
            time += extra_distance / speed_table[speed_interval[interval]][speed_type]
            distance -= extra_distance
        interval -= 1
    return time


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    # invalid case
    if control_dist_km > brevet_dist_km * exceed_number:
        return ""
    # edge case: ending
    elif brevet_dist_km <= control_dist_km <= brevet_dist_km * exceed_number:
        time = finish_time[brevet_dist_km][0]
    # normal case
    else:
        time = compute_time(control_dist_km, determine_interval(control_dist_km), 1)
    day, hour, minute = get_hour_min_day(time)
    final_time = arrow.get(brevet_start_time).shift(days=+day, hours=+hour, minutes=+minute)
    return final_time.isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    # invalid case
    if control_dist_km > brevet_dist_km * exceed_number:
        return ""
    # edge case: beginning
    elif control_dist_km == 0:
        time = arrow.get(brevet_start_time).shift(hours=+1)
        return time.isoformat()
    # edge case: ending
    elif brevet_dist_km <= control_dist_km <= brevet_dist_km * exceed_number:
        time = finish_time[brevet_dist_km][1]
    # normal case
    else:
        time = compute_time(control_dist_km, determine_interval(control_dist_km), 0)
    day, hour, minute = get_hour_min_day(time)
    final_time = arrow.get(brevet_start_time).shift(days=+day, hours=+hour, minutes=+minute)
    return final_time.isoformat()

