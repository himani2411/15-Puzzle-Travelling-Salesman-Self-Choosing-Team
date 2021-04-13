# A1 Part 2
# !/usr/bin/env python3
import route
from subprocess import TimeoutExpired, CalledProcessError
import pytest

def validate_route(answer, args):
    arg_start, arg_end, arg_cost = args
    assert isinstance(answer, dict), "get_route() is not returning a dictionary"
    assert len(answer) == 5, "Too few parts: returned dictionary should have 5 keys"

    segments, miles = answer['total-segments'], answer['total-miles']
    hours, safe, route_taken = answer['total-hours'], answer['total-expected-accidents'], answer['route-taken']

    assert isinstance(segments, int), '"%s" is not an int: total-segments must be int' % segments
    assert segments >= 0, '"%s" < 0: total-segments must be positive' % segments
    assert isinstance(miles, float), '"%s" is not an int: total-miles must be float' % miles
    assert miles >= 0, '"%s" < 0: total-miles must be positive' % miles
    assert isinstance(hours, float), '"%s" is not an int: total-hours must be int' % hours
    assert hours >= 0, '"%s" < 0: total-hours must be positive' % hours
    assert isinstance(safe, float), '"%s" is not an float: Any probability must be float' % safe
    assert safe >= 0, '"%s" < 0: Probability of an accident must be positive' % safe
    assert len(route_taken) == segments, 'Route taken does not correspond to total number of segments'
    # assert route_taken[0][0] == arg_start, '"%s" is not "%s": start-city is wrong' % (route_taken[0][0], arg_start)
    assert route_taken[segments - 1][0] == arg_end, '"%s" is not "%s" not the end-city' % (route_taken[segments - 1][0], arg_end)
    return segments, miles, hours, safe

t = 600
@pytest.mark.timeout(t)
def test_part2_case1():
    script_path = 'route.py'
    for script_args in [('Bloomington,_Indiana', 'Indianapolis,_Indiana', x) for x in
                        ('distance', 'segments', 'time', 'safe')]:
        print("Testing ./%s %s" % (script_path, ' '.join(script_args)))
        output = route.get_route(*script_args)
        assert isinstance(output, dict), "get_route() is not returning a dictionary"
        
        optimal_ans, calculated = {"segments": 3, "distance": 51.0, "time": 1.07949,"safe": 0.000102}, {}
        calculated['segments'], calculated['distance'], calculated['time'], calculated['safe'] = validate_route(output, script_args)
        upper = optimal_ans[script_args[2]] + optimal_ans[script_args[2]]*0.1
        #lower = optimal_ans[script_args[2]] - optimal_ans[script_args[2]]*0.1
        print(script_args[2],  optimal_ans[script_args[2]], calculated[script_args[2]])
        assert calculated[script_args[2]] <= upper, 'Output format is correct but out of range'
        #assert calculated[script_args[2]] <= optimal_ans[script_args[2]],'Output format is correct but optimal %s cost is %s' % (script_args[2], optimal_ans[script_args[2]])

@pytest.mark.timeout(t)
def test_part2_case2():
    script_path = 'route.py'
    for script_args in [('Buffalo,_New_York', 'Westfield,_New_York', x) for x in
                        ('distance', 'segments', 'time', 'safe')]:
        print("Testing ./%s %s" % (script_path, ' '.join(script_args)))

        output = route.get_route(*script_args)
        assert isinstance(output, dict), "get_route() is not returning a dictionary"
        
        optimal_ans, calculated = {"segments": 4, "distance": 80.0, "time": 1.32649,"safe": 0.000094}, {}
        calculated['segments'], calculated['distance'], calculated['time'], calculated['safe'] = validate_route(output, script_args)
        upper = optimal_ans[script_args[2]] + optimal_ans[script_args[2]]*0.1
        #lower = optimal_ans[script_args[2]] - optimal_ans[script_args[2]]*0.1
        assert calculated[script_args[2]] <= upper, 'Output format is correct but out of range'
        #assert calculated[script_args[2]] <= optimal_ans[script_args[2]],'Output format is correct but optimal %s cost is %s' % (script_args[2], optimal_ans[script_args[2]])

