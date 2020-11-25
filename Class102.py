import cv2
import time
import dropbox
import random

startTime=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videocaptureobj=cv2.VideoCapture(0)
    result=True
    while(result==True):
        ret,frame=videocaptureobj.read()
        imageName="Img"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        startTime=time.time()
        result=False
        print("Snapshot Taken")
        return imageName
    videocaptureobj.release()
    cv2.destroyAllWindows()


def upload_file(imageName):
    access_token="50OLt0UhApUAAAAAAAAAAfhFttxJBgEGgJ1jRJzDej5yP86jPhSeXtw3RmjIz3gN"
    fileFrom=imageName
    fileTo="/Test/"+imageName
    dbx=dropbox.Dropbox(access_token)

    with open(fileFrom, 'rb')as f:
        dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)

    print("File Uploaded")



def main():
    while(True):
        if((time.time()-startTime)>=200):
            name=take_snapshot()
            upload_file(name)

main()
