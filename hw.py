import string
import re
import math
import functools
import itertools
import types
import csv
import datetime


#------------------------------------------------------------------------------
def snake2camel(var_name):
    """
    Convert a given var name from snake_style into CamelizedStyle.
    Note: the 1st letter in camel case variable is lowercase.

    Example: 'this_is_var_name'  -> 'thisIsVarName'

    :param var_name: var name to convert
    :return: converted var name
    """
    # var_lst = var_name.split('_')
    # return var_lst[0] + ''.join(term.title() for term in var_lst[1:])

    # result = ''.join(term.title() for term in var_name.split('_'))
    # return result if not result else result[0].lower() + result[1:]

    return ''.join((term, term.title())[idx>0]
                   for idx, term in enumerate(var_name.split('_')))


#------------------------------------------------------------------------------
def is_isogram(value):
    """
    Determine if a word or phrase is an isogram.
    An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

    Examples of isograms:
    lumberjacks
    background
    downstream
    six-year-old
    The word isograms, however, is not an isogram, because the s repeats.

    :param value: value to check
    :return: True if isogram, False otherwise
    """
    new_value = re.sub("[^a-zA-Z]", "", value)
    return len(list(new_value)) == len(set(list(new_value)))


#------------------------------------------------------------------------------
def is_pangram(value):
    """
    Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter")
    is a sentence using every letter of the alphabet at least once. The best known English pangram is:

    The quick brown fox jumps over the lazy dog.
    The alphabet used consists of ASCII letters a to z, inclusive, and is case insensitive. Input will not contain
    non-ASCII symbols.

    :param value: value to check
    :return: True if pangram, False otherwise
    """
    new_value = re.sub("[^a-zA-Z]", "", value)
    return sorted(list(set(new_value.lower()))) == list(string.ascii_lowercase)

#------------------------------------------------------------------------------
def diff_of_squares(num):
    """
    Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

    The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

    The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

    Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares
    of the first ten natural numbers is 3025 - 385 = 2640.

    :param num: denotes first N natural numbers
    :return: difference between the square of the sum and the sum of the squares
    """
    return sum(range(1, num + 1)) ** 2 - sum(n ** 2 for n in range(1, num + 1))


def rle_encode(value):
    """
    Implement run-length encoding and decoding.

    Run-length encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are replaced
    by just one data value and count.

    For example we can represent the original 53 characters with only 13.

    "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"

    RLE allows the original data to be perfectly reconstructed from the compressed data, which makes it a lossless data compression.

    "AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"

    For simplicity, you can assume that the unencoded string will only contain the letters A through Z (either lower or
    upper case) and whitespace. This way data to be encoded will never contain any numbers and numbers inside data
    to be decoded always represent the count for the following character.

    :param value: value to encode
    :return: encoded value
    """

    prev_char = ''
    num_repeats = 0
    result = ''
    for char in value+'0':
        if char != prev_char:
            if prev_char:
                result += prev_char if num_repeats == 1 else str(num_repeats) + prev_char
            prev_char = char
            num_repeats = 1
        else:
            num_repeats += 1

    return result


def rle_decode(value: str):
    """
    See {rle_encode} description

    :param value: value to decode
    :return: decoded value
    """
    result = ''
    curr_num = ''

    for char in value:
        if char.isdigit():
            curr_num += char
        elif curr_num:
            result += char * int(curr_num)
            curr_num = ''
        else:
            result += char

    return result


#------------------------------------------------------------------------------
def flatten_list(lst):
    """
    Take a nested list and return a single flattened list with all values.

    The challenge is to write a function that accepts an arbitrarily-deep nested list-like structure and returns a flattened structure without any nil/null values.

    For Example:
        input: [[1],[],[[[2,3]]],[4,[5,[6]]],7,[[[8]]]]
        output: [1,2,3,4,5,6,7,8]

    :param lst: list to flatten
    :return: flattened list
    """
    # def _flatten_list(lst):
    #     result = []
    #     for elem in lst:
    #         if isinstance(elem, list):
    #             result.extend(_flatten_list(elem))
    #         else:
    #             result.append(elem)
    #     return result
    #
    # return _flatten_list(lst)

    def _flatten_list(lst):
        for elem in lst:
            if isinstance(elem, list):
                yield from _flatten_list(elem)
            else:
                yield elem

    return list(_flatten_list(lst))


