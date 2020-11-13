import os
from datetime import datetime
from pytz import timezone
from crawling_covid19 import parsing_beautifulsoup, extract_dailyCovid_data
from github_utils import get_github_repo, upload_github_issue
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    access_token = os.environ['COVID_ACTION_TOKEN']
    repository_name = "github-action-study-cho512"

    tokyo_timezone = timezone('Asia/Tokyo')
    today = datetime.now(tokyo_timezone)
    today_data = today.strftime("%Y年%m月%d日 %H:%M")

    covid19_in_japan_url = "https://www3.nhk.or.jp/news/special/coronavirus/data/latest-pref-data.json"
    covid19Data = parsing_beautifulsoup(covid19_in_japan_url)
    if ("lastmodifed" in covid19Data): today_data = "lastest update time : "+today.strftime("%Y年")+covid19Data["lastmodifed"]

    issue_title = f"Covid19 information in Japan ( {today_data} )"

    upload_contents = extract_dailyCovid_data(covid19Data)

    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, issue_title, upload_contents)
    print("Upload Github Issue Success!")