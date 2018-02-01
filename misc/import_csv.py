import sys
import os
import csv


# csv
######################################################
def get_data_from_csv(filename):

    f = open(filename, "r")
    list_dicts = [row for row in csv.DictReader(f)]
    f.close()

    return list_dicts


######################################################
def save_age_distribution(deputies, filename):
    import datetime

    f_out = open(filename, "w")

    age_ranges = {}
    for deputy in deputies:
        curr_year = datetime.datetime.now().year
        age = curr_year - int(deputy["birthday"][:4])
        age_range = age//10*10
        age_ranges[age_range] = age_ranges.get(age_range, 0) + 1

    total_deputies = sum(age_ranges[x] for x in age_ranges)
    for age_range in sorted(age_ranges):
        f_out.write("%s: %d\t(%-6.2f%%)\t%s\n" % (age_range,
                              age_ranges[age_range],
                              age_ranges[age_range]/total_deputies * 100,
                              age_ranges[age_range]//2*"*"))
    f_out.close()


if __name__ == "__main__":

    if len(sys.argv) == 3:
        file_in = sys.argv[1]
        file_out = sys.argv[2]
    else:
        print("Invalid usage")
        print("Usage: %s <file_in> <file_out>" % os.path.basename(sys.argv[0]))
        sys.exit(-1)

    deputies = get_data_from_csv(file_in)
    # print_gender_distribution(deputies)
    save_age_distribution(deputies, file_out)
