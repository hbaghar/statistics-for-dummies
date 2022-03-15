import pandas as pd
import scipy.stats
from scipy import stats
from scipy.stats import f_oneway

# Input parameters: sample (pd df), population mean (float), significance level (optional float)
# Return values: p-value, t-value, confidence interval (lower), confidence interval (upper), mean of sample, reject/accept (1 = accept, 0 = reject)
def t_test_1_samp(x, pop_mean, sig_lvl=0.05):

    out = 0

    if out:
        print("One Sample t-test")

    samp_mean = float(x.mean())
    samp_sd = float(x.std())
    n = x.shape[0]

    t = float((samp_mean - pop_mean) / (samp_sd / pow(n, 0.5)))
    p = scipy.stats.t.sf(abs(t), df=n - 1) * 2
    con_1, con_2 = scipy.stats.t.interval(
        alpha=1 - sig_lvl, df=n - 1, loc=samp_mean, scale=scipy.stats.sem(x)
    )

    con_1 = float(con_1)
    con_2 = float(con_2)

    if out:
        print("t = " + str(t))
        print("df = " + str(n - 1))
        print("p-value = " + str(p))

    accept = 1
    if p > sig_lvl:
        if out:
            print("Alternative hypothesis: true mean is not equal to " + str(pop_mean))
        accept = 0
    else:
        if out:
            print("Null hypothesis: true mean is equal to " + str(pop_mean))

    if out:
        print(
            str(100 * (1 - sig_lvl))
            + "% confidence interval: "
            + str(con_1)
            + " "
            + str(con_2)
        )
        print("Mean of x: " + str(samp_mean))

    result = {
        "p_value": p,
        "t_value": t,
        "con_low": con_1,
        "con_up": con_2,
        "sample_mean_1": samp_mean,
        "accept": accept,
    }

    return result


# Input parameters: sample 1 (pd df), sample 2 (pd df), significance level (optional float)
# Return values: p-value, t-value, confidence interval (lower), confidence interval (upper), mean of sample 1, mean of sample 2, reject/accept (1 = accept, 0 = reject)
def t_test_welch(x, y, sig_lvl=0.05):

    out = 0

    if out:
        print("Welch Two sample t-test (unequal variance)")

    mu_1 = float(x.mean())
    mu_2 = float(y.mean())
    s1 = x.std()
    s2 = y.std()
    n1 = x.shape[0]
    n2 = y.shape[0]

    t, p = stats.ttest_ind(x, y, equal_var=False)
    t = float(t)
    p = float(p)

    con_1 = float(
        (mu_1 - mu_2)
        - (
            scipy.stats.t.ppf((1 - sig_lvl / 2), n1 + n2 - 2)
            * pow(((((n1 - 1) * s1 * s1) + ((n2 - 1) * s2 * s2)) / (n1 + n2 - 2)), 0.5)
            * pow((1 / n1 + 1 / n2), 0.5)
        )
    )
    con_2 = float(
        (mu_1 - mu_2)
        + (
            scipy.stats.t.ppf((1 - sig_lvl / 2), n1 + n2 - 2)
            * pow(((((n1 - 1) * s1 * s1) + ((n2 - 1) * s2 * s2)) / (n1 + n2 - 2)), 0.5)
            * pow((1 / n1 + 1 / n2), 0.5)
        )
    )

    if out:
        print("t = " + str(t))
        print("df = " + str(n1 + n2 - 2))
        print("p-value = " + str(p))

    accept = 1
    if p > sig_lvl:
        if out:
            print("Alternative hypothesis: true difference in means is not equal to 0")
        accept = 0
    else:
        if out:
            print("Null hypothesis: true difference in means is equal to 0")

    if out:
        print(
            str(100 * (1 - sig_lvl))
            + "% confidence interval: "
            + str(con_1)
            + " "
            + str(con_2)
        )
        print("Mean of x and mean of y (respectively): " + str(mu_1) + ", " + str(mu_2))
        print()

    result = {
        "p_value": p,
        "t_value": t,
        "con_low": con_1,
        "con_up": con_2,
        "sample_mean_1": mu_1,
        "sample_mean_2": mu_2,
        "accept": accept,
    }
    return result


