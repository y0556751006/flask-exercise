import json
import unittest

import requests
url = "http://localhost:5000"

class MyTestCase(unittest.TestCase):
    def test_index(self):
        res = requests.get(url+"/")
        assert res.status_code == 200
        assert res.json()["result"]["content"] == "hello world!"

    def test_mirror(self):
        res = requests.get(url+"/mirror/Tim")
        assert res.status_code == 200
        assert res.json()["result"]["name"] == "Tim"

    def test_get(self):
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)
        # assert res.status_code==200

    # def test_get_users(self):
    #     res = requests.get(url+"/users")
    #     assert res.status_code == 200
    #
    #     res_users = res.json["result"]["user"]
    #     assert len(res_users) == 4
    #     assert res_users[0]["name"] == "Aria"


    def tests_get_users_with_team(self):
        res = requests.get(url+"/users?team=C2TC")
        assert res.status_code == 200

        res_users = res.json()["result"]["user"]
        assert len(res_users) == 1


    def test_get_user_id(self):
        res = requests.get(url+"/users/1")
        assert res.status_code == 200

        res_user = res.json()["result"]["user"]
        assert res_user["name"] == "Aria"
        assert res_user["age"] == 19


    def test_new_user(self):
        user = {
            "name": "Ron",
            "age": 21,
            "team": "NNB"
               }
        res = requests.post(url+"/users", json=user)
        assert res.status_code == 201

        res_user = res.json()["result"]["user"]


    def test_update(self):
        data = {"team": "C2TC"}
        res = requests.put(url+"/users/2", json=data)
        assert res.status_code == 200

        res_user = res.json()["result"]["user"]
        assert res_user["team"] == "C2TC"


    def test_delete(self):
        res = requests.delete(url+"/users/4")
        assert res.status_code == 200


if __name__ == '__main__':
    unittest.main()