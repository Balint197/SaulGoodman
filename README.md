# SaulGoodman

HACK3 hackathon 2023

[Video](https://www.youtube.com/watch?v=vIq1h3aQqsI)

We created an application that can respond to legal questions posed in natural language based on real Hungarian law data. 

We adapted a language model to work with custom input text data. This means it will find an answer to your questions in the source provided by you, and also cite where it found it.

### Introduction

Law is a complicated field of study, and it is extremely hard to navigate for the average Joe. It shouldn't be this way, because it applies to everyone, so knowing the exact edge cases shouldn't be tied to years of study. Our solution makes asking legal questions possible for everyone, without the need of keeping an expensive lawyer on retainer.

We used a translating service (deepL), and a pre-made chatbot LLM (ChatGPT) to format hungarian user prompts into a suitable format in english that works well with our model.

We used a pre-trained question answering LLM in which we fed our legal data into. We obtained official hungarian law data from a specific field (employment law). Our model searches over this data and returns excellent answers. It also cites the place it found it, so sources can be checked for the answers validity. We translated the hungarian law into english for the input as it works better with the existing model, and we don't need to train an expensive custom LLM. However you can also try it using the hungarian data, but the accuracy will be a lot worse than in english.

We then rephrase our models answer using chatGPT into a longer sentence and translate it back into hungarian in the webapp.

HUN user prompt → EN DeepL → prompted ChatGPT to distill input text to fit our model → Our model → prompted ChatGPT into full sentence based on original question → HU DeepL → display answer for user

![Architecture](Saul.drawio.png "Architecture")

However, you can just use the notebook file in english, as the accuracy of the model is lowered due to the back-and-forth text transformation and translations. To get the best results, ask questions you took from the `data\legal	\source_en.txt` file. 

### How to use the language model

Go to [Google Colab](https://colab.research.google.com) and upload `SaulGoodman.ipynb`

Follow the instructions in the notebook and run the individual cells. 

****ATTENTION:**** Before starting to run the cells, make sure you enable GPU runtime, as instructed in the notebook. Otherwise answering will be very slow. 

**ATTENTION:** You will have to upload the source text file you wish to search over. You can't just run all cells. This is in step `Indexing Documents with a Pipeline`, other than this you can collapse the menus and just run the cell-groups.

*Based on: [Haystack -  Scalable QA system](https://haystack.deepset.ai/tutorials/03_scalable_qa_system)*

### How to run the webapp

`pip3 install virtualenv`

`pip3 install flask`

`python -m app`

Click on the link in the console to access the app.

*Note: Right now we have not deployed the language model, as its a time and money consuming task. So the webapp isn't connected to the model, but the concept is the same. Our chosen solution (Haystack) provides an easy way for the model to communicate with web-based services using an API.* 

### Scraping

We used `scrape.py` to get our data from the Hungarian law site [njt.hu](njt.hu). This process can easily be automated. We didn't need to do a lot of manual work to make this source into a usable format.
