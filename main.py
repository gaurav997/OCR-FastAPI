from fastapi import FastAPI, File, UploadFile
from typing import List
import time
import ocr
import utils
import asyncio

# uvicorn ocr:app --reload
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}

# Create api/v1/extract_text route
# REST API that performs OCR on multiple images concurrently
@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    tasks = []
    for img in Images:
        print("Images Uploaded: ", img.filename)
        temp_file = utils._save_file_to_server(img, path="./input_images/", save_as=img.filename)
        # text = await ocr.read_image(temp_file) # This will not work concurrently.
        # instead of running the read_image() function, we created an asynchronous task and appended it to a list.
        tasks.append(asyncio.create_task(ocr.read_image(temp_file)))
    # gather() function to gather all the coroutines and await them until they are completed.
    # Then, we store the result in text. The result will be in the form of a list. Each element in the list will correspond to the response of one coroutine.
    text = await asyncio.gather(*tasks)
    for i in range(len(text)):
        response[Images[i].filename] = text[i]
        # response[img.filename] = text
    response["Time Taken"] = round((time.time() - s),2)
    return response


