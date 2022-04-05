import unittest
import requests

# Unit Testing
# Run Flask API (main.py) and then python test.py to run tests


class TestApi(unittest.TestCase):

    def test_get(self):
        """
               Test that API can read a specific user.
        """
        self.assertEqual(requests.get("http://127.0.0.1:5000/customers/pmartin@gmail.com").json(),
                         {"name": "Pilar",
                          "surname": "Martin",
                          "birthdate": "19/05/1997"},
                         "ERROR: Something went wrong with GET request.")

    def test_post(self):
        """
               Test that API can create a new user.
        """
        self.assertEqual(requests.post("http://127.0.0.1:5000/customers/lvilla@gmail.com",
                                       json={"name": "Luis",
                                             "surname": "Villa",
                                             "birthdate": "29/10/1996"})
                         .status_code,
                         201,
                         "ERROR: Something went wrong with POST request.")

    def test_put(self):
        """
               Test that API can update an existing user.
        """
        self.assertEqual(requests.put("http://127.0.0.1:5000/customers/pmartin@gmail.com",
                                      json={"name": "Pedro",
                                            "surname": "Martin",
                                            "birthdate": "21/09/1990"})
                         .status_code,
                         200,
                         "ERROR: Something went wrong with PUT request.")

    def test_delete(self):
        """
               Test that API can delete an existing user.
        """
        self.assertEqual(requests.delete("http://127.0.0.1:5000/customers/dsoria@gmail.com").status_code,
                         204,
                         "ERROR: Something went wrong with DELETE request.")


if __name__ == '__main__':
    unittest.main()
