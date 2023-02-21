import dropbox
from dropbox.exceptions import AuthError
from django.conf import settings
import pickle
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def open_folder(request):
    # working with direct token which is bad for live environment but okay for testing purposes
    try:
        dbx = dropbox.Dropbox(settings.DROPBOX_ACCESS_TOKEN)
    except AuthError as e:
        print('Error connecting to Dropbox with access token: ' + str(e))

    dbx.users_get_current_account()
    
    results = dbx.files_list_folder('')
    file_list = [entry.name for entry in results.entries]
    return render(request, 'index.html', {'file_list': file_list})

#TODO
# View that utilizes pickle file generated from authenticate, but does the same thing as view above.
def dropbox_user_view(request):

    # load access token from dbx_token.pickle file
    with open('yourr_token.pickle', 'rb') as f:
        token_data = pickle.load(f)
    access_token = token_data['access_token']

    # create Dropbox client object
    client = dropbox.Dropbox(access_token)

    # list contents of current folder
    result = client.files_list_folder('')
    entries = [entry.name for entry in result.entries]

    # render template with entries
    return render(request, 'dropbox.html', {'entries': entries})

# TODO
# this view will allow the user to redirect to the folder they have clicked on, provided they are authorized.
def redirect_to_dropbox_folder(request):
    # Get the Dropbox access token from the user's session
    # Get the folder path from the URL query parameter
    # Build a Dropbox shared link for the folder
    # Redirect the user to the shared link URL
    pass
