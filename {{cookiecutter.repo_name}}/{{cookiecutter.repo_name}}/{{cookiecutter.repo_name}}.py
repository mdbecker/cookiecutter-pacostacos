"""{{ cookiecutter.project_short_description }}"""
from flask import Flask, request
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Initilize your estimator here.
class DummyEstimator(object):
    """Dummy estimator that just reverses the input."""
    def predict(self, input_):
        return input_[::-1]
estimator = DummyEstimator()


class {{ cookiecutter.class_name }}(Resource):

    """Example API that accepts PUT & POST requests."""

    def put(self):
        """PUT method that accepts input and returns a prediction.

        Accepting input in urlencoded format.

        Example request/response looks like:
        $ curl http://localhost:5000/ -d "data=testing 123" -X PUT
        {
            "result": "321 gnitset"
        }

        """
        data = request.form['data']
        return {'result': estimator.predict(data)}

    def post(self):
        """POST method that duplicates the PUT method."""
        return self.put()


api.add_resource({{ cookiecutter.class_name }}, '/')

if __name__ == '__main__':
    app.run(debug=True)
