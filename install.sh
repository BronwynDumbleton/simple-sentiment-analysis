#!/bin/bash

echo "Creating virtual environment"
virtualenv --python=/usr/bin/python2.7 venv

. flask/bin/activate

echo "Installing requirements with pip"
pip install -r requirements.txt