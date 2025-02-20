import requests

def fetch_youtube_channel_details():
    api_url = "https://api.freeapi.app/api/v1/public/youtube/channel"
    api_response = requests.get(api_url)
    response_data = api_response.json()

    if response_data["success"] and "data" in response_data:
        channel_data = response_data["data"]
        channel_title = channel_data["info"]["snippet"]["title"]
        channel_description = channel_data["info"]["snippet"]["description"]
        return channel_title, channel_description
    else:
        raise Exception("Failed to fetch YouTube channel details")

def main():
    try:
        channel_title, channel_description = fetch_youtube_channel_details()
        print(f"Channel Title: {channel_title} \nChannel Description: {channel_description}")
    except Exception as error:
        print(str(error))

if __name__ == "__main__":
    main()

