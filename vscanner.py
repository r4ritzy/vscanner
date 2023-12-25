import scanner

target_url = "http://URLsToScan"
links_to_ignore = ["http://URLsToIgnore"]

data_dict = {"username": "admin", "password": "password", "Login": "submit"} #change as per the details and requirement

vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("LoginURL(or wherever you need a consistent session", data=data_dict)

vuln_scanner.crawl()
vuln_scanner.run_scanner()
