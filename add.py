# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 
class Square(Resource): 
	def post(self, num): 
		return jsonify({'square': num**2}) 
api.add_resource(Square, '/square/<int:num>')
if __name__ == '__main__': 
	app.run(debug = True) 

