import pandas as pd 
def pytest_sessionfinish(session, exitstatus):
	reporter = session.config.pluginmanager.get_plugin('terminalreporter')
	report = {}
	points = {'test_part2_case1': 8, 'test_part2_case2': 12, 'test_part2_case3': 10, 'test_part2_case4': 8, 'test_part2_case5': 12, 'test_part2_extracredit': 5}
	total = 0 
	try:
		for test in reporter.stats['passed']:
			report[test.location[2]+"_status"]=[test.outcome]
			report[test.location[2]+"_points"]=[points[test.location[2]]]
			total+=points[test.location[2]]
	except KeyError:
		pass
	try:
		for test in reporter.stats['failed']:
			report[test.location[2]+"_status"]=[test.outcome]
			report[test.location[2]+"_points"]=[0]
			
	except KeyError:
		pass
	report=pd.DataFrame.from_dict(report)
	report.sort_index(axis=1, inplace=True)
	report['Part2_Total']=[total]
	report.T.to_csv("autograding_report.csv",header=False)
