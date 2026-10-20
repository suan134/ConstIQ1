"""
Banco de preguntas de EducaLegal.
Material académico inicial: todas las preguntas y referencias deben ser validadas
por un docente de Derecho antes de utilizarse como material definitivo.
"""

QUESTIONS = [
    {
        "id": "B01", "subtopic": "Concepto y fundamento", "difficulty": 1,
        "question": "¿Cuál es el propósito principal del derecho de petición?",
        "options": [
            "Permitir presentar solicitudes respetuosas y obtener una respuesta conforme a la ley",
            "Garantizar que toda solicitud sea aceptada favorablemente",
            "Reemplazar todos los procesos judiciales",
            "Permitir únicamente solicitudes presentadas por abogados"
        ],
        "answer": 0,
        "explanation": "El derecho de petición permite presentar solicitudes respetuosas y obtener una respuesta oportuna y de fondo, en los términos aplicables. No garantiza que la respuesta sea favorable.",
        "source": "Constitución Política de Colombia, artículo 23; Ley 1755 de 2015.",
        "review": True
    },
    {
        "id": "B02", "subtopic": "Concepto y fundamento", "difficulty": 1,
        "question": "¿Quién puede presentar un derecho de petición, de acuerdo con las reglas generales?",
        "options": [
            "Solamente un abogado con tarjeta profesional",
            "Las personas, sin que sea regla general tener que contratar un abogado",
            "Únicamente los ciudadanos mayores de 30 años",
            "Solo las empresas registradas"
        ],
        "answer": 1,
        "explanation": "Como regla general, no se exige contratar un abogado para presentar una petición. Deben revisarse las reglas especiales que puedan aplicar a situaciones concretas.",
        "source": "Constitución Política de Colombia, artículo 23; Ley 1755 de 2015.",
        "review": True
    },
    {
        "id": "B03", "subtopic": "Concepto y fundamento", "difficulty": 2,
        "question": "Una entidad responde dentro del plazo, pero no aborda lo que la persona pidió. ¿Qué aspecto debe revisarse principalmente?",
        "options": [
            "Si la respuesta fue de fondo y congruente con la solicitud",
            "Si la persona escribió con letra legible",
            "Si la respuesta fue favorable, pues siempre debe serlo",
            "Si la persona tiene un abogado"
        ],
        "answer": 0,
        "explanation": "No basta con emitir cualquier comunicación: debe examinarse si la respuesta aborda de fondo lo solicitado. La respuesta no necesariamente tiene que ser favorable.",
        "source": "Ley 1755 de 2015; jurisprudencia constitucional pertinente por verificar.",
        "review": True
    },
    {
        "id": "B04", "subtopic": "Concepto y fundamento", "difficulty": 3,
        "question": "Una persona quiere formular una petición sobre un asunto regulado por una norma especial. ¿Cuál es la mejor actuación antes de afirmar qué reglas aplican?",
        "options": [
            "Usar siempre el mismo término para cualquier petición",
            "Verificar la norma aplicable, el tipo de solicitud y si existe una regla especial",
            "Asumir que la entidad puede responder cuando quiera",
            "Concluir que solo un juez puede recibir solicitudes"
        ],
        "answer": 1,
        "explanation": "La clasificación de la solicitud y la verificación de las normas aplicables son necesarias antes de determinar términos o requisitos concretos.",
        "source": "Ley 1755 de 2015; normas especiales aplicables, según el caso.",
        "review": True
    },
    {
        "id": "B05", "subtopic": "Presentación y requisitos", "difficulty": 1,
        "question": "¿Cuál de estas opciones describe mejor una petición clara?",
        "options": [
            "Una solicitud que identifica lo que se pide de manera comprensible",
            "Un mensaje que contiene insultos para acelerar la respuesta",
            "Una solicitud que no permite saber qué se necesita",
            "Una petición que siempre debe tener formato notarial"
        ],
        "answer": 0,
        "explanation": "La solicitud debe permitir comprender qué pide la persona. La forma concreta depende de las reglas aplicables al trámite.",
        "source": "Ley 1755 de 2015, artículo 16; revisar reglas aplicables al caso.",
        "review": True
    },
    {
        "id": "B06", "subtopic": "Presentación y requisitos", "difficulty": 2,
        "question": "Una persona no sabe qué dependencia debe recibir su petición. ¿Qué enfoque es más prudente?",
        "options": [
            "No presentar nunca la petición",
            "Consultar los canales oficiales de la entidad y conservar constancia de la radicación",
            "Enviar datos personales a cualquier cuenta encontrada en redes sociales",
            "Asumir que una publicación en redes equivale siempre a una radicación formal"
        ],
        "answer": 1,
        "explanation": "Es prudente utilizar canales oficiales y conservar el número o comprobante de radicación. Los efectos de cada canal deben verificarse según la entidad y el trámite.",
        "source": "Ley 1755 de 2015 y canales oficiales de la entidad destinataria.",
        "review": True
    },
    {
        "id": "B07", "subtopic": "Presentación y requisitos", "difficulty": 3,
        "question": "Una petición llega a una autoridad que considera no competente. ¿Qué debería hacerse antes de orientar al usuario sobre el siguiente paso?",
        "options": [
            "Afirmar que la petición queda automáticamente resuelta",
            "Verificar la regla legal sobre falta de competencia y el procedimiento de traslado o información al peticionario",
            "Indicar que nunca puede presentarse ante otra entidad",
            "Borrar el comprobante de radicación"
        ],
        "answer": 1,
        "explanation": "La falta de competencia tiene reglas legales específicas. Antes de dar instrucciones concretas, se debe verificar la norma vigente y las circunstancias del caso.",
        "source": "Ley 1755 de 2015, disposiciones sobre atención de peticiones; verificar texto vigente.",
        "review": True
    },
    {
        "id": "B08", "subtopic": "Términos de respuesta", "difficulty": 1,
        "question": "¿Es correcto afirmar que todas las peticiones tienen exactamente el mismo término de respuesta?",
        "options": [
            "Sí, todas tienen siempre el mismo término",
            "No; el término puede variar según el tipo de solicitud y las reglas aplicables",
            "Sí, pero solo cuando la persona es estudiante",
            "No, porque nunca existen términos legales"
        ],
        "answer": 1,
        "explanation": "Los términos pueden variar según el tipo de petición. Es importante consultar la disposición vigente que corresponda al caso.",
        "source": "Ley 1755 de 2015, artículo 14; revisar texto vigente y posibles reglas especiales.",
        "review": True
    },
    {
        "id": "B09", "subtopic": "Términos de respuesta", "difficulty": 2,
        "question": "Una persona solicita copias o información. ¿Qué debe hacer el sistema antes de indicarle un plazo exacto?",
        "options": [
            "Aplicar automáticamente el término general sin revisar el tipo de solicitud",
            "Identificar la clase de petición y verificar el artículo legal vigente aplicable",
            "Inventar un plazo aproximado",
            "Decir que la entidad no tiene obligación de responder"
        ],
        "answer": 1,
        "explanation": "El sistema debe identificar el tipo de solicitud y contrastarlo con la norma vigente. No debe inventar ni generalizar términos.",
        "source": "Ley 1755 de 2015, artículo 14; validación docente obligatoria.",
        "review": True
    },
    {
        "id": "B10", "subtopic": "Términos de respuesta", "difficulty": 3,
        "question": "La entidad comunica que necesita más tiempo para responder. ¿Cuál es el primer punto que conviene verificar?",
        "options": [
            "Si la comunicación cumple las condiciones legales aplicables para informar la demora y señalar un plazo razonable",
            "Si la entidad puede aplazar sin explicar nada",
            "Si la persona debe retirar la petición de inmediato",
            "Si cualquier demora elimina el derecho a recibir respuesta"
        ],
        "answer": 0,
        "explanation": "La ampliación o comunicación de demora está sujeta a condiciones legales. Debe revisarse el texto vigente y los hechos antes de orientar al usuario.",
        "source": "Ley 1755 de 2015, artículo 14; revisar texto vigente.",
        "review": True
    },
    {
        "id": "B11", "subtopic": "Protección y seguimiento", "difficulty": 1,
        "question": "¿Por qué es útil conservar una constancia de radicación?",
        "options": [
            "Porque ayuda a demostrar cuándo y por qué canal se presentó la solicitud",
            "Porque garantiza que la respuesta será favorable",
            "Porque reemplaza cualquier documento que la entidad solicite legalmente",
            "Porque hace innecesario revisar la respuesta"
        ],
        "answer": 0,
        "explanation": "La constancia puede servir para hacer seguimiento y documentar la presentación de la petición. No garantiza una respuesta favorable.",
        "source": "Orientación práctica; verificar canales y comprobantes de la entidad.",
        "review": True
    },
    {
        "id": "B12", "subtopic": "Protección y seguimiento", "difficulty": 2,
        "question": "Si una persona considera que su derecho de petición no fue atendido adecuadamente, ¿qué debería hacer la herramienta?",
        "options": [
            "Prometer que ganará una acción judicial",
            "Explicar que existen mecanismos que podrían ser pertinentes y recomendar verificar las circunstancias y la orientación jurídica adecuada",
            "Afirmar que siempre debe demandar inmediatamente",
            "Borrar la solicitud y no conservar soportes"
        ],
        "answer": 1,
        "explanation": "La herramienta educativa puede orientar sobre la necesidad de revisar posibles mecanismos, pero no debe garantizar resultados ni sustituir una valoración jurídica del caso.",
        "source": "Constitución Política, artículo 23; jurisprudencia y normas procesales pertinentes por verificar.",
        "review": True
    }
]

SUBTOPIC_GOALS = {
    "Concepto y fundamento": {
        "goal": "Reconocer la finalidad, el fundamento y el alcance general del derecho de petición.",
        "source": "Constitución Política de Colombia, artículo 23; Ley 1755 de 2015."
    },
    "Presentación y requisitos": {
        "goal": "Identificar los elementos de una solicitud clara y los canales de presentación que deben verificarse.",
        "source": "Ley 1755 de 2015, en especial las disposiciones aplicables a contenido y presentación de peticiones."
    },
    "Términos de respuesta": {
        "goal": "Distinguir que los términos dependen del tipo de petición y verificar el texto normativo vigente antes de indicar plazos.",
        "source": "Ley 1755 de 2015, artículo 14; comprobar posibles normas especiales."
    },
    "Protección y seguimiento": {
        "goal": "Conservar soportes, hacer seguimiento y reconocer cuándo se requiere revisar mecanismos de protección.",
        "source": "Constitución Política, artículo 23; normas y jurisprudencia pertinentes, sujetas a validación docente."
    }
}
