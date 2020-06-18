import mysql.connector as mysql

def addAllergen(name, allergens, allergenDictionary):
	
	for i in allergens:

		if name in allergenDictionary[i]:
			
			continue
		
		else:
		
			allergenDictionary[i] = allergenDictionary[i].append(name)

# This function determines how many calories a meal should approximately contain
# based on the users caloric consumption and the type of meal it is 
# Here the input calories are the calories the user needs to consume daily
# determined by the application 
def determineCaloriesForMeal(calories, mealType):
	
	if mealType == "breakfast":

		calories = int(calories*0.20)

	elif mealType == "lunch":

		calories = int(calories*0.30)

	elif mealType == "preworkout":

		calories = int(calories*0.05)

	elif mealType == "postworkout":

		calories = int(calories*0.15)	

	elif mealType == "snack":

		calories = int(calories*0.05)

	elif mealType == "dinner":

		calories == int(calories*25)

	return calories

# This function adds a new meal to the SQL db 
# Here the input calories are the calories the user needs to consume daily
# determined by the application 
def addMeal(name, mealType, calories, protein, carbs, fat, servingSize, allergens, allergenDictionary):
	
	db = mysql.connect(user='root', password='Hermitian', host = 'localhost', \
		database='AIFitness', auth_plugin='mysql_native_password')
	
	cursor = db.cursor()
	
	newstring = "insert into  mealTable VALUES ('" + name + "', '" + mealType + "', " + \
		str(calories) + ","+ str(protein)+ ", " + str(carbs) + ", "+ str(fat)+")"
	
	cursor.execute(str(newstring))
	
	db.commit()
	cursor.close()
	db.close()

	addAllergen(name, allergen, allergenDictionary)


# Here the input calories are the calories the user needs to consume daily
# determined by the application 
def selectMeal(calories, mealType, protein, allergies):

	calories = determineCaloriesForMeal(calories, mealType)

	calorieUpper = int(calories * 1.1)
	calorielower = int(calories * 0.9)

	db = mysql.connect(user='root', password='Hermitian', host = 'localhost', \
	   database='AIFitness', auth_plugin='mysql_native_password')
	
	cursor = db.cursor()
	
	newstring = "select * FROM mealTable WHERE mealType = '"+mealType+" AND calories BETWEEN "+ str(calorielower)+\
		"AND "+ str(calorieUpper)
	
	cursor.execute(newstring)
	
	meals = cursor.fetchall()


	# for each meal, check if they contain any of the allergens that the person 
	#is allergic to and eliminate ones that contain them 

# This function deletes a meal from the db. It considers the serving size because 
# One meal can have multiple instances based on the serving size differences
def deleteMeal(name, servingSize):

	db = mysql.connect(user='root', password='Hermitian', host = 'localhost', \
	   database='AIFitness', auth_plugin='mysql_native_password')
	
	cursor = db.cursor()
	
	newstring = "delete from mealTable where name = '" + name + "' AND servingSize = '"+\
		servingSize+"'"

