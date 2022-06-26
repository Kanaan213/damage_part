# Damage Determination

This Python script is for dealing with generating a csv file which has computed damage to a turbine blade during each flight from Engine Health Monitoring data. The script contains a function that performs the necessary data cleaning to discover 1% corrupt data and remove them. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

Navigate to the directory that has the requirements.txt file in your terminal and paste the following command:

```bash
pip install requirements.txt
```


## Usage

```python

You can run the script using the Engine Health Monitoring data filename without whitespace withtin the name like so:
# returns a csv file containing the computed parameters
python damage.py Scenario_Anonymised_v2.xlsx

```

## Assumptions

 - Uncertainty in temperature measurement was neglected. Beacuse applying a confidence interval to capture the uncertianty in measurement would make the solution computationally expensive without significant benefits. 
           
 - Average temperature of flight climb was generaziled for other flight phases like cruise,takeoff etc. 
