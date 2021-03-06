# Damage Determination

This Python script is for dealing with generating a csv file which has computed damage to a turbine blade during each flight from Engine Health Monitoring data. The script contains a function that performs the necessary data cleaning to discover 1% corrupt data and remove them. 

## Installation

To use the python script type in following command in your terminal : git clone https://github.com/Kanaan213/damage_part.git 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

Navigate to the directory that has the requirements.txt file in your terminal and paste the following command:

```bash
pip install requirements.txt
```


## Usage

```python
You can find the notebook as damage.ipynb with a walkthrough the implementation.

You can also run the python script by navigating to the directory that has damage.py file. Type the following command in the termial :

python damage.py Scenario_Anonymised_v2.xlsx

This will return a csv file containing the computed parameters.

```

## Assumptions

 - Uncertainty in temperature measurement was neglected. Beacuse applying a confidence interval to capture the uncertianty in measurement would make the solution computationally expensive without significant benefits. 
           
 - Average temperature of flight climb was generaziled for other flight phases like cruise,takeoff etc. 
