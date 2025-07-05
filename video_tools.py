import cv2
import numpy
from PIL import Image

def get_vid_info(video_path: str) -> dict:
    vid_cap = cv2.VideoCapture(video_path)
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    frame_count = vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)
    width = vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    duration = frame_count / fps if fps > 0 else 0

    #I only need like two of these but since chatgpt was kind enough to give me more when i asked for video info I'll leave them in ig
    #I made 95% of this alone, don't think this is AI due to one comment
    return {
        "fps": fps,
        "frame_count": frame_count,
        "width": width,
        "height": height,
        "duration": duration
        }

def video_to_frames(video_path: str) -> list:
    vid_cap = cv2.VideoCapture(video_path)

    frames = []
    while True:
        success, frame = vid_cap.read()
        if not success:
            break  # No more frames

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_image = Image.fromarray(frame_rgb)
        frames.append(frame_image)

    vid_cap.release()
    return frames

def frames_to_video(frames: list, output_path: str, video_info: dict, video_writer="mp4v") -> None:
    first_frame = numpy.array(frames[0].convert("RGB"))
    height, width, _ = first_frame.shape 

    # Define the video writer (use 'mp4v' or 'XVID' for .avi)
    fourcc = cv2.VideoWriter_fourcc(*video_writer)
    out = cv2.VideoWriter(output_path, fourcc, video_info["fps"], (width, height))

    # Write each frame
    for img in frames:
        frame = numpy.array(img.convert("RGB"))  # Ensure it's RGB
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to BGR
        out.write(frame_bgr)

    # Release the writer
    out.release()