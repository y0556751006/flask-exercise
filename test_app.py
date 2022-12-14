
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
    res = client.get("/users")
    assert res.status_code == 200

    res_users = res.json["result"]["users"]
    assert len(res_users) == 4
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
    res = client.post("/users", data={
        "name": "Ron",
        "age": 21,
        "team": "NNB"
    })
    assert res.status_code == 200


def test_update(client):
    res = client.put("users/1", data={
        "team": "C2TC"
    })
    assert res.status_code == 200

    res_user = res.json["result"]["user"]
    assert res_user[1]["team"] == "C2TC"


def test_delete(client):
    res = client.delete("users/3")
    assert res.status_code == 200
