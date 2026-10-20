# EducaLegal — Diagnóstico jurídico adaptativo

Prototipo académico en Python + Streamlit sobre el derecho de petición en Colombia.

## Funciones incluidas
- Perfil básico del usuario: formación, objetivo y tiempo disponible.
- Banco de 12 preguntas organizadas por subtema y dificultad.
- Selección adaptativa de preguntas según aciertos y vacíos observados.
- Clasificación inicial: básico, intermedio o avanzado.
- Resultados por subtema y ruta con prioridades, objetivos, tiempos y fuentes.
- Justificación de cada recomendación.
- Panel de revisión docente y descarga del diagnóstico en JSON.

## Requisitos
- Python 3.10 o superior recomendado.
- Conexión a internet solo para instalar Streamlit la primera vez.

## Instalación
Abre una terminal dentro de la carpeta `EducaLegal` y ejecuta:

```bash
python -m venv .venv
```

Activa el entorno:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Instala las dependencias y ejecuta:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Streamlit abrirá la aplicación en el navegador. Si no lo hace automáticamente, copia en el navegador la dirección local que aparece en la terminal.

## Cómo demostrarlo
1. Completa el perfil.
2. Responde varias preguntas y muestra que la dificultad puede cambiar.
3. Abre «Diagnóstico y ruta» y explica puntaje, nivel y resultados por subtema.
4. Muestra cómo la ruta prioriza los vacíos detectados y justifica cada recomendación.
5. Abre «Revisión docente» para mostrar preguntas, explicaciones, fuentes y alertas.
6. Descarga el diagnóstico en JSON.

## Decisiones de diseño
- La adaptación se hace mediante reglas explícitas, no mediante IA generativa.
- Los umbrales de clasificación son provisionales y deben validarse con el docente.
- Una sola pregunta por subtema no permite concluir dominio con alta confianza; el sistema señala evidencia limitada.
- La ruta recomienda qué estudiar, pero no genera clases ni sustituye asesoría jurídica.

## Validación jurídica obligatoria
Este proyecto es un prototipo educativo. Antes de utilizarlo como material académico definitivo, un docente debe verificar las preguntas, respuestas, explicaciones, referencias normativas, jurisprudencia, términos legales, excepciones y normas especiales vigentes. Las fuentes de referencia iniciales incluyen la Constitución Política de Colombia, artículo 23, y la Ley 1755 de 2015.
