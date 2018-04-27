def bagdiff(xs, ys):
    """ bagdiff for the first list."""
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished, we're done
            return result

        if yi >= len(ys):  # If ys list is finished
            result.extend(xs[xi:])  # Add the last elements of xs
            return result  # And we're done

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1


print(bagdiff([1, 2, 5, 7], [1, 3, 5, 6]))
print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))
print(bagdiff([7, 8, 11], [5, 7, 11, 11, 11, 12, 13]))