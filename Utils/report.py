# utils/report.py

import datetime
from Config import config

def generate_html_report(test_results):
    report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(config.REPORT_PATH, 'w') as f:
        f.write('<html><head><title>Automation Test Report</title></head>')
        f.write('<body>')
        f.write('<h1>Automation Test Report</h1>')
        f.write(f'<p>Report generated on: {report_date}</p>')
        f.write('<h2>Test Results:</h2>')
        f.write('<table border="1">')
        f.write('<tr><th>Test Case</th><th>Result</th></tr>')
        for test, result in test_results.items():
            f.write(f'<tr><td>{test}</td><td>{result}</td></tr>')
        f.write('</table>')
        f.write('</body></html>')
