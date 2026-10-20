import json
from datetime import datetime
import streamlit as st

from preguntas import QUESTIONS, SUBTOPIC_GOALS
from logica import choose_next_question, summarize_results, build_learning_route

st.set_page_config(page_title="EducaLegal", page_icon="⚖️", layout="wide")

st.title("⚖️ EducaLegal")
st.subheader("Diagnóstico jurídico adaptativo")
st.caption("Prototipo académico sobre el derecho de petición en Colombia")

st.warning(
    "Esta herramienta es educativa. No presta asesoría jurídica ni reemplaza la revisión "
    "de un profesional. Las preguntas, normas y rutas deben validarse por un docente antes "
    "de usarse como orientación definitiva."
)

if "started" not in st.session_state:
    st.session_state.started = False
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
if "profile" not in st.session_state:
    st.session_state.profile = {}
if "question_order" not in st.session_state:
    st.session_state.question_order = []

with st.sidebar:
    st.header("Acerca del prototipo")
    st.write("**Tema:** Derecho de petición en Colombia")
    st.write("**Método:** reglas adaptativas explicables")
    st.write("**Fuentes base:** Constitución Política, art. 23; Ley 1755 de 2015.")
    st.caption("Versión inicial: los umbrales y preguntas son configurables y requieren validación docente.")

tab1, tab2, tab3 = st.tabs(["1. Perfil y evaluación", "2. Diagnóstico y ruta", "3. Revisión docente"])

with tab1:
    if not st.session_state.started:
        st.markdown("### Cuéntanos sobre tu objetivo")
        with st.form("profile_form"):
            name = st.text_input("Nombre o alias (opcional)")
            background = st.selectbox(
                "¿Cuál es tu formación?",
                ["Persona sin formación jurídica", "Estudiante de Derecho", "Abogado/a", "Profesional de otra área"]
            )
            objective = st.selectbox(
                "¿Qué quieres lograr?",
                ["Comprender mis derechos", "Aprender a presentar una petición", "Profundizar conocimientos jurídicos", "Preparación académica"]
            )
            minutes = st.slider("¿Cuántos minutos puedes dedicar por sesión?", 5, 60, 20, step=5)
            submitted = st.form_submit_button("Iniciar diagnóstico", type="primary")
        if submitted:
            st.session_state.profile = {
                "name": name.strip() or "Usuario",
                "background": background,
                "objective": objective,
                "minutes": minutes
            }
            st.session_state.started = True
            st.rerun()
    else:
        profile = st.session_state.profile
        st.success(f"Perfil: {profile['background']} · Objetivo: {profile['objective']} · {profile['minutes']} min por sesión")
        answers = st.session_state.answers
        answered_ids = set(answers)
        if len(answered_ids) < len(QUESTIONS):
            summary_so_far = summarize_results(QUESTIONS, answers)
            chosen = choose_next_question(
                QUESTIONS, answered_ids, st.session_state.current_level, summary_so_far["subtopics"]
            )
            if chosen:
                st.progress(len(answered_ids) / len(QUESTIONS), text=f"Pregunta {len(answered_ids)+1} de {len(QUESTIONS)}")
                st.markdown(f"**Subtema:** {chosen['subtopic']}  ·  **Dificultad:** {'Básica' if chosen['difficulty']==1 else 'Intermedia' if chosen['difficulty']==2 else 'Avanzada'}")
                st.markdown(f"### {chosen['question']}")
                choice = st.radio(
                    "Selecciona una respuesta:",
                    options=list(range(len(chosen["options"]))),
                    format_func=lambda i: f"{chr(65+i)}. {chosen['options'][i]}",
                    key=f"choice_{chosen['id']}",
                    index=None
                )
                if st.button("Enviar respuesta", type="primary", disabled=choice is None):
                    st.session_state.answers[chosen["id"]] = choice
                    if choice == chosen["answer"]:
                        st.session_state.current_level = min(3, st.session_state.current_level + 1)
                    else:
                        st.session_state.current_level = max(1, st.session_state.current_level - 1)
                    st.session_state.question_order.append(chosen["id"])
                    st.rerun()
                st.caption("La dificultad de la siguiente pregunta se ajustará según el resultado. La ruta final se basará en los aciertos por subtema.")
        else:
            st.success("¡Evaluación completada!")
            st.info("Abre la pestaña «Diagnóstico y ruta» para consultar tus resultados.")
        if st.button("Reiniciar evaluación"):
            for key in ["started", "answers", "current_level", "profile", "question_order"]:
                st.session_state.pop(key, None)
            st.rerun()

