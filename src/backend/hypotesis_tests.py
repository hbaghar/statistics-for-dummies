import pandas as pd
import scipy.stats
from scipy import stats
from scipy.stats import f_oneway
import numpy as np

### Doin' Keegan shit over here ###

# Input parameters: sample (pd df), population mean (float), significance level (optional float)
# Return values: p-value, t-value, confidence interval (lower), confidence interval (upper), mean of sample, reject/accept (1 = accept, 0 = reject)
def t_test_1_samp(x, pop_mean, sig_lvl = 0.05):

    print("One Sample t-test")

    samp_mean = float(x.mean())
    samp_sd = float(x.std())
    n = x.shape[0]

    t = float((samp_mean-pop_mean)/(samp_sd/pow(n, 0.5)))
    p = scipy.stats.t.sf(abs(t), df=n-1)*2
    con_1, con_2 = scipy.stats.t.interval(alpha=1-sig_lvl,df=n-1, loc=samp_mean, scale=scipy.stats.sem(x))

    con_1 = float(con_1)
    con_2 = float(con_2)

    print("t = " + str(t))
    print("df = " + str(n-1))
    print("p-value = " + str(p))

    accept = 1
    if(p > sig_lvl):
        print("Alternative hypothesis: true mean is not equal to " + str(pop_mean))
        accept = 0
    else:
        print("Null hypothesis: true mean is equal to " + str(pop_mean))

    print(str(100*(1-sig_lvl)) + "% confidence interval: " + str(con_1) + " " + str(con_2))
    print("Mean of x: " + str(samp_mean))
    print()

    return p, t, con_1, con_2, samp_mean, accept

# Input parameters: sample 1 (pd df), sample 2 (pd df), significance level (optional float)
# Return values: p-value, t-value, confidence interval (lower), confidence interval (upper), mean of sample 1, mean of sample 2, reject/accept (1 = accept, 0 = reject)
def t_test_welch(x, y, sig_lvl=0.05):

    print("Welch Two sample t-test (unequal variance)")

    mu_1 = float(x.mean())
    mu_2 = float(y.mean())
    s1 = x.std()
    s2 = y.std()
    n1 = x.shape[0]
    n2 = y.shape[0]

    t, p = stats.ttest_ind(x,y, equal_var = False)
    t = float(t)
    p = float(p)

    con_1 = float((mu_1-mu_2) - (scipy.stats.t.ppf((1-sig_lvl/2), n1+n2-2)*pow(((((n1-1)*s1*s1)+((n2-1)*s2*s2))/(n1+n2-2)),0.5)*pow((1/n1 + 1/n2),0.5)))
    con_2 = float((mu_1-mu_2) + (scipy.stats.t.ppf((1-sig_lvl/2), n1+n2-2)*pow(((((n1-1)*s1*s1)+((n2-1)*s2*s2))/(n1+n2-2)),0.5)*pow((1/n1 + 1/n2),0.5)))

    print("t = " + str(t))
    print("df = " + str(n1 + n2 - 2))
    print("p-value = " + str(p))

    accept = 1
    if (p > sig_lvl):
        print("Alternative hypothesis: true difference in means is not equal to 0")
        accept = 0
    else:
        print("Null hypothesis: true difference in means is equal to 0")

    print(str(100 * (1 - sig_lvl)) + "% confidence interval: " + str(con_1) + " " + str(con_2))
    print("Mean of x and mean of y (respectively): " + str(mu_1) + ", " + str(mu_2))
    print()

    return p, t, con_1, con_2, mu_1, mu_2, accept

