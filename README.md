# translate_mattermost_i18n
This program to batch modify the translation file of mattermost's i18n file


useage:


* Prepare a json file containing the mattermost target i18n variable to be changed.


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

* Prepare json files for i18n of mattermost 

Prepare json and python files in the same location.


ex) de.json, en.json, es.json, fr.json, ja.json, ko.json, nl.json, pt-BR.json, ru.json, zh_CN.json, zh_TW.json

* Edit a line of function for output_translate on translate_i18n.py .
* Required parameters are two - <locale>.json and locale list
```python
text_define()
output_translate(output_i18n.get('ko'),ko) // translate for ko.json file 
output_translate(output_i18n.get('de'),de) // translate for de.json file
```


