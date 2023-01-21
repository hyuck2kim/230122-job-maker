import pymysql
import random, time
import socket

MAX_ROW_COUNT = 1000
MIN_DELAY_TIME = 1
MAX_DELAY_TIME = 2

countQeury = "select count(*) from work;"

while 1:
  try:
    conn = pymysql.connect(host= 'host.docker.internal', user = 'root', password='sang224', db='test', charset='utf8')
    with conn:
      with conn.cursor() as cur:
        print("check total works count")
        cur.execute(countQeury)
        row = cur.fetchone()
        rowCnt = row[0]
        print(f"Works counts: {rowCnt}")

        if rowCnt < MAX_ROW_COUNT:
          print("creating work starts")
          createQuery =f'insert into work (worker) values ("{socket.gethostname()}");'
          cur.execute(createQuery)
          conn.commit()
          print("creating work finished")
        else:
          print(f"Row count is more than {MAX_ROW_COUNT}")
  except Exception as e:    
    print('Execption: ', e)
      
  delayTime = MIN_DELAY_TIME+(MAX_DELAY_TIME-MIN_DELAY_TIME)*random.random()
  time.sleep(delayTime)
  print(f"delayTime: {delayTime}")
  print("------------------------")
