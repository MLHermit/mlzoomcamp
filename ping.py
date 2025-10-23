from flask import Flask
app = Flask('first_service')

@app.route('/first_service', methods = ['GET'])
def ding():
    return "Dong"
if __name__ == '__main__':
    app.run(debug= True, host= '0.0.0.0', port= 9696)