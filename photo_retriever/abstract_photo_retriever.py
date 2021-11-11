"""class handling nasa api"""
from abc import ABC, abstractmethod
import os
from datetime import datetime, timedelta
import nasapy
import requests
from dotenv import load_dotenv

class PhotoRetriever(ABC):
    """Photo retriever"""

    @abstractmethod
    def retrieve_picture_infos(self):
        """retrieving picture info"""

    @abstractmethod
    def download_picture(self, apod):
        """download picture"""

class NasaPhotoRetriever(PhotoRetriever):
    """Retrieve photos from the nasa api"""

    def retrieve_picture_infos(self):
        load_dotenv()
        nasa_api_key = os.getenv('NASA_API_KEY')
        nasa = nasapy.Nasa(key=nasa_api_key)
        today = datetime.today()
        yesterday = today - timedelta(days=2)
        date_string = today.strftime('%Y-%m-%d')
        apod = nasa.picture_of_the_day(date=date_string, hd=True)
        print(apod)
        return apod

    def download_picture(self, apod):
        # check if there is an image
        if apod["media_type"] == "image":
            # if there is an image choose between hd and low res
            if"hdurl" in apod.keys():
                self.download(apod["hdurl"])
            else:
                self.download(apod["url"])
            # rename and download image
        else:
            return -1

    def download(self, url):
        """download the image"""
        response = requests.get(url)
        file = open("sample_image.png", "wb")
        file.write(response.content)
        file.close()
