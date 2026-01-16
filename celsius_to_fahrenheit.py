def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python celsius_to_fahrenheit.py <celsius>")
        sys.exit(1)
    print("Fahrenheit:", celsius_to_fahrenheit(float(sys.argv[1])))