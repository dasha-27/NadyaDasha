NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит


def classify(X):
    answer = 0
    iq_level, articles_count, has_education, ratio = X

    if iq_level <= 70:
        answer = NOT_FIT
    else:
        if articles_count == 0:
            answer = NOT_FIT
        elif articles_count == 1:
            answer = FIT
        else:
            if ratio <= 2.5:
                answer = FIT
            elif ratio > 2.5:
                answer = NOT_FIT
    return answer
