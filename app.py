import requests

def getHoliday(country: str, year: int, month: int, day: int) -> dict:
    """
    Get holiday information for a given country and date.
    """
    api_key = "5414c7fb33b7474c9a50c4952ddf6032"
    url = f"https://holidays.abstractapi.com/v1/?api_key={api_key}&country={country}&year={year}&month={month}&day={day}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return {
                "name": data[0].get("name"),
                "type": data[0].get("type"),
                "location": data[0].get("location"),
                "date": data[0].get("date")
            }
        else:
            return {"message": "No holiday on this date."}
    else:
        return {"error": "Failed to retrieve data from API"}
