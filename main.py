"""Main module"""
from background_changer.background_changer import update_background
from photo_retriever.abstract_photo_retriever import NasaPhotoRetriever
from Image_resizer.image_resizer import add_context


def main():
    """Main func"""
    nasa = NasaPhotoRetriever()
    infos = nasa.retrieve_picture_infos()
    nasa.download_picture(infos)
    # add_context(infos['title'])
    update_background('Linux')

if __name__ == "__main__":
    main()
