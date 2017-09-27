import problems_by_url
import problem_to_pdf

problems_list = []
debug = problems_by_url.debug
for start in xrange(0, 101, 50):
    url = "http://www.spoj.com/problems/classical/sort=0,start=%d" % start
    debug("fetching problems for start=%d" % start)
    cur_problems_list = problems_by_url.problems_list(url)
    problems_list.extend(cur_problems_list)

for problem in problems_list:
    debug("Writing pdf for %s" % problem.name)
    problem_to_pdf.convert(problem)
