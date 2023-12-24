import random
import googleapiclient.discovery

def getVideo(playlist, api_key):
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    playlist_items = []
    next_page_token = None
    while True:
        playlist_request = youtube.playlistItems().list(            
                part='contentDetails',
                maxResults=500,
                playlistId=playlist,
                pageToken=next_page_token)     
        playlist_response = playlist_request.execute()
        playlist_items.extend(playlist_response['items'])
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break

    video_ids = [item['contentDetails']['videoId'] for item in playlist_items]
    random_video_id = random.choice(video_ids)
    video_url = f'https://www.youtube.com/watch?v={random_video_id}'
    embedurl="https://www.youtube.com/embed/"+random_video_id
    return embedurl

