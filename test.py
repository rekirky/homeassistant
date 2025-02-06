def validate_login(site,password):    
    url = f"{site}/login"
    params = {"password": {password}}
    response = requests.get(url, params=params)
    root = ET.fromstring(response.text)
    if root.find(".//authenticated").text == '1':
        return True
    else: 
        return False

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect.

    Data has the keys from STEP_USER_DATA_SCHEMA with values provided by the user.
    """
    await hass.async_add_executor_job(validate_login(), data[CONF_HOST], data[CONF_PASSWORD])
    

    hub = PlaceholderHub(data[CONF_HOST])

    if not await hub.authenticate(data[CONF_PASSWORD]):
        raise InvalidAuth

    # If you cannot connect:
    # throw CannotConnect
    # If the authentication is wrong:
    # InvalidAuth

    # Return info that you want to store in the config entry.
    return {"title": "Name of the device"}
