from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

# Initialize the Google Translate Translator
translator = Translator()

@app.route('/')
def home():
    # Return the home page for language selection and input text
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    # Get the source and target languages, and the text to be translated
    source_text = request.form['text']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    
    # Translate the text using the Google Translate API
    translated = translator.translate(source_text, src=source_lang, dest=target_lang)
    
    # Return the translated text back to the webpage
    return render_template('index.html', translated_text=translated.text, 
                           source_lang=source_lang, target_lang=target_lang, source_text=source_text)

if __name__ == '__main__':
    app.run(debug=True)



# pip install googletrans==4.0.0-rc1
# pip install Flask
