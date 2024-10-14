import pandas as pd # type: ignore
import ydata_profiling as pf

from plotnine import ( # type: ignore
    ggplot, aes, geom_point, geom_smooth, labs, theme_xkcd
)


df = pd.read_csv('rockyou-20.txt')
print(df.head())

##PANDAS PROFILING

report = pf.ProfileReport(df)
report.to_file('a.html')

##PLOTLINE BONUS
