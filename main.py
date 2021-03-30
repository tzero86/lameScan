from libs import menu
from libs import vulnScan

# lame = lameScanner.LameScan()
# lame.new_run()
# menu = menu.ConfigMenu()

#  just a test
# menu.print_options()
#pprint(lame.scan_results, indent=1, sort_dicts=False)



vuln = vulnScan.VulnScanner()

vuln.new_scan()