# Input parameters: sample 1 (pd df), sample 2 (pd df), significance level (optional float)
# Return values: p-value, t-value, confidence interval (lower), confidence interval (upper), mean of sample 1, mean of sample 2, reject/accept (1 = accept, 0 = reject)
def t_test_2_samp_equal_var(x, y, sig_lvl=0.05):

    print("Two sample t-test (equal variance)")

    mu_1 = float(x.mean())
    mu_2 = float(y.mean())
    s1 = x.std()
    s2 = y.std()
    n1 = x.shape[0]
    n2 = y.shape[0]

    t = float((mu_1-mu_2)/(pow((s1*s1/n1)+(s2*s2/n2),0.5)))

    p = scipy.stats.t.sf(abs(t), df=n1+n2-2)*2
    con_1 = float((mu_1-mu_2) - (scipy.stats.t.ppf((1-sig_lvl/2), n1+n2-2)*pow(((((n1-1)*s1*s1)+((n2-1)*s2*s2))/(n1+n2-2)),0.5)*pow((1/n1 + 1/n2),0.5)))
    con_2 = float((mu_1-mu_2) + (scipy.stats.t.ppf((1-sig_lvl/2), n1+n2-2)*pow(((((n1-1)*s1*s1)+((n2-1)*s2*s2))/(n1+n2-2)),0.5)*pow((1/n1 + 1/n2),0.5)))

    print("t = " + str(t))
    print("df = " + str(n1 + n2 - 2))
    print("p-value = " + str(p))

    accept = 1
    if (p > sig_lvl):
        print("Alternative hypothesis: true difference in means is not equal to 0")
        accept = 0
    else:
        print("Null hypothesis: true difference in means is equal to 0")

    print(str(100 * (1 - sig_lvl)) + "% confidence interval: " + str(con_1) + " " + str(con_2))
    print("Mean of x and mean of y (respectively): " + str(mu_1) + ", " + str(mu_2))
    print()

    return p, t, con_1, con_2, mu_1, mu_2, accept

# Input parameters: sample (pd df), population mean (float), significance level (optional float)
# Return values: p-value, z-value, confidence interval (lower), confidence interval (upper), mean of sample, reject/accept (1 = accept, 0 = reject)
def z_test_1_samp(x, pop_mean, sig_lvl=0.05):

    print("1 sample z-test (two-tailed)")

    samp_mu = float(x.mean())
    pop_std = float(x.std())
    n = float(x.shape[0])

    z = float((samp_mu-pop_mean)/(pop_std/pow(n,0.5)))
    p = scipy.stats.norm.sf(abs(z))*2

    print("z: " + str(z))
    print("p-value: " + str(p))

    accept = 1
    if (p > sig_lvl):
        print("Alternative hypothesis: the sample mean and population means are NOT equal")
        accept = 0
    else:
        print("Null hypothesis: the sample mean and population means are equal")

    con_1 = float(samp_mu - scipy.stats.norm.ppf(1-sig_lvl/2) * pop_std/pow(n,0.5))
    con_2 = float(samp_mu + scipy.stats.norm.ppf(1-sig_lvl/2) * pop_std / pow(n, 0.5))

    print(str(100 * (1 - sig_lvl)) + "% confidence interval: " + str(con_1) + " " + str(con_2))
    print("Mean of x: " + str(samp_mu))
    print()

    return p, z, con_1, con_2, samp_mu, accept

# Input parameters: sample 1 (pd df), sample 2 (pd df), significance level (optional float)
# Return values: p-value, z-value, confidence interval (lower), confidence interval (upper), mean of sample 1, mean of sample 2, reject/accept (1 = accept, 0 = reject)
def z_test_2_samp(x,y, sig_lvl=0.05):

    print("2 sample z-test (two tailed)")

    mu_1 = float(x.mean())
    mu_2 = float(y.mean())
    std_1 = float(x.std())
    std_2 = float(y.std())
    n1 = x.shape[0]
    n2 = y.shape[0]

    z = (mu_1-mu_2)/pow((std_1**2/n1 + std_2**2/n2),0.5)
    p = scipy.stats.norm.sf(abs(z)) * 2

    print("z: " + str(z))
    print("p-value: " + str(p))

    accept = 1
    if (p > sig_lvl):
        print("Alternative hypothesis: the population means are NOT equal")
        accept = 0
    else:
        print("Null hypothesis: the population means are equal")

    con_1 = float((mu_1 - mu_2) - (scipy.stats.norm.ppf((1 - sig_lvl / 2)) * pow(((((n1 - 1) * std_1 * std_1) + ((n2 - 1) * std_2 * std_2)) / (n1 + n2 - 2)), 0.5) * pow((1 / n1 + 1 / n2), 0.5)))
    con_2 = float((mu_1 - mu_2) + (scipy.stats.norm.ppf((1 - sig_lvl / 2)) * pow(((((n1 - 1) * std_1 * std_1) + ((n2 - 1) * std_2 * std_2)) / (n1 + n2 - 2)), 0.5) * pow((1 / n1 + 1 / n2), 0.5)))

    print(str(100 * (1 - sig_lvl)) + "% confidence interval: " + str(con_1) + " " + str(con_2))
    print("Mean of x and mean of y (respectively): " + str(mu_1) + ", " + str(mu_2))
    print()

    return p, z, con_1, con_2, mu_1, mu_2, accept

