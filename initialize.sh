mkdir -p data/raw
mkdir data/codes
mkdir -p data/stats
wget -O data/raw/codes_windows.txt http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2010-2014.txt
iconv -f WINDOWS-1252 -t UTF-8 data/raw/codes_windows.txt > data/raw/codes.txt
rm data/raw/codes_windows.txt
wget -O data/raw/pums.zip http://www2.census.gov/acs2013_5yr/pums/csv_pus.zip
7z x -o ./data/raw data/raw/pums.zip
echo copying part a
cp data/raw/ss13pusa.csv data/raw/pums.csv
echo adding part b
tail +1 data/raw/ss13pusb.csv >> data/raw/pums.csv
echo adding part c
tail +1 data/raw/ss13pusc.csv >> data/raw/pums.csv
echo adding part d
tail +1 data/raw/ss13pusd.csv >> data/raw/pums.csv
echo finished compiling data.
npm install
echo done.