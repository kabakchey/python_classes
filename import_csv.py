import sys
import os

# csv
######################################################
def get_data_from_csv(filename):
    import csv

    f = open(filename, "r")

    dict_reader = csv.DictReader(f)
    list_dicts = []

    for row in dict_reader:
        list_dicts.append(row)

    f.close()
    return list_dicts


######################################################
def print_gender_distribution(deputies):
    total_male = 0
    total_female = 0

    for deputy in deputies:
        if deputy["gender"] == "1":
            total_male += 1
        else:
            total_female += 1

    total_deputies = total_female + total_male
    print("Female: %d (%.2f%%), male: %d (%.2f%%)" % (
            total_female, total_female/total_deputies*100,
            total_male, total_male/total_deputies*100 ))


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

    if len(sys.argv) >= 3:
        file_in = sys.argv[1]
        file_out = sys.argv[2]
    else:
        print("Invalid usage: missing files")
        print("Usage: %s <file_in> <file_out>" % os.path.basename(sys.argv[0]))
        sys.exit(-1)

    deputies = get_data_from_csv(file_in)
    save_age_distribution(deputies, file_out)
