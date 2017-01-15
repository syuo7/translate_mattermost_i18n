import simplejson as json
import os
import codecs

arr_key=[]

de=[]
en=[]
es=[]
fr=[]
ja=[]
ko=[]
nl=[]
pt_BR=[]
ru=[]
zh_CN=[]
zh_TW=[]
json_count=11

in_text='translate_text.json'
output_i18n={'de':'de.json','en':'en.json','es':'es.json','fr':'fr.json','ja':'ja.json','ko':'ko.json','nl':'nl.json','pt_BR':'pt-BR.json','ru':'ru.json','zh_CN':'zh_CN.json','zh_TW':'zh_TW.json'}

def text_define():
	with codecs.open(in_text,'r','utf-8') as f:
		temp=[]
		data=json.load(f)
		for key in data.keys():
			if 'default' not in data[key]:
				print(key,"의 default 값이 없습니다. 다시 작성해주세요.")
				continue
			arr_key.append(key)
			for k in output_i18n.keys():
				if k in data[key]:
					temp.append(data[key][k])
				else:
					temp.append(data[key]['default'])
		for s in range(len(arr_key)):
			de.append(temp[s*json_count])
			en.append(temp[s*json_count+1])
			es.append(temp[s*json_count+2])
			fr.append(temp[s*json_count+3])
			ja.append(temp[s*json_count+4])
			ko.append(temp[s*json_count+5])
			nl.append(temp[s*json_count+6])
			pt_BR.append(temp[s*json_count+7])
			ru.append(temp[s*json_count+8])
			zh_CN.append(temp[s*json_count+9])
			zh_TW.append(temp[s*json_count+10])

def output_translate(json_file,locale):
	with codecs.open(json_file,'r','utf-8') as f:	
		i=0
		c=0
		json_data=json.load(f)
		for line in json_data:
			for i in range(len(arr_key)):
				if(line==arr_key[i]):
					json_data[line]=locale[c]
					c=c+1
	with codecs.open(json_file,'w','utf-8') as f:
		json.dump(json_data,f,indent=4,ensure_ascii=False,encoding="utf-8")

text_define()
output_translate(output_i18n.get('ko'),ko) 
output_translate(output_i18n.get('de'),de)		