import sys 

def generate_pattern(n, pattern, output_name):
    with open(output_name, "w") as file:
        for i in range(1, int(n) + 1):
            line = pattern * i + "\n"
            file.write(line)

inputs = sys.argv
n = inputs[1]
pattern = inputs[2]
output_name = inputs[3]
print(n)
print(pattern)
print(output_name)
generate_pattern(n, pattern, output_name)
