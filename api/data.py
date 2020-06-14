from db import connection

c = connection.cursor()


c.execute(
        '''CREATE TABLE IF NOT EXISTS jobs
        (id SERIAL PRIMARY KEY, blinds integer, placemats integer, water integer, cat_food integer, cat_litter integer, dishes integer ,kitchen integer, pack_up_din integer, read integer, learning integer, rubbish integer, set_table integer, wipe_surface integer, bathroom integer, bedrooms integer, dinner_baking integer, dishwasher integer, jump_jam integer, mop integer, os_able integer, shower integer , sweep integer, vacuum integer, washing integer, lounge integer, clean_car integer, garage integer, heis_room integer, clean_window integer, my_room integer, penalty integer, lying integer) '''
        )

#Could be used if you want to run the adding/subtraction from the server side.
#c.execute(
 #       '''INSERT INTO jobs
  #      (blinds, placemats, water, cat_food, cat_litter, dishes, kitchen, pack_up_din, read, learning, rubbish, set_table, wipe_surface, bathroom, bedrooms, dinner_baking, dishwasher, jump_jam, mop, os_able, shower, sweep, vacuum, washing, lounge, clean_car, garage, heis_room, clean_window, my_room, penalty, lying) VALUES(5, 5, 10, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 100, 100, 200, 200, 250, 100, 250) '''
        )

connection.commit()
