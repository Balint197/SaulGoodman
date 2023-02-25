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
    base_prompt_in  = "Rephrase the following text into maximum 20 words without altering its meaning. Reword it in a way, so that it's easy to give legal advice on it for a lawyer: "
    base_prompt_out0 = "I want you to act as a lawyer giving legal advice. I will provide you with a question to which I want you to answer with the given information. The question is """
    base_prompt_out1 = " "" The information you will answer with as a lawyer is: "

    if request.method == 'POST':

        message = request.form['text']

        # translate to EN
        question_en = translator.translate_text(text=message, source_lang="HU", target_lang="EN-US")

        # reword with chatGPT
        prompt_in = base_prompt_in + question_en
        
        gpt_question = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_in,
        temperature=0.3, # play with temperature... (lower = more predictable, 'normal')
        max_tokens=150,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
        )

        print(gpt_question.choices[0].text)

        # insert this above response into our model (Colab notebook) and paste its response here:
        goodman_advice = "10032000-01425190-00000000" # for question: "What is the Administrative account number of the Ministry of National Resources?"

        # re-word as a lawyer into a complete sentence
        prompt_out = base_prompt_out0 + question_en + base_prompt_out1 + goodman_advice

        gpt_answer = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_out,
        temperature=0.3,
        max_tokens=150,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
        )

        print(gpt_answer.choices[0].text)

        result = translator.translate_text(text=gpt_answer.choices[0].text, source_lang="EN-US", target_lang="HU")
        
        messages.append(result.text)
        print(result.text)
        
    return render_template('my-form.html', messages=messages)



if __name__ == "__main__":
    app.run(debug=True)

