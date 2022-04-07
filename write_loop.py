with open("even_loop.py", "w") as loop_file:
    for number in range(0, 31, 2):
        loop_file.write(f"{number}\n")
with open("even_loop.py") as loop_file:
        content = loop_file.read()