@pytest.mark.timeout(t)
def test_part2_case3():
    script_path = 'route.py'
    for script_args in [('Mountain_View,_California', 'Watsonville,_California', x) for x in
                        ('distance', 'segments', 'time', 'safe')]:
        print("Testing ./%s %s" % (script_path, ' '.join(script_args)))
        output = route.get_route(*script_args)
        assert isinstance(output, dict), "get_route() is not returning a dictionary"
       
        optimal_ans, calculated = {"segments": 6, "distance": 61.0, "time": 1.131119,"safe": 0.000114}, {}
        calculated['segments'], calculated['distance'], calculated['time'], calculated['safe'] = validate_route(output, script_args)
        upper = optimal_ans[script_args[2]] + optimal_ans[script_args[2]]*0.1
        #lower = optimal_ans[script_args[2]] - optimal_ans[script_args[2]]*0.1
        assert calculated[script_args[2]] <= upper, 'Output format is correct but out of range'
        #assert calculated[script_args[2]] <= optimal_ans[script_args[2]],'Output format is correct but optimal %s cost is %s' % (script_args[2], optimal_ans[script_args[2]])

@pytest.mark.timeout(t)
def test_part2_case4():
    script_path = 'route.py'
    for script_args in [('New_Castle,_Pennsylvania', 'Kittanning,_Pennsylvania', x) for x in
                        ('distance', 'segments', 'time', 'safe')]:
        print("Testing ./%s %s" % (script_path, ' '.join(script_args)))
        output = route.get_route(*script_args)
        assert isinstance(output, dict), "get_route() is not returning a dictionary"
        
        optimal_ans, calculated = {"segments": 3, "distance": 69.0, "time": 1.419658,"safe": 0.000138}, {}
        calculated['segments'], calculated['distance'], calculated['time'], calculated['safe'] = validate_route(output, script_args)
        upper = optimal_ans[script_args[2]] + optimal_ans[script_args[2]]*0.1
        #lower = optimal_ans[script_args[2]] - optimal_ans[script_args[2]]*0.1
        assert calculated[script_args[2]] <= upper, 'Output format is correct but out of range'
        #assert calculated[script_args[2]] <= optimal_ans[script_args[2]],'Output format is correct but optimal %s cost is %s' % (script_args[2], optimal_ans[script_args[2]])

@pytest.mark.timeout(t)
def test_part2_case5():
    script_path = 'route.py'
    for script_args in [('Shamrock,_Texas', 'Jacksboro,_Texas', x) for x in
                        ('distance', 'segments', 'time', 'safe')]:
        print("Testing ./%s %s" % (script_path, ' '.join(script_args)))
        output = route.get_route(*script_args)
        assert isinstance(output, dict), "get_route() is not returning a dictionary"
        
        optimal_ans, calculated = {"segments": 6, "distance": 246.0, "time": 5.000777,"safe": 0.000454}, {}
        calculated['segments'], calculated['distance'], calculated['time'], calculated['safe'] = validate_route(output, script_args)
        upper = optimal_ans[script_args[2]] + optimal_ans[script_args[2]]*0.2
        #lower = optimal_ans[script_args[2]] - optimal_ans[script_args[2]]*0.1
        assert calculated[script_args[2]] <= upper, 'Output format is correct but out of range'
        #assert calculated[script_args[2]] <= optimal_ans[script_args[2]],'Output format is correct but optimal %s cost is %s' % (script_args[2], optimal_ans[script_args[2]])

@pytest.mark.timeout(t)
def test_part2_extracredit():
    script_path = 'route.py'
    script_args = ('Portland,_Maine', 'Helena,_Montana', 'statetour')
    print("Testing ./%s %s" % (script_path, ' '.join(script_args)))
    output = route.get_route(*script_args)
    assert isinstance(output, dict), "statetour not attempted"
    
    optimal_ans, calculated = {"segments": 48, "distance": 6813.0, "time": 124.0}, {}
    calculated['segments'], calculated['distance'], calculated['time'], calculated['safe'] = validate_route(output, script_args)
    upper = optimal_ans['distance'] + optimal_ans['distance']*0.1
    assert calculated['distance'] <= upper, 'Output format is correct for statetour but out of chosen range'
    