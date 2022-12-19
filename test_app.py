
# pytest automatically injects fixtures
# that are defined in conftest.py
# in this case, client is injected

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["result"]["content"] == "hello world!"


def test_mirror(client):
    res = client.get("/mirror/Tim")
    assert res.status_code == 200
    assert res.json["result"]["name"] == "Tim"


def test_get_users(client):
    res = client.get("/users/all")
    assert res.status_code == 200

    res_users = res.json["result"]["users"]
    assert len(res_users) == 5
    assert res_users[0]["name"] == "Aria"


def tests_get_users_with_team(client):
    res = client.get("/users?team=LWB")
    assert res.status_code == 200

    res_users = res.json["result"]["users"]
    assert len(res_users) == 2
    assert res_users[1]["name"] == "Tim"


def test_get_user_id(client):
    res = client.get("/users/1")
    assert res.status_code == 200

    res_user = res.json["result"]["user"]
    assert res_user["name"] == "Aria"
    assert res_user["age"] == 19


def test_new_user(client):
    user = {
        "name": "Ron",
        "age": 21,
        "team": "NNB"
    }
    res = client.post("http://localhost:5000/users", json=user)
    assert res.status_code == 201


def test_update(client):
    data = {"team": "C2TC"}
    res = client.put("/users/2", json=data)
    assert res.status_code == 200

    res_user = res.json["result"]["Updated user"]
    assert res_user["team"] == "C2TC"


def test_delete(client):
    res = client.delete("/users/4")
    assert res.status_code == 200
