def generate_pattern(n):
    with open("pattern3.txt", "w") as file:
        for i in range(1, n + 1):
            line = "%2E%2E%2F" * i + "\n"
            file.write(line)

n = 30  # Change this to the desired value of n
generate_pattern(n)
