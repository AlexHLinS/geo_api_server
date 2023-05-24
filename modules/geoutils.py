from geopy.geocoders import get_geocoder_for_service


async def geocode(
    query: str,
    geocoder: str = "nominatim",
    config: dict = {"user_agent": "test/script"}
) -> tuple | None:
    """Retuns a tuple of coordinates

    Args:
        query (str): address line
        geocoder (str, optional): _description_. 
        Defaults to "nominatim".
        config (_type_, optional): _description_. 
        Defaults to {"user_agent": "test/script"}.

    Returns:
        tuple | None: Retuns a tuple of coordinates if geocode was successful,
        or None 
    """
    cls = get_geocoder_for_service(geocoder)
    geolocator = cls(**config)
    location = geolocator.geocode(query)
    if location:
        longitude, latitude, _ = location.point
        return longitude, latitude
    return None
