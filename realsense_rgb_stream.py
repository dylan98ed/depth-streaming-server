import cv2
import numpy as np
import pyrealsense2 as rs
from flask import Flask, Response

app = Flask(__name__)

# Inicializar la cámara RealSense solo con el stream RGB
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

# Generador de frames RGB
def generate_rgb_frames():
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue
        
        frame = np.asanyarray(color_frame.get_data())
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Ruta para el stream RGB
@app.route('/video_feed')
def video_feed():
    return Response(generate_rgb_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Página HTML para ver el stream RGB
@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>Stream RGB - Intel RealSense</title>
            <style>
                body { background-color: black; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; }
            </style>
        </head>
        <body>
            <div>
                <h2 style="text-align:center;">Stream RGB</h2>
                <img src="/video_feed" width="640" height="480">
            </div>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
