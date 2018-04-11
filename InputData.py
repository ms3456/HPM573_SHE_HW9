# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1       # years

COMBO_RR = 0.65
COMBO_DEATH=1.05
# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,    0,    0.1],   # CD4_200to500
    [0,     0,    1,    0],   # CD4_200
    [0,     0.25,      0.55,   0.2],   # AIDS
    [0,0,0,1]]

TRANS_MATRIX_COMBO=[
[0.75,  0.15,    0,    0.1],   # CD4_200to500
    [0,     0,    1,    0],   # CD4_200
    [0,     0.1625,      0.701,   0.1365],   # AIDS
]
# annual cost of each health state
ANNUAL_STATE_COST = [
    2756.0,   # CD4_200to500
    3025.0,   # CD4_200
    9007.0    # AIDS
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    0.75,   # CD4_200to500
    0.50,   # CD4_200
    0.25    # AIDS
    ]

# annual drug costs
Zidovudine_COST = 2278.0
Lamivudine_COST = 2086.0

# treatment relative risk
TREATMENT_RR = 0.509