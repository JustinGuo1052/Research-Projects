import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.linear_model import LogisticRegression


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
    train = pd.DataFrame(columns=factors, index=df.index[~np.isnan(df['Label'])])
    for factor in factors:
        train.loc[:, factor] = df[factor].apply(MAPPINGS[factor])
    train[:] = KNNImputer().fit_transform(train)
    model = LogisticRegression().fit(train, df.loc[~np.isnan(df['Label']), 'Label'])
    print(model.score(train, df.loc[~np.isnan(df['Label']), 'Label']))
    print(factors)
    print(list(model.coef_[0]), model.intercept_[0])


if __name__ == '__main__':
    main()
