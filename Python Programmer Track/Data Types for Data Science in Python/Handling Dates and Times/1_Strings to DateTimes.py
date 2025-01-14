# Import the datetime object from datetime
from datetime import datetime

dates_list = ['02/19/2001',
 '04/10/2001',
 '05/30/2001',
 '07/19/2001',
 '09/07/2001',
 '10/27/2001',
 '12/16/2001',
 '02/04/2002',
 '03/26/2002',
 '05/15/2002',
 '07/04/2002',
 '08/23/2002',
 '10/12/2002',
 '12/01/2002',
 '01/20/2003',
 '03/11/2003',
 '04/30/2003',
 '06/19/2003',
 '08/08/2003',
 '09/27/2003',
 '11/16/2003',
 '01/05/2004',
 '02/24/2004',
 '04/14/2004',
 '06/03/2004',
 '07/23/2004',
 '09/11/2004',
 '10/31/2004',
 '12/20/2004',
 '02/08/2005',
 '03/30/2005',
 '05/19/2005',
 '07/08/2005',
 '08/27/2005',
 '10/16/2005',
 '12/05/2005',
 '01/24/2006',
 '03/15/2006',
 '05/04/2006',
 '06/23/2006',
 '08/12/2006',
 '10/01/2006',
 '11/20/2006',
 '01/09/2007',
 '02/28/2007',
 '04/19/2007',
 '06/08/2007',
 '07/28/2007',
 '09/16/2007',
 '11/05/2007',
 '12/25/2007',
 '02/13/2008',
 '04/03/2008',
 '05/23/2008',
 '07/12/2008',
 '08/31/2008',
 '10/20/2008',
 '12/09/2008',
 '01/28/2009',
 '03/19/2009',
 '05/08/2009',
 '06/27/2009',
 '08/16/2009',
 '10/05/2009',
 '11/24/2009',
 '01/13/2010',
 '03/04/2010',
 '04/23/2010',
 '06/12/2010',
 '08/01/2010',
 '09/20/2010',
 '11/09/2010',
 '12/29/2010',
 '02/17/2011',
 '04/08/2011',
 '05/28/2011',
 '07/17/2011',
 '09/05/2011',
 '10/24/2011',
 '11/12/2011',
 '01/01/2012',
 '02/20/2012',
 '04/10/2012',
 '05/30/2012',
 '07/19/2012',
 '09/07/2012',
 '10/27/2012',
 '12/16/2012',
 '02/04/2013',
 '03/26/2013',
 '05/15/2013',
 '07/04/2013',
 '08/23/2013',
 '10/12/2013',
 '12/01/2013',
 '01/20/2014',
 '03/11/2014',
 '04/30/2014',
 '06/19/2014',
 '08/08/2014',
 '09/27/2014',
 '11/16/2014',
 '07/05/2014',
 '01/24/2015',
 '03/15/2015',
 '05/04/2015',
 '06/23/2015',
 '08/12/2015',
 '10/01/2015',
 '11/20/2015',
 '01/09/2016',
 '02/28/2016',
 '04/18/2016',
 '06/07/2016',
 '07/27/2016',
 '09/15/2016',
 '11/04/2016']
# Iterate over the dates_list
for date_str in dates_list:
    # Convert each date to a datetime object: date_dt
    date_dt = datetime.strptime(date_str, '%m/%d/%Y')

    # Print each date_dt
    print(date_dt)

