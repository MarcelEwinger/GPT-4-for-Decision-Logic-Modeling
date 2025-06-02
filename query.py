"""
Program for querying GPT-3 through the OpenAI API.
For each description (prompt1-6), it goes through the entire conversation three
times at four different temperature values, and saves the complete output.

Author: Simon Vandevelde <s.vandevelde@kuleuven.be>
"""
import os
import openai
import time

openai.api_key = "YOUR_KEY_HERE"


def query_openai(prompt, temp):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=temp,
      max_tokens=2048,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.6,
    )
    return response.choices[0].text


prompt1 = """The BMI of a person can be calculated based on their weight in kilogram and their length in meters by using the following formula: weight/(length*length). If the BMI value is above 30, then the BMI-level is considered Obese. If you are a male and the BMI-value is under 18.5 then the BMI-level is severely underweight and if you are female, then you are considered underweight with the same bmi-value. If the BMI-value is between 18.5 and 25 (without 25), then the BMI-level is underweight for a male and normal for a female. Lastly, if the BMI-value is between 25 and 30 and you are male then the BMI-level is normal but if you are a female then BMI-level is overweight.
"""

prompt2 = """A couple is planning their future and is determining under which conditions to adopt a certain pet. Together they decided that if someone has allergies and they have no time to take care of a pet, then no pet is adopted. The couple also decided to not take in an animal if they don't have kids. However, if they have an average or a large amount of time available, then if they have allergies they want to take in a fish. The couple decides that they also want a fish if they have kids and no allergies, even if they don't have a lot of time available. The couple decides to take in a cat or a dog only if no one has allergies. A dog is taken in if they have a garden, kids and a lot of time. The dog is also adopted if they have a garden, no kids and have normal or a lot oflarge amount of time to spare. In all the remaining cases, the couple decides they want to have a cat.
"""

prompt3 = """Whether a person is eligible to get their driver's license depends on their age, on being a national resident and on if they have sufficient practical skills. The practical skills are evaluated based on theoretical knowledge, driving skills, maneuvring skills and anticipation capabilities. Each of these aspects is evaluated with 'Excellent', 'Good' or 'Fail'. A person only passes the practical skills if they have no fails on any of the 4 aspects making up the practical skills. A person can only receive their driver's license if they are 18 or more, are a national resident and passed their practical skills test.
"""

prompt4 = """Every employee receives at least 22 days of vacation. Additional days are provided according to the following criteria: Only employees who are younger than 18 or at least 60 years old, or employees with at least 30 years of service will receive 5 extra days. Employees with at least 30 years of service and also employees of age 60 or more, receive 3 extra days, on top of possible additional days already given.
 If an employee has at least 15 but less than 30 years of service, 2 extra days are given. These 2 days are also provided for employees of age 45 or more. These 2 extra days can not be combined with the extra 5 days.
"""

prompt5 = """An institution decides to distribute scholarships but can obviously not give them to everyone. Therefore, they decide to distribute them based on grades, annual income and whether that person already received any scholarships. In short, a person can only be eligible for a scholarship if their grades are excellent or good, they earn less than 50000 a year and have not received any other scholarship yet. All the other cases make that the person is not eligible for that scholarship.
"""

prompt6 = """A person has the possibility to chose one of three transportation modes: walking, biking and driving a car. This person chooses their mode of transportation based on the distance, the weather and whether they are in a hurry. If the distance is bigger or equal to 10 km and the person is not in a hurry, then they choose to bike if it is sunny or cloudy and if it is rainy or freezing then the car is chosen. In any case, if the distance is more than 10 km and the person is in a hurry then the chosen mode of transportation is car. For medium distances between 5 and 10 kilometers, if it is raining the car is chosen. For the same medium distance, if the person is in a hurry the car is chosen. Again for medium distances and there is no hurry to arrive, the bike is chosen if it sunny or cloudy and if it is freezing then the car is chosen. For a distance between 2 and 5 kilometers, the car is chosen if it raining or if the person is in a hurry and it is sunny, cloudy or freezing outside; otherwise the bike is chosen. Finally, for a distance smaller than 2 kilometers, it the person is in a hurry the bike is chosen and otherwise the person will go by foot.
"""


# prompts = [prompt1, prompt2, prompt3, prompt4, prompt5, prompt6]
prompts = [
           ('BMI',
            prompt1,
            "What is the-BMI level of a male of 1.76m weighing 68 kgs?",
            "What is the-BMI level of a girl of 1.4m weighing 42 kgs?"),
           ('pet',
            prompt2,
            "What pet should a couple with allergies choose if they have a lot of time to take care of it?",
            "What is the pet going to be of a couple without allergies and average amount of time, no kids and with a garden?"),
           ('driver',
            prompt3,
            'Is a 23 year old person who did not pass their practical test and is a national resident eligible for a driver\'s license?',
            'Is a 32 year old person that failed the theoretical test and is a national resident eligible for a driver\'s licence?',
            ),
           ('vacation',
            prompt4,
            'How many holidays does a 32 year old receive if they have 6 years of service?',
            'How many holidays does a 64 year old receive if they have 32 years of service?'
            ),
           ('scholarship',
            prompt5,
            'Is a student with good grades and an annual income of 33000 eligible if he has no other scholarships assigned?',
            'Is a student with excellent grades and an annual income of 88000 eligible if he has no other scholarships assigned?'
            ),
           ('transport',
            prompt6,
            'What method of transport should I use if I want to go 15kms, have plenty of time and the sun is shining?',
            'What method of transport should I use if I want to go 1.8kms, am in a hurry and the weather is freezing?'
            )
           ]


def run_questions(prompt, challenge1, challenge2, temp):
    questions = [f'We will ask you a series of questions on Decision Model and Notation tables. Each question starts with "Q:", and each response should start with "A:". Below is a decision description, between quotation marks.  What does this description decide?\n\n\"\"\"{prompt}\"\"\"\n\n',
                 f'{challenge1}',
                 'What are the variables that influence this decision?',
                 'For each input and output, give me an overview of their data type and their possible values.',
                 'What are the relevant values of the numerical variables?',
                 'Could you generate a DMN decision table for this description? Make sure the table can be read horizontally: the column headers contain the inputs and output.',
                 'Make the rules mutually exclusive.',
                 'Is this table complete? (I.e., is there an applicable rule for each set of inputs?) If it is incomplete, can you find an example for which no rule would be applicable?',
                 f'According to your table, answer the following question.  {challenge2}',
                 ]
    query = ''
    for question in questions:
        query += f"Q: {question}"
        resp = query_openai(query, temp)
        query += f"\n\n{resp}\n\n"
        time.sleep(10)  # Sleep we do not hit the throughput limit.
    return query

for name, prompt, challenge1, challenge2, in prompts:
    for i in range(0, 3):
        for j in [0, 0.3, 0.7, 1]:
            try:
                result = run_questions(prompt, challenge1, challenge2, j)
                with open(f'{name}_temp{j}_{i}.txt', 'w') as fp:
                    fp.write(result)
            except openai.error.ServiceUnavailableError:
                # OpenAI down. Try again in 60s!
                import time
                time.sleep(60)
                result = run_questions(prompt, challenge1, challenge2, j)
                with open(f'{name}_temp{j}_{i}.txt', 'w') as fp:
                    fp.write(result)
            print(f'Finished {name}_temp{j}_{i}')
    break
