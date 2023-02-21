import dropbox
import pickle

# Dropbox app key and secret
app_key = 'your_app_key_here'
app_secret = 'your_app_secret_here'

# authorize app with Dropbox API and get access token
auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = auth_flow.start()
print(f"Go to {authorize_url} to authorize the app.")
auth_code = input("Enter the authorization code: ")
access_token, user_id = auth_flow.finish(auth_code)
print(f"Access token: {access_token}")

# save access token to dbx_token.pickle file
token_data = {'access_token': access_token, 'user_id': user_id}
with open('your_token.pickle', 'wb') as f:
    pickle.dump(token_data, f)
