from home.models import Gps
import datetime


def calculate_api_hits_time_diff():
    # pobierz wszystkie obiekty z tabeli Gps
    query = Gps.objects.all()

    # lista różnic czasu pomiędzy zapytaniami
    diff_list = []

    for j, x in enumerate(query):
        try:
            # oblicz jaki czas upłynął pomiędzy zapytaniami
            diff = query[j+1].datetime - x.datetime
            # odrzuć wszstkie błędne zapytania
            if diff < datetime.timedelta(minutes=1):
                diff_list.append(diff)
        except:
            pass

    # oblicz średnią z różnic
    diff = sum(diff_list, datetime.timedelta()) / len(diff_list)
    return diff


print(calculate_api_hits_time_diff())
