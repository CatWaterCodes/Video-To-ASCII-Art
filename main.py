from ascii_converter import image_to_ascii 
import video_tools

repeat1, repeat2 = True, True

settings = {
    "pixels_per_char":8,
    "background":(255,255,255),
    "foreground":(0,0,0),
    "letter_size":20
}

def video_to_ascii(vid: str) -> None:
    global settings
    vid_info = video_tools.get_vid_info(video_path=vid)
    frames = video_tools.video_to_frames(video_path=vid)

    ascii_frames = [image_to_ascii(image=frame, 
                                   pixels_per_char=settings["pixels_per_char"], 
                                   background=settings["background"], 
                                   foreground=settings["foreground"], 
                                   letter_size=settings["letter_size"]) for frame in frames]
    
    video_tools.frames_to_video(frames=ascii_frames, 
                                output_path="result.mp4", 
                                video_info=vid_info)

vid_path = input("Please input the path to the video you want to convert to ascii art \n>>> ")
while repeat1:
    repeat1 = False

    choice1 = input("Would you like to modify any settings? (y/n) \n>>> ")
    if(choice1 not in ["y", "n"]):
        repeat1 = True
        print("Invalid response, please try again.")

    elif(choice1 == "y"):
        print("Here are the current settings:\n")
        for setting in settings:
            print(f'"{setting}"={settings[setting]}')
        print()

        while repeat2:
            repeat2 = False

            choice2 = input("Type the name of the setting you want to modify, or type 'end' to save these settings and move on \n>>> ")

            if(choice2 == "end"):
                print("The video will be made with the settings you've saved.")
            
            elif(choice2 not in settings):
                repeat2 = True
                print("Invalid response, please try again.")

            else:
                repeat2 = True

                if(choice2 == "pixels_per_char"):
                    print("This setting represents the size of a square on the image that will be covered by a single character.")
                    print("!! this value has to be a pair integer !!")
                    new_value = input("What value would you like to set this setting to? \n>>> ")
                    settings[choice2] = int(new_value)
                    print(f'The setting "{choice2}" has been set to {new_value}')
                elif(choice2 == "background"):
                    print("This setting represents the background color of the final result as an RGB value.")
                    print("!! enter the RGB values, separating them with commas (ex: 123, 234, 84) !!")
                    new_value = input("What value would you like to set this setting to? \n>>> ")
                    settings[choice2] = tuple(map(int, new_value.split(',')))
                    print(f'The setting "{choice2}" has been set to {new_value}')
                elif(choice2 == "foreground"):
                    print("This setting represents the foreground color (color of the letters) of the final result as an RGB value.")
                    print("!! enter the RGB values, separating them with commas (ex: 123, 234, 84) !!")
                    new_value = input("What value would you like to set this setting to? \n>>> ")
                    settings[choice2] = tuple(map(int, new_value.split(',')))
                    print(f'The setting "{choice2}" has been set to {new_value}')
                else:
                    print("This setting represents the size in pixels of a letter.")
                    print("!! this value has to be an integer !!")
                    new_value = input("What value would you like to set this setting to? \n>>> ")
                    settings[choice2] = int(new_value)
                    print(f'The setting "{choice2}" has been set to {new_value}')

                print()
    
    else:
        print("The video will be made with the default settings.")

video_to_ascii(vid=vid_path)