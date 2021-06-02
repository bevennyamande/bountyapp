## Facial Recognition Application / Script
- Based on the python facial recognition library, Fastapi for python API design

### Assumption

- You have handled the correct data type posted ie its an images, and also the file extensions
- You have limited the size of your uploads to a certain file limit, this helps not overload the server 
- You have a delay period just to wait for the response from server 


### Tech Stack

- FastAPI (API framework)
- Uvicorn (server)
- Python-multipart (Form data)

## Installation
- clone the repo or move the train.py, app.py and requirements.txt file to your project file directory
- To install the dependencies

```python
pip install -r requirements.txt
```

## Starting the local webserver or API

<img src='images/server_running.png' />

- Navigate to http://127.0.0.1:8000/docs#/ & get the documentation of the API

<img src='images/api_docs.png' />
<img src='images/api_docs2.png' />
<img src='images/api_docs3.png' />
<img src='images/api_docs4.png' />

## Starting the local server in development

```bash
uvicorn main:app --reload
```

## Train Directory Structure
- Contains the images to train the model please note the structure

<img src='images/train_dir.png' />

## Application and Folder Structureu

<img src='images/directory structure.png' />
