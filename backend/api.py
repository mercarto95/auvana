# from FeatureExtraction.Utils import Processing
# import FeatureExtraction

from fastapi import FastAPI
import uvicorn
from fastapi import FastAPI, Request, Depends, BackgroundTasks, File, UploadFile
from pydantic import BaseModel
from schemas import ProjectRequest
import sqlalchemy
import models
from db import SessionLocal, engine
from sqlalchemy.orm import Session
from models import Project
import os
import sys
from glob import glob
# from pytube import YouTube

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

import sys
sys.path.append('/backend/FeatureExtraction')

# origins = [
#     "http://localhost:8080",
#     "http://localhost",
#     "https://localhost:8080",
# ]

# middleware = [
#     Middleware(CORSMiddleware,
#     allow_origins=origins)
# ]

# app = FastAPI(middleware=middleware)
# CORSMiddleware,
# allow_origins=["*"],

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"]
)

# create database
models.Base.metadata.create_all(bind=engine)


# check if the db is connected
def get_db():
    try:
        db = SessionLocal()
        yield db

    finally:
        db.close()


@ app.post('/api/add_projects')
async def post_project(project_request: ProjectRequest, db: Session = Depends(get_db)):

    project = Project()
    project.ProjectTitle = project_request.ProjectTitle
    # project.videoURL = project_request.videoURL
    # project.projectDirectory = project.ProjectTitle

    # donwload YT video
    # os.chdir("../assets")

    # yt = YouTube(project.videoURL)
    # stream = yt.streams.first()
    # # stream.download(project.projectDirectory)
    # # os.rename(project.projectDirectory, '1.mp4')
    # stream.download()

    # os.chdir("./")

    # project.videoTitle = yt.title
    project.VideoTitle = project_request.VideoTitle

    project.VideoPath = project_request.VideoPath

    db.add(project)
    db.commit()
    return project.ProjectId


@ app.get('/api/all_projects')
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()


@app.get('/api/projects/{project_id}')
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.ProjectId == project_id).first()
    return(project)

# @app.get('/video_processing')
# def video_processing(video):
#     vid = Processing(video)
#     fbs = vid.get_fb()
#     return fbs

    #   function() {
    #     this.projects.projectName = "";
    #     this.projects.videoURL = "";
    #   }.bind(this)



## PROJECTS ###
# def downloadYT(videoURL, outPath):
#     try:
#         # videoURL = "https://www.youtube.com//watch?v=" + videoURL
#         os.mkdir(outPath)
#         os.chdir(outPath)
#         YouTube(videoURL).streams.first().download()
#         os.chdir("./")

#     except:
#         print("There is somethign wrong with PyTube")



