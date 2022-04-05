from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

# Initialize dict with sample customers
customers = {"pperez@gmail.com": {"name": "Pedro", "surname": "Perez", "birthdate": "07/10/1978"},
             "lsuarez@gmail.com": {"name": "Laura", "surname": "Suarez", "birthdate": "11/03/1996"},
             "agomez@hotmail.com": {"name": "Adrian", "surname": "Gomez", "birthdate": "14/02/1999"},
             "mvelez@yahoo.es": {"name": "Marina", "surname": "Velez", "birthdate": "21/09/1990"},
             "dsoria@gmail.com": {"name": "David", "surname": "Soria", "birthdate": "07/11/1981"},
             "pmartin@gmail.com": {"name": "Pilar", "surname": "Martin", "birthdate": "19/05/1997"},
             "agonzalez@hotmail.com": {"name": "Alejandro", "surname": "Gonzalez", "birthdate": "14/10/1985"},
             "gjimenez@yahoo.es": {"name": "Gabriela", "surname": "Jimenez", "birthdate": "22/12/2001"}
             }


# 404 - Customer does not exist
def abort_no_customer(email):
    if email not in customers:
        abort(404, message='Customer does not exist')


# 409 - Customer already exists
def abort_is_customer(email):
    if email in customers:
        abort(409, message='Customer already exists')


# parsers -> values required for POST method
customer_create_args = reqparse.RequestParser()
customer_create_args.add_argument("name", help="First name of customer", required=True)
customer_create_args.add_argument("surname", help="Surname of customer", required=True)
customer_create_args.add_argument("birthdate", help="Customer birth date", required=True)


# Individual customer class for API endpoint
class Customer(Resource):
    # CRUD = HTTP methods (POST, GET, PUT, DELETE = Create, Read, Update, Delete)

    def get(self, email):  # Method to retrieve a single customer. We will use email as customer_id (unique value).
        abort_no_customer(email)
        return customers[email], 200  # 200 is the default http Flask response if OK, added for clarity

    def post(self, email):
        args = customer_create_args.parse_args(strict=True)
        abort_is_customer(email)
        customers[email] = args
        return customers[email], 201  # Successful created response

    def put(self, email):  # PUT method because PATCH can update only some attributes.
        args = customer_create_args.parse_args(strict=True)
        abort_no_customer(email)
        customers[email] = args
        return customers[email], 200

    def delete(self, email):
        abort_no_customer(email)
        del customers[email]
        return '', 204  # Successful delete response


# Get all customer data from API.
class Customers(Resource):

    def get(self):
        return customers, 200  # Successful HTTP request


# API resource routing: all customers and specific customers.
api.add_resource(Customer, '/customers/<string:email>')  # Must pass email as customer_id
api.add_resource(Customers, '/customers/')


if __name__ == '__main__':
    app.run()  # run Flask app
