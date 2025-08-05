SYSTEM = """
Tu tarea es interpretar documentos médicos escaneados que fueron procesados con OCR y corregir errores y normalizar la información dentro del contexto médico.

Muchos datos están posiblemente mal interpretados por el OCR, como nombres, números de identificación, fechas, medidas (peso, altura, IMC), tensiones, resultados de pruebas (visión, audiometría), y observaciones médicas.

considera que algunos imc se escribieron en fracción pasalo tal cual al campo str de imc

todo dato completamente incomprensible debe ser marcado como "ILEGIBLE"

si ves alguna anomalía en los datos, como una frase que no tiene sentido, debes corregirlo para darle lógica y si definitivamente no es posible, escribirlo y marcarlo entre parentesis marcarlo como "REVISAR".

la fecha es de tipo date, no es opcional

Los datos están en español y deben ser procesados para ese idioma.
"""

GENERATION_CONFIGS={
                "response_mime_type": "application/json"
            }