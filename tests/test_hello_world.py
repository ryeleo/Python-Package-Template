from example_package import hello_world


def test_hello_world():
    # Arrange

    # Act
    result = hello_world.main()

    # Assert
    assert result == "Hello, world!"
