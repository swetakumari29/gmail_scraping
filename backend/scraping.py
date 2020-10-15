from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class GmailScraping(object):

    def __init__(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # flow = InstalledAppFlow.from_client_secrets_file(
                #     'credentials.json', SCOPES)
                from GmailScraping.settings import GMAIL_SCRAPING_CREDENTIALS
                flow = InstalledAppFlow.from_client_config(GMAIL_SCRAPING_CREDENTIALS, SCOPES)

                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('gmail', 'v1', credentials=creds)

    # Get Email Content For selected message content
    def get_email_content(self, email_limit=20, user_id='me', query_text='invoice OR subscription OR bill OR amount'):

        response = self.service.users().messages().list(userId=user_id, q=query_text).execute()  #Search email for gven text word

        result = []
        for r in response['messages'][:email_limit]:
            rs = self.service.users().messages().get(userId=user_id, id=r['id']).execute()
            # print("\nMessage Body Snippet: ", rs['snippet'])
            # print("Message Content Payload: ", )
            # for x in rs['payload']:
            #     print("     ", x, rs['payload'][x])
            result.append({'snippet_message': rs['snippet'], 'payload': rs['payload']})
        # print("Top "+str(email_limit)+" Emails details shows above for more details increase the limit")

        return result

#
# if __name__ == '__main__':
#     gmail_scraping = GmailScraping()
#     result = gmail_scraping.get_email_content(email_limit=20, query_text="invoice OR subcription")
#     print("result", result)

