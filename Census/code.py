# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print(data)
census=np.concatenate((data,new_record))

print(data.shape)
print(census.shape)
age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)
#print(age.max())
def extractRace(raceId):
    return census[:,2]==raceId

# Extract different races
race_0 = census[extractRace(0), :]
race_1 = census[extractRace(1), :]
race_2 = census[extractRace(2), :]
race_3 = census[extractRace(3), :]
race_4 = census[extractRace(4), :]


# length of each nd-array created
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

races = np.array([len_0, len_1,len_2,len_3,len_4])
print(races)
# finding the smallest array
minority_race_number = np.min(races)

# Fetching the index of the array with the smallest length
minority_race = list(races).index(minority_race_number)
print(minority_race)

senior_citizens=census[census[:,0]>60,:]
working_hours_sum=np.sum(senior_citizens[:,7])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
high=census[census[:,1]>10,:]
low = census[census[:,1]<10,:]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.around(np.mean(low[:,7]),decimals = 2) + 0.01
avg_pay_high > avg_pay_low









