import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer


def identity_normalizer(x):
    return x


def infinite_domain_normalizer(x):
    return 1 - 1 / (1 + np.log(1 + x))


def logistic_normalizer(x, bound):
    if x < bound:
        return 0
    return 1 - 1 / (1 + np.log(2 + x - bound))


def distance_normalizer(x):
    return 1 - 4 * (x - 0.5) ** 2


def ratio_to_float(x):
    if x != x:
        return x
    a, b = map(float, x.split(':'))
    return a / (a + b)


MAPPINGS = {
    'FollowersOnYoutube': infinite_domain_normalizer,
    'FollowersOnInstagram': infinite_domain_normalizer,
    'FollowersOnTwitter': infinite_domain_normalizer,
    'MemberNationNumbers': lambda x: logistic_normalizer(x, 75),
    'ContinentalSpan': lambda x: logistic_normalizer(x, 4),
    'VRIncorporation': identity_normalizer,
    'Safety': distance_normalizer,
    'SustainabilityFactor': identity_normalizer,
    'NumberOfAntiDopingSamples': infinite_domain_normalizer,
    'MaleFemaleRatio': lambda x: distance_normalizer(ratio_to_float(x)),
    'YoutubeMostViews': infinite_domain_normalizer,
    'PhysicalExertion': identity_normalizer,
    'Entertainment': lambda x: x / 2,
}


def main():
    df = pd.read_excel('Sports.xlsx', index_col=0)
    factors = list(MAPPINGS.keys())
    train = pd.DataFrame(columns=factors)
    for factor in factors:
        train.loc[:, factor] = df[factor].apply(MAPPINGS[factor])
    train[:] = KNNImputer().fit_transform(train)
    train.to_excel('N_Sports.xlsx')


if __name__ == '__main__':
    main()
