from flask import Flask,request,jsonify
app = Flask(__name__)

result={"1":"one","2":"two","3":"three"}

@app.route('/')
def hello():
 print("called")
 return jsonify(result),203

@app.route("/<string:name>", methods=['GET', 'POST'])
def hello_name(name):
 if request.method == 'POST':
  t = str(request.data.get('text', ''))	
  return "save {}".format(name)
 else:
  return "Hello {}!".format(name)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5100,debug=True)
 
 #pip install flask
 #pip install pyopenssl
 #openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
 #app.run(host='0.0.0.0', port=5100,debug=True,ssl_context = ('D:\work\pythonwork\cert.pem', 'D:\work\pythonwork\key.pem'))