### BIODS 253 HW2: Turtle house
Group: Betty Xiong, Elana Simon, Joseph Boen, Max Schuessler

### Project description
This repo implements drawing a house with several windows, doors, trees and clouds using python's turtle package.

### Instructions to run

# Create a local copy:
In a first step, clone this repository by using
`git clone https://github.com/ElanaPearl/turtle_house.git` or `git clone git@github.com:ElanaPearl/turtle_house.git`

# Install dependencies: create a conda environment
`conda env create -f env.yml`

`conda activate bds253`

# Test the implementation
To check the drawin/implementation, run `python draw_house.py` which will draw a house and save the output to `house.svg`

# Activate pre-commit checks
Run `pre-commit install --hook-type pre-push` to enable pre-commit checks

Note, this is only relevant if making changes to the git repo. If you run this command, then everytime you push it will run black, flake8, and a check to ensure no CSVs have been uploaded.
