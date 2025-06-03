# GPT-4 for Decision Logic Modeling 

This repository contains the data for the course project titled [GPT-3 for Decision Logic Modeling](https://lirias.kuleuven.be/retrieve/720326).
 The goal of the project was to evaluate our own prompting strategy for leveraging large language models in decision logic modeling tasks. 


The data is as follows:

* descriptions: the problem descriptions used for testing
* query.py: a Python program that runs through the Q&As and queries GPT-3 via the OpenAI API.
* generated_outputs: the outputs generated through each run
* gpt-dmn-evaluation.xlsx: the evaluation of these results, as cross-validated by both first authors

------------------------------------------------------------------
### Ground Truth
 - The BMI of a person can be calculated based on weight in kgs and length of a person in meters by using the following formula: weight/(length*length). If the BMI value is above 30, then the BMI-level is considered Obese. If you are a male and the BMI-value is under 18.5 then the BMI-level is severely underweight and if you are female, then you are considered underweight with the same bmi-value. If the BMI-value is between 18.5 and 25 (without 25), then the BMI-level is underweight for a male and normal for a female. Lastly, if the BMI-value is between 25 and 30 and you are a Male then the BMI-level is normal but if you are a female then BMI-level is overweight.
      
   -    Q1: What does this description decide?
        -  The description decide the BMI can be calculated based on the weight and height of an person using the following formula: weight / (heigth * heigth). If a person's BMI is less than 18.5 and they are male, they are classified as severely underweight. If the              BMI is less than 18.5 and the person is female, they are classified as underweight. When the BMI is between 18.5 and 25 (excluding 25) and the person is male, the classification is underweight, whereas a female with the same BMI range is considered to have             normal weight. For BMIs between 25 and 30 (inclusive), males are classified as normal, while females fall into the overweight category. If the BMI is greater than 30, both males and females are classified as obese.
          
   -    Q2: What is the-BMI level of a male of 1.76m weighing 68 kgs?
         - BMI = 68 / (1,76 * 1,76) = 21,95 --> **normal**
           
   -    Q3: What are the variables that influence this decisin?
         - The variables that influences the decision are: Weight in kg, Height in meters and Gender 
    
   -    Q4: For each input and output, give me an overview of their data type and their possible values.
         - Inputs:
            - Gender: **String**
            - Weight: **Integer** --> posetive
            - Height: **Float** --> posetive    
         - Outputs: BMI-Level: **String**; **severely underweight**, **underweight**, **normal**, **overweight**, **Obese**
   
   -    Q5: What are the relevant values of the numerical variables?
        - For Weight any **positive** Interger and for Height any **postive** Float
        
   -    Q6: Could you generate a DMN decision table for this description? Make sure the the table can be read horizontally: the column headers contain the inputs and output.
         | BMI-Scale               | Gender     | Length | Category                |
         |:------------------------|:----------:|:------:|-------------------------:|
         | < 18.5                  | male       |  any   | severely underweight    |
         | < 18.5                  | female     |  any   | underweight             |
         | >= 18.5 and < 25        | male       |  any   | underweight             |
         | >= 18.5 and < 25        | female     |  any   | normal                  |
         | >= 25 and <= 30         | male       |  any   | normal                  |
         | >= 25 and <= 30         | female     |  any   | overweight              |
         | > 30                    | male       |  any   | Obese                   |
         | > 30                    | female     |  any   | Obese                   |

         - Q6.1: Does the table contain the correct input variables?
         - Q6.2: Does the table contain the correct output variable?
         - Q6.3: Does the table contain at least one correct rule?
         - Q6.4: Is the table a correct decision table for the problem?
           
   -    Q7: Make the rules matually exclusive.
         | BMI-Scale               | Gender     | Length | Category                |
         |:------------------------|:----------:|:------:|-------------------------:|
         | < 18.5                  | male       |  any   | severely underweight    |
         | < 18.5                  | female     |  any   | underweight             |
         | >= 18.5 and < 25        | male       |  any   | underweight             |
         | >= 18.5 and < 25        | female     |  any   | normal                  |
         | >= 25 and <= 30         | male       |  any   | normal                  |
         | >= 25 and <= 30         | female     |  any   | overweight              |
         | > 30                    | male       |  any   | Obese                   |
         | > 30                    | female     |  any   | Obese                   |
   
   -     Q8: Is this table complete? (I.e., is there an applicable rule for each set of inputs?) If it is incomplete, can you find an example for which no rule would be applicable?
        -  This table is complete, as there is an applicable rule for each set of inputs.
     
   -    Q9: Accourding to your table, answer the following questions. What is the-BMI level of a girl of 1.4m weighing 42 kgs? 
        - BMI = 42 / (1,40 * 1,40) = 21.4 --> **normal**
          
* A couple is planning their future and is determining under which conditions a certain pet is adopted.
Together they decided that if someone has **allergies** and that no one has  **time** to take care of a pet then that no pet is adopted. The couple also decided to not take in an animal if they don't have kids, don't have time even if they don't have allergies. However, if they have a an average amount of time available or a lot and even if they have allergies then they want to take in a fish. The couple decides that they also want a fish if they have kids, no allergies even if they don't have a lot of time available. The couple decides to take in a cat or a dog only if no one has allergies. A dog is taken in if they have a garden, kids and they have a lot of time. The dog is also adopted if they have a garden, no kids and have normal or a lot of time to spare. In all the remaining cases, the couple decides they want to have a cat.

   - Q1: What does this description decide?
      - This description outlines the decision-making process for determining which pet (fish, dog, cat, or none) a family wants to adopt, based on the variables allergies, time, children, and garden.

   - Q2: What pet should a couple with allergies choose if they have a lot of time to take care of it?
      - Fish 

   - Q3: What are the variables that influence this decision?
      - Allergies
      - Time Available
      - Kids
      - Garden

   - Q4: For each input and output, give me an overview of their data type and their possible values.
      - Input:
         - Allergies: **Boolean** --> Yes or No
         - Time Available: **String** --> None, Average, Little or Lot
         - Kid: **Boolean** --> No or Yes
         - Garden: **Boolean** --> No or Yes
      - Output
         - Pet Adopted: **String** --> No Pet, Fish, Dog or Cat  

   - Q5: What are the relevant values of the numerical variables?

   - Q6: Could you generate a DMN decision table for this description? Make sure the table can be read horizontally: the column headers contain the inputs and output.
   | **Allergies** | **Time Available**     | **Kids** | **Garden** | **Pet Adopted** |
   |---------------|------------------------|----------|------------|------------------|
   | Y             | None                   | any      | any        | N                |
   | N             | None                   | N        | any        | N                |
   | Y             | Average or Lot         | any      | any        | Fish             |
   | N             | None                   | Y        | any        | Fish             |
   | N             | Lot                    | Y        | Y          | Dog              |
   | N             | Average                | N        | Y          | Dog              |
   | N             | Lot                    | N        | Y          | Dog              |
   | N             | Average                | N        | N          | Cat              |
   | N             | Lot                    | N        | N          | Cat              |
   | N             | Average                | N        | N          | Cat              |
   | N             | Average                | Y        | N          | Cat              |
     
         - Q6.1: Does the table contain the correct input variables?
         - Q6.2: Does the table contain the correct output variable?
         - Q6.3: Does the table contain at least one correct rule?
         - Q6.4: Is the table a correct decision table for the problem?

   - Q7: Make the rules mutually exclusive.
     | **Allergies** | **Time Available** | **Kids** | **Garden** | **Pet Adopted** |
     |---------------|--------------------|----------|------------|------------------|
     | Yes           | None               | Any      | Any        | No Pet           |
     | Yes           | Average or Lot     | Any      | Any        | Fish             |
     | No            | None               | No       | Any        | No Pet           |
     | No            | None               | Yes      | Any        | Fish             |
     | No            | Little             | Any      | Any        | Fish             |
     | No            | Average or Lot     | Yes      | Yes        | Dog              |
     | No            | Average or Lot     | No       | Yes        | Dog              |
     | No            | Average or Lot     | Any      | No         | Cat              |

   - Q8: Is this table complete? (I.e., is there an applicable rule for each set of inputs?) If it is incomplete, can you find an example for which no rule would be applicable?

   - Q9: According to your table, answer the following question: What is the pet going to be of a couple without allergies and average amount of time, no kids and with a garden?")
      -  Dog

* A person is eligible to get their driver's license based on their **age**, on being a **national resident** and if they have sufficient **practical skills**. The practical skills are evaluated based on the theoretical knowledge, driving skills, maneuvring skills and anticipation capabilities. Each of these aspects are evaluated with 'Excellent', 'Good' or 'Fail'. A person only passes the practical skills if they have no fails on any of the 4 aspects making up the practical skills. A person can only receive their driver's license if they are 18 or more, are a national resident and passed their practical skills test.

   - Q1: What does this description decide?
      - This description determines whether a person will receive a driver's license or not. The decision depends on three main points: age (>= 18), whether the person is a national resident, and practical driving skills, which are each assessed separately in theoretical knowledge, driving skills, maneuvering skills, and anticipation capabilities. Each of these four parts must be passed positively.

   - Q2: Is a 23 year old person who did not pass their practical test and is a national resident eligible for a driver\'s license?
      - No he isn't, because he did not pass the practical test.    

   - Q3: What are the variables that influence this decision?
      - Age
      - National resident status
      - practical skills
         - theoretical knowledge
         - driving skills
         - maneuvring skills
         - anticipation capabilities

   - Q4: For each input and output, give me an overview of their data type and their possible values.
      - Input:
         - Age: **Integer** --> any posetiv value
         - National resident status: **Boolean** --> Yes or No
         - practical skills: **Boolean** --> Yes or No
            - theoretical knowledge: **String*** --> 'Excellent', 'Good' or 'Fail'
            - driving skills: **String*** --> 'Excellent', 'Good' or 'Fail'
            - maneuvring skills: **String*** --> 'Excellent', 'Good' or 'Fail'
            - anticipation capabilities **String*** --> 'Excellent', 'Good' or 'Fail'
      - Output:
         - eligible for driver livesen: **Boolean** --> Yes or No
 
   - Q5: What are the relevant values of the numerical variables?
      - Age: posetiv Integer >= 18

   - Q6: Could you generate a DMN decision table for this description? Make sure the table can be read horizontally: the column headers contain the inputs and output.
        | Age (years) | National Resident | Theoretical Knowledge | Driving Skills    | Maneuvering Skills | Anticipation      | Passed Practical Skills | Eligible for License |
        | ----------- | ----------------- | --------------------- | ----------------- | ------------------ | ----------------- | ----------------------- | -------------------- |
        | < 18        | Any               | Any                   | Any               | Any                | Any               | -                       | No                   |
        | ≥ 18        | No                | Any                   | Any               | Any                | Any               | -                       | No                   |
        | ≥ 18        | Yes               | Fail                  | Any               | Any                | Any               | No                      | No                   |
        | ≥ 18        | Yes               | Any                   | Fail              | Any                | Any               | No                      | No                   |
        | ≥ 18        | Yes               | Any                   | Any               | Fail               | Any               | No                      | No                   |
        | ≥ 18        | Yes               | Any                   | Any               | Any                | Fail              | No                      | No                   |
        | ≥ 18        | Yes               | Good or Excellent     | Good or Excellent | Good or Excellent  | Good or Excellent | Yes                     | Yes                  |
 
         - Q6.1: Does the table contain the correct input variables?
         - Q6.2: Does the table contain the correct output variable?
         - Q6.3: Does the table contain at least one correct rule?
         - Q6.4: Is the table a correct decision table for the problem?

   - Q7: Make the rules mutually exclusive.
       | Age Condition | National Resident | Theoretical Knowledge | Driving Skills    | Maneuvering Skills | Anticipation      | Eligible for License |
       | ------------- | ----------------- | --------------------- | ----------------- | ------------------ | ----------------- | -------------------- |
       | < 18          | Any               | Any                   | Any               | Any                | Any               | No                   |
       | ≥ 18          | No                | Any                   | Any               | Any                | Any               | No                   |
       | ≥ 18          | Yes               | Fail                  | Any               | Any                | Any               | No                   |
       | ≥ 18          | Yes               | Good or Excellent     | Fail              | Any                | Any               | No                   |
       | ≥ 18          | Yes               | Good or Excellent     | Good or Excellent | Fail               | Any               | No                   |
       | ≥ 18          | Yes               | Good or Excellent     | Good or Excellent | Good or Excellent  | Fail              | No                   |
       | ≥ 18          | Yes               | Good or Excellent     | Good or Excellent | Good or Excellent  | Good or Excellent | Yes                  |


   - Q8: Is this table complete? (I.e., is there an applicable rule for each set of inputs?) If it is incomplete, can you find an example for which no rule would be applicable?
      - Yes this table is complete  

   - Q9: According to your table, answer the following question: Is a 32 year old person that failed the theoretical test and is a national resident eligible for a driver\'s licence?
      - No the person is not  eligible for a driver\'s licence.

* Every employee receives at **least 22 days**. Additional days are provided according to the following criteria:
Only employees younger than 18 or at least 60 years, or employees with at least 30 years of service will receive 5 extra days.
Employees with at least 30 years of service and also employees of age 60 or more, receive 3 extra days, on top of possible additional days already given.
If an employee has at least 15 but less than 30 years of service, 2 extra days are given. These 2 days are also provided for employees of age 45 or more. These 2 extra days can not be combined with the extra 5 days.

   - Q1: What does this description decide?
      - This description outlines how many vacation days an employee can receive within the company. Every employee is entitled to a minimum of 22 vacation days.
        Additional vacation days may be granted under specific conditions. Employees who are under the age of 18 are entitled to 5 extra vacation days. The same applies to employees who are at least 60 years old, as well as those who have worked for the company         for at least 30 years.
        It is, however, mathematically impossible for an employee to be under 18 years of age and have worked more than 30 years at the company.
        Employees who are both at least 60 years old **and** have worked at the company for at least 30 years receive an additional 3 vacation days, regardless of whether they have already received other additional vacation days.
        Furthermore, employees who have worked for the company for at least 15 years but less than 30 years receive 2 extra vacation days. These 2 days are also provided for employees of age 45 or more These may not be combined with the 5 additional days                mentioned above.

   - Q2: How many holidays does a 32 year old receive if they have 6 years of service?
      - 22 days

   - Q3: What are the variables that influence this decision?
      - Age
      - Number of working years

   - Q4: For each input and output, give me an overview of their data type and their possible values.
      - Input:
         - Age: any posetiv **Integer** number
         - Working Years: any posetiv **Integer** number
       - Output:
          - Number of vecation days: any posetiv **Integer** number greater than 22 

   - Q5: What are the relevant values of the numerical variables?
      - Age: 18, 45, 60
      - Working Years: 15,30
      -  Number of vacation days: 22, 5, 3, 2

   - Q6: Could you generate a DMN decision table for this description? Make sure the table can be read horizontally: the column headers contain the inputs and output.
      - Extracted from: https://dmcommunity.org/wp-content/uploads/2016/01/good-decision-table-challenge-jan-2016-garyhallmark.pdf 
      - Total Days Formula: Base Days(**22**) + (if Extra 5 Days then 5 else 0) + (if Extra 3 Days then 3 else 0) + (if Extra 2 Days and not(Extra 5 Days) then 2 else 0)
      - Extra 5 Days
        | A | Age       | Years of Service | Flag |
        | - | --------- | ---------------- | ---- |
        | 1 | <18, >=60 | -                | true |
        | 2 | -         | >= 30            | true |
     
     - Extra 3 Days
       | A | Age  | Years of Service | Flag |
       | - | ---- | ---------------- | ---- |
       | 1 | >=60 | -                | true |
       | 2 | -    | >= 30            | true |

     - Extra 2 Days
       | A | Age  | Years of Service | Flag |
       | - | ---- | ---------------- | ---- |
       | 1 | >=45 | -                | true |
       | 2 | -    | \[15..30)        | true |

     - Disclaimer: It is unclear whether 5 extra days can be awarded twice (e.g. to a 60 year old with 30 years of service).

         - Q6.1: Does the table contain the correct input variables?
         - Q6.2: Does the table contain the correct output variable?
         - Q6.3: Does the table contain at least one correct rule?
         - Q6.4: Is the table a correct decision table for the problem?

   - Q7: Make the rules mutually exclusive.
        - Extra 5 Days
        | A | Age       | Years of Service | Flag |
        | - | --------- | ---------------- | ---- |
        | 1 | <18, >=60 | -                | true |
        | 2 | -         | >= 30            | true |
     
     - Extra 3 Days
       | A | Age  | Years of Service | Flag |
       | - | ---- | ---------------- | ---- |
       | 1 | >=60 | -                | true |
       | 2 | -    | >= 30            | true |

     - Extra 2 Days
       | A | Age  | Years of Service | Flag |
       | - | ---- | ---------------- | ---- |
       | 1 | >=45 | -                | true |
       | 2 | -    | \[15..30)        | true |
  
   - Q8: Is this table complete? (I.e., is there an applicable rule for each set of inputs?) If it is incomplete, can you find an example for which no rule would be applicable?

   - Q9: According to your table, answer the following question: How many holidays does a 64 year old receive if they have 32 years of service?

* A person has the possibility to chose out of three transportation modes: **walking, bike and driving a car**. This person makes their transportation mode choice based on the **distance, weather and whether that person is in a hurry**. If the distance is bigger or equal to 10 and the person is not in a hurry, then the bike chosen if it is sunny or cloudy and if it is rainy or freezing then the car is chosen. In any case if the distance is more than 10 and the person is in a hurry then the model of transportation is car. For medium distances between 5 and 10 kilometers, if it is raining the car is chosen. For the same medium distance, if the person is in a hurry the car is chosen. Again for medium distances and there is no hurry to arrive, the bike chosen if it sunny or cloudy and if it is freezing then the car is chosen. For a distance between 2 and 5 kilometers, the car is chosen if it raining or if the person is in a hurry and it is sunny, cloudy or freezing outside, otherwise the bike is chosen. Finally for a small distance smaller than 2 kilometers, it the person is in a hurry the bike is chosen otherwise the person will go by foot.

   - Q1: What does this description decide?
     - This description is intended to help choose the optimal means of transportation (walking, car, or bicycle) based on the weather (cloudy, sunny, rainy, or freezing), the distance, and whether the person is in a hurry or not.

   - Q2: What method of transport should I use if I want to go 15kms, have plenty of time and the sun is shining?
      - Bike 

   - Q3: What are the variables that influence this decision?
      - Distance
      - Weather
      - Hurry 

   - Q4: For each input and output, give me an overview of their data type and their possible values.
      - Input:
         - Distance: **Integer** --> posetiv: >=10, >= 5 and < 10, >=2 and < 5 and < 2
         - Weather: **String** --> sunny, cloudly, freezing or sunny
         - Hurry: **Boolean** --> Yes or No
      - Output: Bike, Car, Walking
     
   - Q5: What are the relevant values of the numerical variables?
      - Distance: **Integer** --> posetiv: >=10, >= 5 and < 10, >=2 and < 5 and < 2

   - Q6: Could you generate a DMN decision table for this description? Make sure the table can be read horizontally: the column headers contain the inputs and output.
     | Distance         | Weather             | Hurry | Transport Models |
     |------------------|----------------------|--------|-------------------|
     | >= 10            | Sunny or Cloudly     | N      | Bike              |
     | >= 10            | Rainy or freezing    | N      | Car               |
     | >= 10            | any                  | Y      | Car               |
     | >= 5 and < 10    | rainy or freezing    | any    | Car               |
     | >= 5 and < 10    | sunny or cloudly     | N      | Bike              |
     | >= 5 and < 10    | sunny or cloudly     | Y      | Car               |
     | >=2 and < 5      | any                  | Y      | Car               |
     | >=2 and < 5      | Sunny or Cloudly     | N      | Bike              |
     | >=2 and < 5      | freezing and rainy   | N      | Car               |
     | < 2              | any                  | Y      | Bike              |
     | < 2              | any                  | N      | Walking           |

         - Q6.1: Does the table contain the correct input variables?
         - Q6.2: Does the table contain the correct output variable?
         - Q6.3: Does the table contain at least one correct rule?
         - Q6.4: Is the table a correct decision table for the problem?

   - Q7: Make the rules mutually exclusive.
     | Distance         | Weather             | Hurry | Transport Models |
     |------------------|----------------------|--------|-------------------|
     | >= 10            | Sunny or Cloudly     | N      | Bike              |
     | >= 10            | Rainy or freezing    | N      | Car               |
     | >= 10            | any                  | Y      | Car               |
     | >= 5 and < 10    | rainy or freezing    | any    | Car               |
     | >= 5 and < 10    | sunny or cloudly     | N      | Bike              |
     | >= 5 and < 10    | sunny or cloudly     | Y      | Car               |
     | >=2 and < 5      | any                  | Y      | Car               |
     | >=2 and < 5      | Sunny or Cloudly     | N      | Bike              |
     | >=2 and < 5      | freezing and rainy   | N      | Car               |
     | < 2              | any                  | Y      | Bike              |
     | < 2              | any                  | N      | Walking           |

   - Q8: Is this table complete? (I.e., is there an applicable rule for each set of inputs?) If it is incomplete, can you find an example for which no rule would be applicable?
      - Yes it is complete 

   - Q9: According to your table, answer the following question: What method of transport should I use if I want to go 1.8kms, am in a hurry and the weather is freezing?
      - Bike
         
* An institution decides to distribute scholarships but can obviously not give them to everyone. Therefore, they decide to distribute them based on the grades, annual income and whether that person already received any scholarships for the year they are applying to. In short a person can only be eligible for a scholarship if the grades are **excellent** or **good**, they earn less than 50.000 a year and have not received any other scholarship yet. All the other cases make that the person is not eligible for that scholarship.

   - Q1: What does this description decide?
      - It concerns the decision of whether someone receives a scholarship or not. The decision variables include grades, income, and whether a person has already received a scholarship before. A person cannot receive one if their grades are          excellent or good, if they earn less than 50,000, and if they have not received a scholarship before.

   - Q2: Is a student with good grades and an annual income of 33000 eligible if he has no other scholarships assigned.
     - Yes he is, because the grade is good, the income is less than 50000 a year and he has no other scholarship

   - Q3: What are the variables that influence this decision?
     - Grades, income and scholarship status 

   - Q4: For each input and output, give me an overview of their data type and their possible values.
      - Inputs:
            - Grades: **String**
            - Annual Income: **Integer** --> posetive
            - Scholarship Received : **Boolean** --> yes or no    
         - Outputs: Scholarship Status : **Boolean**; **yes** or **no**

   - Q5: What are the relevant values of the numerical variables?
      - For the income any posetive Integer --> 0-50.000

   - Q6: Could you generate a DMN decision table for this description? Make sure the table can be read horizontally: the column headers contain the inputs and output.
        | Grade       | Annual Income (< 50,000?) |  Scholarship Received | Scholarship Status |
        |-------------|---------------------------|-----------------------|--------------------|
        | Excellent   | Yes                       | No                    | Yes                |
        | Good        | Yes                       | No                    | Yes                |
        | Excellent   | Yes                       | Yes                   | No                 |
        | Good        | Yes                       | Yes                   | No                 |
        | Excellent   | No                        | No                    | No                 |
        | Good        | No                        | No                    | No                 |
        | Excellent   | No                        | Yes                   | No                 |
        | Good        | No                        | Yes                   | No                 |
        | Average     | yes                       | yes                   | No                 |
        | Average     | yes                       | no                    | No                 |
        | Average     | no                        | yes                   | No                 |
        | Average     | yes                       | no                    | No                 |
       
         - Q6.1: Does the table contain the correct input variables?
         - Q6.2: Does the table contain the correct output variable?
         - Q6.3: Does the table contain at least one correct rule?
         - Q6.4: Is the table a correct decision table for the problem?

   - Q7: Make the rules mutually exclusive.
       | Grade       | Annual Income (< 50,000?) |  Scholarship Received | Scholarship Status |
        |-------------|---------------------------|-----------------------|--------------------|
        | Excellent   | Yes                       | No                    | Yes                |
        | Good        | Yes                       | No                    | Yes                |
        | Excellent   | Yes                       | Yes                   | No                 |
        | Good        | Yes                       | Yes                   | No                 |
        | Excellent   | No                        | No                    | No                 |
        | Good        | No                        | No                    | No                 |
        | Excellent   | No                        | Yes                   | No                 |
        | Good        | No                        | Yes                   | No                 |
        | Average     | any                       | any                   | No                 |
  

   - Q8: Is this table complete? (I.e., is there an applicable rule for each set of inputs?) If it is incomplete, can you find an example for which no rule would be applicable?
      - No this table is complete

   - Q9: According to your table, answer the following question: Is a student with excellent grades and an annual income of 88000 eligible if he has no other scholarships assigned?
      - no they are not, because they earn too much.
