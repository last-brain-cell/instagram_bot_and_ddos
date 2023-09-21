# import requests
# from fastapi import FastAPI
#
# app = FastAPI()
#
# API_KEY = 'b4155e0dd54c4e45943c42e760a9ecb6'
#
#
# @app.get("/home")
# def home(playlist_id: str):
#     response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', API_KEY)
#     return response.json()
#
#
# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app)