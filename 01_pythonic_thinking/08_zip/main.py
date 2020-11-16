

if __name__ == '__main__':
    names = ['Cecilla', 'Lise', 'Marie']
    counts = [len(x) for x in names]
    print(counts)
    longest_name = None
    max_count = 0
    # for i in range(0, len(names)):
    #     count = counts[i]
    # for i, name in enumerate(names):
    for name, count in zip(names, counts):
        if count > max_count:
            longest_name = name
            max_count = count
    print(longest_name)
