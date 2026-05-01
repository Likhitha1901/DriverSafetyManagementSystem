accident_zones = [
    {"lat": 12.9716, "lon": 77.5946},
    {"lat": 13.0352, "lon": 77.5970}
]

def check_zone(lat, lon):
    for zone in accident_zones:
        if abs(lat - zone["lat"]) < 0.01 and abs(lon - zone["lon"]) < 0.01:
            return True
    return False
