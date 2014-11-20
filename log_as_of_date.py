import sys
from datetime import datetime
import pandas as pd

def log_as_of(date_string):
	input_date = datetime.strptime(date_string,"%Y-%m-%d")
	df = pd.read_excel('cm_history_log.xlsx',0)
	if 'CM History Record Create Time' in df.columns:
		df = df.ix[df['CM History Record Create Time'] <= input_date]
	df.drop_duplicates(subset='Person Id',inplace=True,take_last=True)
	return df

if __name__ == '__main__':
	input_date = sys.argv[1]
	log_as_of(input_date).to_excel('cm_records_as_of_' + str(input_date) + '.xlsx',index=False)