with tab2:
    if not st.session_state.started or not st.session_state.answers:
        st.info("Completa al menos una pregunta en la pestaña «Perfil y evaluación» para ver resultados.")
    else:
        summary = summarize_results(QUESTIONS, st.session_state.answers)
        c1, c2, c3 = st.columns(3)
        c1.metric("Puntaje actual", f"{summary['percent']} %")
        c2.metric("Nivel estimado", summary["level"])
        c3.metric("Preguntas respondidas", f"{summary['answered']} / {len(QUESTIONS)}")

        if summary["answered"] < len(QUESTIONS):
            st.info("Este diagnóstico es provisional hasta completar todas las preguntas.")
        st.markdown("### Resultados por subtema")
        for name, stats in summary["subtopics"].items():
            st.write(f"**{name}:** {stats['percent']} % ({stats['correct']}/{stats['total']})")
            st.progress(stats["percent"] / 100)
        st.markdown("### Ruta de aprendizaje recomendada")
        route = build_learning_route(summary, st.session_state.profile, SUBTOPIC_GOALS)
        for index, item in enumerate(route, start=1):
            with st.expander(f"{index}. {item['subtopic']} — Prioridad {item['priority']}", expanded=(index == 1)):
                st.write(f"**Objetivo:** {item['objective']}")
                st.write(f"**Por qué aparece en tu ruta:** {item['reason']}")
                st.write(f"**Tiempo sugerido:** aproximadamente {item['suggested_time_minutes']} minutos por sesión")
                st.write(f"**Fuente sugerida:** {item['source']}")
                st.warning("Requiere validación docente antes de considerarse una recomendación jurídica definitiva.")
        export_data = {
            "profile": st.session_state.profile,
            "summary": summary,
            "route": route,
            "generated_at": datetime.now().isoformat(timespec="minutes"),
            "notice": "Prototipo educativo sujeto a revisión docente."
        }
        st.download_button(
            "Descargar diagnóstico y ruta (JSON)",
            data=json.dumps(export_data, ensure_ascii=False, indent=2),
            file_name="diagnostico_educalegal.json",
            mime="application/json"
        )

with tab3:
    st.markdown("### Panel de revisión docente")
    st.write("Esta vista ayuda a identificar contenido que necesita validación. La aprobación formal debe realizarla el docente responsable.")
    st.write(f"**Preguntas en el banco:** {len(QUESTIONS)}")
    st.write(f"**Preguntas marcadas para revisión:** {sum(1 for q in QUESTIONS if q.get('review'))}")
    st.write("**Fuentes base declaradas:** Constitución Política de Colombia, artículo 23; Ley 1755 de 2015.")
    st.warning("Verificar texto normativo vigente, términos, excepciones, jurisprudencia y posibles normas especiales antes de usar el banco en una actividad real.")
    for q in QUESTIONS:
        with st.expander(f"{q['id']} · {q['subtopic']} · Nivel {q['difficulty']}"):
            st.write(q["question"])
            st.write(f"**Respuesta prevista:** {q['options'][q['answer']]}")
            st.write(f"**Explicación:** {q['explanation']}")
            st.write(f"**Fuente declarada:** {q['source']}")
            st.checkbox("Marcar como revisada por el docente (solo en esta sesión)", key=f"review_{q['id']}")
    st.caption("En esta versión, las marcas de revisión no se guardan en una base de datos ni constituyen una aprobación jurídica oficial.")
