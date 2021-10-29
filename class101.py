import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A7R7Ib4WXMKAeDrSuMLPkNKunxlpSq0ybT89U1tipJF_xv82jatuE1FJWEO6VWA2yMSp4_7NBmFdrE1a_4fu3g0oJKK3GFADY7LiOoYXqIICidqP3JxbFtVeldZfs9P5CHRrhII'
    transferData = TransferData(access_token)

    file_from = input('Enter file location: ')
    file_to = input('Enter destination: ') # The full path to upload the file to, including the file name

    # API v2  
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()