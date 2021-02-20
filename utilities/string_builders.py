def conditions_builder(values):
    conditions = []
    for k, v in values.items():
        if isinstance(v, str):
            conditions.append(str(k) + ' = ' + '\'' + str(v) + '\'')
        else:
            conditions.append(str(k) + ' = ' + str(v))
    return conditions
