import pandas as pd
import psycopg2
from util import database_connect
postgres_engine = database_connect()

def question_1(): 
    '''What are the 5 nearest ports to Singapore's JURONG ISLAND port? 
         (country = 'SG', port_name = 'JURONG ISLAND').
        Your answer should include the columns port_name and distance_in_meters only.'''

    query = '''
    select * from world_port.public.wpi_data
    limit 5
    '''
    q1 = pd.read_sql(query, postgres_engine)
    print(q1)

def question_2():
    ''' Which country has the largest number of ports with a cargo_wharf? 
    Your answer should include the columns country and port_count only. '''
    query = '''


    '''
    q2 = pd.read_sql(query, postgres_engine)

def question_3():
    ''' You receive a distress call from the middle of the North Atlantic Ocean. The person on the line gave you a coordinates of 
    # lat: 32.610982, long: -38.706256 and asked for the nearest port with provisions, water, fuel_oil and diesel. 
    # Your answer should include the columns country,
    # port_name, port_latitude and port_longitude only. '''

    query = '''
    

    '''

    q3 = pd.read_sql(query, postgres_engine)


#question_1() 
question_2() 
#question_3() 



# country_codes                           Country Code                            Country Name
# country_codes_old                       Country Code                            Country Name
# depth_code_lut                          Depth Code                              Feet                                          Meters
# drydock_marine_railway                  Drydock/Marine Railway Code Drydock     Marine Railway Code Description
# harbor_size                             Harbor Size Code                        Harbor Size
# harbor_type                             Harbor Type Code                        Harbor Type Description
# maximum_size_vessel                     Maximum Size Vessel Code                Maximum Size Vessel Description
# repairs_code                            Repairs Code                            Repairs Code Description
# shelter_afforded                        Shelter Afforded Code                   Shelter Afforded Description
# wpi_data                          World_port_index_number/ Region_index / Main_port_name / Wpi_country_code / Latitude_degrees / 
#                                      / Supplies_deck / Supplies_engine / Repair_code / Drydock Railway
# wpi_import             
# wpi_region

# world_port.public.country_codes