def station_announcement(stations):
    for station in stations:
        yield (f"Next station is {station}")
        
stations = ["Railway Station", "Ambedkar Circle", "Corporation", "Chenamma Circle", "Hosur Road", "Hosur Bus Stand", "KIMS", "Vidyanagar", "BVB", "Unkal Cross"]

announcement = station_announcement(stations)

for announcement in stations:
    print(next(announcement))