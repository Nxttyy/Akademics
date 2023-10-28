from flask import Flask, render_template
from json_parser import parse_json

app = Flask("__name__")


courses = parse_json()



@app.route('/')
def home():
	return render_template('home.html', title="Akademics", courses=courses, years=["1","2","3","4","5"])



# if __name__ == "__main__":
# 	app = create_app()
# 	app.run(debug=True)