# Input parameters: sample 1 (pd df), sample 2 (pd df), significance level (optional float)
# Return values: p-value, t-value, confidence interval (lower), confidence interval (upper), mean of sample 1, mean of sample 2, reject/accept (1 = accept, 0 = reject)
def t_test_2_samp_equal_var(x, y, sig_lvl=0.05):

    out = 0

    if out:
        print("Two sample t-test (equal variance)")

    mu_1 = float(x.mean())
    mu_2 = float(y.mean())
    s1 = x.std()
    s2 = y.std()
    n1 = x.shape[0]
    n2 = y.shape[0]

    t = float((mu_1 - mu_2) / (pow((s1 * s1 / n1) + (s2 * s2 / n2), 0.5)))

    p = scipy.stats.t.sf(abs(t), df=n1 + n2 - 2) * 2
    con_1 = float(
        (mu_1 - mu_2)
        - (
            scipy.stats.t.ppf((1 - sig_lvl / 2), n1 + n2 - 2)
            * pow(((((n1 - 1) * s1 * s1) + ((n2 - 1) * s2 * s2)) / (n1 + n2 - 2)), 0.5)
            * pow((1 / n1 + 1 / n2), 0.5)
        )
    )
    con_2 = float(
        (mu_1 - mu_2)
        + (
            scipy.stats.t.ppf((1 - sig_lvl / 2), n1 + n2 - 2)
            * pow(((((n1 - 1) * s1 * s1) + ((n2 - 1) * s2 * s2)) / (n1 + n2 - 2)), 0.5)
            * pow((1 / n1 + 1 / n2), 0.5)
        )
    )

    if out:
        print("t = " + str(t))
        print("df = " + str(n1 + n2 - 2))
        print("p-value = " + str(p))

    accept = 1
    if p > sig_lvl:
        if out:
            print("Alternative hypothesis: true difference in means is not equal to 0")
        accept = 0
    else:
        if out:
            print("Null hypothesis: true difference in means is equal to 0")

    if out:
        print(
            str(100 * (1 - sig_lvl))
            + "% confidence interval: "
            + str(con_1)
            + " "
            + str(con_2)
        )
        print("Mean of x and mean of y (respectively): " + str(mu_1) + ", " + str(mu_2))
        print()

    result = {
        "p_value": p,
        "t_value": t,
        "con_low": con_1,
        "con_up": con_2,
        "sample_mean_1": mu_1,
        "sample_mean_2": mu_2,
        "accept": accept,
    }
    return result


# Input parameters: sample (pd df), population mean (float), significance level (optional float)
# Return values: p-value, z-value, confidence interval (lower), confidence interval (upper), mean of sample, reject/accept (1 = accept, 0 = reject)
def z_test_1_samp(x, pop_mean, sig_lvl=0.05):

    out = 0

    if out:
        print("1 sample z-test (two-tailed)")

    samp_mu = float(x.mean())
    pop_std = float(x.std())
    n = float(x.shape[0])

    z = float((samp_mu - pop_mean) / (pop_std / pow(n, 0.5)))
    p = scipy.stats.norm.sf(abs(z)) * 2

    if out:
        print("z: " + str(z))
        print("p-value: " + str(p))

    accept = 1
    if p > sig_lvl:
        if out:
            print(
                "Alternative hypothesis: the sample mean and population means are NOT equal"
            )
        accept = 0
    else:
        if out:
            print("Null hypothesis: the sample mean and population means are equal")

    con_1 = float(
        samp_mu - scipy.stats.norm.ppf(1 - sig_lvl / 2) * pop_std / pow(n, 0.5)
    )
    con_2 = float(
        samp_mu + scipy.stats.norm.ppf(1 - sig_lvl / 2) * pop_std / pow(n, 0.5)
    )

    if out:
        print(
            str(100 * (1 - sig_lvl))
            + "% confidence interval: "
            + str(con_1)
            + " "
            + str(con_2)
        )
        print("Mean of x: " + str(samp_mu))
        print()

    result = {
        "p_value": p,
        "z_value": z,
        "con_low": con_1,
        "con_up": con_2,
        "sample_mean_1": samp_mu,
        "accept": accept,
    }
    return result


# Input parameters: sample 1 (pd df), sample 2 (pd df), significance level (optional float)
# Return values: p-value, z-value, confidence interval (lower), confidence interval (upper), mean of sample 1, mean of sample 2, reject/accept (1 = accept, 0 = reject)
def z_test_2_samp(x, y, sig_lvl=0.05):

    out = 0

    if out:
        print("2 sample z-test (two tailed)")

    mu_1 = float(x.mean())
    mu_2 = float(y.mean())
    std_1 = float(x.std())
    std_2 = float(y.std())
    n1 = x.shape[0]
    n2 = y.shape[0]

    z = (mu_1 - mu_2) / pow((std_1 ** 2 / n1 + std_2 ** 2 / n2), 0.5)
    p = scipy.stats.norm.sf(abs(z)) * 2

    if out:
        print("z: " + str(z))
        print("p-value: " + str(p))

    accept = 1
    if p > sig_lvl:
        if out:
            print("Alternative hypothesis: the population means are NOT equal")
        accept = 0
    else:
        if out:
            print("Null hypothesis: the population means are equal")

    con_1 = float(
        (mu_1 - mu_2)
        - (
            scipy.stats.norm.ppf((1 - sig_lvl / 2))
            * pow(
                (
                    (((n1 - 1) * std_1 * std_1) + ((n2 - 1) * std_2 * std_2))
                    / (n1 + n2 - 2)
                ),
                0.5,
            )
            * pow((1 / n1 + 1 / n2), 0.5)
        )
    )
    con_2 = float(
        (mu_1 - mu_2)
        + (
            scipy.stats.norm.ppf((1 - sig_lvl / 2))
            * pow(
                (
                    (((n1 - 1) * std_1 * std_1) + ((n2 - 1) * std_2 * std_2))
                    / (n1 + n2 - 2)
                ),
                0.5,
            )
            * pow((1 / n1 + 1 / n2), 0.5)
        )
    )

    if out:
        print(
            str(100 * (1 - sig_lvl))
            + "% confidence interval: "
            + str(con_1)
            + " "
            + str(con_2)
        )
        print("Mean of x and mean of y (respectively): " + str(mu_1) + ", " + str(mu_2))
        print()

    result = {
        "p_value": p,
        "z_value": z,
        "con_low": con_1,
        "con_up": con_2,
        "sample_mean_1": mu_1,
        "sample_mean_2": mu_2,
        "accept": accept,
    }
    return result


