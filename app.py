from flask import Flask, request, render_template
import openai
import deepl

openai.api_key = "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"
auth_key = "f0fdeeed-e503-f96d-3ee1-748b1bb68de1:fx"
translator = deepl.Translator(auth_key)

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():                         #TÚL NAGY, DARABOLNI!

    messages = []
    if request.method == 'POST':
        message = request.form['text']
        
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.6,
        max_tokens=150,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
        )

        result = translator.translate_text(text=response.choices[0].text, source_lang="HU", target_lang="EN-US")
        
        messages.append(result.text)
        print(result.text)
        
    return render_template('my-form.html', messages=messages)



if __name__ == "__main__":
    app.run(debug=True)

