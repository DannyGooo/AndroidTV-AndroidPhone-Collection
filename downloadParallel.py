from gpapi.googleplay import GooglePlayAPI
import json
import time
import os.path
import multiprocessing
import os
import shutil
import glob

aimFileMobile ='/Users/dannyGooo/Documents/project-in-master-by-research/research-project/andro-tv/my-gooleplay-api-env/googleplay-api/mobile/apps/'
aimFileTV ='/Users/dannyGooo/Documents/project-in-master-by-research/research-project/andro-tv/my-gooleplay-api-env/googleplay-api/tv/apps/'

def downloadAPK(deviceServer, apkID, aimPath):  
    print(apkID) 
    path=f"{aimPath}{apkID}-folder/"
    if not os.path.exists(path):
        os.mkdir(path) 
    deviceServer.download(apkID,download_path=path)    


if __name__ == '__main__':    


    mail_TV = "dannyGooo@gmail.com"
    passwd_TV = 'password'

    mail_Mobile = 'dannyGooo@gmail.com'
    passwd_Mobile = 'password'


    apiTV = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename="x86TV_30_720")
    apiTV.login(email=mail_TV, password=passwd_TV)

    apiMobile = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename="pixel4_30")
    apiMobile.login(email=mail_Mobile, password=passwd_Mobile)



    # download apk
    f = open('/Volumes/Seagate/TV_Mobile_pair/pairs.json')
    totalPairs = json.load(f)
    f.close()

    


    currentPass, currentPassTV, currentDownloadTV, currentPassMobile, currentDownloadMobile = 0, 0, 0, 0, 0



    for pair in totalPairs:
        tvApkID = pair['apk_id_TV']
        mobileApkID = pair['apk_id_Mobile']
        try:
            p1 = multiprocessing.Process(target=downloadAPK, args=(apiTV, tvApkID, aimFileTV ))
            p2 = multiprocessing.Process(target=downloadAPK, args=(apiMobile, mobileApkID, aimFileMobile))

            p1.start()
            p2.start()

            p1.join()
            p2.join()
            


        except:
            print("An exception occurred for", tvApkID) 

        currentPass += 1
        print(currentPass)
        

