# Smoky - Detector de Humo de Incendios Forestales

Smoky es un proyecto de detección de humo de incendios forestales mediante el uso de inteligencia artificial. El objetivo principal de este proyecto es ayudar a prevenir incendios forestales mediante la deteccióntemprana del humo. Smoky utiliza el algoritmo Faster-RCNN mediante TensorFlow para detectar y clasificar el humo en las imágenes.

## Características

- Detección precisa de humo de incendios forestales mediante inteligencia artificial.
- Interfaz de usuario fácil de usar para cargar y procesar imágenes.
- Alto rendimiento gracias al uso del algoritmo Faster-RCNN.

## Instalación

Para ejecutar Smoky, se requiere tener instalado TensorFlow 2.0. También se recomienda utilizar una GPU compatible para un mejor rendimiento.

Para instalar Smoky, siga los siguientes pasos:

1. Clone el repositorio en su máquina local.
2. Instale los requisitos utilizando el archivo `requirements.txt`.

```
pip install -r requirements.txt
```

3. Ejecute el archivo `smoky.py`.

```
python 'app.py'.
```

## Uso

Smoky cuenta con una interfaz de usuario fácil de usar para cargar y procesar imágenes. Una vez ejecutado, se montará un servidor web al cual podrá acceder en https://localhost:5050/

Para cargar una imagen, simplemente haga clic en el botón "Cargar Imagen" y seleccione la imagen deseada. Smoky procesará la imagen y mostrará el resultado en la pantalla.

Asimismo, en la pestaña "cámaras", el software extrae de forma automática imágenes desde cámaras web de acceso público, particularmente de aeródromos en Chile, para detectar columnas de humo de incendios forestales en etapa inicial.

## Contribuir

Si desea contribuir al proyecto, ¡estamos abiertos a sus sugerencias y aportes! Siéntase libre de enviar solicitudes de extracción o informar problemas.

## Créditos

- Desarrollador principal: [Daniel Eldan R.]
- Algoritmo utilizado: Faster-RCNN mediante TensorFlow

## Licencia

Smoky está disponible bajo la Licencia MIT. Consulte el archivo `LICENSE` para obtener más información.
