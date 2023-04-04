import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        query = request.form["query"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=query.format(query.capitalize()),
            temperature=0.5,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    print("The result is", result)
    return render_template("index.html", result=result)
