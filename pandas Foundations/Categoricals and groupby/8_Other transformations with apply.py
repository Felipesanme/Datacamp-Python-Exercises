# In this exercise, you're going to analyze economic disparity within regions of the world using the Gapminder data set for 2010. To do this you'll define a function to compute the aggregate spread of per capita GDP in each region and the individual country's z-score of the regional per capita GDP. You'll then select three countries - United States, Great Britain and China - to see a summary of the regional GDP and that country's z-score against the regional mean. The 2010 Gapminder DataFrame is provided for you as gapminder_2010. Pandas has been imported as pd. The following function has been defined for your use:
# # def disparity(gr):
#     # Compute the spread of gr['gdp']: s
#     s = gr['gdp'].max() - gr['gdp'].min()
#     # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
#     z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
#     # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
#     return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})

# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China']])
