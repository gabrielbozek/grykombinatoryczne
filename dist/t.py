A = [1, 4, 5, 7, 8, 12]    # in sorted order
Aset = set(A)

for d in range(1, 12):
    already_seen = set()
    for a in A:
        if a not in already_seen:
            b = a
            count = 1
            while b + d in Aset:
                b += d
                count += 1
                already_seen.add(b)
            print "found %d items in %d .. %d" % (count, a, b)
            # collect here the largest 'count'