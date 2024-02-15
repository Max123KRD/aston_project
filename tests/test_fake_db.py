from .fake_db import StudentDB
import pytest


@pytest.fixture(scope="module")
def db():
    print("\n------ setup ------")
    db = StudentDB()
    db.connect(r"D:\Projects\DRF\drf\tests\data.json")
    yield db
    print("\n------ teardown ------")
    db.close()


# def teardown_module(module):
#     print("\n------ teardown ------")
#     db.close()


def test_scott_data(db):
    scott_data = db.get_data("Scott")
    assert scott_data["id"] == 1
    assert scott_data["name"] == "Scott"
    assert scott_data["result"] == "pass"


def test_mark_data(db):
    mark_data = db.get_data("Mark")
    assert mark_data["id"] == 2
    assert mark_data["name"] == "Mark"
    assert mark_data["result"] == "fail"
