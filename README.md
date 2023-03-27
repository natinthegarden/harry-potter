# Harry Potter Fanfiction Data Analysis
*Practice Data Analyasis Project*

<img src="https://images.unsplash.com/photo-1551269901-5c5e14c25df7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2669&q=80"  width="60%" height="30%">

I use a **Harry Potter Fanfiction dataset** from Kaggle to practice data analysis. This dataset includes info about all fan written harry potter stories uploaded to the site fanfic.net from 2001-2019.  

I **explore** this data in a jupyter notebook with Pandas, and then **clean** the data. I then **analyze** this data and **create visuals** to go with my analysis!

---

<h3>Summary</h3>

This was a fun student project to get familiar with data cleaning and analysis tools with Python.

- Install the **requirements.txt** to get specific *package install requirements* to pip install pandas, numpy and specific Python version. 

- The **explore_harry.ipynb** can be opened and read to see where I *explored my raw data*. I made choices in this exploration about what cleaning functions would be needed.

- My **cleanharry.py** file contains my *cleaning scripts* where I delete certain columns, split certain columns, remove null values, and remove specific column categories. 

- The **analyze_harry.ipynb** can be opened and read to see where I further analyzed my clean data and made plots using matplotlib.

---

<h3>Project Requirements Included</h3>

- Pandas **read_csv** function to read in the CSV file

- Cleaned data using built-in pandas and numpy functions to remove 0’s and null values, split an existing date column into two columns (for month and year), removed unwanted columns(Last Updated, story links, language, and original mm-yr columns), removed unwanted categories from columns (languages other than english), and saved all changes to a new clean data csv.

- Pandas functions used in both jupyter notebooks
   
     .head(), .columns, .shape, .info(), .isnull().sum().sort_values(ascending=False), .unique(), .value_counts(), .describe(), .groupby, print, 

- Made 2 basic plots with matplotlib

   .plot(kind='bar'), plt.scatter

- Wrote markdown in Jupyter Notebooks explaining process in between all lines of code