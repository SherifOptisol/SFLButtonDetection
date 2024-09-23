# SFL Button Detection

## Overview
This project repo aims to detect the knob and spring in the shown components based on multiple colours like silver, pink and gold. For this poc purpose, we have used the cv functionalities to detect these colours and to draw contours around them without any deep learning models

![Component without spring](assests/Media(2).jpg)
![Component with spring](assests/Media(5).jpg)

## Requirements

- Create a virtual environment and activate it
    For window , 
    ```
    python -m venv env
    env\Scripts\activate
    ```
- Install the requirements file
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the inference file
2. See the detection video from the opencv window
3. The inferred video will be saved in the [assests](assests)