# Input parameters: pd df of group categoricals, pd df of corresponding values, significance level (optional)
# Return values: p-value, f-value, variance between, var within, degrees of freedom between, df within, df total, Sum of Squares between, ss within, ss total, accept (1 = accept, 0 = reject)
def one_way_anova(dictionary, sig_lvl=0.05):

    out = 0

    if out:
        print("One way ANOVA")
        
    cat_val = ""
    num_val = ""

    if "cat_NaN_found" in dictionary:
        cat_val = dictionary.pop("cat_NaN_found")
    if 'num_NaN_found' in dictionary:
        num_val = dictionary.pop("num_NaN_found")
    sep_values = [list(value) for key, value in dictionary.items()]
    f, p = f_oneway(*sep_values)

    if out:
        print(f, p)

    unique_groups = pd.DataFrame(list(dictionary.keys()))
    k = unique_groups.shape[0]
    n = sum([len(value) for key, value in dictionary.items()])
    df_between = k - 1
    df_within = n - k
    df_total = n - 1

    grand_mean = sum([item for sublist in sep_values for item in sublist]) / n
    total = 0
    for i in range(len(sep_values)):
        group_mean = 0
        for j in range(len(sep_values[i])):
            group_mean = group_mean + sep_values[i][j]
        group_mean = group_mean / len(sep_values[i])
        total = total + (grand_mean - group_mean) ** 2 * len(sep_values[i])
    total2 = 0
    for i in range(len(sep_values)):
        gm = 0
        for j in range(len(sep_values[i])):
            gm = gm + sep_values[i][j]
        gm = gm / len(sep_values[i])
        for j in range(len(sep_values[i])):
            total2 = total2 + (sep_values[i][j] - gm) ** 2

    ss_between = float(total)
    ss_within = float(total2)
    ss_total = float(total + total2)
    var_between = float(total / df_between)
    var_within = float(total2 / df_within)

    row_headers = ["Sum of Squares", "d.f.", "Variance", "F", "p"]
    col_headers = ["Between Groups", "Within Groups", "Total"]
    data = [
        [
            str("%.2f" % ss_between),
            str("%.0f" % df_between),
            str("%.2f" % var_between),
            str("%.6f" % f),
            str("%.6f" % p),
        ],
        [
            str("%.2f" % ss_within),
            str("%.0f" % df_within),
            str("%.2f" % var_within),
            "--",
            "--",
        ],
        [str("%.2f" % ss_total), str("%.0f" % df_total), "--", "--", "--"],
    ]

    if out:
        print(pd.DataFrame(data, col_headers, row_headers))

    accept = 1
    if p > sig_lvl:
        if out:
            print("Alternative hypothesis: true difference in means is not equal to 0")
        accept = 0
    else:
        if out:
            print("Null hypothesis: true difference in means is equal to 0")

    if out:
        print()

    result = {
        "p_value": p,
        "f_value": f,
        "var_between": var_between,
        "var_within": var_within,
        "df_between": df_between,
        "df_within": df_within,
        "df_total": df_total,
        "ss_between": ss_between,
        "ss_within": ss_within,
        "ss_total": ss_total,
        "accept": accept,
    }
    dictionary["cat_NaN_found"] = cat_val
    dictionary["num_NaN_found"] = num_val
    return result


if __name__ == "__main__":

    ### Testing ###
    x = pd.DataFrame([1, 40, 60, 110])
    y = pd.DataFrame([5, 6, 7, 8])
    groups = pd.DataFrame(["A", "A", "A", "A", "B", "B", "B", "B", "C", "C", "C", "C"])
    values = pd.DataFrame([1, 2, 3, 4, 4, 6, 5, 9, 12, 12, 1, 11])
    dictio = {
        "A": [1.0, 2.0, 3.0, 4.0],
        "B": [4.0, 6.0, 5.0, 9.0],
        "C": [12.0, 12.0, 1.0, 11.0],
        "cat_NaN_found": False,
        "num_NaN_found": False,
    }

    # T tests
    t_test_1_samp(x, 3)
    t_test_2_samp_equal_var(x, y)
    t_test_welch(x, y)

    # Z tests
    z_test_1_samp(x, 50)
    z_test_2_samp(x, y)

    # ANOVA
    print(one_way_anova(dictio))
