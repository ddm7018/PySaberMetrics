import pandas as pd
import numpy as np

class League():
	def __init__(self,league_df):
		self.league_df = league_df

	#calculate best exponent to use for Pythagorean W-L calculcation 
	def calculatePyWinLoss(self):
		mad_exp_dict = {'best_exp':0, 'best_mad':1}
		for exp in np.arange(1, 4.5, 0.1):
			run_exp = self.league_df['R']**(exp)
			run_allowed = self.league_df['RA']**(exp)
			absolute_errors = abs(self.league_df['W-L%'] - (run_exp/(run_exp+run_allowed)))
			if mad_exp_dict['best_mad'] > absolute_errors.mean():
				mad_exp_dict['best_mad'] = absolute_errors.mean()
				mad_exp_dict['best_exp'] = exp
		print("Lowest Mad Value " + str(mad_exp_dict['best_mad']) + " with exponent value of " + str(mad_exp_dict['best_exp']))
		


league = League(league_df = pd.read_csv("al_east_2018.csv"))
league.calculatePyWinLoss()
