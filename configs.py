#structure your URI ie tell flask which DB to use

class Developement:
    #URI - Uniform Resource Identifier...type of db://defualt user:postgres password@ip address where db is located:port number/name of db created eg abcDB
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:0000@127.0.0.1:5432/abcDB'
    #to be able to see errors,set debug as true
    DEBUG=True
    SECRET_KEY='hvkhvkjblhiy856698uijhv'

class Production:
    pass