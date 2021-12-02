import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def uploadFile(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        
        for root, dir, files in os.walk(fileFrom):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.join(root, filename)
                dropbox_path = os.path.join(fileTo, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken = "OY-YXlSZLz8AAAAAAAAAAXhqrVynfw3fF5OColawtGY2gxbh_ZHmZ3lLdxWMygCN"
    transferData = TransferData(accessToken)  
    fileFrom = input("Enter The File To Be Transffered -> ") 
    fileTo = input("Enter The Path To Upload To Dropbox -> ")
    transferData.uploadFile(fileFrom,fileTo)
    print("File has been moved")
main()             