datetimes_list = [datetime.datetime(2001, 2, 19, 0, 0),
 datetime.datetime(2001, 4, 10, 0, 0),
 datetime.datetime(2001, 5, 30, 0, 0),
 datetime.datetime(2001, 7, 19, 0, 0),
 datetime.datetime(2001, 9, 7, 0, 0),
 datetime.datetime(2001, 10, 27, 0, 0),
 datetime.datetime(2001, 12, 16, 0, 0),
 datetime.datetime(2002, 2, 4, 0, 0),
 datetime.datetime(2002, 3, 26, 0, 0),
 datetime.datetime(2002, 5, 15, 0, 0),
 datetime.datetime(2002, 7, 4, 0, 0),
 datetime.datetime(2002, 8, 23, 0, 0),
 datetime.datetime(2002, 10, 12, 0, 0),
 datetime.datetime(2002, 12, 1, 0, 0),
 datetime.datetime(2003, 1, 20, 0, 0),
 datetime.datetime(2003, 3, 11, 0, 0),
 datetime.datetime(2003, 4, 30, 0, 0),
 datetime.datetime(2003, 6, 19, 0, 0),
 datetime.datetime(2003, 8, 8, 0, 0),
 datetime.datetime(2003, 9, 27, 0, 0),
 datetime.datetime(2003, 11, 16, 0, 0),
 datetime.datetime(2004, 1, 5, 0, 0),
 datetime.datetime(2004, 2, 24, 0, 0),
 datetime.datetime(2004, 4, 14, 0, 0),
 datetime.datetime(2004, 6, 3, 0, 0),
 datetime.datetime(2004, 7, 23, 0, 0),
 datetime.datetime(2004, 9, 11, 0, 0),
 datetime.datetime(2004, 10, 31, 0, 0),
 datetime.datetime(2004, 12, 20, 0, 0),
 datetime.datetime(2005, 2, 8, 0, 0),
 datetime.datetime(2005, 3, 30, 0, 0),
 datetime.datetime(2005, 5, 19, 0, 0),
 datetime.datetime(2005, 7, 8, 0, 0),
 datetime.datetime(2005, 8, 27, 0, 0),
 datetime.datetime(2005, 10, 16, 0, 0),
 datetime.datetime(2005, 12, 5, 0, 0),
 datetime.datetime(2006, 1, 24, 0, 0),
 datetime.datetime(2006, 3, 15, 0, 0),
 datetime.datetime(2006, 5, 4, 0, 0),
 datetime.datetime(2006, 6, 23, 0, 0),
 datetime.datetime(2006, 8, 12, 0, 0),
 datetime.datetime(2006, 10, 1, 0, 0),
 datetime.datetime(2006, 11, 20, 0, 0),
 datetime.datetime(2007, 1, 9, 0, 0),
 datetime.datetime(2007, 2, 28, 0, 0),
 datetime.datetime(2007, 4, 19, 0, 0),
 datetime.datetime(2007, 6, 8, 0, 0),
 datetime.datetime(2007, 7, 28, 0, 0),
 datetime.datetime(2007, 9, 16, 0, 0),
 datetime.datetime(2007, 11, 5, 0, 0),
 datetime.datetime(2007, 12, 25, 0, 0),
 datetime.datetime(2008, 2, 13, 0, 0),
 datetime.datetime(2008, 4, 3, 0, 0),
 datetime.datetime(2008, 5, 23, 0, 0),
 datetime.datetime(2008, 7, 12, 0, 0),
 datetime.datetime(2008, 8, 31, 0, 0),
 datetime.datetime(2008, 10, 20, 0, 0),
 datetime.datetime(2008, 12, 9, 0, 0),
 datetime.datetime(2009, 1, 28, 0, 0),
 datetime.datetime(2009, 3, 19, 0, 0),
 datetime.datetime(2009, 5, 8, 0, 0),
 datetime.datetime(2009, 6, 27, 0, 0),
 datetime.datetime(2009, 8, 16, 0, 0),
 datetime.datetime(2009, 10, 5, 0, 0),
 datetime.datetime(2009, 11, 24, 0, 0),
 datetime.datetime(2010, 1, 13, 0, 0),
 datetime.datetime(2010, 3, 4, 0, 0),
 datetime.datetime(2010, 4, 23, 0, 0),
 datetime.datetime(2010, 6, 12, 0, 0),
 datetime.datetime(2010, 8, 1, 0, 0),
 datetime.datetime(2010, 9, 20, 0, 0),
 datetime.datetime(2010, 11, 9, 0, 0),
 datetime.datetime(2010, 12, 29, 0, 0),
 datetime.datetime(2011, 2, 17, 0, 0),
 datetime.datetime(2011, 4, 8, 0, 0),
 datetime.datetime(2011, 5, 28, 0, 0),
 datetime.datetime(2011, 7, 17, 0, 0),
 datetime.datetime(2011, 9, 5, 0, 0),
 datetime.datetime(2011, 10, 24, 0, 0),
 datetime.datetime(2011, 11, 12, 0, 0),
 datetime.datetime(2012, 1, 1, 0, 0),
 datetime.datetime(2012, 2, 20, 0, 0),
 datetime.datetime(2012, 4, 10, 0, 0),
 datetime.datetime(2012, 5, 30, 0, 0),
 datetime.datetime(2012, 7, 19, 0, 0),
 datetime.datetime(2012, 9, 7, 0, 0),
 datetime.datetime(2012, 10, 27, 0, 0),
 datetime.datetime(2012, 12, 16, 0, 0),
 datetime.datetime(2013, 2, 4, 0, 0),
 datetime.datetime(2013, 3, 26, 0, 0),
 datetime.datetime(2013, 5, 15, 0, 0),
 datetime.datetime(2013, 7, 4, 0, 0),
 datetime.datetime(2013, 8, 23, 0, 0),
 datetime.datetime(2013, 10, 12, 0, 0),
 datetime.datetime(2013, 12, 1, 0, 0),
 datetime.datetime(2014, 1, 20, 0, 0),
 datetime.datetime(2014, 3, 11, 0, 0),
 datetime.datetime(2014, 4, 30, 0, 0),
 datetime.datetime(2014, 6, 19, 0, 0),
 datetime.datetime(2014, 8, 8, 0, 0),
 datetime.datetime(2014, 9, 27, 0, 0),
 datetime.datetime(2014, 11, 16, 0, 0),
 datetime.datetime(2014, 7, 5, 0, 0),
 datetime.datetime(2015, 1, 24, 0, 0),
 datetime.datetime(2015, 3, 15, 0, 0),
 datetime.datetime(2015, 5, 4, 0, 0),
 datetime.datetime(2015, 6, 23, 0, 0),
 datetime.datetime(2015, 8, 12, 0, 0),
 datetime.datetime(2015, 10, 1, 0, 0),
 datetime.datetime(2015, 11, 20, 0, 0),
 datetime.datetime(2016, 1, 9, 0, 0),
 datetime.datetime(2016, 2, 28, 0, 0),
 datetime.datetime(2016, 4, 18, 0, 0),
 datetime.datetime(2016, 6, 7, 0, 0),
 datetime.datetime(2016, 7, 27, 0, 0),
 datetime.datetime(2016, 9, 15, 0, 0),
 datetime.datetime(2016, 11, 4, 0, 0)]
# Loop over the first 10 items of the datetimes_list
for item in datetimes_list[:10]:
    # Print out the record as a string in the format of 'MM/DD/YYYY'
    print(item.strftime('%m/%d/%Y'))

    # Print out the record as an ISO standard string
    print(item.isoformat())
