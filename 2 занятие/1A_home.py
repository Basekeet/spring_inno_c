with open("input.txt") as f:
    data = f.read()

f, c = map(float, data.split())
res_c = 5/9*(f - 32)
res_f = 9/5*c + 32

with open("output.txt", "w") as f:
    f.write(str(res_c) + "\n" + str(res_f))