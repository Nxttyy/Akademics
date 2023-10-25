from flask import Flask, render_template

app = Flask("__name__")

years = []


for year in range(1,6):
	years.append(year)
	# print("Year" + str(year) + "\n")
	# print("Sem I")
	# print("Sem II")

@app.route('/')
def home():
	return render_template('home.html', title="Akademics", years=years)



# if __name__ == "__main__":
# 	app = create_app()
# 	app.run(debug=True)