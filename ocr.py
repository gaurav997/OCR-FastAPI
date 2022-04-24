import pytesseract
import asyncio

async def read_image(img_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(img_path, lang=lang)
        # for each image, the API waits for 2 seconds, Instead of this, the API should take a 2 seconds pause for only one time (concurrent processing).
        await asyncio.sleep(2)
        return text
    except:
        return "[Error] Unable to process file: {0}".format(img_path)