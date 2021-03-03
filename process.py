log_file = open("um-server-01.txt") #open and read file


def sales_reports(log_file):  
    for line in log_file: #reading code line by line
        line = line.rstrip()  #removing space from right side
        day = line[0:3]       #just getting first three indexs
        if day == "Wed":      #checking for wed
            print(line)


sales_reports(log_file)

