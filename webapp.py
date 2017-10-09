from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
        color = request.args['color']
        #The request object stores information that was sent by the client to the server.
        #the args is a multidict
        #the way we get info from args is that it is visible in a url. - the information in args is visible in the url for hte page being requested(ex. .../response?color=blue)
        if color is 'black':
            response = 'Thats my favorite color too!'
        else:
            response = 'ewww'
        renturn render_template('response.html', response = response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
