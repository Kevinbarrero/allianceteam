###Product Attributes

REQUIRED_SOFTWARE_RELIABILITY = {"очень высокий":0.75, "высокий":0.88, "Номинальный":1.00, "низкий":1.15, "очень низкий":1.40}
SIZE_OF_APPLICATION_DATABASE = 	[0.94, 1.00, 1.08, 1.16]
COMPLEXITY_OF_THE_PRODUCT = [0.70, 0.85, 1.00, 1.15, 1.30]

###Hardware Attributes

RUNTIME_PERFORMANCE_CONSTRAINTS = [1.00, 1.11, 1.30]
MEMORY_CONSTRAINTS = [1.00, 1.06, 1.21]
VOLATILITY_OF_THE_VIRTUAL_MACHINE_ENVIRONMENT = [0.87, 1.00, 1.15, 1.30]
REQUIRED_TURNABOUT_TIME = [0.94, 1.00, 1.07, 1.15]
###Personnel attributes

ANALYST_CAPABILITY = [1.46, 1.19, 1.00, 0.86, 0.71]
APPLICATIONS_EXPERIENCE = [1.29, 1.13, 1.00, 0.91, 0.82]
SOFTWARE_ENGINEER_CAPABILITY = [1.42, 1.17, 1.00, 0.86, 0.70]
VIRTUAL_MACHINE_EXPERIENCE = 	[1.21, 1.10, 1.00,0.90]
PROGRAMMING_LANGUAGE_EXPERIENCE = [1.14,1.07,1.00, 0.95] 

##Project Attributes

APPLICATION_OF_SOFTWARE_ENGINEERING_METHODS = [1.24,1.10, 1.00, 0.91, 0.82]
USE_OF_SOFTWARE_TOOLS= [1.24, 1.10, 1.00,0.91,0.83]
REQUIRED_DEVELOPMENT_SCHEDULE = [1.23,1.08,1.00,1.04,1.10]

###type model VALUE A, B, C

ORGANIC = [3.2, 1.05, 0.38]
SEMI_DETACHED = [3.0, 1.12, 0.35]
EMBEDDED = [2.8, 1.20, 0.32]


t1 = {'a1':{'очень высокий':0.75, 'высокий':0.88, 'Номинальный':1.00, 'низкий':1.15, 'очень низкий':1.40},
        'a2':{'очень высокий':0.75, 'высокий':0.88, 'Номинальный':1.00, 'низкий':1.15, 'очень низкий':1.40},
        'a3':  {'очень высокий':0.88, 'высокий':0.94,  'Номинальный':1.00, 'низкий':1.08,  'очень низкий':1.16,},
        'a4':  {'очень высокий':1.46,  'высокий':1.19, 'Номинальный':1.00,  'низкий':0.86,   'очень низкий':0.71},
        'a5':  {'очень высокий':1.29,   'высокий':1.13,  'Номинальный':1.00,   'низкий':0.91,  'очень низкий':0.82},
        'a6': {'очень высокий':1.42,   'высокий':1.17,   'Номинальный':1.00,  'низкий':0.86,  'очень низкий':0.70 },
        'a7': {'очень высокий':1.19,    'высокий':1.21,    'Номинальный':1.10,   'низкий':1.00,  'очень низкий':0.90 },
        'a8': {'очень высокий':1.10,    'высокий':1.14,    'Номинальный':1.07,   'низкий':1.00, 'очень низкий': 0.95 },

      }

        
print(t1['a1']['очень высокий'])

