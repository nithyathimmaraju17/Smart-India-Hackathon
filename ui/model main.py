from flask import Flask,render_template

app=Flask(__name__,template_folder='templates')


@app.route("/")
def home():
	return render_template('index.html')
@app.route("/record")
def record():
    return render_template('record.html')
@app.route("/ownrec")
def record1():
    return render_template('ownrec.html')




if __name__=="__main__":
    app.run(debug=True)
