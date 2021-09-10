<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Webcam AI Virtual Mouse" />

  &#xa0;

  <!-- <a href="https://webcamaivirtualmouse.netlify.app">Demo</a> -->
</div>

<h1 align="center">Webcam AI Virtual Mouse</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/cynthiachiu/webcam-ai-virtual-mouse?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/cynthiachiu/webcam-ai-virtual-mouse?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/cynthiachiu/webcam-ai-virtual-mouse?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/cynthiachiu/webcam-ai-virtual-mouse?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/cynthiachiu/webcam-ai-virtual-mouse?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/cynthiachiu/webcam-ai-virtual-mouse?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/cynthiachiu/webcam-ai-virtual-mouse?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Webcam Ai Virtual Mouse 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/cynthiachiu" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Takes in live webcam video feed, detects a single hand, recognizes your hand gestures and control the mouse in real-time. To move the mouse, close your hand except for the pointer finger and move. You will see the mouse move across your screen in accordance with your hand motion. To do a mouse click, bring up you middle finger alongside your index, and tap them together. You will see the mouse perform a click on your screen.

![Alt Text](demo.gif)

## :sparkles: Features ##

:heavy_check_mark: Python3;\
:heavy_check_mark: OpenCV;\
:heavy_check_mark: Hand Detection and Gesture Recognition;\
:heavy_check_mark: Real time control of your mouse input;

## :rocket: Technologies ##

The following tools were used in this project:

- [Python3](https://www.python.org/downloads/)
- [cvzone and AI](https://github.com/cvzone/cvzone)
- [OpenCV](https://pypi.org/project/opencv-python/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python3](https://www.python.org/downloads/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/cynthiachiu/webcam-AI-virtual-mouse

# Access
$ cd webcam-AI-virtual-mouse

# Initiate the python virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Install packages
$ pip install -r requirements.txt 

# Run the project
$ python main.py

# A frame will appear with your webcam feed. Hold your hand up and it will recognize you hand gestures and control you mouse in real-time.
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/cynthiachiu" target="_blank">cynthiachiu</a>

&#xa0;

<a href="#top">Back to top</a>
