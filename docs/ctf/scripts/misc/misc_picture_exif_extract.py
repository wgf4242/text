# import PIL.Image
# img = PIL.Image.open('mmm.jpg')
# exif_data = img._getexif()
# print(exif_data)

# path to the image or video
from PIL import Image
from PIL.ExifTags import TAGS

# read the image data using PIL
image = Image.open("mmm.jpg")
# extract EXIF data
exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes
    if isinstance(data, bytes):
        data = data.decode('utf16', 'ignore')
    print(f"{tag:25}: {data}")