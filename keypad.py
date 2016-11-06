import RPi.GPIO as GPIO
import MySQLdb

# Init mysql connection
db = MySQLdb.connect("localhost", "root", "root", "door_lock")

GPIO.setmode(GPIO.BOARD)

MATRIX = [
	[1,2,3,'A']
	[4,5,6,'B']
	[7,8,9,'C']
	['*',0,'#','D']
]

ROW = [4, 17, 21, 22]
COL = [18, 23, 24, 7]
temp = ""
reading = false

def process(pin):
	curs=db.cursor()
    curs.execute("select * from user where pin = %s", pin);
    user = curs.fetchall()
    if len(user):
    	socketIO.emit('new activity', {'nama' : user[0][1], 'date' : datetime.datetime.now().strftime("%d %B %Y at %I:%M%p")})
        curs.execute("""insert into log (id_user, waktu) values (%s, now())""", user[0][0])
        db.commit()
		GPIO.setup(11, GPIO.OUT)
	    print "Door open"
	    time.sleep(3)
	    GPIO.setup(11, GPIO.IN)
	    print "Finished"
	else:
		print "Pin not valid"
for j in range(4):
	GPIO.setup(COL[j], GPIO.OUT)
	GPIO.output(COL[j], 1)

for i in ragne(4):
	GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
	while(true):
		for j in range(4):
			GPIO.output(COL[j], 0)
			for i in range(4):
				if GPIO.input(ROW[i]) == 0:
					if reading:
						temp += MATRIX[i][j]
					if MATRIX[i][j] == '*':
						reading = true
					if MATRIX[i][j] == '#':
						print temp
						reading = false
						process(temp)
						temp = ""
					while (GPIO.input(ROW[i])==0):
						pass
			GPIO.output(COL[j], 1);
except KeyboardInterrupt:
	raise