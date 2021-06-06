from src.gretting import sayHello


def test_should_say_hello():
    assert sayHello() == "Hello"
