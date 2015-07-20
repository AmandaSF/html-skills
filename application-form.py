from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/application', methods=["post"])
def submit_application():
	application_args = request.args.post()
	return render_template("response.html")
















if __name__ == '__main__':
	app.run(debug=True)