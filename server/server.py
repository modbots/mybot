from flask import Flask

app = Flask(__name__)

@app.route("/")
async def route():
    return "<h1>Check <a href='https://github.com/arun017s/AutoDelete'>AutoDelete</a></h1>"

if __name__ == "__main__":     
   app.run()
