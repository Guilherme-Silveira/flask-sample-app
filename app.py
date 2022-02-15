from flask import Flask, jsonify
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
# Set the required service name. Allowed characters:
# a-z, A-Z, 0-9, -, _, and space
'SERVICE_NAME': 'python-flask-app',

# Use if APM Server requires a secret token
'SECRET_TOKEN': 'g2pnJXJ3vf2y3Y9t4D5837ZA',

# Set the custom APM Server URL (default: http://localhost:8200)
'SERVER_URL': 'http://apm-server-quickstart-apm-http:8200',

# Set the service environment
'ENVIRONMENT': 'production',
}
apm = ElasticAPM(app)

@app.route('/')
def home():
  return jsonify({'message': 'Hello World'})

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=False)