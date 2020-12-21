from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app=Flask(__name__)




@app.route('/', methods= ['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        hours=request.form['hours']
        message=model.answer(hours)
        return render_template('index.html', message = message)


if __name__=='__main__':
    app.run(port = 5000, debug=True)
