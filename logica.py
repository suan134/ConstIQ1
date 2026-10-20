"""Lógica de evaluación, clasificación y rutas de aprendizaje."""

from collections import defaultdict


def choose_next_question(questions, answered_ids, current_level, subtopic_scores):
    """Elige una pregunta no respondida priorizando vacíos y cercanía de dificultad."""
    remaining = [q for q in questions if q["id"] not in answered_ids]
    if not remaining:
        return None

    def score(q):
        subtopic = q["subtopic"]
        stats = subtopic_scores.get(subtopic, {"total": 0, "correct": 0})
        mastery = (stats["correct"] / stats["total"]) if stats["total"] else 0.5
        # Priorizar subtemas con menor dominio y preguntas cercanas al nivel actual.
        difficulty_distance = abs(q["difficulty"] - current_level)
        return (mastery, difficulty_distance, q["difficulty"], q["id"])

    return sorted(remaining, key=score)[0]


def classify_level(percent):
    """Umbrales iniciales ilustrativos; deben validarse con el docente."""
    if percent < 50:
        return "Básico"
    if percent < 80:
        return "Intermedio"
    return "Avanzado"


def summarize_results(questions, answers):
    by_subtopic = defaultdict(lambda: {"total": 0, "correct": 0, "question_ids": []})
    total_correct = 0
    for q in questions:
        if q["id"] not in answers:
            continue
        stats = by_subtopic[q["subtopic"]]
        stats["total"] += 1
        stats["question_ids"].append(q["id"])
        is_correct = answers[q["id"]] == q["answer"]
        if is_correct:
            stats["correct"] += 1
            total_correct += 1

    answered = sum(s["total"] for s in by_subtopic.values())
    percent = round(100 * total_correct / answered) if answered else 0
    subtopics = {}
    for name, stats in by_subtopic.items():
        score = round(100 * stats["correct"] / stats["total"]) if stats["total"] else 0
        subtopics[name] = {
            **stats,
            "percent": score,
            "evidence": "Limitada" if stats["total"] < 2 else "Inicial"
        }
    return {
        "answered": answered,
        "correct": total_correct,
        "percent": percent,
        "level": classify_level(percent),
        "subtopics": subtopics
    }


def build_learning_route(summary, profile, subtopic_goals):
    """Genera recomendaciones explicables; no genera contenido formativo."""
    route = []
    for name, goal_info in subtopic_goals.items():
        stats = summary["subtopics"].get(name)
        if stats is None:
            percent = 0
            reason = "Este subtema no se evaluó o no hay respuestas suficientes."
            priority = "Pendiente de diagnóstico"
        else:
            percent = stats["percent"]
            if percent < 50:
                priority = "Alta"
                reason = f"El resultado fue {percent} %; se recomienda empezar por este vacío."
            elif percent < 80:
                priority = "Media"
                reason = f"El resultado fue {percent} %; conviene reforzar antes de avanzar."
            else:
                priority = "Baja"
                reason = f"El resultado fue {percent} %; se observa una fortaleza relativa, sujeta a más evaluación."
        if stats and stats["total"] < 2:
            reason += " La evidencia es limitada porque hay menos de dos preguntas respondidas en este subtema."
        minutes = max(5, min(30, int(profile.get("minutes", 20) / 2)))
        route.append({
            "subtopic": name,
            "priority": priority,
            "mastery": percent,
            "objective": goal_info["goal"],
            "reason": reason,
            "suggested_time_minutes": minutes,
            "source": goal_info["source"],
            "teacher_review": True
        })

    priority_order = {"Alta": 0, "Media": 1, "Pendiente de diagnóstico": 2, "Baja": 3}
    route.sort(key=lambda item: (priority_order[item["priority"]], item["mastery"]))
    return route
