import os
import googleapiclient.errors
import googleapiclient.discovery
import google_auth_oauthlib.flow

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python


class Searcher:
    def search(self, term):
        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = os.environ['YT_CLIENT_SECRET_PATH']

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        request = youtube.search().list(
            part="snippet",
            maxResults=10,
            q=term,
            safeSearch="none",
            type="video"
        )
        response = request.execute()

        print(response)


Searcher().search("one day polygon audio")
