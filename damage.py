# import libaries
import pandas as pd
import numpy as np
import sys
from scipy import stats

def clean(argv):
    """ This function determines if there is corrupt data and cleans it. 

    Args:
        PATH (str): path to the Engine Health Monitoring data.

    Returns:
        dataframe: clean data free from data corruption.
    """
    assert argv
    # load damage measurement file
    df = pd.read_excel(argv)
    # select all columns except last three as there are not input features of the damage equation
    df = df.iloc[: , :-3]
    # limit the dataframe to a (float), b (int) and e (timedelta)
    cols = df.select_dtypes('number').columns  
    # drop rows with nan values
    df.dropna(subset=cols, inplace=True)

    return df

def data_wraggling(argv):
    """ This function performs data manipulations to compute average temperature for each flight phase and average time of each flight phase.

    Args:
        PATH (str): path to the Engine Health Monitoring data

    Returns:
        dataframe: contains dataframe with all input features to compute turbine blade damage
    """ 
    assert argv
    df = clean(argv)
    # group the categorical features to aggregate the mean of numerical features
    df = df.groupby(['Flight Phase', 'Engine Serial Number','Operator']).agg({'Temperature / Degrees': ['mean'],'Time / seconds': ['mean']})
    # create new columns of average temperature and average time of flight phase
    df.columns = ['average_temp','average_flight_phase_time']
    df = df.reset_index()

    return df

def compute_damage(argv):
    """This function damage to a turbine blade during each flight.

    Args:
        PATH (str): path to the Engine Health Monitoring data.

    Returns:
        dataframe: contains the actual part damage and predicted part damage for each flight phase.
    """

    assert argv
    df = data_wraggling(argv)
    AVERAGE_TEMP_FOR_CLIMB_PHASE = df['average_temp']
    OPERATOR_FACTOR = {'ABC':1,'DEF':1.1}
    df['Op_factor'] = df['Operator'].map(OPERATOR_FACTOR)
    damage = df['Op_factor'] * 1.2e-11 * AVERAGE_TEMP_FOR_CLIMB_PHASE **2.88
    # infered from the relationship within validation data
    predicted_damage = damage - 1e-04

    df['actual_part_damage'] = damage
    df['predicted_part_damage'] = predicted_damage
    return df


if __name__ == '__main__':
    df = compute_damage(sys.argv[1])
    # PATH = 'Scenario Anonymised v2.xlsx'
    # df = compute_damage(PATH)
    df.to_csv('damage_actual_predicted.csv')

