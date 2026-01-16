from celsius_to_fahrenheit import celsius_to_fahrenheit

def test_celsius():
    assert celsius_to_fahrenheit(10) == 50.0
    assert celsius_to_fahrenheit(5) == 41.0
    assert celsius_to_fahrenheit(6) == 42.8
