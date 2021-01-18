from openpyxl import load_workbook
import math
date = input()
시트 = load_workbook("아파트(매매)_실거래가_%s.xlsx"%(date), data_only=True)['아파트 매매 실거래가'];

행정구역={}
import csv
f = open('행정구역.csv','r',  encoding='UTF8')
rdr = csv.reader(f)
i=0;
for row in rdr:
    i+=1
    if not i-1: continue
    #print(row)
    행정구역[row[0]] = row[1][:-2]

읽기시작=False
data={}
for row in 시트:
    if not 읽기시작:
        if row[0].value=="시군구": 읽기시작=True
        continue;
    
    지역 = row[0].value
    평단가 = float(row[8].value.replace(" ","").replace(",","")) / float(row[5].value)
    if 지역 not in data:
        data[지역] = [평단가]
    else: data[지역].append(평단가)

ch={
'고양덕양구':"고양시 덕양구",
'고양일산동구':"고양시 일산동구",
'고양일산서구':"고양시 일산서구",  
'성남분당구':"성남시 분당구",
'성남중원구':"성남시 중원구",
'성남수정구':"성남시 수정구",
'수원권선구':"수원시 권선구",
'수원영통구':"수원시 영통구",
'수원장안구':"수원시 장안구",
'수원팔달구':"수원시 팔달구",
'안산단원구':"안산시 단원구",
'안산상록구':"안산시 상록구",
'안양동안구':"안양시 동안구",
'안양만안구':"안양시 만안구",
'용인기흥구':"용인시 기흥구",
'용인수지구':"용인시 수지구",
'용인처인구':"용인시 처인구",
'창원마산합포구':"창원시 마산합포구",
'용인처인구':"용인시 처인구",
}
동={
    '북문로2가동': '북문로2가',
    '북문로3가동': '북문로3가',
    '남문로1가동': '남문로1가'
    
}

def get_js_fn(d_id,vlaue):
    global M;
    return """try{document.getElementById("%s").style.fill=pcolor("%s")}catch{}"""%(d_id,str((vlaue-M[0])/(M[1]-M[0])))

M=[9999999999999999,-9999999999999999]
M=[25, 3300]
"""for i in data:
    data[i].sort()
    if len(data[i])%2: 값 = data[i][len(data[i])//2]
    else: 값 = (data[i][len(data[i])//2]+data[i][len(data[i])//2-1])/2
    #값=sum(data[i]) / len(data[i])
    M[0]=min(M[0],값)
    M[1]=max(M[1],값)
print("M",M)
"""


file = open("k - 복사본 - 복사본.txt",'a')
file.write("list['%s']=`"%date)


for i in data:
    ii = i.split()
    """if ii[1] in ch:
        ii[1]=ch[ii[1]]"""
    if "세종특별자치시" in i: 1+1;
        
    
    elif i not in 행정구역:
        ii[1] = ii[1][:2]+'시 '+ii[1][2:]
    
    if ii[-1] in 동:
        ii[-1] = 동[ii[-1]]
    ii=" ".join(ii)
    #if len(data[i])%2: 값 = data[i][len(data[i])//2]
    #else: 값 = (data[i][len(data[i])//2]+data[i][len(data[i])//2-1])/2
    값=sum(data[i]) / len(data[i])
    print(get_js_fn(행정구역[ii], 값))
    file.write(get_js_fn(행정구역[ii], 값)+'\n')
    
file.write('`\n');
file.close()

