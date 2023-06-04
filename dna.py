import csv
import sys
from collections import Counter


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py FILENAME")

    # TODO: Read database file into a variable
    dbase = []
    datafile = sys.argv[1]
    with open(datafile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            dbase.append(row)
    # TODO: Read DNA sequence file into a variable
    sequen = ""
    sequenfile = sys.argv[2]
    with open(sequenfile, "r") as file:
        sequen = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    match_long = {}
    keys = dbase[0].keys()
    for i in keys:
        match_long[i] = str(longest_match(sequen, i))

    # TODO: Check database for matching profiles
    matches = []
    for i in range(len(dbase)):
        for j in keys:
            if j == 'name':
                continue
            elif (match_long.get(j) in dbase[i].get(j)):
                matches.append(dbase[i].get('name'))
            else:
                break
    no_matches = "No match"
    count = Counter(matches)
    for i in count.keys():
        if (count[i]) == len(keys) - 1:
            no_matches = i
            break
    print(no_matches)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
