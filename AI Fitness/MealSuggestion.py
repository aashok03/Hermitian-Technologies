import mysql.connector as mysql


#Calculates caloric and macronutrient intake levels based on user information
#and dependent on the user's goals 

def suggestedIntake(weight, BMR, goal, ECB):
	
	caloricOutput = BMR+ECB
	
	if goal == 0:
		caloricIntake = 0.85*caloricOutput
	
	elif goal == 1:	
		caloricIntake = caloricOutput
        
	elif goal == 2:
    		caloricIntake = 1.15*caloricOutput
		
	proteinCalories = 0.18*caloricIntake 
    	protein = proteinCalories/4
	
	carbCalories = 0.55*caloricIntake
	carbs = carbCalories/4
	
	fatCalories = 0.27*caloricIntake
	fat = fatCalories/5
    
    optimalLevels = [caloricIntake, protein, carbs, fat] #List of intake data
    #calories followed by macronutrients in grams 
    
    return optimalLevels

#uses values calculated from above function + allergy data 
#to make meal recommendations to the user
def mealSuggestion(suggestedLevels, allergies):
	


