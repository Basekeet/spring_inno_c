import sys

s = input()
st = []

for c in s:
    if c in "([{":
        st.append(c)
    elif len(st) == 0:
        print("NO")
        sys.exit(0)
    else:
        if c == ")" and st[-1] != "(" or \
           c == "]" and st[-1] != "[" or \
           c == "}" and st[-1] != "{":
            print("NO")
            sys.exit(0)
        else:
            st.pop(-1)

if len(st) != 0:
    print("NO")
else:
    print("YES")
