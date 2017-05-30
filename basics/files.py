import sys

def delete_content(pfile):
    pfile.seek(0)
    pfile.truncate()

def swap_files_content(name_file1, name_file2):
    f = open(name_file1, 'r+')
    d = open(name_file2, 'r+')
    buffer_f = f.read()
    buffer_d = d.read()
    delete_content(f)
    delete_content(d)
    f.write(buffer_d)
    d.write(buffer_f)
    f.close()
    d.close()

swap_files_content('yyy.txt', 'zzz.txt')

######################################################
def read_plus_to_file(filename):
    f = open(filename, "r+")
    buffer = f.read()
    print(buffer)
    f.seek(0, 2) #os.SEEK_END
    f.write("Hello, Python!\n")
    f.close()

def append_to_file(filename):
    f = open(filename, "a+")
    buffer = f.read()
    print(buffer)
    #f.seek(0, 2) #os.SEEK_END
    f.write("Hello, Python!\n")
    f.close()

def write_plus_to_file(filename):
    f = open(filename, "w+")
    buffer = f.read()
    print(buffer)
    f.seek(0, 2) #os.SEEK_END
    f.write("Hello, Python!\n")
    f.close()

def read_line_by_line(filename):
    f = open(filename)
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()
    f.close()
    

    
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
def print_age_distribution(deputies):
    import datetime

    age_ranges = {}
    for deputy in deputies:
        curr_year = datetime.datetime.now().year
        age = curr_year - int(deputy["birthday"][:4])
        age_range = age//10*10
        age_ranges[age_range] = age_ranges.get(age_range, 0) + 1

    total_deputies = sum(age_ranges[x] for x in age_ranges)
    for age_range in sorted(age_ranges):
        print("%s: %d (%.2f%%)\t%s" % (age_range,
                              age_ranges[age_range],
                              age_ranges[age_range]/total_deputies * 100,
                              age_ranges[age_range]//3*"="))


######################################################
def print_parties_distribution(deputies, parties):
    dict_parties = {party["id"]: party["name"] for party in parties}
#     for deputy in deputies:
#         print("%s: %s" % (deputy["fullname"],
#                           dict_parties.get(deputy["party_id"], "<Unknown party>")))
    
    party_num = {}
    for deputy in deputies:
        party_id = deputy["party_id"]
        party_num[party_id] = party_num.get(party_id, 0) + 1

    total_deputies = sum(party_num[x] for x in party_num)

    for party_id in sorted(party_num, reverse=True, key=party_num.get):
        print("%-55s: %d (%.2f%%)" % (dict_parties.get(party_id, "<Unknown party>"),
                                      party_num[party_id],
                                      party_num[party_id]/total_deputies*100))


######################################################
def traverse_dir(dir, indent_level=0):
    import os

    for name in os.listdir(dir):
        if not name.startswith("."):
            path = os.path.join(dir, name)
            prefix = indent_level*(" "*4)
            if os.path.isfile(path):
                print("%s (%d bytes)" % (prefix + "╰─── " + name,
                                         os.path.getsize(path)))
            else:
                print(prefix + name + ":")
                traverse_dir(path, indent_level+1)
                
                
######################################################
print_top_n_words("/home/db/Downloads/22907_clarke-arthur_rama-revealed.txt", 20)
print_top_ngrams("/home/db/Downloads/CrimeAndPunishment.txt")
traverse_dir("/home/db/Downloads/Dropbox")

# taken from http://opendata.rada.gov.ua/?q=dataset/informaciya-pro-narodnyh-deputativ-ukrayiny-8-sklykannya
deputies = get_data_from_csv("/home/db/Downloads/mps_8_4.csv")
parties = get_data_from_csv("/home/db/Downloads/parties_8_0.csv")
print_gender_distribution(deputies)
print_age_distribution(deputies)
print_parties_distribution(deputies, parties)
