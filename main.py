import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 25)
pd.set_option('display.expand_frame_repr', False)

path = 'C:/Users/a_khl/PycharmProjects/dataFrame/venv/Data/'
countries_file = 'countries.csv'
departments_file = 'departments.csv'
employees_file = 'employees.csv'
job_history_file = 'job_history.csv'
jobs_file = 'jobs.csv'
locations_file = 'locations.csv'
regions_file = 'regions.csv'

# employee_file = pd.read_csv('./venv/Data/countries.csv')

# Creation des dataframes

countries_df = pd.read_csv(f"{path}{countries_file}", delimiter=";")
departments_df = pd.read_csv(f"{path}{departments_file}", delimiter=";")
employees_df = pd.read_csv(f"{path}{employees_file}", delimiter=";", parse_dates=['HIRE_DATE'], dayfirst=True)
job_history_df = pd.read_csv(f"{path}{job_history_file}", delimiter=";")
jobs_df = pd.read_csv(f"{path}{jobs_file}", delimiter=";")
locations_df = pd.read_csv(f"{path}{locations_file}", delimiter=";")
regions_df = pd.read_csv(f"{path}{regions_file}", delimiter=";")

# Merge the dataframes into a single dataframe
hr = employees_df.merge(departments_df.merge(locations_df.merge
    (countries_df.merge(regions_df, how="left", on="REGION_ID"), how="left", on="COUNTRY_ID"),
    how="left", on="LOCATION_ID"), how="left", on="DEPARTMENT_ID")

print(hr)
print(hr.info())


# Grouper le dataframe par region
regions = hr.groupby('REGION_NAME')


print('\n' * 2)
print('Total salaire par region')
print('-' * len('Total salaire par region'))

# Afficher le total des salaires par region
for region in regions.groups:
    print(f"le total des salaires de la region {region} est {regions.get_group(region)['SALARY'].sum()}")

# Afficher le total des salaires par region simple
print('\n' * 1)
print('Total salaires par region')
print(regions['SALARY'].sum())





# Grouper le dataframe par pays
countries = hr.groupby('COUNTRY_NAME')

print('\n' * 2)
print('Total salaires par pays')
print('-' * len('Total salaires par pays'))

# Afficher le total des salaires par pays
for country in countries.groups:
    print(f"le total des salaires du pays {country} est {countries.get_group(country)['SALARY'].sum()}")

# Afficher le total des salaires par pays simple
print('\n' * 1)
print('Total salaires par pays')
print(countries['SALARY'].sum())



print('\n' * 2)
print('10 premiers salaires')
print('-' * len('10 premiers salaires'))

#Afficher les 10 premiers employés en terme de salaire
emp_sort_salary = employees_df.sort_values(by=['SALARY'], ascending=False)
print(emp_sort_salary[['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'SALARY']].head(10))



# Grouper le dataframe par department
departments = hr.groupby('DEPARTMENT_NAME')

print('\n' * 2)
print('Minimal recrutement date par departement')
print('-' * len('Minimal recrutement date par departement'))

# Afficher la date minimale du recrutement par department
for department in departments.groups:
    print(f"la date minimale de recrutement du department {department} est {departments.get_group(department)['HIRE_DATE'].min()}")

# Afficher la date minimale du recrutement par department simple
print('\n' * 1)
print('Date minimale de recrutement par department')
print(departments['HIRE_DATE'].min())



print('\n' * 2)
print('Maximale recrutement date par departement')
print('-' * len('Maximale recrutement date par departement'))

# Afficher la date maximale du recrutement par department
for department in departments.groups:
    print(f"la date maximale de recrutement du department {department} est {departments.get_group(department)['HIRE_DATE'].max()}")

# Afficher la date maximale du recrutement par department simple
print('\n' * 1)
print('Date maximale de recrutement par department')
print(departments['HIRE_DATE'].max())


# Grouper le dataframe par jobs
jobs = hr.groupby('JOB_ID')

print('\n' * 2)
print('Nombre total des employes par fonction')
print('-' * len('Nombre total des employes par fonction'))

# Afficher le nombre total des employes par job
for job in jobs.groups:
    print(f"le nombre total des employes qui occuppent un poste de {job} est {jobs.get_group(job)['EMPLOYEE_ID'].count()}")


# Afficher le nombre total des employes par job simple
print('\n' * 1)
print('Le nombre total des employes par fonction ')
print(jobs['EMPLOYEE_ID'].count())
