# translate_mattermost_i18n
This program to batch modify the translation file of mattermost's i18n file


useage:
Prepare a json file containing the mattermost target i18n variable to be changed.


ex)
```
{
	"about.close":
		{
			"ko" : "창 닫기",
			"ja" : "ウィンドウを閉じる",
			"default" :"close the about",
		},
	"about.version" :
		{
			"ko" : "버전정보"			
			"de" : "Versionen"
			"default" : "version"		
		},
	"activity_log.logout" :
		{
			"ko" : "로그아웃",
			"default" : "logout"
		}
}
```
