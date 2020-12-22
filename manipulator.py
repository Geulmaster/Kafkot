def read_results():
    with open("results.txt") as results_file:
        lines = results_file.readlines()
    for line in lines:
        print(line)

read_results()