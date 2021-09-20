from background_changer.background_changer import update_background
from photo_retriever.abstract_photo_retriever import NasaPhotoRetriever
from Image_resizer.image_resizer import resize_image


def main():
    nasa = NasaPhotoRetriever()
    infos = nasa.retrievePictureInfos()
    nasa.downloadPicture(infos)
    resize_image(1920, 1080, infos['title'])
    update_background('Linux')

if __name__ == "__main__":
    main()