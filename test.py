# Нұсқа 4

class Course:
	def __init__(self, title, credits):
		self._title = title
		self._credits = credits

	def get_course_info(self, title, credits):
		pass
	
	def calc_res(self):
		return self._credits * 3
	

class OnlineCourse(Course):
	def start_video_lecture(self):
		print("Vidio start")

	def get_course_info(self):
		print(f"Онлайн курс")


class OfflineCourse(Course):
	def schedule_classroom(self):
		print("Lessons start")

	def get_course_info(self,):
		print(f"Оффлайн курс")


