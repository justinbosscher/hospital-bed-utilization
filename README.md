![Python v3.8.1](https://img.shields.io/badge/python-3.8.1-blue?style=plastic&logo=appveyor.svg)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-notebook-orange?style=plastic)
![License](https://img.shields.io/github/license/justinbosscher/hospital-bed-utilization?style=plastic&logo=appveyor.svg)

![Under Construction](https://ps.w.org/easy-under-construction/assets/banner-772x250.png?rev=2417171)

# Hospital Bed Utilization
## Table of Contents
* [Project Objective](#project-objective)
* [Methods](#methods)
* [Technologies](#technologies)
* [Getting Started](#getting-started)
* [Project Description](#project-description)
* [Training Models Results](#training-models-results)
    * [SOME MODEL](#SOME-MODEL)
    * [SOME MODEL](#SOME-MODEL)
    * [SOME MODEL](#SOME-MODEL)
    * [Model Comparison](#model-comparison)
* [Test Model Results](#test-model-results)
    * [SOME MODEL Test Model](#linear-discriminant-analysis-test-model)
* [License](#license)

## Project Objective
#### Hopefully, this project will predict bed utilization rates using Google Trends data. Currently, I am still looking for relevant hospital data. MySQL and Python will be used on Ubuntu in a Docker Image on a Raspberry Pi.

## Methods
* Data Visualization
* Survival Analysis
* Kaplan-Meier Estimator
* Nelson-Aalen Estimator
* Log-Rank-Test
* Cox-Regression

## Technologies
* Python 3.8.1
* Python Virtual Environment
* Jupyter Notebook
* Python Packages
    * requests
    * pandas
    * numpy
    * KaplanMeierFitter
    * NelsonAalenFitter
    * logrank_test
    * CoxPHFitter
    * matplotlib

## Getting Started
1. If necessary, install the python3-venv package running:
    sudo apt install python3.8-venv
2. Create virtual environment by running:
    python3 -m venv hospitals-wkspc
3. Change directory to workspace folder by running: cd hospitals-wkspc
4. Activate the environment by running:
    source bin/activate
5. Install necessary packages by running: python3 -m pip install -r requirements.txt

## Project Description
## Training Models Results
### SOME MODEL
### SOME MODEL
### SOME MODEL
## Test Model Results
### SOME MODEL

## License
Copyright (c) 2021 Justin Bosscher

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

