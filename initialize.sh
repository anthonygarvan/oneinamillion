mkdir -p data/raw
mkdir data/codes
mkdir -p data/stats
wget -O data/raw/codes_windows.txt http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2010-2014.txt
iconv -f WINDOWS-1252 -t UTF-8 data/raw/codes_windows.txt > data/raw/codes.txt
rm data/raw/codes_windows.txt
wget -O data/raw/pums.zip http://www2.census.gov/acs2009_5yr/pums/csv_pus.zip
unzip -d ./data/raw data/raw/pums.zip
echo copying part a
cp data/raw/ss09pusa.csv data/raw/pums.csv
echo adding part b
tail +1 data/raw/ss09pusb.csv >> data/raw/pums.csv
echo adding part c
tail +1 data/raw/ss09pusc.csv >> data/raw/pums.csv
echo adding part d
tail +1 data/raw/ss09pusd.csv >> data/raw/pums.csv
echo finished compiling data.
npm install
echo done.