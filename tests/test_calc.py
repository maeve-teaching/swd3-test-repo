import pytest
import hypot.calc

def test_square_1():
    # Arrange
    test_val = 1
    expected_output = 1
    # Act
    output = hypot.calc.square(test_val)
    # Assert
    assert output == expected_output

def test_add_1():
    # Arrange
    test_val_1 = 1
    test_val_2 = 2
    expected_output = 3
    # Act
    output = hypot.calc.add(test_val_1, test_val_2)
    # Assert
    assert output == expected_output

def test_square_root():
    # Arrange
    test_val = 3
    expected_output = 1.73205080757
    # Act
    output = hypot.calc.square_root(test_val)
    # Assert
    assert output == pytest.approx(expected_output, rel=1e-6)

def test_pythag():
    # Arrange
    test_val_1 = 2
    test_val_2 = 5
    expected_output = 5.385164807134504
    # Act
    output = hypot.calc.pythag(test_val_1, test_val_2)
    print(output)
    # Assert
    assert output == pytest.approx(expected_output, rel=1e-6)