# Input parameters: pd df of group categoricals, pd df of corresponding values, significance level (optional)
# Return values: p-value, f-value, variance between, var within, degrees of freedom between, df within, df total, Sum of Squares between, ss within, ss total, accept (1 = accept, 0 = reject)
def one_way_anova(groups, values, sig_lvl=0.05):

    print("One way ANOVA")

    unique_groups = list(np.unique(groups))
    unique_groups = pd.DataFrame(unique_groups)

    sep_values = []
    for i in range(int(groups.nunique())):
        method_values = []
        for j in range(len(groups)):
            if unique_groups.iloc[i].equals(groups.iloc[j]):
                method_values.append(float(values.iloc[j]))
        sep_values.append(method_values)

    f, p = f_oneway(*sep_values)

    k = unique_groups.shape[0]
    n = groups.shape[0]

    df_between = k - 1
    df_within = n - k
    df_total = n - 1

    grand_mean = values.mean()
    total = 0
    for i in range(len(sep_values)):
        group_mean = 0
        for j in range(len(sep_values[i])):
            group_mean = group_mean + sep_values[i][j]
        group_mean = group_mean/len(sep_values[i])
        total = total + (grand_mean-group_mean)**2*len(sep_values[i])

    total2 = 0
    for i in range(len(sep_values)):
        gm = 0
        for j in range(len(sep_values[i])):
            gm = gm + sep_values[i][j]
        gm = gm/len(sep_values[i])

        for j in range(len(sep_values[i])):
            total2 = total2 + (sep_values[i][j] - gm)**2

    ss_between = float(total)
    ss_within = float(total2)
    ss_total = float(total+total2)
    var_between = float(total/df_between)
    var_within = float(total2/df_within)

    row_headers = ["Sum of Squares", "d.f.", "Variance", "F", "p"]
    col_headers = ["Between Groups", "Within Groups", "Total"]
    data = [[str("%.2f" % ss_between), str("%.0f" % df_between), str("%.2f" % var_between), str("%.6f" % f), str("%.6f" % p)], [str("%.2f" % ss_within), str("%.0f" % df_within), str("%.2f" % var_within), "--", "--"],[str("%.2f" % ss_total), str("%.0f" % df_total), "--", "--", "--"]]

    print(pd.DataFrame(data, col_headers, row_headers))

    accept = 1
    if (p > sig_lvl):
        print("Alternative hypothesis: true difference in means is not equal to 0")
        accept = 0
    else:
        print("Null hypothesis: true difference in means is equal to 0")
    print()

    return p, f, var_between, var_within, df_between, df_within, df_total, ss_between, ss_within, ss_total, accept

if __name__ == "__main__":

    ### Testing ###
    x = pd.DataFrame([1, 40, 60, 110])
    y = pd.DataFrame([5, 6, 7, 8])
    groups = pd.DataFrame(["A","A","A","A","B","B","B","B","C","C","C","C"])
    values = pd.DataFrame([1,2,3,4,4,6,5,9,12,12,1,11])

    # T tests
    t_test_1_samp(x, 3)
    t_test_2_samp_equal_var(x, y)
    t_test_welch(x,y)

    # Z tests
    z_test_1_samp(x,50)
    z_test_2_samp(x,y)

    # ANOVA
    one_way_anova(groups,values)