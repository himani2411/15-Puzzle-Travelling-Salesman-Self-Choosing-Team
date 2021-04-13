import pandas as pd
#For Grading A1
def pytest_sessionfinish(session, exitstatus):
	anum=0
	qnums=1
	casenums=5
	reporter = session.config.pluginmanager.get_plugin('terminalreporter')
	report={}
	points={'test_part1_case1':9,'test_part1_case2':11.5,'test_part1_case4':14, 'test_part1_case5':15.5}
	total=0
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
	report['Part1_Total']=[total]
	report.T.to_csv("autograding_report.csv",header=False)