from assertpy import assert_that

from example_package import hello_world


def test_hello_world():
    # Act
    result = hello_world.main()

    # Assert
    assert_that(result).is_equal_to("Hello, world!")
