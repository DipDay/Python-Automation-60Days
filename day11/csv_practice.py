import csv

with open('e:\\Code\\Python-Automation-60Days\\day11\\jobs.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)

    # next(csv_reader)                                                        # remove the first line (header line)
   
    # for line in csv_reader:
    #     print(line['Job name'])
        # if line[0] != '':
        #     print(line)


    # with open('e:\\Code\\Python-Automation-60Days\\day11\\new_jobs.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file)
    #     # csv_writer = csv.writer(new_file , delimiter='\t')

    #     for line in csv_reader:
    #         if line[0] != '':
    #             csv_writer.writerow(line)

    with open('e:\\Code\\Python-Automation-60Days\\day11\\new_jobs.csv', 'w') as new_file:
        field_names = ['Job name', 'Company name', 'Location']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names)

        csv_writer.writeheader()
        for line in csv_reader:
            del line['More info']
            csv_writer.writerow(line)