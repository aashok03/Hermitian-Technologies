
#--------------------Unit Conversions--------------------

#Convert from pounds to kilograms
def lb_to_kg (weight_lb):
	return weight_lb * 0.45359237

#Convert from kilograms to pounds
def kg_to_lb (weight_kg):
	return weight_kg * 2.20462262185

#Convert from inches to meters
def in_to_m (height_in):
	return height_in * 0.0254

#Convert meters to inches
def m_to_in (height_m):
	return height_m * 39.37007874


#--------------------BMI--------------------

#Calculate Body Mass Index (BMI)
def calc_BMI (weight_kg, height_m):
	return weight_kg / (height_m ** 2)


#--------------------BMR--------------------

#Calculate Basic Metabolic Rate (BMR) using Mifflin-St Jeor Equation
def calc_BMR_msj (weight_kg, height_m, age, gender):

	if gender == 'm':
		return (10 * weight_kg) + (6.25 * height_m * 100) - (5 * age) + 5
	else:
		return (10 * weight_kg) + (6.25 * height_m * 100) - (5 * age) - 161


#Calculate Basic Metabolic Rate (BMR) using Revised Harris-Benedict Equation
def calc_BMR_rhb (weight_kg, height_m, age, gender):

	if gender == 'm':
		return (13.397 * weight_kg) + (4.799 * height_m * 100) - (5.677 * age) + 88.362
	else:
		return (9.247 * weight_kg) + (3.098 * height_m * 100) - (4.330 * age) + 447.593


#Calculate Basic Metabolic Rate (BMR) using Katch-McArdle Equation
def calc_BMR_km (BFP, weight_kg):
	return 370 + 21.6 * (1 - BFP) * weight_kg


#--------------------FM,LM--------------------

#Calculate Fat Mass (FM) and Lean Mass (LM) in kilograms using BMI 
def calc_FM_LM_bmi (weight_kg, age, BMI, gender):

	if gender == 'm' and age >= 18:
		BFP = 1.20 * BMI + 0.23 * age - 16.2
	elif gender == 'f' and age >= 18:
		BFP = 1.20 * BMI + 0.23 * age - 5.4
	elif gender == 'm' and age < 18:
		BFP = 1.51 * BMI - 0.70 * age - 2.2
	else: 
		BFP = 1.51 * BMI - 0.70 * age + 1.4

	FM = (BFP / 100) * weight_kg
	LM = weight_kg - FM
	return FM, LM


#Calculate Fat Mass (FM) and Lean Mass (LM) in kilograms using Boer Equation
def calc_FM_LM_boer (weight_kg, height_m, gender):
	
	if gender == 'm':
		LM = (0.407 * weight_kg) + (0.267 * height_m * 100) - 19.2
		FM = weight_kg - LM
		return FM, LM
	else:
		LM = (0.252 * weight_kg) + (0.473 * height_m * 100) - 48.3
		FM = weight_kg - LM
		return FM, LM


#Calculate Fat Mass (FM) and Lean Mass (LM) in kilograms using James Equation
def calc_FM_LM_james (weight_kg, height_m, gender):

	if gender == 'm':
		LM = (1.1 * weight_kg) - (128 * ((weight_kg/(height_m * 100)) ** 2))
		FM = weight_kg - LM
		return FM, LM
	else:
		LM = (1.07 * weight_kg) - (148 * ((weight_kg/(height_m * 100)) ** 2))
		FM = weight_kg - LM
		return FM, LM


#Calculate Fat Mass (FM) and Lean Mass (LM) in kilograms using Humes Equation
def calc_FM_LM_hume (weight_kg, height_m, gender):

	if gender == 'm':
		LM = 0.32810 * weight_kg + 0.33929 * height_m * 100 - 29.5336
		FM = weight_kg - LM
		return FM, LM
	else:
		LM = 0.29569 * weight_kg + 0.41813 * height_m * 100- 43.2933
		FM = weight_kg - LM
		return FM, LM


#--------------------Macros Calculators--------------------


'''
Calculate caloric intake based on BMR, goal, and ECB

Goal:  -1 --> Lose weight
	   0 --> Keep weight
	   1 --> Gain weight
'''
def get_caloric_intake_percentages(BMR, goal, ECB):
	
	caloricOutput = BMR + ECB
	
	if goal == -1:
		caloricIntake = 0.85 * caloricOutput
	
	elif goal == 0:	
		caloricIntake = caloricOutput
        
	elif goal == 1:
		caloricIntake = 1.15 * caloricOutput  

	return caloricOutput

'''
Calculate caloric intake based on BMR, activity levels, and weight goal

Goal: Any float between -2 and +2 (which indicates lb/week gain or loss)
Activity: Factor of 1 - 1.9 based on how much exercises is done daily
'''
def get_caloric_intake_activity(BMR, activity_level, weight_rate_goal):
	
	calories_burned = BMR * activity_level
	caloric_intake = calories_burned + (weight_rate_goal * 500)

	return caloric_intake


#Return grams of protein, fat, and carbs based on caloric intake
def get_macros (caloricIntake):
		
	proteinCalories = 0.18 * caloricIntake 
	protein = proteinCalories / 4
	
	carbCalories = 0.55 * caloricIntake
	carbs = carbCalories / 4
	
	fatCalories = 0.27 * caloricIntake
	fat = fatCalories / 5
    
	return [protein, carbs, fat] 
