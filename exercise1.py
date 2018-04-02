#Problem 1 - lists of name, gender, and hair color
a = ["Jim Halpert", "Male", "Brown"]
b = ["Pam Beesly", "Female", "Blonde"]
c = ["Kevin Malone", "Male", "Brown"]
d = ["Meredith Palmer", "Female", "Red"]
e = ["Michael Scott", "Male", "Brown"]
f = ["Stanley Hudson", "Male", "Brown"]
g = ["Creed Bratton", "Male", "White"]
h = ["Andy Bernard", "Male", "Brown"]
i = ["Jo Bennet", "Female", "White"]
j = ["Kelly Kapoor", "Female", "Brown"]
print a, b, c, d, e, f, g, h, i, j
#Problem 2 - tuples with name and specialty
a = (a[0], "Sales")
b = (b[0], "Sales")
c = (c[0], "Accounting")
d = (d[0], "Customer Service")
e = (e[0], "Manager")
f = (f[0], "Sales")
g = (g[0], "Customer Service")
h = (h[0], "Sales")
i = (i[0], "Corporate")
j = (j[0], "Customer Service")
print a, b, c, d, e, f, g, h, i, j
#Problem 3
week = 0
while week < 1:
    print "Week 1 Tasks:"
    a = [a[0], "Sell Paper"]
    b = [b[0], "Take down calls"]
    c = [c[0], "Find Surplus in Budget"]
    d = [d[0], "Contact Blue Ribbon"]
    e = [e[0], "Talk to Corporate"]
    f = [f[0], "Contact Pretzel Day Providers"]
    g = [g[0], "Customer Service"]
    h = [h[0], "Call Cornell Alumnus Program"]
    i = [i[0], "Find investors"]
    j = [j[0], "Get in touch with India"]
    print a, b, c, d, e, f, g, h, i, j
    week = week + 1
while week < 2:
        print "Week 2 Tasks:"  
        b = [b[0], "Take down calls", "Sell Paper - Jim's Week 1 Task"]
        d = [d[0], "Contact Blue Ribbon"]
        e = [e[0], "Talk to Corporate", "Find Surplus in Budget - Kevin's Week 1 Task"]
        f = [f[0], "Contact Pretzel Day Providers"]
        g = [g[0], "Customer Service"]
        h = [h[0], "Call Cornell Alumnus Program"]
        i = [i[0], "Find investors"]
        j = [j[0], "Get in touch with India"]
        print b, d, e, f, g, h, i, j
        week = week + 1