from flask import Blueprint, render_template, request, jsonify
from refactoredgpt import generateGPT


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("test.html")

@views.route('/gptapi', methods=['POST'])
def gptapi():

    text_input = request.form['feel']
    poem_type = request.form['type']
    len_poem = request.form['length']

    # Process the input_text (you can call your Python functions here)
    processed_result = generateGPT(text_input, poem_type, len_poem)
    #processed_result = repeat(text_input, poem_type, len_poem)

    data, img = processed_result

    return render_template("base.html", data = data, img=img) #processed_result