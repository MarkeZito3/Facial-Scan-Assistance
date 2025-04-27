# Sistema de Asistencia por Reconocimiento Facial 👥

## ¡Actualización 2025! 🎉

Después de 5 años de inactividad, he decidido actualizar este proyecto implementando tecnologías más modernas y eficientes. Esta actualización representa un gran salto tecnológico en la forma en que el sistema detecta y reconoce rostros.

### Cambios Principales 🔄

- **Eliminación de Haarcascade**: Se ha removido el sistema antiguo basado en Haarcascade.
- **Implementación de MediaPipe**: Ahora utilizamos MediaPipe Face Detection, una solución más robusta y precisa para la detección facial.
- **Mejoras en el Reconocimiento**: Implementación de EigenFace Recognizer para un reconocimiento facial más preciso.
- **Interfaz Mejorada**: Nueva interfaz gráfica con barras de progreso y mejor feedback visual.

### Características Actuales ✨

- Registro de nuevos alumnos con captura de múltiples ángulos
- Edición de registros existentes
- Sistema de asistencia en tiempo real
- Exportación de registros en formato Excel y TXT
- Lista de asistencia con checkboxes para mejor visualización
- Ordenamiento alfabético de alumnos

### Requisitos 📋

```
Python 3.10.0
opencv-python==4.11.0.86
mediapipe==0.10.21
pandas==2.2.3
numpy==1.26.4
pillow==11.2.1
matplotlib==3.10.1
```

### Configuración del Entorno 🛠️

1. Instalar Python 3.10.0:
   - Descargar Python 3.10.0 desde el sitio oficial:
     - Windows: [Python 3.10.0 Windows x64](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)
     - Windows x86: [Python 3.10.0 Windows x86](https://www.python.org/ftp/python/3.10.0/python-3.10.0.exe)
     - macOS: [Python 3.10.0 macOS](https://www.python.org/ftp/python/3.10.0/python-3.10.0-macos11.pkg)
     - Linux: Usar el gestor de paquetes de tu distribución o [descargar el código fuente](https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz)
   
   > ⚠️ **Importante**: Durante la instalación en Windows, asegúrate de marcar la casilla "Add Python 3.10 to PATH"

2. Verificar la instalación:
   ```
   python --version
   ```
   Debería mostrar: `Python 3.10.0`

3. Crear un entorno virtual:
   ```
   python -m venv venv
   ```

4. Activar el entorno virtual:
   - En Windows:
     ```
     .\venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```
     source venv/bin/activate
     ```

5. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

### Uso 🚀

1. Activar el entorno virtual (ver paso 3 de Configuración)
2. Ejecutar `main.py` para iniciar la aplicación
3. Usar "Agregar Alumno" para registrar nuevos estudiantes o editar existentes
4. **¡Importante!** Después de registrar todos los alumnos, presionar el botón "Entrenar"
   > ⚠️ **Advertencia**: El proceso de entrenamiento puede tomar varios minutos. Durante este tiempo, la IA está aprendiendo a reconocer cada rostro y asociándolo con el nombre correspondiente. No cerrar la aplicación durante este proceso.
5. Una vez completado el entrenamiento, usar "Tomar Asistencia" para iniciar el reconocimiento en tiempo real
6. Los registros se guardan automáticamente en la carpeta "Presentes"

### Tecnologías Utilizadas 🛠️

- **Python**: Lenguaje principal de desarrollo
- **OpenCV**: Procesamiento de imágenes y reconocimiento facial
- **MediaPipe**: Detección facial moderna y precisa
- **Pandas**: Manejo y exportación de datos
- **NumPy**: Procesamiento numérico
- **Tkinter**: Interfaz gráfica

### Posibles Mejoras Planificadas 🔜

- [ ] Implementación de deep learning para mejor reconocimiento
- [ ] Interfaz web para acceso remoto

### Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si tienes alguna idea o mejora, no dudes en crear un pull request.

---
Actualizado: Abril 2025
