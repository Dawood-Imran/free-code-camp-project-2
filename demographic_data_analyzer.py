import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = ((df[df['education']=='Bachelors']['education'].count()/df.shape[0])*100).round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    specific_categories = ['Bachelors','Masters','Doctorate']
    filtered_df = df[df['education'].isin(specific_categories)]
    salary = (filtered_df['salary'].value_counts()/filtered_df.shape[0])*100
    
    # percentage of educated people with salary >50K
    higher_education_rich = round(salary.iloc[1],1)

    
    # Percentage of people with low education making >50K

    filtered_df_lower_education = df[~df['education'].isin(specific_categories)]
    lower_salary = (filtered_df_lower_education['salary'].value_counts()/filtered_df_lower_education.shape[0])*100
   
    lower_education_rich = round(lower_salary.iloc[1],1)



    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minimum_hours = df[df['hours-per-week'] == 1]
    minimum_hours_salary = (minimum_hours['salary'].value_counts()/minimum_hours.shape[0])*100
    rich_percentage = minimum_hours_salary.iloc[1]


    
    # What country has the highest percentage of people that earn >50K?
    grouped_df = df.groupby('native-country')['salary'].value_counts().unstack()
    grouped_df = grouped_df.fillna(0)
    grouped_df['>50K_percentage'] = (grouped_df['>50K'] / (grouped_df['>50K'] + grouped_df['<=50K'])) * 100

    max_country = grouped_df['>50K_percentage'].idxmax()
    max_percentage = grouped_df['>50K_percentage'].max()

    
    highest_earning_country = max_country
    highest_earning_country_percentage = round(max_percentage,1)
    

    # Identify the most popular occupation for those who earn >50K in India.
    filtered_df = df[df['native-country'] == 'India']
    filtered_df = filtered_df.groupby('occupation')['salary'].value_counts().unstack()
    filtered_df = filtered_df.fillna(0)
    higest_payed_occupation = filtered_df['>50K'].idxmax()

    top_IN_occupation = higest_payed_occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
