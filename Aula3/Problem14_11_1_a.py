def merge(xs, ys):
    """ merge common elements of sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        # If one of the lists is finished, merge is over
        if xi >= len(xs) or yi >= len(ys):
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            result.append(xs[xi])
            xi += 1
            yi += 1


print(merge([1,2,5,7], [1,3,5,6]))