def allergies(score):
    """
    Given a person's allergy score, determine whether or not they're allergic to a given item,
    and their full list of allergies.

    An allergy test produces a single numeric score which contains the information about all the allergies the person
    has (that they were tested for).

    The list of items (and their value) that were tested are:

        eggs (1)
        peanuts (2)
        shellfish (4)
        strawberries (8)
        tomatoes (16)
        chocolate (32)
        pollen (64)
        cats (128)

    So if Tom is allergic to peanuts and chocolate, he gets a score of 34.

    Now, given just that score of 34, your program should be able to say:
        - All the allergens Tom is allergic to.

    Note: a given score may include allergens not listed above (i.e. allergens that score 256, 512, 1024, etc.).
    Your program should ignore those components of the score. For example, if the allergy score is 257, your program
    should only report the eggs (1) allergy.

    :param score: allergy score
    :return: tuple of allergens (empty if there are no allergens)
    """
    allergens = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats',
    }

    return tuple(allergens[2**idx]
                for idx, bit in enumerate(bin(score%256)[:1:-1])
                if bit != '0')


#------------------------------------------------------------------------------
def is_valid_credit_card(credit_card):
    """
    Given a value determine whether or not it is valid per the Luhn formula.

    The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers,
    such as credit card numbers.

    The task is to check if a given string is valid.
    Strings of length 1 or less are not valid. Spaces are allowed in the input,
    but they should be stripped before checking. All other non-digit characters are disallowed.

    Example 1: valid credit card number

        4539 1488 0343 6467

        Step 1
        The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling
        4_3_ 1_8_ 0_4_ 6_6_

        Step 2
        If doubling the number results in a number greater than 9 then subtract 9 from the product.
        The results of our doubling:
        8569 2478 0383 3437

        Step 3
        Then sum all of the digits:
        8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80

        Step 4
        If the sum is evenly divisible by 10, then the number is valid. This number is valid!

    Example 2: invalid credit card number

        8273 1232 7352 0569

        Step 1, 2
        Double the second digits, starting from the right
        7253 2262 5312 0539

        Step 3
        Sum the digits
        7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57

        Step 4
        57 is not evenly divisible by 10, so this number is not valid.

    :param score: credit card to check (string)
    :return: True if valid, False otherwise
    """
    if re.findall("[^ 0-9]", credit_card):
        return False

    stripped = [int(char) for char in re.sub(' ', '', credit_card)]

    # double = lambda x: x*2 - 9 if x*2 > 9 else x*2
    double_it = lambda x: (x*2, x*2 - 9)[x*2 > 9]

    doubled = [double_it(digit) for digit in stripped[-2::-2]]

    zipped = zip(stripped[-1::-2], doubled[::-1])

    # result = sum(sum(t) for t in zipped)
    # result = sum(map(lambda t: sum(t), zipped))
    result = functools.reduce(lambda prev, t: prev+sum(t), zipped, 0)

    return result%10 == 0

