from niponcred_api.api import app

# Inicia o server da api
if __name__ == "__main__":

    app.run(host='0.0.0.0', debug=True, threaded=True)

