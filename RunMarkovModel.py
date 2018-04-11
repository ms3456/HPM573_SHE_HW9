import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)


# simulate the cohort
simOutputs = cohort.simulate()


# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve without anticoagulation',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )


# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_strokes(),
    title='Number of strokes without anticoagulation',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)



# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'Without anticoagulation:')



print('Mean number of stroke without anticoagulation:',simOutputs.get_mean_strokes())

cohortTm=MarkovCls.Cohort(id=0, therapy=P.Therapies.COMBO)

simOutputsTm=cohortTm.simulate()

PathCls.graph_sample_path(
    sample_path=simOutputsTm.get_survival_curve(),
    title='Survival curve with anticoagulation',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

Figs.graph_histogram(
    data=simOutputsTm.get_strokes(),
    title='Number of strokes with anticoagulation',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1)
SupportMarkov.print_outcomes(simOutputsTm, ' With anticoagulation:')

print('Mean number of stroke with anticoagulation:',simOutputsTm.get_mean_strokes())
