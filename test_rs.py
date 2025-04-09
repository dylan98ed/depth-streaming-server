import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 424, 240, rs.format.bgr8, 15)

try:
    pipeline.start(config)
    print("Esperando frame...")
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    if not color_frame:
        print("No se recibió frame")
    else:
        frame = np.asanyarray(color_frame.get_data())
        print("Frame recibido con tamaño:", frame.shape)
finally:
    pipeline.stop()
