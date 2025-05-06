from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from icebreaker import ice_break_with

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route(rule="/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with(name=name)
    print("-----------")
    print(profile_pic_url)
    return jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "photoUrl": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
