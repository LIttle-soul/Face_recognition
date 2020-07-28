import sys
# for line in sys.stdin:
#     a, b = (float(x) for x in line.split())
#     print(a+b)
while True:
    line = sys.stdin.readline()
    if not line:
        break
    a, b = (int(x) for x in line.split())
    print(a + b)