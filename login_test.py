
import unittest


def login(username, password):
    if not username or not password:
        return "Username and password are required"
    if username == "student1" and password == "pass123":
        return "Login successful"
    return "Invalid username or password"


class LoginTest(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(
            login("student1", "pass123"),
            "Login successful"
        )

    def test_invalid_password(self):
        self.assertEqual(
            login("student1", "wrong"),
            "Invalid username or password"
        )

    def test_empty_fields(self):
        self.assertEqual(
            login("", ""),
            "Username and password are required"
        )


if __name__ == "__main__":
    unittest.main()
