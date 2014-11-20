from unittest.mock import patch
from cm_history_log.log_as_of_date import log_as_of
import pandas as pd
from datetime import datetime

def test_one_cm_per_row():
	sample_file = pd.DataFrame({'Person Id':[1,1,2]})
	with patch('pandas.read_excel',return_value=sample_file):
		df = log_as_of('2014-01-01')
	assert df.set_index('Person Id').index.is_unique

def test_take_last_record():
	sample_file = pd.DataFrame({'Person Id':[1,1,2],'is_last':[False,True,True]})
	with patch('pandas.read_excel',return_value=sample_file):
		df = log_as_of('2014-01-01')
	assert df.is_last.all()

def test_return_most_recent_record_before_date():
	sample_file = pd.DataFrame({'Person Id':[1,1,2],
		'CM History Record Create Time':[datetime(2013,1,1),datetime(2014,5,1),datetime(2013,1,1)]})
	with patch('pandas.read_excel',return_value=sample_file):
		df = log_as_of('2014-01-01')
	assert (df['CM History Record Create Time'] <= datetime(2014,1,1)).all()