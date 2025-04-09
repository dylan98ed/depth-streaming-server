import cv2
import numpy as np
import pyrealsense2 as rs
from flask import Flask, Response

app = Flask(__name__)

# Inicializar la cámara RealSense solo con el stream de profundidad
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

# Escalar el mapa de profundidad para visualización
def depth_to_colormap(depth_frame):
    depth_image = np.asanyarray(depth_frame.get_data())
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
    return depth_colormap

# Generador de frames de profundidad
def generate_depth_frames():
    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            continue
        
        depth_colormap = depth_to_colormap(depth_frame)
        _, buffer = cv2.imencode('.jpg', depth_colormap)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Ruta para el stream de profundidad
@app.route('/video_feed')
def video_feed():
    return Response(generate_depth_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Página HTML mínima para ver el stream
@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>Stream de Profundidad</title>
            <style>
                body { background-color: black; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; }
            </style>
        </head>
        <body>
            <div>
                <h2 style="text-align:center;">Stream de Profundidad</h2>
                <img src="/video_feed" width="640" height="480">
            </div>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
