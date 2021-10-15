import math

from scipy.stats import norm
from modules import data_parser


def calculate_pert(data_array, desired_time):
    result_arr = []
    sum_et = 0
    sum_var = 0
    for data in data_array:
        op_val = int(data["optimisticValue"])
        ml_val = int(data["mostLikelyValue"])
        pes_val = int(data["pessimisticValue"])
        expected_val = get_expected_time(op_val, ml_val, pes_val)
        std_dev = get_standard_deviation(op_val, pes_val)
        variance = get_variance(std_dev)
        result_arr.append(data_parser.parse_results_to_json(data["taskName"], expected_val, std_dev, variance))
        sum_et += expected_val
        sum_var += variance
    z = calculate_z_value(sum_et, sum_var, int(desired_time))
    print(z)
    return result_arr, {
        "sumExpectedValue": sum_et,
        "sumVariance": sum_var,
        "zValue": round(z, 3),
        "probability": round(norm.cdf(z), 3) * 100
    }



def get_expected_time(o, m, p):
    return (o+4*m+p)/6


def get_standard_deviation(o, p):
    return (p-o)/6


def get_variance(standardDeviation):
    return standardDeviation*standardDeviation


#calculate Z value
def calculate_z_value(sum_et, sum_var, desired_time):
    return (desired_time - sum_et) / math.sqrt(sum_var)
