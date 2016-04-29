# One in a Million

#### An online quiz, powered by the U.S. Census

This is an online quiz powered by 2009-2013 [American Community Survey (ACS)](https://www.census.gov/programs-surveys/acs/) provided by the U.S. Census Bureau.
Users are guided through a series of questions, and after each question they are told how unique they are
(1 in 200, 1 in 10,000, etc.)

### Method

The code uses a simple methodology: it counts the number of occurrences of a particular combination of demographic parameters in the PUMS data set, which contains anonymized individual-level data. The only caveat I have is that I ignore individuals who did not have complete information (in practice, this only occurred when the job field, `SOCP12`, was blank). This reduces the sample size from about 15 million to about 9 million. 

America is a very diverse place. In fact, by only the simple demographics contained in this survey (sex, race, hispanic origin, education, state, and employment), 13.6% of Americans are "one in a million."

### Running the code on MacOS
Requirements: 
- nodejs
- python3.x

Then run:
```bash
$ brew update
$ brew install p7zip
$ sh initialize.sh
$ python process/get_codes.py
$ python process/get_counts.py
```

Then serve with your favorite static file server (I use node's `http-server`). 

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.