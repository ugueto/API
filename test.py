import unittest
from main import app


# Unit Testing


class TestApi(unittest.TestCase):

    def test_get_all(self):
        """
               Test that API can read all users.
        """
        response = app.test_client().get("/customers/")
        self.assertEqual(response.status_code, 200, "ERROR: Something went wrong with GET request.")

    def test_get(self):
        """
               Test that API can read a specific user.
        """
        response = app.test_client().get("/customers/pmartin@gmail.com")
        self.assertEqual(response.status_code, 200, "ERROR: Something went wrong with GET request.")

    def test_post(self):
        """
               Test that API can create a new user.
        """
        response = app.test_client().post("/customers/lvilla@gmail.com",
                                          json={"name": "Luis",
                                                "surname": "Villa",
                                                "birthdate": "29/10/1996"})
        self.assertEqual(response.status_code, 201, "ERROR: Something went wrong with POST request.")

    def test_put(self):
        """
               Test that API can update an existing user.
        """
        response = app.test_client().put("/customers/pmartin@gmail.com",
                                         json={"name": "Pedro",
                                               "surname": "Martin",
                                               "birthdate": "21/09/1990"})
        self.assertEqual(response.status_code, 200, "ERROR: Something went wrong with PUT request.")

    def test_delete(self):
        """
               Test that API can delete an existing user.
        """
        response = app.test_client().delete("/customers/dsoria@gmail.com")
        self.assertEqual(response.status_code, 204, "ERROR: Something went wrong with DELETE request.")


if __name__ == '__main__':
    unittest.main()
