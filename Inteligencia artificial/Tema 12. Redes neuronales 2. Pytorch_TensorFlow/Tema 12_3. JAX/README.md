# Proyecto: Conociendo JAX

Este proyecto tiene como objetivo explorar y aprender el uso de **JAX**, una biblioteca de Python desarrollada por Google que permite realizar cálculos numéricos eficientes con aceleración mediante GPUs y TPUs. 

A lo largo del cuaderno Jupyter, se abordan conceptos básicos de JAX, como su modelo de programación funcional, diferenciación automática y operaciones en paralelo, además de esto, se tratarán varios puntos con la librería **FLAX**, la cual se centra en las *Redes Neuronales* usando **JAX** como base.

## Configuración del entorno virtual
Para evitar instalar las dependencias de forma global en el sistema, se recomienda utilizar un entorno virtual de Python. Sigue estos pasos:

### 1. Crear un entorno virtual, puede cambiar el nombre `jax_env` al que quiera
```bash
python -m venv jax_env
```

### 2. Activar el entorno virtual
- **Windows**:
  ```bash
  jax_env\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  source jax_env/bin/activate
  ```

### 3. Instalar las dependencias
Una vez activado el entorno virtual, instala o actualiza las dependencias en caso de ser necesario ejecutando:
```bash
pip install -r requirements.txt
```

### 4. Si desea salir use:
```bash
deactivate
```

Luego, abre el cuaderno correspondiente para comenzar a trabajar con JAX.

## Recursos y enlaces de referencia
Durante el desarrollo del proyecto, se han utilizado los siguientes recursos como guía:

- [QuickStart with JAX](https://jax.readthedocs.io/en/latest/quickstart.html)  

- [JAX Characteristics](https://jax.readthedocs.io/en/latest/notebooks/Common_Gotchas_in_JAX.html)  

- [FLAX Basics](https://flax.readthedocs.io/en/latest/nnx_basics.html)  

- [FLAX Mnist Tutorial](https://flax.readthedocs.io/en/latest/mnist_tutorial.html) 

¡Espero que este proyecto sea de utilidad para conocer JAX y sus capacidades! 🚀

