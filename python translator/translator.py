from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'templates', 'datatranslate.csv')

translations = {}
try:
    with open(csv_path, 'r', encoding='utf-8') as csvtranslate:
        reader = csv.reader(csvtranslate)
        for row in reader:
            if len(row) >= 2:
                translations[row[0].strip().lower()] = row[1].strip()
except FileNotFoundError:
    print(f"Помилка: Файл {csv_path} не знайдено!")

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        input_text = request.form['word'].strip().lower()
        translated_text = translations.get(input_text, "Переклад не знайдено 😞")

    return render_template('translator.html', translation=translated_text)

if __name__ == "__main__":
    app.run(debug=True)