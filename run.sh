#!/bin/bash

# folder name for virtual python environment
VENV_FOLDER=".venv"

# check if folder already exists
if [ ! -d "$VENV_FOLDER" ]; then
  echo 'creating virtual environment'

  # create virtual environment
  python -m venv $VENV_FOLDER                   
fi

# activate virtual environment
source $VENV_FOLDER/Scripts/activate

# install all libraries from requirements.txt
if [ -f requirements.txt ]; then
  python -m pip install -r requirements.txt
fi

# flask related variables
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1

# start flask server
flask run