#------------------------------------------------------------------------------
def prime_factors(num):
    """
    Compute the prime factors of a given natural number.

    A prime number is only evenly divisible by itself and 1.

    Note that 1 is not a prime number.

    Example:
    What are the prime factors of 60?

        Our first divisor is 2. 2 goes into 60, leaving 30.
        2 goes into 30, leaving 15.
        2 doesn't go cleanly into 15. So let's move on to our next divisor, 3.
        3 goes cleanly into 15, leaving 5.
        3 does not go cleanly into 5. The next possible factor is 4.
        4 does not go cleanly into 5. The next possible factor is 5.
        5 does go cleanly into 5.
        We're left only with 1, so now, we're done.

    Our successful divisors in that computation represent the list of prime factors of 60: 2, 2, 3, and 5.

    You can check this yourself:

        2 * 2 * 3 * 5
        = 4 * 15
        = 60
        Success!

    :param num: number to factorize
    :return: list of primes
    """
    # for i in range(2, int(math.sqrt(num)+1)):


    if num == 1:
        result = []

    elif num == 2:
        result = [2]

    else:
        result = []
        factor = 2
        exhuasted = False

        while not exhuasted:
            dividend, remainder = divmod(num, factor)
            if remainder == 0:
                result.append(factor)
                num = dividend
            else:
                factor += 1

            exhuasted = dividend == 1 and remainder == 0

    return result


#------------------------------------------------------------------------------
def etl(filepath_in, filepath_out):
    """
    We are going to do the Transform step of an Extract-Transform-Load.

    Extract-Transform-Load (ETL) is a fancy way of saying, "We have some crufty, legacy data over in this system,
    and now we need it in this shiny new system over here, so we're going to migrate this."

    (Typically, this is followed by, "We're only going to need to run this once.")

    The goal

    We're going to extract some scores from a legacy system.

    The old system stored a list of words per page:

    p. 1: "America", "index", "orange", "utility", "loan", "new", "substring", "transform"
    p. 2: "dog", "zero"
    p. 3: "ball", "substring", "loan", "parameter"
    p. 4: "football", "orange", "vicroty", "war", "loan"
    p. 5: "new"
    p. 8: "orange", "index"
    p.10: "quit", "zero"

    The shiny new system instead stores the pages per word, which makes it much
    faster and easier to find pages for a word.

    "America": 1
    "index": 1, 8
    "orange": 1, 4, 8
    "utility": 1
    "loan": 1, 3, 4
    "new": 1, 5
    "substring": 1, 2
    "transform": 1
    "dog": 2
    "zero": 2, 10
    ...

    Your mission, should you choose to accept it, is to transform the legacy data format file to the shiny new format file.

    :param filepath_in, filepath_out: filepathes to the input/output files
    :return: None
    """
    pass


#------------------------------------------------------------------------------
def age_distribution(filename):
    """
    You are given a csv-file with a list of UA deputies
    Extract information about age distribution in the following format:
        - 1st tuple contains age "buckets" like (20, 30, 40, 50, ...)
        - 2nd tuple contains number of deputies in the corresponding bucket. Ex.: (10, 15, 41, 48, ...)

    Note, that cardinality of tuples should be the same

    :return: return 2 tuples
    """
    with open(filename, "r", encoding="utf8") as f:
        deputies = list(csv.DictReader(f))

    age_ranges = {}
    for deputy in deputies:
        curr_year = datetime.datetime.now().year
        age = curr_year - int(deputy["birthday"][:4])
        age_range = age//10*10
        age_ranges[age_range] = age_ranges.get(age_range, 0) + 1

    ages = sorted(age_ranges.keys())
    return ages, [age_ranges[age] for age in ages]


def my_enumerate(iterable):
    """
    Implement your own enumerate

    :return: return id and value on each call until iterable is exhausted
    """
    idx = 0
    for item in iterable:
        yield idx, item
        idx += 1
    # return zip(itertools.count(), iterable)



def take_while(predicate, iterable):
    """
    Take only those items from iterable that satisfies the given predicate

    :return: return next item from iterable on each call that satisfies the given predicate
    """
    for item in iterable:
        if predicate(item):
            yield item


def drop_while(predicate, iterable):
    """
    Skip those items from iterable that satisfies the given predicate

    :return: return next item from iterable on each call that DEOSN'T satisfy the given predicate
    """
    for item in iterable:
        if not predicate(item):
            yield item


