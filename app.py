from flask import Flask, request, render_template
import openai
import deepl

openai.api_key = ""
deepl_key = ""

translator = deepl.Translator(deepl_key)

app = Flask(__name__)

""" @app.route('/')
def index():
    return render_template('index.html') """

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.6,
        max_tokens=150,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )

    result = translator.translate_text(text=response.choices[0].text, source_lang="HU", target_lang="EN-US")
    
    return result.text;


if __name__ == "__main__":
    app.run(debug=True)

