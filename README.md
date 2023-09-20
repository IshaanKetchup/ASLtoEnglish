# ASL to English Alphabet Translator - Review 1

Seeing the lack of ASL to English Translators available online, we decided to start this project.
Using OpenCV to process video, and MediaPipe to track hand gestures (using landmark coordinates), we aim to first, effectively and accurately translate ASL to the English Alphabet.

## Issues 
i. Tracking dynamic hand gestures for alphabets like J and Z is proving to be a little difficult uing MediaPipe and OpenCV
  Our solution - to map the static final position of such dynamically gestured letters

## Goal
While currently still a little buggy and incomplete, the finished project will be be used to help people learn ASL Gestures by practicing on the web.

## Upcoming Features
Once we've finished mapping remaining ASL Gestures and fixing bugs, we intend to beautify the webpages a little more, and make the web framework more elaborate using Flask, JS and CSS.  


Note: Each gesture has been mapped accurately - a little too much so, so minor differences from the actual gesture could result in the gesture not being recognised. However, we assure you the mapping is accurate, so just try a few more times :)

![image](https://github.com/IshaanKetchup/brein/assets/88713875/3a845ee0-0fa8-4131-aa69-f5e38fb6d2fd)

Note: Gesture for 'F' in above image is different from the gesture we have mapped, try rotating your hand so that the circular portion faces the camera :p