#------------------------------------------------------------------------------
test_suite = {

    snake2camel: (
        (("this_is_var_name",), "thisIsVarName"),
        (("var",), "var"),
        (("x",), "x"),
        (("",), ""),
    ),

    is_isogram: (
        (("lumberjacks",),  True),
        (("background",),   True),
        (("downstream",),   True),
        (("six-year-old",), True),
        (("isograms",), False),
        (("Python",),   True),
        (("xyzXYZz",),  False),
        (("",),         True),
    ),

    is_pangram: (
        ((string.ascii_lowercase,), True),
        (("The quick brown fox jumps over the lazy dog.",), True),
        (("the_quick_brown_fox_jumps_over_the_lazy_dog.",), True),
        (("The quick brown hare jumps over the lazy dog.",), False),
        (("abcd",), False),
        (("",), False),
    ),

    rle_encode: (
        (('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB',), '12WB12W3B24WB'),
        (('abc',), 'abc'),
        (('abcc',), 'ab2c'),
        (('aabbbcccc',), '2a3b4c'),
        (('aa bbb cc  cc ',), '2a 3b 2c2 2c '),
        ((' ',), ' '),
        (('',), ''),
    ),

    rle_decode: (
        (('abc',), 'abc'),
        (('ab2c',), 'abcc'),
        (('12WB12W3B24WB',), 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'),
        (('2a3b4c',), 'aabbbcccc'),
        (('2a 3b 2c2 2c ',), 'aa bbb cc  cc '),
        ((' ',), ' '),
        (('',), ''),
    ),

    diff_of_squares: (
        ((1,), 0),
        ((5,), 170),
        ((42,), 789824),
        ((100,), 25164150),
    ),

    allergies: (
        ((0,), ()),
        ((1,), ('eggs',)),
        ((3,), ('eggs', 'peanuts')),
        ((34,), ('peanuts', 'chocolate')),
        ((42,), ('peanuts', 'strawberries', 'chocolate')),
        ((248,), ('strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats')),
        ((257,), ('eggs',)),
        ((509,), ('eggs', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats')),
    ),

    flatten_list: (
        (([1],), [1]),
        (([],), []),
        (([[1],[],[[[2,3]]],[4,[5,[6]]],7,[[[8]]]],), [1,2,3,4,5,6,7,8]),
        (([1,[2,3,4],[],5],), [1,2,3,4,5]),
    ),

    is_valid_credit_card: (
        (('8273 1232 7352 0569',), False),
        (('055-444-285',), False),
        (('4539 1488 0343 6467',), True),
    ),

    prime_factors: (
        ((1,), []),
        ((2,), [2]),
        ((8,), [2, 2, 2]),
        ((9,), [3, 3]),
        ((12,), [2, 2, 3]),
        ((901255,), [5, 17, 23, 461]),
        ((93819012551,), [11, 9539, 894119]),
    ),

    age_distribution: (
        (('mps_8_4.csv',), ([20, 30, 40, 50, 60, 70, 80], [6, 105, 192, 102, 48, 4, 2])),
    ),

    take_while: (
        ((lambda x: x<5, range(100),), list(range(5))),
    ),

    drop_while: (
        ((lambda x: x%2==0, range(100),), [x for x in range(1, 100, 2)]),
    ),

    my_enumerate: (
        ((range(10, 20),), list(zip(itertools.count(), range(10, 20)))),
    ),

}


#------------------------------------------------------------------------------
def run_tests():
    failed_once = False
    for func, tests in test_suite.items():
        for test in tests:
            args, expected = test
            actual = func(*args)
            if isinstance(actual, types.GeneratorType):
                actual = list(actual)
            try:
                assert expected == actual
            except:
                failed_once = True
                msg_error = "ARGS:\t'%s'\nEXPECT:\t%s\nACTUAL:\t%s" % (args, expected, actual)
                print("FAILED: %s\n%s\n" % (func.__name__, msg_error))

    if not failed_once:
        print("SUCCESS!")


#------------------------------------------------------------------------------
if __name__ == "__main__":
    run_tests()
