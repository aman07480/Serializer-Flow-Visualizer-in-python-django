SENSITIVE_FIELDS = ["password", "token", "secret"]


def mask_sensitive_data(data):

    if not isinstance(data, dict):
        return data

    masked = {}

    for key, value in data.items():

        if key.lower() in SENSITIVE_FIELDS:
            masked[key] = "******"
        else:
            masked[key] = value

    return masked