import csv

data = []
fieldnames = []
with open('subway.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    reader.fieldnames.append("latitude")
    reader.fieldnames.append("longitude")
    for row in reader:       
        #print row['the_geom']
        startLat = row['the_geom'].find('(') + 1 
        endLat = row['the_geom'].find(' ', startLat)
        row['latitude'] = row['the_geom'][startLat : endLat]
        row['longitude'] = row['the_geom'][endLat : len(row['the_geom']) - 1]
        data.append(row)


        

        #print reader.fieldnames

        mywriter = csv.DictWriter(open("subway_fixed.csv", 'wb'),
                                      fieldnames=reader.fieldnames)
        for row in data:
           # print(row['latitude'])
            mywriter.writerow(row)
#with open('subway_fixed.csv', 'wb') as myfile:
 #   wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
  #  wr.writerows(data)
#writer = csv.writer(open("subway_fixed.csv","w"))
#for row in data:
#      writer.writerow(row["latitude"])
#out = csv.writer(open("subway_fixed.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
#out.writerow(data)



#['URL', 'OBJECTID', 'NAME', 'the_geom', 'LINE', 'NOTES']