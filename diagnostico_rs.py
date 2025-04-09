import pyrealsense2 as rs
import numpy as np
import cv2
import time

def test_stream(pipeline, config, stream_name):
    try:
        pipeline.start(config)
        print(f"✅ [{stream_name}] iniciado correctamente. Esperando frame...")
        frames = pipeline.wait_for_frames()
        frame = None

        if stream_name == "Color":
            frame = frames.get_color_frame()
        elif stream_name == "Depth":
            frame = frames.get_depth_frame()
        elif stream_name == "Infrared":
            frame = frames.get_infrared_frame()
        
        if not frame:
            print(f"❌ [{stream_name}] No se recibió frame.")
        else:
            print(f"✅ [{stream_name}] Frame recibido con tamaño: {np.asanyarray(frame.get_data()).shape}")
    except Exception as e:
        print(f"❌ [{stream_name}] Error al iniciar stream: {e}")
    finally:
        pipeline.stop()
        time.sleep(1)  # pequeña pausa entre pruebas

# --------- DIAGNÓSTICO PRINCIPAL ----------

print("🔎 Verificando conexión con cámara RealSense...")

ctx = rs.context()
devices = ctx.query_devices()

if len(devices) == 0:
    print("🚫 No se detectó ninguna cámara RealSense conectada.")
else:
    print(f"✅ Cámara detectada: {devices[0].get_info(rs.camera_info.name)}")
    print("Iniciando pruebas de streams...\n")

    # Test Color
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    test_stream(pipeline, config, "Color")

    # Test Depth
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    test_stream(pipeline, config, "Depth")

    # Test Infrared
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.infrared, 640, 480, rs.format.y8, 30)
    test_stream(pipeline, config, "Infrared")

print("\n🔧 Diagnóstico finalizado.")
