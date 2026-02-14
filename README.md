# 🧮 Calculadora API - Práctica de CI/CD y Calidad Automatizada

![CI Pipeline](https://github.com/Halberch/calculadora-python/actions/workflows/pipeline.yml/badge.svg)

## 📋 Descripción del Proyecto
Este proyecto es una API REST sencilla construida con **Python y Flask**. 
El objetivo principal de este repositorio no es la complejidad de la aplicación en sí, sino **simular el ciclo de vida completo de desarrollo de software** aplicando buenas prácticas DevOps:
* **Integración Continua (CI):** Uso de pipelines automatizados.
* **Desarrollo Guiado por Pruebas (TDD):** Ciclo Fallo-Paso-Refactor.
* **Calidad de Código:** Análisis estático automatizado.

## 🚀 Arquitectura y Estructura
El código se ha diseñado de forma desacoplada para facilitar la ejecución de los distintos cuadrantes de pruebas:

* `logic.py`: Contiene la lógica pura (operaciones matemáticas). Ideal para aislar las pruebas unitarias.
* `app.py`: Contiene el controlador web (API Flask) para las pruebas de integración.
* `tests/`: Directorio con la suite de pruebas automatizadas.
* `.github/workflows/`: Contiene la configuración del pipeline CI/CD en GitHub Actions.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.9+
* **Framework Web:** Flask
* **Testing (Q1/Q2):** Pytest
* **Análisis Estático (Q4):** Flake8
* **CI/CD:** GitHub Actions

## ⚙️ Instalación y Uso Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Halberch/calculadora-python.git](https://github.com/Halberch/calculadora-python.git)
   cd calculadora-python
   ```

2. **Crear y activar el entorno virtual:**
   * En Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * En Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la API:**
   ```bash
   python app.py
   ```
   *La API estará disponible en `http://localhost:5000`*

## 🧪 Estrategia de Pruebas (Cuadrantes Ágiles)

El proyecto cubre los siguientes cuadrantes de pruebas requeridos:

### Q1 (Unitarias) y Q2 (Integración)
Se utiliza `pytest` para verificar tanto la lógica de negocio aislada como los endpoints de la API.
```bash
pytest -v
```

### Q4 (Tecnología / Crítica)
Se utiliza `flake8` como linter para el análisis estático del código, asegurando que cumple con los estándares PEP8 y previniendo errores de sintaxis.
```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## 🔄 Pipeline de Integración Continua (CI)
El archivo `.github/workflows/pipeline.yml` define un flujo automatizado que se dispara con cada `push` o `Pull Request` a la rama `main`. El pipeline consta de:
1. **Build:** Preparación del entorno e instalación de dependencias.
2. **Linting (Q4):** Análisis estático. Falla el build si el código es defectuoso.
3. **Test (Q1 & Q2):** Ejecución de las pruebas unitarias y de integración.

---
**Autores:**
* Alberto García Cruz
* Marta García Valero