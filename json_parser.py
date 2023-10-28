import json

js = open("./electrical_json.json")

tables_data = json.load(js)

class Course:
	def __init__(self,course_name="No Name"):
		self.course_name = course_name
		self.course_code = None
		self.credit_hour = 0
		self.pre_requisite = []
		self.semister = None
		self.year = None



# get single table data among many tables across pages
def parse_json():

	new_course = None
	is_course_name = False
	is_course_code = False
	is_credit_hour = False
	is_prerequisite = False
	is_semister = False
	is_year = False

	finished = False

	courses = []

	for table_data in tables_data:

		# get rows wrapped in extra "[]" if there are multiple (means table_data["text"][0])
		for every_data in table_data["data"]:

			# loop through all the rows
			for row in every_data:
				cell_text = row["text"] 

				if (cell_text):
					if "\r" in cell_text:
						# print("*")
						cell_text = cell_text.replace("\r", " ")

					if(is_course_name):
						new_course.course_name = cell_text
						is_course_name = False

					elif(is_course_code):
						new_course.course_code = cell_text
						is_course_code = False

					elif(is_credit_hour):
						new_course.credit_hour = cell_text
						is_credit_hour = False

					elif(is_semister):
						new_course.semister = cell_text
						is_semister = False

					elif(is_year):
						new_course.year = cell_text
						is_year = False

					elif(is_prerequisite):
						new_course.pre_requisite.append(cell_text)
						is_prerequisite = False
						finished = True
					
					

					if finished:
					# courses.remove(new_course)
						courses.append(new_course)
						finished = False
						# print(cell_text)

					if (cell_text == "Course Name"):
						new_course = Course()
						is_course_name = True

					elif (cell_text == "Course Code:"):
						# new_course = Course()
						is_course_code = True
					
					elif ("Semester:" in cell_text):
						# new_course = Course()
						is_semister = True

					elif (cell_text == "Year:"):
						# new_course = Course()
						is_year = True

					elif (cell_text == "Credit Hour:"):
						# new_course = Course()
						is_credit_hour = True

					elif ("Prerequisit" in cell_text): #== "Prerequisit e/ Co- requisite: (if any)"):
						# new_course = Course()
						is_prerequisite = True

	return courses


# parse_json()
				

				

				# print(cell_text)
		# print("\n")

# for course in courses:
# 	print("name: " + course.course_name)
# 	print("course code: " + course.course_code)
# 	print(course.credit_hour)
# 	print("semester: " + course.semister)
# 	print("year: " + course.year)

# 	print(course.pre_requisite)
# 	print("\n***********")


js.close()
print("Done")