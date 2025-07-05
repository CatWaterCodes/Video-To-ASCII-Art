# Overview:
This project is a user friendly console app, meant for applying an ASCII art effect to videos. It uses PIL, OpenCV and NumPy. It has modifiable settings to allow for more creative use and guarantee the best outcome possible.

# Settings:
## • pixels per character
> [!IMPORTANT] 
> This value always has to be set to a pair integer

This setting represents the length of the side of a square in pixels that will become a singular character in the final result. Lower numbers give a higher "resolution". 
## • background
> [!TIP]
> Values are RGB, and set as a triplet of integers separated by commas

This setting dictates the background color of the result
## • foreground
> [!TIP]
> Values are RGB, and set the same way as they are for the background

This setting changes the foreground color of the result, aka the color of the characters in the ASCII art. 
## • letter size
> [!TIP]
> Takes integer values only as it is a size in pixels

This setting defines the font size of letters in the resulting video, which also means it dictates the resolution of the video.
