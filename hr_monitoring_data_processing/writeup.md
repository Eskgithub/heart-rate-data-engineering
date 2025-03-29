## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[Missing data or "NO DATA" means the heart rate wasn’t recorded, possibly due to the user not wearing the sensor, body movement, sensor issues, transmission errors, or poor signal quality. Filtering these out risks bias, gaps in trends, interference with real heart rate fluctuations, or missing key events like exercise.]

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

[Phase 0 (Blue) shows relatively low heart rate values and less fluctuation, which could indicate sleep.
Phase 1 (Orange) & Phase 2 (Green) have higher and more fluctuating heart rates, likely indicating activity.
Phase 3 (Red) starts with low HR but later spikes, possibly transitioning from rest to activity. Given that sleep is expected to have the lowest maximum HR, Phase 0 (Blue) is the most likely sleep phase. This aligns with the previously calculated stats (avg = 4.0, max = 7.0, stddev = 2.0), showing a lower HR trend compared to other phases.]

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

[Phase 2 shows the highest heart rate, around 120 bpm (per 60 minutes), with a max heart rate of 7.0, significantly higher than the average of 4.0. The graph of Phase 2 is consistently above the others, except for a brief spike at 110 bpm in Phase 1. These indicators suggest that Phase 2 corresponds to the exercise period, where the highest heart rate was recorded.]

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

[Phase 3 graph shows a lower heart rate compared to other phases. The standard deviation also spikes, particularly towards the end of the graph, where the heart rate fluctuates between 100 and 80 bpm.]
