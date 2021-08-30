from background_changer.background_changer import updateBackground
from photo_retriever.abstract_photo_retriever import NasaPhotoRetriever


def main():
    nasa = NasaPhotoRetriever()
    infos = nasa.retrievePictureInfos()
    nasa.downloadPicture(infos)
    updateBackground()

if __name__ == "__main__":
    main()