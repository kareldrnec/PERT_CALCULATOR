

def parse_to_json(task_name, optimistic, most_likely, pessimistic):
    return {
        "taskName": task_name,
        "optimisticValue": optimistic,
        "mostLikelyValue": most_likely,
        "pessimisticValue": pessimistic
    }


def parse_results_to_json(task_name, expected_time, std_dev, variance):
    return {
        "taskName": task_name,
        "expectedTime": expected_time,
        "stdDev": std_dev,
        "variance": variance
    }
