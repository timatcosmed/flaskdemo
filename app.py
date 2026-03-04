from flask import Flask
 
app = Flask(__name__)
@app.route("/")
def main():
    # return "Hello World!"
    return "Hello from the new feature branch! from Branch"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
# Commit時，需要加入 Commit Message，不然會一直等待中