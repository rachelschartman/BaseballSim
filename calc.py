i = raw_input("P/B ");
if (i == 'b'):
    name = raw_input("Name: ");
    ba = input("BA ");
    ab = input("AB ");
    hr = input("Hr ");
    db = input("Db ");
    trp = input("Trp ");
    so = input("So ");
    bb = input("BB ");
    print("%s: %.3f, %.3f, %.3f, %.3f, %.3f, %.3f" % (name, ba, float(bb) / (ab + bb), float(hr)/ab, float(db)/ab, float(trp)/ab, float(so)/ab));
elif (i == 'p'):
    name = raw_input("Name: ");
    baa = input("BAA ");
    bf = input("BF ");
    bb = input("BB ");
    pt = input("Avg Pitch: ");
    ptstd = input("Pitch Stddev: ");
    print("%s: %.3f, %.3f, %.3f, %.3f" % (name, baa, float(bb)/bf, pt, ptstd));

