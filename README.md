# WoodWorking-Estimations
A python package that is meant to optimize the cost and time estimations for woodworking projects. This was a personal project of mine that I worked on off and on for a year. The goal was create quick estimations of how much wood I would need for various projects and to optimize the usage of the bought wood. At some point, this project was used in a school assignment, which added other features like price estimation and time estimation.

Currently it can do the following:
- Indicate if a the desired cuts can fit in the wood you have available.
- Indicate how much board feet you need for a project
- Calculate a wood cost estimate.
- Calculate a time estimate for cutting the wood.

## Quick Start
- Download the repo
- Run the following command: 
  ```python basicUI.py```
- Use option 2 and input the dimensions required.

## Future Development
- Create a printout of where each cut should be for canFit.
- Create board objects from a given .stl file (CAD)
- From the .stl file, find the number of joints need to calculate the gluing/joining cost
- Estimate the amount of coating needed for the project
- Create estimators for sanding and joining and update current estimators to be more robust
- Create a better UI for the package

