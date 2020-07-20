import json


def pred_to_dict(prediction_items):
    pred_dict = {}
    for k, v in prediction_items.items():
        pred_dict[k] = json.loads(v) if k == 'prediction' else v
    return pred_dict
