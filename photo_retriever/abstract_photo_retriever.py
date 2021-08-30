from abc import ABC, abstractmethod
import nasapy
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

class PhotoRetriever(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def retrievePictureInfos(self):
        pass

    @abstractmethod
    def downloadPicture(self):
        pass

# Retrieve photos from the nasa api
class NasaPhotoRetriever(PhotoRetriever):
    def __init__(self):
        super().__init__()

    def retrievePictureInfos(self):
        load_dotenv()
        NASA_API_KEY = os.getenv('NASA_API_KEY')
        nasa = nasapy.Nasa(key = NASA_API_KEY)
        d= datetime.today().strftime('%Y-%m-%d')
        apod = nasa.picture_of_the_day(date=d, hd=True)
        print(apod)
        return apod

    def downloadPicture(self, apod):
        # check if there is an image
        if(apod["media_type"] == "image"):
            # if there is an image choose between hd and low res
            if("hdurl" in apod.keys()):
                self.download(apod["hdurl"])
            else:
                self.download(apod["url"])
            # rename and download image
        else:
            return -1
    
    def download(self, url):
        response = requests.get(url)
        file = open("sample_image.png", "wb")
        file.write(response.content)
        file.close()