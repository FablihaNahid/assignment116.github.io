from flask import Flask, redirect, url_for, request, render_template
app=Flask(__name__)

#@app.route('/')
#def mainpage():
#      return render_template("index.html")

@app.route('/about')
def aboutpage():
     return render_template("about.html")

@app.route('/books')
def bookspage():
    return render_template("books.html")



@app.route('/', defaults={'name': " "})
@app.route('/<name>')
def mainpage(name):
    return render_template("index.html", name = name)










#@app.route('/', defaults={'name' : " "})
#@app.route('/<name>')        #landing page e giye run korbe
#def mainpage(name):
 #   return render_template("assi1.html",name=name)



@app.route('/submit',methods=['GET'])
def sub():
    print(request.method)
    if request.method == 'GET':
        sl=request.args['SL']
        sw=request.args['SW']
        print(float(sl)+float(sw))
        return redirect(url_for('mainpage',name=float(sl)+float(sw))) 
        #print(" "+ sl + " " + sw)
        #return redirect(url_for('mainpage', name = " "+ sw+" "+sl))
        
   
    else :
         return redirect(url_for('mainpage'))
         
         
if __name__ == '__main__':
    app.run(debug=True)
