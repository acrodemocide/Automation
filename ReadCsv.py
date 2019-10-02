import csv

class CSVServices:
    def getCSVData(self, filePath):
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            csv_data = []
            for row in csv_reader:
                csv_data.append(row)
                line_count += 1
            print(f'Processed {line_count} lines.')
            return csv_data
    
    def reduce(self, filePath, desiredColumnNumbers):
        if (not(isinstance(desiredColumnNumbers, list))):
            raise Exception('desiredColumnNumbers should be an array')
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            reduced_data = []
            for row in csv_reader:
                reduced_row = []
                for x in desiredColumnNumbers:
                    reduced_row.append(row[x])
                reduced_data.append(reduced_row)
                line_count += 1
            print(f'Processed {line_count} lines.')
            return reduced_data
    
    def reduceAndWriteToFile(self, inputFilePath, outputFilePath, desiredColumnNumbers):
        if (not(isinstance(desiredColumnNumbers, list))):
            raise Exception('desiredColumnNumbers should be an array')
        with open(inputFilePath) as csv_input_file:
            with open(outputFilePath, 'w', newline='') as csv_output_file:
                csv_reader = csv.reader(csv_input_file, delimiter=',')
                csv_writer = csv.writer(csv_output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                line_count = 0
                for row in csv_reader:
                    reduced_row = []
                    for x in desiredColumnNumbers:
                        reduced_row.append(row[x])
                    csv_writer.writerow(reduced_row)
                    # csv_writer.write(reduced_row)
                    print(reduced_row)
                    line_count += 1
    
    def transform(self, inputFilePath, outputFilePath, desiredKeys):
        with open(inputFilePath) as csv_input_file:
            with open(outputFilePath, 'w', newline='') as csv_output_file:
                csv_reader = csv.reader(csv_input_file, delimiter=',')
                csv_writer = csv.writer(csv_output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in csv_reader:
                    for x in desiredKeys:
                        transformed_row = row.copy()
                        transformed_row.insert(0, row[x])
                        csv_writer.writerow(transformed_row)
                        print(transformed_row)

                    


filePath = 'C:\\Users\\Acrod\\Downloads\\Utahcontacts - contacts.csv'
outputFilePath = 'C:\\Users\\Acrod\\Downloads\\reducedOutput.csv'
transformedFilePath = 'C:\\Users\\Acrod\\Downloads\\transformedOutput.csv'
csv_services = CSVServices()
# csv_data = csv_services.getCSVData(filePath)

# line_count = 0
# for row in csv_data:
#     if line_count == 0:
#         print(f'Column names are {", ".join(row)}')
#         line_count += 1
#     else:
#         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#         line_count += 1

# csv_reduced_data = csv_services.reduce(filePath, [0, 2, 4, 7, 10, 13])

# line_count = 0
# for row in csv_reduced_data:
#     if line_count == 0:
#         print(f'Column names are {", ".join(row)}')
#         line_count += 1
#     else:
#         print(f'\t{row[0]},{row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}')
#         line_count += 1

csv_services.reduceAndWriteToFile(filePath, outputFilePath, [0, 2, 4, 7, 10, 13])
csv_services.transform(outputFilePath, transformedFilePath, [2, 3, 4, 5])