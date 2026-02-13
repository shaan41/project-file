
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route("/")
def index(): 
    return render_template("index.html")

@app.route('/response', methods = ["POST"])
def response():
    data = request.get_json()
    print(f"Response received: {data['answer']}")
    return jsonify({"status": "success", "message": "yay! thanks for answereing "})
    
if __name__ == "__main__":
    app.run(debug=True)