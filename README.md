# PRUEBA PRÁCTICA – ANÁLISIS CLÍNICO E INFORMES DE SALUD

## Objetivo

Evaluar la capacidad para transformar datos estructurados y no estructurados en un informe técnico-clínico útil para un cliente corporativo.

## Descripción del Proyecto

Este proyecto resuelve una prueba técnica para la integración y análisis de datos clínicos provenientes de dos fuentes:

1. **Base de Datos Estructurada:**  
   - Archivo `PLANTILLA_500_PACIENTES.xlsx` con información de pacientes.
   - Se genera un informe ejecutivo consolidando:
     - Número total de pacientes evaluados.
     - Distribución por tipo de examen (Ingreso, Periódico, Egreso).
     - Estadísticas por edad, sede, género, cargo, peso y talla.
     - Frecuencia de diagnósticos principales.
     - Distribución del estado de aptitud.
     - Recomendaciones clínicas generales basadas en los hallazgos.

2. **Historias Clínicas Manuscritas:**  
   - Imagen `Historias_Clinicas_Manuales.png` con 5 historias clínicas simuladas a mano.
   - Se procesan mediante IA y OCR, integrando los datos como pacientes adicionales en el informe.

## Proceso de Integración

- Los datos manuscritos se digitalizan usando OCR y se normalizan con IA (Google Gemini).
- Se corrigen errores y se marcan datos ilegibles o dudosos según reglas médicas.
- Los datos estructurados y los digitalizados se consolidan en una base de datos relacional.
- El análisis y visualización se realiza en **Power BI**, generando tablas, gráficos y observaciones cualitativas.

## Entregable Esperado

- Documento PDF con:
  - Introducción.
  - Análisis cuantitativo (tablas y gráficos).
  - Observaciones cualitativas relevantes.
  - Conclusiones.
  - Descripción del proceso de integración digital de los datos manuales.

## Tecnologías Utilizadas

- **Backend:** FastAPI, SQLModel, Pydantic, Google Generative AI.
- **Frontend:** Streamlit (visualización y carga de imágenes).
- **Base de datos:** PostgreSQL (configurable vía Render).
- **Visualización:** Power BI.
- **OCR & IA:** Procesamiento de imágenes médicas manuscritas.

## Estructura del Proyecto

```
src/
  main.py                # API backend para procesamiento y almacenamiento
  front/app.py           # Interfaz Streamlit para carga y visualización
  utilies/ia/            # Módulos de IA, OCR y modelos de datos
render.yaml              # Configuración de despliegue en Render
requirements.txt         # Dependencias del proyecto
pyproject.toml           # Metadata y dependencias
```

## Ejecución

1. Instalar dependencias:  
   `pip install -r requirements.txt`
2. Configurar variables de entorno (DATABASE_URL, etc.).
3. Ejecutar backend:  
   `uvicorn src.main:app --host 0.0.0.0 --port 10000`
4. Ejecutar frontend:  
   `streamlit run src/front/app.py`
5. Visualizar y analizar datos en Power BI.

## Observaciones

- El procesamiento de imágenes manuscritas se realiza con IA, siguiendo reglas estrictas de validación y corrección.
- El sistema es robusto ante errores de OCR y permite marcar datos como "ILEGIBLE" o "REVISAR" según corresponda.
- La integración de datos manuales y estructurados es transparente para el usuario final.
- Se utiliza IA en vez de un OCR, porque como las imagenes a su vez son generadas por ia, un OCR no es óptimo.