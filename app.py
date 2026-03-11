from flask import Flask, render_template, request
from analyzer import analyze_url

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def home():

    result = None
    score = None
    reasons = []

    if request.method == "POST":

        url = request.form["url"]

        score, reasons = analyze_url(url)

        if score >= 40:
            result = "Website Looks Safe"
        else:
            result = "Potentially Risky Website"

    return render_template(
        "index.html",
        result=result,
        score=score,
        reasons=reasons
    )


if __name__ == "__main__":
    app.run(debug=True)