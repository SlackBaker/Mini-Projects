from flask import Flask, request, render_template, redirect, url_for, session
import sympy as sp
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Унікальний ключ для сесій
app.config['SESSION_TYPE'] = 'filesystem'

from flask_session import Session
Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    x, y = sp.symbols("x y")
    answer = ''
    answer_latex = ''
    question = ''
    task_type = ''

    if 'history' not in session:
        session['history'] = []

    history = session['history']

    if request.method == 'POST':
        question = request.form.get('question', '').lower().replace(" ", "")
        if not question:
            answer = "Будь ласка, введіть вираз."
        else:
            try:
                if "=" in question and "and" in question and "y" in question:
                    task_type = "Система рівнянь"
                    equations = question.split("and")
                    eqs = [sp.Eq(sp.sympify(eq.split("=")[0]), sp.sympify(eq.split("=")[1])) for eq in equations]
                    latex_eqs = [sp.latex(eq) for eq in eqs]
                    solution = sp.solve(eqs, (x, y))
                    answer = str(solution)
                    answer_latex = "\\begin{cases} " + " \\\\ ".join(latex_eqs) + " \\end{cases} \\implies " + sp.latex(solution)

                elif "=" in question:
                    task_type = "Рівняння"
                    lhs, rhs = question.split("=")
                    expr = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
                    solution = sp.solve(expr, x)
                    answer = str(solution)
                    answer_latex = sp.latex(expr) + " \\implies " + sp.latex(solution)

                elif "∫" in question or "integrate" in question:
                    task_type = "Інтеграл"
                    expression = question.replace("∫", "").replace("integrate", "")
                    expr = sp.sympify(expression)
                    result = sp.integrate(expr, x)
                    answer = str(result)
                    answer_latex = "\\int " + sp.latex(expr) + " \\, dx = " + sp.latex(result)

                elif "d/dx" in question or "diff" in question:
                    task_type = "Похідна"
                    expression = question.replace("d/dx", "").replace("diff", "")
                    expr = sp.sympify(expression)
                    result = sp.diff(expr, x)
                    answer = str(result)
                    answer_latex = "\\frac{d}{dx}(" + sp.latex(expr) + ") = " + sp.latex(result)

                else:
                    task_type = "Многочлен/Вираз"
                    expr = sp.sympify(question)
                    simplified = sp.simplify(expr)
                    expanded = sp.expand(expr)
                    factored = sp.factor(expr)
                    answer = str((simplified, expanded, factored))
                    answer_latex = (
                            "Спрощено: " + sp.latex(simplified) + " \\\\ " +
                            "Розкладено: " + sp.latex(expanded) + " \\\\ " +
                            "Факторизовано: " + sp.latex(factored)
                    )

                if answer:
                    history.append({
                        "question": question,
                        "task_type": task_type,
                        "response": answer,
                        "response_latex": answer_latex
                    })
                    session['history'] = history

            except Exception as e:
                answer = f"Помилка: {str(e)}"

    return render_template('index.html', answer=answer, answer_latex=answer_latex, history=history, question=question)


@app.route('/clear', methods=['POST'])
def clear_history():
    session['history'] = []
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)