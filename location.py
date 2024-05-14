import requests

def get_location_from_ip(ip_address):
    try:
        response = requests.get(f'http://ipinfo.io/{ip_address}/json')
        data = response.json()
        location = {
            'ip': data['ip'],
            'city': data['city'],
            'region': data['region'],
            'country': data['country'],
            'loc': data['loc'],
            'org': data['org']
        }
        return location
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
# 110.224.187.91
# Example usage:
ip_address = '110.224.187.91'  # Example IP address (Google's public DNS)
location_info = get_location_from_ip(ip_address)
if location_info:
    print("Location Information:")
    print(f"IP Address: {location_info['ip']}")
    print(f"City: {location_info['city']}")
    print(f"Region: {location_info['region']}")
    print(f"Country: {location_info['country']}")
    print(f"Location (latitude, longitude): {location_info['loc']}")
    print(f"Organization: {location_info['org']}")
