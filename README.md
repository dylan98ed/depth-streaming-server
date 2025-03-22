# 📌 Intel RealSense Streaming Server (RGB + Depth)

Este repositorio contiene un servidor basado en Flask que transmite en vivo el video de una cámara **Intel RealSense D435** o similar, mostrando tanto el **streaming RGB** como el **mapa de profundidad** en una interfaz web.

## 🚀 Características
- **Transmite en vivo** el video de la cámara RealSense en tiempo real.
- **Muestra dos streams en paralelo**: RGB y Profundidad.
- **Genera un mapa de profundidad con escala de colores** usando OpenCV.
- **Accesible desde cualquier dispositivo** en la misma red mediante un navegador web.

## 🛠 Tecnologías utilizadas
- **Python 3**
- **Flask** (para el servidor web)
- **OpenCV** (para procesamiento de imágenes)
- **Intel RealSense SDK (pyrealsense2)** (para obtener frames de la cámara)

## 📦 Instalación de dependencias
Antes de ejecutar el script, asegúrate de tener instaladas todas las dependencias necesarias.

### 1️⃣ Instalar los paquetes necesarios
```bash
sudo apt update
sudo apt install python3 python3-pip libgl1 -y
```

### 2️⃣ Instalar las bibliotecas de Python
```bash
pip3 install flask opencv-python numpy pyrealsense2
```

### 3️⃣ Verificar la conexión de la cámara RealSense
Conecta tu cámara Intel RealSense y ejecuta:
```bash
rs-enumerate-devices
```
Si la cámara está bien conectada, debería mostrar información del dispositivo.

## 🚀 Ejecución del servidor
Clona este repositorio y navega al directorio:
```bash
git clone https://github.com/dylan98ed/depth-streaming-server.git
cd depth-streaming-server
```
Luego, ejecuta el servidor:
```bash
python3 realsense_dual_stream.py
```

## 🌐 Acceder al streaming
Desde cualquier dispositivo en la misma red, abre un navegador y accede a:
```
http://<IP_DE_LA_JETSON>:5000
```
Ejemplo:
```
http://192.168.1.100:5000
```
Aquí verás dos streams en paralelo:
- **RGB Stream** (Imagen a color de la cámara)
- **Depth Stream** (Mapa de profundidad en escala de colores)

## 🖥 Ejemplo de interfaz web
La interfaz muestra los dos streams en paralelo:

```
+----------------+  +----------------+
|  RGB Stream   |  | Depth Stream   |
|  (Video)      |  | (Colormap)     |
+----------------+  +----------------+
```

## 📜 Licencia
Este proyecto es de código abierto y puedes usarlo, modificarlo y compartirlo libremente.

---
Si encuentras útil este código, considera darle una estrella ⭐ en GitHub y compartirlo con la comunidad. ¡Gracias! 🚀

