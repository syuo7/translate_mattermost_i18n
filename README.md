# translate_mattermost_i18n
This program to batch modify the translation file of mattermost's i18n file
d
useaged:
Prepare a json file containing the mattermost target i18n variable to be changed.
ex)
```
{
	"about.close":
		{
			"ko" : "창 닫기",
			"ja" : "dskk",
			"default" :"close about",
			"de" : "close fafafaafaㄴsadsa"
		},
	"about.version" :
		{
			"ko" : "버전정보입니당 !!",
			"default" : "default정보 입니다."		
		},
	"activity_log.logout" :
		{
			"ko" : "로그아웃 !!!!",
			"default" : "logout_test"
		}
}
```
