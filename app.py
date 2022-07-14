import logging
import os
from flask import Flask, jsonify
from elasticapm.contrib.flask import ElasticAPM

if not os.path.isdir('./logs'):
  os.mkdir('./logs')

logging.basicConfig(
  #filename='./logs/app.log',
  format='%(asctime)s - %(levelname)s - %(message)s',
  level=logging.INFO
  )

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
# Set the required service name. Allowed characters:
# a-z, A-Z, 0-9, -, _, and space
'SERVICE_NAME': 'python-flask-app',

# Use if APM Server requires a secret token
'SECRET_TOKEN': 'HUxkxRDqm1D0sWjdd4',

# Set the custom APM Server URL (default: http://localhost:8200)
'SERVER_URL': 'https://92ed1f715f4440a6b72897f383b6384d.apm.us-central1.gcp.cloud.es.io:443',

# Set the service environment
'ENVIRONMENT': 'development'

}
#apm = ElasticAPM(app, logging=True)
apm = ElasticAPM(app)

@app.route('/')
def home():
  logging.info('Home page request was successful')
  return jsonify({'message': 'Hello World'})

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5001, debug=False)
