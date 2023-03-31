# Harry Potter Fanfiction Data Analysis
*Practice Data Analyasis Project*

<img src="https://images.unsplash.com/photo-1551269901-5c5e14c25df7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2669&q=80"  width="60%" height="30%">

I use a **Harry Potter Fanfiction dataset** from Kaggle to practice data analysis. This dataset includes info about all fan written harry potter stories uploaded to the site fanfic.net from 2001-2019.  

*dataset link:* https://www.kaggle.com/datasets/nehatiwari03/harry-potter-fanfiction-data?resource=download

I **explore** this data in a jupyter notebook with Pandas, and then **clean** the data. I then **analyze** this data and **create visuals** to go with my analysis!

---

<h3>Instructions</h3>


- Fork the repo to your gihub account
- Clone the fork of the repo to your computer
- Create a virtual environment and activate it
- Install the **requirements.txt** to get specific *package install requirements* to pip install pandas, numpy and specific Python version. 
- download the dataset from Kaggle to your computer and then place it into your Harry Potter code repo (link:* https://www.kaggle.com/datasets/nehatiwari03/harry-potter-fanfiction-data?resource=download)

---

<h3>Summary</h3>

This was a fun student project to get familiar with data cleaning and analysis tools with Python.

- The **explore_harry.ipynb** can be opened and read to see where I *explored my raw data*. I made choices in this exploration about what cleaning functions would be needed.

- My **cleanharry.py** file contains my *cleaning scripts* where I delete certain columns, split certain columns, remove null values, reformat, and remove specific column categories. 

- The **analyze_harry.ipynb** can be opened and read to see where I further analyzed my clean data and made plots using matplotlib.

---

<h3>Project Requirements Included</h3>

- Pandas **read_csv** function to read in the CSV file

- **Cleaned data** using built-in pandas and numpy functions to: 
   - remove 0’s and null values
   - split an existing date column into two columns (for month and year)
   - removed unwanted columns(Last Updated, story links, language, and original mm-yr columns)
   - removed unwanted categories from columns (languages other than english)
   - changed Month Published column from listing months as numbers to listing months as words (12-> december)
   - made a new column to sort list items alphabetically to remove issues of different orderings counting as different values ('pairing sorted' removed issue of 'ron,harry' and 'harry,ron' counting as different)
   - saved all changes to a new clean data csv.

- **Pandas functions** used in both **explore_harry** and **analyze_harry** jupyter notebooks
   
     .head(), .columns(), .shape(), .info(), .isnull(), .sum(), .sort_values(), .unique(), .value_counts(), .describe(), .groupby(), print(), int(), .iloc, .median, split(), .join(), lambda

- Made **basic plots with matplotlib**. A scatter plot, bar graph, and pie chart.

   .plot(kind='bar'), plt.scatter, ax.pie

- Wrote **markdown in Jupyter Notebooks** explaining process and findings in between all lines of code