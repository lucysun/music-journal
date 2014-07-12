from datetime import datetime

class MusicJournal(object):
	entries = []
	def __init__(self, entries):
		self.entries = entries
	
class Time(object):
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
	
class SongInfo(object):
	def __init__(self, title, artist):
		self.title = title
		self.artist = artist

class Menu(MusicJournal):
	def print_options():
		print "Options:"
		print " 'p' print options"
		print " 'l' log today's song"
		print " 's' search past"
		print " 'q' quit program"
		
	choice = "p"
	while choice != "q":
		if choice == "l":
			now = datetime.now()
			year = now.year
			month = now.month
			day = now.day
			time = Time(year, month, day)

			title = str(raw_input("Song title: "))
			artist = str(raw_input("Artist: "))
			song_info = SongInfo(title, artist)
			
			entry = [str(time.year), str(time.month), str(time.day), song_info.title, song_info.artist]
			MusicJournal.entries.append(entry)
			
		elif choice == "s":
			year = int(raw_input("Year (YYYY): "))
			month = int(raw_input("Month (1-12): "))
			day is None
			time = Time(year, month, day)
			for entry in MusicJournal.entries:
				if str(time.year) == entry[0] and str(time.month) == entry[1]:
					print entry[1] + "-" + entry[2] + "-" + entry[0] + ": " + entry[3] + ", by " + entry[4]
			
		elif choice == "p":
			print_options()
		choice = raw_input("option: ")
		
