#샘플데이터 - 강원도 3개 만들기
from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient("mongodb://localhost:27017/")
#client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient("mongodb://localhost:27017/")


db = client.dbproject

places = [

        {"name": "하조대", "area":"강원","longitude": 128.73568, "latitude": 38.02112,'image':"https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130916_110%2Fykahn007_1379286942805Q9B2U_JPEG%2F130916-3083-1.jpg","address":"강원도 양양군 현북면"},
        {"name": "남애항","area":"강원", "longitude": 128.78742, "latitude": 37.94521,'image':"https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130121_182%2Fdante001_1358768187698mKCs5_JPEG%2F472727.jpg02.jpg","address":"강원도 양양군 현남면"},
        {"name": "정동진해변", "area":"강원","longitude": 129.03455, "latitude": 37.69084,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130120_217%2Fcykim0712_1358672150992f0IxJ_JPEG%2F_MG_8677.jpg','address':'강원도 강릉시 강동면'},
        {"name": "태백산", "area":"강원","longitude": 128.9151, "latitude": 37.0966,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131113_277%2Fmichindavid_13842879508044t1yW_JPEG%2Fnew__DSC1954.jpg','address':'강원도 태백시 소도동'},
        {"name": "추암해수욕장", "area":"강원","longitude": 129.0934, "latitude": 37.4776,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131016_288%2Fhgs1224_138190715972682uNa_JPEG%2F1C6L5276.JPG','address':'강원도 동해시 북평동 '},


        {"name": "하늘공원", "area":"서울","longitude": 126.8854, "latitude": 37.5674,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2012%2F1%2F14%2F60%2F%2F_dsc8522_lghkor.jpg','address':'서울특별시 마포구 상암동'},
        {"name": "선유도공원", "area":"서울","longitude": 126.8997, "latitude": 37.5441,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130211_11%2Ffaustepis_136058229609078X6L_JPEG%2FIMG_2899.JPG','address':' 서울특별시 영등포구 양화동'},
        {"name": "아차산 정상", "area":"서울","longitude": 127.1034, "latitude": 37.5714,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131230_165%2Fmazinga___1388387763625UkKh6_JPEG%2F_MG_68210.jpg','address':'서울특별시 광진구 광장동'},


        {"name": "민머루해수욕장", "area":"인천","longitude": 126.3334, "latitude": 37.6513,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20120726_188%2Fxorgns0649_1343283037360tPWvR_JPEG%2F5K0C5779-2.jpg','address':'인천광역시 강화군 삼산면'},
        {"name": "동막해수욕장", "area":"인천","longitude": 126.4582, "latitude": 37.5927,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20121212_107%2Fracer1041_1355322187778G7WEG_JPEG%2F(untitled)_37.jpg','address':'인천광역시 강화군 화도면'},
        {"name": "영종도", "area":"인천","longitude": 126.5358, "latitude": 37.5008,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130427_134%2Fkjh23644_1367052819951qMGFq_JPEG%2F%25C5%25A9%25B1%25E2%25BA%25AF%25C8%25AF_%25BC%25B1%25B3%25E0%25B9%25D9%25C0%25A7_%25C0%25CF%25B8%25F4001.jpg','address':'인천광역시 중구 운서동'},
        {"name": "을왕리해수욕장", "area":"인천","longitude": 126.3725, "latitude": 37.4477,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20121210_134%2Fhdong222_1355101640267HVh6K_JPEG%2FIMG_8768.jpg','address':'인천광역시 중구 을왕동'},
        {"name": "마시안해변", "area":"인천","longitude": 126.4165, "latitude": 37.4316,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20121129_95%2Fkakws_1354186565970J4h8M_JPEG%2FIMG_5360-1.jpg','address':'인천광역시 중구 덕교동'},


        {"name": "울릉도", "area":"울릉군","longitude": 130.8571, "latitude": 37.5068,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131104_175%2Fcaruso25_1383548444766o0rHC_JPEG%2F%25C0%25CF%25C3%25E2.JPG','address':'경상북도 울릉군 울릉읍'},
        {"name": "독도", "area":"울릉군","longitude": 131.8648, "latitude": 37.2415,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2008%2F7%2F18%2F255%2F%2Fdokdo1_hz4.jpg%3Ftype%3Dw685','address':'경상북도 울릉군 울릉읍'},


        {"name": "탄도항", "area":"경기","longitude": 126.6449, "latitude": 37.1925,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2008%2F7%2F18%2F255%2F%2Fdokdo1_hz4.jpg%3Ftype%3Dw685','address':'경기도 안산시 단원구'},
        {"name": "궁평리마을", "area":"경기","longitude": 126.6810, "latitude": 37.1152,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130817_96%2Fyeo6407_1376704774182DiIgi_JPEG%2FDSC08212_','address':'경기도 화성시 서신면'},


        {"name": "왜목마을", "area":"충남","longitude": 126.5272, "latitude": 37.0454,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130304_61%2Fbisang319_1362390475206UvOKi_JPEG%2FDSC_8597-%25C5%25A9%25B7%25CE.JPG','address':'충청남도 당진시 석문면'},
        {"name": "간월암", "area":"충남","longitude": 126.4112, "latitude": 36.6037,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20121125_87%2Fdemian67_1353848582477YHmrx_JPEG%2FIMG_2538_resize.jpg%3Ftype%3Da760','address':'충청남도 서산시 부석면'},
        {"name": "꽃지해안공원", "area":"충남","longitude": 126.3350, "latitude": 36.4962,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131107_241%2Fchs9856_1383785867521icr9c_JPEG%2F2.jpg','address':'충청남도 태안군 안면읍'},
        {"name": "마량포해돋이마을", "area":"충남","longitude": 126.5041, "latitude": 36.1460,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2010%2F3%2F29%2F259%2F%2Fdsc_5074_shindolsae.jpg','address':'충청남도 서천군 서면'},


        {"name": "도담삼봉", "area":"충북","longitude": 128.3427, "latitude": 37.0009,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131014_27%2Fsidna_1381737759768csqSa_JPEG%2F1a_DSC3394.jpg','address':'충청북도 단양군 매포읍'},



        {"name": "우포늪", "area":"경남","longitude": 128.4161, "latitude": 35.5488,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130517_59%2F1092spdlqj_1368757984940DFE0Y_JPEG%2FIMG_2131.JPG','address':'경상남도 창녕군 유어면'},
        {"name": "지리산 천왕봉", "area":"경남","longitude": 127.7302, "latitude": 35.3369,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130123_44%2Ffurilla4_1358936449693IPIem_JPEG%2FJH_1176.jpg','address':'경상남도 산청군 시천면'},
        {"name": "보리암", "area":"경남","longitude": 127.9831, "latitude": 34.7521,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20120926_210%2Fkybzss_1348665587953HIPio_JPEG%2Fdata_764_%25BB%25E7%25BA%25BB.jpg','address':'경상남도 남해군 상주면'},


        {"name": "부석사", "area":"경북","longitude": 128.6865, "latitude": 36.9967,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131104_174%2Fsyw2517_1383524019673zTOiV_JPEG%2F131031-064.jpg','address':'경상북도 영주시 부석면'},
        {"name": "망양정", "area":"경북","longitude": 129.4122, "latitude": 36.9675,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto02%2F2008%2F1%2F29%2F151%2F%2Fdpp_11133_mylie79.jpg','address':'경상북도 울진군 근남면'},
        {"name": "삼사해상공원", "area":"경북","longitude": 129.3818, "latitude": 36.3390,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2011%2F8%2F16%2F138%2F%2F1313474291_fdscf1337_rayu_.jpg','address':'경상북도 영덕군 강구면'},
        {"name": "호미곶", "area":"경북","longitude": 129.5546, "latitude": 36.0817,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130828_197%2Fhjkohhh_137765500490071rWg_JPEG%2F_W9A0741.jpg','address':'경상북도 포항시 남구'},
        {"name": "읍천항", "area":"경북","longitude": 129.4736, "latitude": 35.6908,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131212_289%2Fscms1139_1386831647096nzoUg_JPEG%2F%25C0%25BE%25C3%25B5%25C7%25D7%25C0%25CF%25C3%25E2.jpg','address':'경상북도 경주시 양남면'},
        {"name": "혼신지", "area":"경북","longitude": 128.7089, "latitude": 35.6690,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20121213_195%2Fsslee3227_1355387794954RUetl_PNG%2F%25C8%25A5%25BD%25C5%25C1%25F6_066.png','address':'경상북도 청도군 화양읍 '},

        {"name": "변산반도", "area":"전북","longitude": 126.5305, "latitude": 35.6802,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131106_261%2Fjch6478_1383704143854NA9tV_JPEG%2F%25BC%25D6%25BC%25B67-1.jpg','address':'전라북도 부안군 변산면'},
        {"name": "채석강", "area":"전북","longitude": 126.4660, "latitude": 35.6249,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2011%2F9%2F16%2F219%2F%2Fdsc_8832_loveyun29.jpg','address':'전라북도 부안군 변산면'},
        {"name": "곰소항", "area":"전북","longitude": 126.6045, "latitude": 35.5859,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131201_227%2Fkil154_1385903169916o5PDT_JPEG%2FIMG_8323.JPG','address':'전라북도 부안군 진서면'},

        {"name": "도리포", "area":"전남","longitude": 126.3469, "latitude": 35.15737,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2010%2F6%2F4%2F225%2F%2Fdsc_3554_2_3_mars032.jpg','address':'전라남도 무안군 해제면'},
        {"name": "순천만", "area":"전남","longitude": 127.5098, "latitude": 34.8871,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131001_143%2Fhabakuk40_1380576462318IKHfG_JPEG%2FWO0X0035-1.jpg','address':'전라남도 순천시 대대동'},
        {"name": "향일암", "area":"전남","longitude": 127.8039, "latitude": 34.5915,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130604_280%2Fdlquf3512_13703530113535HVFJ_JPEG%2FDSC_1640.JPG','address':'전라남도 여수시 돌산읍'},
        {"name": "남열해수욕장", "area":"전남","longitude": 127.4866, "latitude": 34.5804,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2009%2F1%2F2%2F158%2F%2F2008.12.27.%25BF%25B5%25B3%25B2%25B8%25E9_%25BB%25E7%25C0%25DA%25B9%25D9%25C0%25A7%252C%25BF%25EC%25B5%25B5_%25C0%25CF%25B8%25F4_055_youn66040.jpg','address':'전라남도 고흥군 영남면'},
        {"name": "세방낙조전망대", "area":"전남","longitude": 126.1034, "latitude": 34.4402,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130809_240%2Fydy10042001_13760138355897QUgG_JPEG%2FIMG_6077.JPG','address':'전라남도 진도군 지산면'},
        {"name": "땅끝마을", "area":"전남","longitude": 126.5287, "latitude": 34.2978,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto02%2F2011%2F9%2F7%2F69%2F%2F%25BE%25C6%25BA%25FC110904_0039_bukak123.jpg','address':'전라남도 해남군 송지면'},
        {"name": "완도타워", "area":"전남","longitude": 126.7665, "latitude": 34.3106,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto02%2F2009%2F4%2F26%2F38%2F%2F%25BF%25CF%25B5%25B5-%25B9%25D9%25C5%25C1%25C8%25AD%25B8%25E9_ufodark.jpg','address':'전라남도 완도군 완도읍'},

        {"name": "강양항", "area":"울산","longitude": 129.3467, "latitude": 35.3904,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131127_162%2Fhak1253_1385549064925zBKfp_JPEG%2FIMG_0701-h.jpg','address':'울산광역시 울주군 온산읍'},
        {"name": "간절곶", "area":"울산","longitude": 129.3602, "latitude": 35.3590,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2Fexphoto01%2F2011%2F2%2F22%2F151%2F%2Fdsc_6727_sunkyboy.jpg','address':'울산광역시 울주군 서생면'},
        {"name": "죽성성당", "area":"부산","longitude": 129.2484, "latitude": 35.2409,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131018_114%2Fsides5347_1382081036306mtKFJ_JPEG%2FBL7A1425.jpg','address':'부산광역시 기장군 기장읍'},
        {"name": "다대포", "area":"부산","longitude": 128.9661, "latitude": 35.0468,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20131213_112%2Fjazzstation_1386900718520qIq7s_JPEG%2F%25B4%25D9%25B4%25EB%25C6%25F7_16.jpg','address':'부산광역시 사하구 다대동'},

        {"name": "성산일출봉", "area":"제주","longitude": 126.9425, "latitude": 33.4582,'image':'https://search.pstatic.net/common?quality=75&direct=true&src=http%3A%2F%2Fthumb.photo.naver.net%2F20130905_156%2Fzoomkr_1378338085166gG4X8_JPEG%2FDSC_4032.jpg','address':'제주특별자치도 서귀포시'},
]


db.sample.insert_many(places)
