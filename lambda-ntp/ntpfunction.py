import ntplib

# retrieve the response offset from a given ntp server
def get_ntp(ntpserver):
    print('querying ntp server ' + ntpserver + ' ...')

    try:
        ntpclient = ntplib.NTPClient()
        response = ntpclient.request(ntpserver)
        print('success - ntp server ' + ntpserver + ' returned response offset ' + str(response.offset) + ' \n')

    except Exception as e:
        print('error - ntp server ' + ntpserver + ' could not be reached \n')
        print(str(e) + ' \n')

# lambda handler
def handler(event, context):

    # check external ntp server    
    ntpserver = '0.pool.ntp.org'
    get_ntp(ntpserver)

    # check local ntp server
    ntpserver = '169.254.169.123'
    get_ntp(ntpserver)
