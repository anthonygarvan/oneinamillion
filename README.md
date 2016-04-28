# One in a Million

#### A census-powered quiz for exploring your uniqueness

This is an online quiz powered by 2009-2013 [American Community Survey (ACS)](https://www.census.gov/programs-surveys/acs/) provided by the U.S. Census.
Users are guided through a series of question, and after each question they are told how unique they are
(1 in 200, 1 in 10,000, etc.)

### Method

The code uses a simple methodology: it counts the number of occurrences of a particular combination of demographic parameters in the PUMS data set, which contains anonymized individual-level data. The only caveat I have is that I ignore individuals who did not have complete information (in practice, this only occurred when the job field, `SOCP12`, was blank). This reduces the sample size from about 15 million to about 9 million. 

America is a very diverse place. In fact, by only the simple demographics contained in this survey (sex, race, hispanic origin, education, state, and employment), over 13.6% of Americans are "one in a million."

### Running the code on mac. 
```bash
$ brew update
$ brew install p7zip
$ sh initialize.sh
$ python process/get_codes.py
$ python process/get_counts.py
```

Then serve with your favorite static file server (I use node `http-server`). 