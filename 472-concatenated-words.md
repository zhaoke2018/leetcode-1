- [Intro](#intro)
- [DP](#dp)
- [Recursion By John](#recursion-by-john)





## Intro


range0开始没通过的那个，应该是有空字符串的原因！  



- https://leetcode.com/problems/concatenated-words/
  - Given a list of words (without duplicates), returns all concatenated words in the given list of words.
  - 输入string dict,返回dict中所有拼接而成的字符串.["big","bi","g"],那么就返回["big"].
  - comprise 包含.
  - 好像,把所有子集和拼不出的字符串去掉就行了.

## DP



- 给定一个字符串数组,返回数组中能够自组合的长字符串 https://leetcode.com/problems/concatenated-words/
  - 不管使用何种验证逻辑, 本题的关键关于 “拆解单词,并验证子集是否在words中”
- DP / DFS / Trie
  - 本题使用 DFS 容易理解一些, DP的思想并不是很明显.



- 知识点
1. set 可以加快查找速度. but why?
  - hashset 可以直接定位, 而不用遍历!
2. 从 0  开始 range 会在某些情况下报错, 是因为那些情况中有 空字符串, 直接导致所有情况都通过. **所以必须从1开始range**
3. 为啥这算是 DFS? 对于每一个 word, 将其验证直到通过. 而不是每个 word 都先遍历前 n 个.
  - 其实说是普通遍历也不为过.

```py
# DFS
def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    wordset = set(words) # 不使用 set 将会超时
    
    def dfs(word):
        for i in range(1, len(word)): # 一分两半, 进行递归
            prefix = word[:i]
            suffix = word[i:]
            if prefix in wordset and suffix in wordset:
                return True
            if prefix in wordset and dfs(suffix): # i 从小到大遍历, 因此不用 dfs(prefix) 了
                return True
        return False
    
    res = []
    for word in words:
        if dfs(word):
            res.append(word)
    return res
```

```py
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        
        memo = {}
        def isConcatenatedWord(w): # 对于每个单词
            if w in memo: return memo[w] # 记忆化可以省去以下的计算
            
            for i in range(1, len(w)): # 拆解单词, 并验证
                if w[:i] not in s: continue
                
                r = w[i:]
                if r in s or isConcatenatedWord(r): # 如果 word局部r 在set中 or word局部r所有子集 都在set中,就缓存
                    memo[w] = True
                    return True
                
            memo[w] = False
            return False
        
        return filter(isConcatenatedWord, words)
```





## Recursion By John


```py
from typing import *
from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        # ovytgaufpjl
        def dfs(word):
            for i in range(0, len(word)): # 一分两半, 进行递归
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix): # i 从小到大遍历, 因此不用 dfs(prefix) 了
                    return True
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res
        



# output = Solution().findAllConcatenatedWordsInADict(["rfkqyuqfjkx","","vnrtysfrzrmzl","gfve","qfpd","lqdqrrcrwdnxeuo","q","klaitgdphcspij","hbsfyfv","adzpbfudkklrw","aozmixr","ife","feclhbvfuk","yeqfqojwtw","sileeztxwjl","ngbqqmbxqcqp","khhqr","dwfcayssyoqc","omwufbdfxu","zhift","kczvhsybloet","crfhpxprbsshsjxd","ilebxwbcto","yaxzfbjbkrxi","imqpzwmshlpj","ta","hbuxhwadlpto","eziwkmg","ovqzgdixrpddzp","c","wnqwqecyjyib","jy","mjfqwltvzk","tpvo","phckcyufdqml","lim","lfz","tgygdt","nhcvpf","fbrpzlk","shwywshtdgmb","bkkxcvg","monmwvytby","nuqhmfj","qtg","cwkuzyamnerp","fmwevhwlezo","ye","hbrcewjxvcezi","tiq","tfsrptug","iznorvonzjfea","gama","apwlmbzit","s","hzkosvn","nberblt","kggdgpljfisylt","mf","h","bljvkypcflsaqe","cijcyrgmqirz","iaxakholawoydvch","e","gttxwpuk","jf","xbrtspfttota","sngqvoijxuv","bztvaal","zxbshnrvbykjql","zz","mlvyoshiktodnsjj","qplci","lzqrxl","qxru","ygjtyzleizme","inx","lwhhjwsl","endjvxjyghrveu","phknqtsdtwxcktmw","wsdthzmlmbhjkm","u","pbqurqfxgqlojmws","mowsjvpvhznbsi","hdkbdxqg","ge","pzchrgef","ukmcowoe","nwhpiid","xdnnl","n","yjyssbsoc","cdzcuunkrf","uvouaghhcyvmlk","aajpfpyljt","jpyntsefxi","wjute","y","pbcnmhf","qmmidmvkn","xmywegmtuno","vuzygv","uxtrdsdfzfssmel","odjgdgzfmrazvnd","a","rdkugsbdpawxi","ivd","bbqeonycaegxfj","lrfkraoheucsvpi","eqrswgkaaaohxx","hqjtkqaqh","berbpmglbjipnuj","wogwczlkyrde","aqufowbig","snjniegvdvotu","ocedkt","bbufnxorixibbd","rzuqsyr","qghoy","evcuanuujszitaoa","wsx","glafbwzdd","znrvjqeyqi","npitruijvyllsi","objltu","ryp","nvybsfrxtlfmp","id","zoolzslgd","owijatklvjzscizr","upmsoxftumyxifyu","xucubv","fctkqlroq","zjv","wzi","ppvs","mflvioemycnphfjt","nwedtubynsb","repgcx","gsfomhvpmy","kdohe","tyycsibbeaxn","wjkfvabn","llkmagl","thkglauzgkeuly","paeurdvexqlw","akdt","ihmfrj","janxk","rqdll","cyhbsuxnlftmjc","yybwsjmajbwtuhkk","ovytgaufpjl","iwbnzhybsx","mumbh","jqmdabmyu","br","lwstjkoxbczkj","vhsgzvwiixxaob","fso","qnebmfl","ooetjiz","lq","msxphqdgz","mqhoggvrvjqrp","xbhkkfg","zxjegsyovdrmw","jav","mshoj","ax","biztkfomz","hujdmcyxdqteqja","gqgsomonv","reqqzzpw","lihdnvud","lznfhbaokxvce","fhxbldylqqewdnj","rlbskqgfvn","lfvobeyolyy","v","iwh","fpbuiujlolnjl","gvwxljbo","ypaotdzjxxrsc","mwrvel","umzpnoiei","ogwilaswn","yw","egdgye","hsrznlzrf","mwdgxaigmxpy","yaqgault","dtlg","cyvfiykmkllf","zxqyhvizqmamj","lvvgoifltzywueyp","abinmy","ppzaecvmx","qsmzc","iddymnl","uskihek","evxtehxtbthq","jvtfzddlgch","czohpyewf","ufzazyxtqxcu","brxpfymuvfvs","xrrcfuusicc","aqhlswbzievij","rv","udvmara","upityz","fecd","suxteeitxtg","dfuydrtbfypbn","cypqodxr","wikfuxwjht","jrliuaifpp","vkmxys","wvpfyfpkvgthq","rmajxis","jncxgviyu","av","nmhskodmidaj","lkfrimprrhen","uip","hstyopbvuiqc","p","vwduwmjpblqo","fnxwgqtvwztje","xwnbcuggl","iehimvoymyjasin","spsqiu","flhyfac","mqrbq","pstsxhplrrmbeddv","hnegtuxx","alsyxezjwtlwmxv","jtxytykkcku","bhhlovgcx","xhhivxnutkx","had","aysulvk","m","anhsyxli","jdkgfc","potn","lcibpxkidmwexp","gwoxjicdkv","tltienw","ngiutnuqbzi","o","tzlyb","vumnwehj","os","np","lhv","uzvgyeette","ipfvr","lpprjjalchhhcmh","k","pciulccqssaqgd","tp","dmzdzveslyjad","wtsbhgkd","eouxbldsxzm","vhtonlampljgzyve","xhnlcrldtfthul","xhflc","upgei","rlaks","yfqvnvtnqspyjbxr","phouoyhvls","voibuvbhhjcdflvl","rgorfbjrofokggaf","dqhqats","zchpicyuawpovm","yzwfor","koat","pybf","fhdzsbiyjld","gznfnqydisn","xz","po","tcjup","wygsnxk","kqlima","fgxnuohrnhg","publurhztntgmimc","zuufzphd","iucrmmmjqtcey","wnnbq","rghzyz","ukjqsjbmp","mdtrgv","vyeikgjdnml","kxwldnmi","apzuhsbssaxj","tkbkoljyodlipof","nkq","ktwtj","vgmkgjwle","t","agylw","vomtuy","jbtvitkqn","vtdxwrclpspcn","rdrls","yxfeoh","upj","myctacn","fdnor","ahqghzhoqprgkym","phiuvdv","jp","fdgpouzjwbq","hqoyefmugjvewhxu","qfzwuwe","fnsbijkeepyxry","oja","qthkcij","zpmqfbmnr","ybaibmzonzqlnmd","svo","gjftyfehik","jfrfgznuaytvaegm","aljhrx","odjq","ogwaxrssjxgvnka","zaqswwofedxj","lugpktauixp","dc","odknlbvxrs","jeobu","vqythyvzxbcgrlbg","hwc","erpbaxq","ujxcxck","rrklkb","wlrwyuy","zmg","yyhga","xwdbycdu","htedgvsrhchox","wr","suhesetv","jonqwhkwezjvjgg","sqqyrxtjkcalswq","hvyimhe","pjzdkmoue","zbphmgoxq","lbdlcumdgixjbcq","ztzdjqmadthtdmv","qcagsyqggcf","if","jpjxcjyi","chyicqibxdgkqtg","iwpdklhum","wljmg","micmun","npdbamofynykqv","ijsnfkpfy","lmq","oyjmeqvhcrvgm","mqopusqktdthpvz","fz","r","qbsqtipq","nxtsnason","xbpipyhh","topsuqomfjrd","islif","gbndakaq","bwnkxnwpzeoohlx","hrtbfnq","fguvomeepxoffg","mat","dzfpfnwbfuj","onlvy","cwcchvsasdylb","rxfcztzqopdi","ybrhodjn","oqkijy","ncvrjo","dphbfaal","xgtpdtkz","sebevsopjvciwljf","rcumyacqdapwczen","mabkapuoud","pbozezeygljfftvy","bvazmzbndl","vl","qiaixdtbhqvlzd","ffjfb","svthrfmkoxbho","cvet","ucgqyvopafyttrh","lbgihet","naiqyufxffdw","vruh","uz","ukffmudygjavem","dccamymhp","wofwgjkykm","fbuujzxhln","kmm","lzandlltowjpwsal","fapfvrmezbsjxs","wiw","sc","soqlh","hzaplclkwl","gcdqbcdwbwa","gadgt","pgowefka","juffuguqepwnfh","nbuinl","cpdxf","sox","fq","lfnrhgsxkhx","xrcorfygjxpi","mwtqjwbhgh","loc","fkglorkkvx","nlzdhucvayrz","azefobxutitrf","rlrstkcbtikklmh","ggk","sbphcejuylh","nraoenhd","zngyodiqlchxyycx","rrbhfwohfv","krzolrglgn","cpjesdzy","yoifoyg","hqqevqjugi","ahmv","xgaujnyclcjq","evhyfnlohavrj","byyvhgh","hyw","kedhvwy","ysljsqminajfipds","rglnpxfqwu","cibpynkxg","su","mbntqrlwyampdg","nig","ldhlhqdyjcfhu","jfymrbafmyoc","tyjmnhlfnrtz","dlazixtlxyvm","fbiguhsfuqo","rhymsno","rkbdlchs","ocbbwwd","astaiamnepwkya","mplirup","edkxjq","g","exlwulswtvot","tlnc","vnrrzerz","ygeraoozbtt","yyifkin","eo","ua","qgztvqdolf","rlzddjzcshvd","khxkdxflwxme","kk","zylbhoaac","cw","iizic","gcdxstpz","kjwdqeg","earjrncmmkdel","kbesuhquepj","nrzbllldgdmyrpgl","hllwnqozf","djpchowhwevbqvjj","zsmhylnjpktb","pxnktxkm","fxwiaqqb","qjwufmwresfsfaok","aa","d","iobioqm","svjgzk","khbzp","euexyudhrioi","yqsj","ngrwqpoh","rwuvd","eruffmlg","bxzovyew","faz","pmvfvyguqdi","jlxnoixsy","hyfrdngjf","ly","eibcapetpmeaid","tpnwwiif","pfgsp","kvhhwkzvtvlhhb","pjxurgqbtldims","rncplkeweoirje","akyprzzphew","wyvfpjyglzrmhfqp","ubheeqt","rmbxlcmn","taqakgim","apsbu","khwnykughmwrlk","vtdlzwpbhcsbvjno","tffmjggrmyil","schgwrrzt","mvndmua","nlwpw","glvbtkegzjs","piwllpgnlpcnezqs","xkelind","urtxsezrwz","zechoc","vfaimxrqnyiq","ybugjsblhzfravzn","btgcpqwovwp","zgxgodlhmix","sfzdknoxzassc","wgzvqkxuqrsqxs","dwneyqisozq","fg","vhfsf","uspujvqhydw","eadosqafyxbmzgr","tyff","blolplosqnfcwx","uwkl","puenodlvotb","iizudxqjvfnky","cjcywjkfvukvveq","jrxd","igwb","dftdyelydzyummmt","uvfmaicednym","oai","higfkfavgeemcgo","naefganqo","iqebfibigljbc","ulicojzjfrc","igxprunj","cymbrl","fqmwciqtynca","zjyagi","mzuejrttefhdwqc","zyiurxvf","wrjxffzbjexsh","wrxw","mhrbdxjwi","htknfa","wfrvxqdkhbwwef","vqsghhhutdget","cwupzrts","hbjnb","wpccoa","nx","howbzhaoscgyk","bilt","wqqatye","zceuuwg","jxzon","kkfj","bwsezd","ifdegsyjtswselk","xweimxlnzoh","tqthlftjblnpht","ww","ss","b","jmruuqscwjp","nxbk","wd","cqkrtbxgzg","xhppcjnq","cfq","tkkolzcfi","wblxki","ijeglxsvc","kcqjjwcwuhvzydm","gubqavlqffhrzz","hiwxrgftittd","caybc","ncsyjlzlxyyklc","poxcgnexmaajzuha","dhaccuualacyl","mtkewbprs","oncggqvr","sqqoffmwkplsgbrp","ioajuppvqluhbdet","dzwwzaelmo","afumtqugec","wglucmugwqi","zveswrjevfz","nxlbkak","pzcejvxzeoybb","fd","vewj","ivws","zjhudtpqsfc","zcmukotirrxx","zksmx","umofzhhowyftz","zbotrokaxaryxlk","ueolqk","dxmzhoq","zvu","cjl","esfmqgvxwfy","npbep","vbgjtbv","poeugoqynkbfiv","fewjjscjrei","yqssxzsydgllfzmo","urxkwcypctjkabi","wqtldwhjouas","tovdtkr","onzgeyddkqwuhnim","ffxviyvsktqrfa","qujhd","pvcz","hiyjlkxmeplnrvxg","hdykehkefp","vepcxhozpjxtreyn","liguhuxudbnh","f","ordxzm","klgohcmmbukz","yrmooliaobbnlap","dutnbetocxylcey","ywdsjegd","cr","blbxhjsgcuoxmqft","ngzdc","srfyjjumcbxole","dazwzwtdjoyuqeqj","xazjarqgfm","fxyfqbeoktcc","qrsjchxp","iltaqzawhgu","sgenjcfxr","yfikp","dvwhbyumthkiktb","walsx","jyajrkcvysicisab","brdeumb","tviihjwxdcz","dnrrgmem","ydgxlrjzucxyid","cdvdpvjlagwmg","ngnpxjkxims","gvyhnchlimsxc","w","jtizpezjl","qe","rjzv","vhnqvi","qm","iedzqswrsnfmnn","lt","utqfcqyrrwm","wtelvsqrru","fjwrhjcrtbcytn","qmqxceuohpiffaq","rmoybqjjgdyo","pmxttqftypfexlv","tg","qa","iqbqjlnpbf","kgaynkddbzllecd","tccvslp","curkxfoimnw","fvnyqkzlheruxr","iiygnzfov","coqs","oa","eiu","vzemmxtklis","lxu","nrwsjaxzwmh","tdayz","oxbbemejgosgcynf","ykbcn","hesvnctfvdsp","ku","rjhykpadahbhj","at","sxlngbtxmqr","wqrom","qzyabzrco","rbbyklndcqdj","cnsmgmwmpbgjq","krvnaf","qrwfajnfahyqocdb","fnlaozmff","vmoymbmytjvfcgt","cijyy","jdgwjbztl","swmalgbgpaplqgz","hfl","typttkrpfvx","tkzpzrscwbx","bwfqqvjcukjbsg","nxqmxr","x","eyavnz","il","dhthp","eyelg","npsoqsw","reogbmveofvusdsx","jvdrjkhxkq","qzjbrpljwuzpl","czqeevvbvcwh","vzuszqvhlmapty","yu","yldwwgezlqur","vorxwgdtgjilgydq","pknt","bgihl","ckorgrm","ixylxjmlfv","bpoaboylced","zea","igfagitkrext","ipvqq","dmoerc","oqxbypihdv","dtjrrkxro","rexuhucxpi","bvmuyarjwqpcoywa","qwdmfpwvamisns","bhopoqdsref","tmnm","cre","ktrniqwoofoeenbz","vlrfcsftapyujmw","updqikocrdyex","bcxw","eaum","oklsqebuzeziisw","fzgyhvnwjcns","dybjywyaodsyw","lmu","eocfru","ztlbggsuzctoc","ilfzpszgrgj","imqypqo","fump","sjvmsbrcfwretbie","oxpmplpcg","wmqigymr","qevdyd","gmuyytguexnyc","hwialkbjgzc","lmg","gijjy","lplrsxznfkoklxlv","xrbasbznvxas","twn","bhqultkyfq","saeq","xbuw","zd","kng","uoay","kfykd","armuwp","gtghfxf","gpucqwbihemixqmy","jedyedimaa","pbdrx","toxmxzimgfao","zlteob","adoshnx","ufgmypupei","rqyex","ljhqsaneicvaerqx","ng","sid","zagpiuiia","re","oadojxmvgqgdodw","jszyeruwnupqgmy","jxigaskpj","zpsbhgokwtfcisj","vep","ebwrcpafxzhb","gjykhz","mfomgxjphcscuxj","iwbdvusywqlsc","opvrnx","mkgiwfvqfkotpdz","inpobubzbvstk","vubuucilxyh","bci","dibmye","rlcnvnuuqfvhw","oorbyyiigppuft","swpksfdxicemjbf","goabwrqdoudf","yjutkeqakoarru","wuznnlyd","vfelxvtggkkk","mxlwbkbklbwfsvr","advraqovan","smkln","jxxvzdjlpyurxpj","ssebtpznwoytjefo","dynaiukctgrzjx","irzosjuncvh","hcnhhrajahitn","vwtifcoqepqyzwya","kddxywvgqxo","syxngevs","batvzmziq","mjewiyo","pzsupxoflq","byzhtvvpj","cqnlvlzr","akvmxzbaei","mwo","vg","ekfkuajjogbxhjii","isdbplotyak","jvkmxhtmyznha","lqjnqzrwrmgt","mbbhfli","bpeohsufree","ajrcsfogh","lucidbnlysamvy","tutjdfnvhahxy","urbrmmadea","hghv","acnjx","athltizloasimp","gu","rjfozvgmdakdhao","iephs","uztnpqhdl","rfuyp","crcszmgplszwfn","zihegt","xbspa","cjbmsamjyqqrasz","ghzlgnfoas","ljxl","cnumquohlcgt","jm","mfccj","hfedli","vtpieworwhyiucs","tdtuquartspkotm","pnkeluekvelj","ugrloq","zljmwt","fkyvqguqq","tpjidglpxqfxv","l","tvvimvroz","yy","opwyfovdz","pwlumocnyuoume","vjqpzkcfc","ihicd","dtttiixlhpikbv","goblttgvmndkqgg","gwsibcqahmyyeagk","prtvoju","lcblwidhjpu","kbu","pey","gkzrpc","bqajopjjlfthe","bc","lqs","zkndgojnjnxqsoqi","zyesldujjlp","drswybwlfyzph","xzluwbtmoxokk","bedrqfui","opajzeahv","lehdfnr","mnlpimduzgmwszc","velbhj","miwdn","wruqc","kscfodjxg","wcbm"])
# expected = ["gfve","qfpd","lqdqrrcrwdnxeuo","hbsfyfv","ife","feclhbvfuk","ngbqqmbxqcqp","khhqr","dwfcayssyoqc","omwufbdfxu","ilebxwbcto","ta","hbuxhwadlpto","tpvo","phckcyufdqml","lfz","tgygdt","nhcvpf","shwywshtdgmb","bkkxcvg","monmwvytby","qtg","cwkuzyamnerp","ye","tfsrptug","gama","nberblt","mf","gttxwpuk","xbrtspfttota","qxru","phknqtsdtwxcktmw","pbqurqfxgqlojmws","hdkbdxqg","ge","ukmcowoe","xdnnl","yjyssbsoc","uvouaghhcyvmlk","pbcnmhf","qmmidmvkn","xmywegmtuno","vuzygv","uxtrdsdfzfssmel","eqrswgkaaaohxx","ocedkt","qghoy","wsx","glafbwzdd","ryp","nvybsfrxtlfmp","upmsoxftumyxifyu","xucubv","fctkqlroq","ppvs","nwedtubynsb","repgcx","gsfomhvpmy","kdohe","llkmagl","thkglauzgkeuly","paeurdvexqlw","akdt","rqdll","mumbh","br","fso","qnebmfl","lq","xbhkkfg","ax","gqgsomonv","reqqzzpw","rlbskqgfvn","lfvobeyolyy","mwrvel","ogwilaswn","yw","egdgye","yaqgault","dtlg","iddymnl","evxtehxtbthq","brxpfymuvfvs","rv","udvmara","fecd","dfuydrtbfypbn","cypqodxr","vkmxys","wvpfyfpkvgthq","av","vwduwmjpblqo","xwnbcuggl","flhyfac","mqrbq","pstsxhplrrmbeddv","hnegtuxx","bhhlovgcx","had","aysulvk","potn","os","np","lhv","uzvgyeette","tp","wtsbhgkd","eouxbldsxzm","xhnlcrldtfthul","xhflc","rlaks","phouoyhvls","dqhqats","koat","pybf","po","wygsnxk","kqlima","fgxnuohrnhg","wnnbq","mdtrgv","nkq","agylw","vomtuy","vtdxwrclpspcn","rdrls","yxfeoh","myctacn","fdnor","qfzwuwe","svo","dc","odknlbvxrs","hwc","erpbaxq","rrklkb","wlrwyuy","yyhga","xwdbycdu","htedgvsrhchox","wr","suhesetv","qcagsyqggcf","wljmg","npdbamofynykqv","lmq","oyjmeqvhcrvgm","nxtsnason","gbndakaq","hrtbfnq","fguvomeepxoffg","mat","onlvy","cwcchvsasdylb","dphbfaal","mabkapuoud","vl","ffjfb","svthrfmkoxbho","cvet","ucgqyvopafyttrh","vruh","ukffmudygjavem","dccamymhp","kmm","sc","soqlh","gcdqbcdwbwa","gadgt","pgowefka","cpdxf","sox","fq","lfnrhgsxkhx","loc","fkglorkkvx","ggk","nraoenhd","rrbhfwohfv","yoifoyg","ahmv","byyvhgh","hyw","kedhvwy","rglnpxfqwu","su","mbntqrlwyampdg","jfymrbafmyoc","rhymsno","rkbdlchs","ocbbwwd","exlwulswtvot","tlnc","eo","ua","khxkdxflwxme","kk","cw","pxnktxkm","aa","ngrwqpoh","rwuvd","eruffmlg","bxzovyew","hyfrdngjf","ly","pfgsp","akyprzzphew","ubheeqt","rmbxlcmn","apsbu","khwnykughmwrlk","mvndmua","nlwpw","btgcpqwovwp","sfzdknoxzassc","fg","vhfsf","tyff","blolplosqnfcwx","uwkl","puenodlvotb","naefganqo","cymbrl","wrxw","htknfa","wfrvxqdkhbwwef","vqsghhhutdget","wpccoa","nx","bilt","wqqatye","bwsezd","ww","ss","jmruuqscwjp","nxbk","wd","cfq","gubqavlqffhrzz","caybc","dhaccuualacyl","mtkewbprs","oncggqvr","sqqoffmwkplsgbrp","afumtqugec","nxlbkak","fd","ueolqk","esfmqgvxwfy","npbep","yqssxzsydgllfzmo","tovdtkr","hdykehkefp","ordxzm","dutnbetocxylcey","cr","ngzdc","fxyfqbeoktcc","walsx","brdeumb","dnrrgmem","gvyhnchlimsxc","qe","qm","lt","utqfcqyrrwm","wtelvsqrru","qmqxceuohpiffaq","pmxttqftypfexlv","tg","qa","tccvslp","coqs","oa","lxu","ykbcn","hesvnctfvdsp","ku","at","sxlngbtxmqr","wqrom","krvnaf","hfl","typttkrpfvx","nxqmxr","dhthp","eyelg","npsoqsw","reogbmveofvusdsx","yu","pknt","ckorgrm","bpoaboylced","dmoerc","bhopoqdsref","tmnm","cre","vlrfcsftapyujmw","bcxw","eaum","dybjywyaodsyw","lmu","eocfru","fump","oxpmplpcg","qevdyd","gmuyytguexnyc","lmg","lplrsxznfkoklxlv","twn","bhqultkyfq","saeq","xbuw","kng","uoay","kfykd","armuwp","gtghfxf","pbdrx","adoshnx","rqyex","ng","sid","re","vep","ebwrcpafxzhb","opvrnx","vubuucilxyh","rlcnvnuuqfvhw","goabwrqdoudf","wuznnlyd","vfelxvtggkkk","mxlwbkbklbwfsvr","advraqovan","smkln","kddxywvgqxo","syxngevs","mwo","vg","bpeohsufree","lucidbnlysamvy","urbrmmadea","hghv","gu","uztnpqhdl","rfuyp","xbspa","cnumquohlcgt","tdtuquartspkotm","ugrloq","fkyvqguqq","yy","pwlumocnyuoume","goblttgvmndkqgg","lcblwidhjpu","kbu","pey","bc","lqs","xzluwbtmoxokk","lehdfnr","wruqc","wcbm"]

# # output = [1, 2, 3]
# # expected = [3, 4, 5]
# # print('output', output)
# # print('expected_more', expected_more)

# # reduceAlldifference = list(set(output)^set(expected))
# output_more = set(output).difference(expected)
# # {'ovytgaufpjl', 'oadojxmvgqgdodw', 'ydgxlrjzucxyid', 'w', 'batvzmziq', 'hiyjlkxmeplnrvxg', 'spsqiu', 'hbrcewjxvcezi', 'mplirup', 'qrwfajnfahyqocdb', 'yybwsjmajbwtuhkk', 'kczvhsybloet', 'fbiguhsfuqo', 'rjfozvgmdakdhao', 'vumnwehj', 'mkgiwfvqfkotpdz', 'faz', 'uspujvqhydw', 'ljxl', 'dibmye', 'zksmx', 'poeugoqynkbfiv', 'gwsibcqahmyyeagk', 'janxk', 'wogwczlkyrde', 'rghzyz', 'pjzdkmoue', 'toxmxzimgfao', 'ngnpxjkxims', 'rgorfbjrofokggaf', 'ncvrjo', 'ypaotdzjxxrsc', 'qiaixdtbhqvlzd', 'sgenjcfxr', 'jvdrjkhxkq', 'vwtifcoqepqyzwya', 'fdgpouzjwbq', 'urxkwcypctjkabi', 'zkndgojnjnxqsoqi', 'wblxki', 'fhxbldylqqewdnj', 'ufzazyxtqxcu', 'astaiamnepwkya', 'lznfhbaokxvce', 'athltizloasimp', 'bljvkypcflsaqe', 'ldhlhqdyjcfhu', 'ipfvr', 'nmhskodmidaj', 'ifdegsyjtswselk', 'gkzrpc', 'nbuinl', 'zvu', 'vepcxhozpjxtreyn', 'yyifkin', 'poxcgnexmaajzuha', 'uz', 'hzkosvn', 'vgmkgjwle', 'gcdxstpz', 'igwb', 'lwhhjwsl', 'voibuvbhhjcdflvl', 'vtpieworwhyiucs', 'jrliuaifpp', 'nwhpiid', 'rlrstkcbtikklmh', 'ygeraoozbtt', 'iltaqzawhgu', 'ybaibmzonzqlnmd', 'nrwsjaxzwmh', 'klgohcmmbukz', 'jedyedimaa', 'zyesldujjlp', 'mnlpimduzgmwszc', 'khbzp', 'hqqevqjugi', 'dvwhbyumthkiktb', 'o', 'odjq', 'xazjarqgfm', 'rmajxis', 'ioajuppvqluhbdet', 'xweimxlnzoh', 'qujhd', 'f', 'jdkgfc', 'gjftyfehik', 'ffxviyvsktqrfa', 'mjewiyo', 'lbgihet', 'glvbtkegzjs', 'kcqjjwcwuhvzydm', 'eyavnz', 'a', 'nrzbllldgdmyrpgl', 'berbpmglbjipnuj', 'jtizpezjl', 'eiu', 'vzuszqvhlmapty', 'mfomgxjphcscuxj', 'zgxgodlhmix', 'ktrniqwoofoeenbz', 'dtttiixlhpikbv', 'bgihl', 'alsyxezjwtlwmxv', 'apzuhsbssaxj', 'lwstjkoxbczkj', 'zylbhoaac', 'ijeglxsvc', 'acnjx', 'yzwfor', 'evhyfnlohavrj', 'hzaplclkwl', 'oxbbemejgosgcynf', 'tvvimvroz', 'iephs', 'juffuguqepwnfh', 'dftdyelydzyummmt', 'dzfpfnwbfuj', 'micmun', 'jm', 'zjhudtpqsfc', 'bbqeonycaegxfj', 'oja', 'ivws', 'sqqyrxtjkcalswq', 'howbzhaoscgyk', 'bci', 'zcmukotirrxx', 'owijatklvjzscizr', 'upityz', 'fxwiaqqb', 'tffmjggrmyil', 'hvyimhe', 'jncxgviyu', 'vzemmxtklis', 'higfkfavgeemcgo', 'kkfj', 'updqikocrdyex', 'zxbshnrvbykjql', 'jpjxcjyi', 'ulicojzjfrc', 'bqajopjjlfthe', 'ivd', 'qgztvqdolf', 'msxphqdgz', 'schgwrrzt', 'upj', 'yfikp', 'crfhpxprbsshsjxd', 'cyhbsuxnlftmjc', 'rlzddjzcshvd', 'abinmy', 'zea', 'qthkcij', 'd', 'wjute', 'uip', 'ahqghzhoqprgkym', 'adzpbfudkklrw', 'tqthlftjblnpht', 'lqjnqzrwrmgt', 'wnqwqecyjyib', 'k', 'tdayz', 'iiygnzfov', 'iwh', 'drswybwlfyzph', 'sileeztxwjl', 'jvtfzddlgch', 'mqopusqktdthpvz', 'fmwevhwlezo', 'tpjidglpxqfxv', 'ujxcxck', 'wmqigymr', 'ovqzgdixrpddzp', 'kscfodjxg', 'ghzlgnfoas', 'czohpyewf', 'qplci', 'kxwldnmi', 'rxfcztzqopdi', 'vtdlzwpbhcsbvjno', 'cyvfiykmkllf', 'rzuqsyr', 'mshoj', 'hujdmcyxdqteqja', 'ipvqq', 'wrjxffzbjexsh', 'jtxytykkcku', 'ztzdjqmadthtdmv', 'wjkfvabn', 'y', 'xgaujnyclcjq', 'cnsmgmwmpbgjq', 'jonqwhkwezjvjgg', 'fbuujzxhln', 'zceuuwg', 'm', 'jfrfgznuaytvaegm', 'zd', 'mzuejrttefhdwqc', 'jlxnoixsy', 'zchpicyuawpovm', 'fnxwgqtvwztje', 'apwlmbzit', 'lbdlcumdgixjbcq', 'mflvioemycnphfjt', 'fapfvrmezbsjxs', 'uskihek', 'zjyagi', 'pzsupxoflq', 'ywdsjegd', 'xrrcfuusicc', 'zsmhylnjpktb', 'lvvgoifltzywueyp', 'cjl', 'rbbyklndcqdj', 'dxmzhoq', 'jxxvzdjlpyurxpj', 'iucrmmmjqtcey', 'oqxbypihdv', 'jvkmxhtmyznha', 'umofzhhowyftz', 'cqkrtbxgzg', 'ilfzpszgrgj', 'ijsnfkpfy', 'yeqfqojwtw', 'mowsjvpvhznbsi', 'sngqvoijxuv', 'bwfqqvjcukjbsg', 'tkbkoljyodlipof', 'pbozezeygljfftvy', 'wsdthzmlmbhjkm', 'xz', 'vhtonlampljgzyve', 'irzosjuncvh', 'qjwufmwresfsfaok', 'lim', 'eadosqafyxbmzgr', 'zjv', 'jyajrkcvysicisab', 'znrvjqeyqi', 'pmvfvyguqdi', 'ukjqsjbmp', 't', 'ktwtj', 'xrcorfygjxpi', 'id', 'zmg', 'wgzvqkxuqrsqxs', 'rmoybqjjgdyo', 'r', 'iqbqjlnpbf', 'byzhtvvpj', 'lkfrimprrhen', 'naiqyufxffdw', 'xkelind', 'onzgeyddkqwuhnim', 'fhdzsbiyjld', 'v', 'hllwnqozf', 'urtxsezrwz', 'dazwzwtdjoyuqeqj', 'wyvfpjyglzrmhfqp', 'qzjbrpljwuzpl', 'upgei', 'aajpfpyljt', 'zpmqfbmnr', 'ogwaxrssjxgvnka', 'rjzv', 'yqsj', 'oklsqebuzeziisw', 'bvazmzbndl', 'hstyopbvuiqc', 'jy', 'sebevsopjvciwljf', 'gznfnqydisn', 'p', 'iwbnzhybsx', 'il', 'mwdgxaigmxpy', 'oorbyyiigppuft', 'mbbhfli', 'azefobxutitrf', 'yaxzfbjbkrxi', 'zoolzslgd', 'rncplkeweoirje', 'lihdnvud', 'npitruijvyllsi', 'hbjnb', 'wglucmugwqi', 'qsmzc', 'yfqvnvtnqspyjbxr', 'wikfuxwjht', 'u', 'curkxfoimnw', 'tiq', 'oai', 'czqeevvbvcwh', 'pjxurgqbtldims', 'publurhztntgmimc', 'velbhj', 'cjbmsamjyqqrasz', 'fnlaozmff', 'yjutkeqakoarru', 'evcuanuujszitaoa', 'ihmfrj', 'suxteeitxtg', 'zechoc', 'ncsyjlzlxyyklc', 'hcnhhrajahitn', 'uvfmaicednym', 'mhrbdxjwi', 'dmzdzveslyjad', 'inx', 'hqoyefmugjvewhxu', 'iwbdvusywqlsc', 'swmalgbgpaplqgz', 'pvcz', 'zagpiuiia', 'iqebfibigljbc', 'gjykhz', 'qrsjchxp', 'jeobu', 'pzcejvxzeoybb', 'aozmixr', 'fbrpzlk', 'rcumyacqdapwczen', 'zbotrokaxaryxlk', 'tviihjwxdcz', 'nuqhmfj', 'lrfkraoheucsvpi', 'klaitgdphcspij', 'ixylxjmlfv', 'rexuhucxpi', 'biztkfomz', 'jf', 'zbphmgoxq', 'vnrtysfrzrmzl', 'zz', 'pzchrgef', 'zuufzphd', 'jxigaskpj', 'n', 'mlvyoshiktodnsjj', 'cdzcuunkrf', 'iizudxqjvfnky', 'q', 'hiwxrgftittd', 'eibcapetpmeaid', 'wzi', 'umzpnoiei', 'lzandlltowjpwsal', 'pnkeluekvelj', 'bwnkxnwpzeoohlx', 'cijcyrgmqirz', 'g', 'opwyfovdz', 'jqmdabmyu', 'mqhoggvrvjqrp', 'kvhhwkzvtvlhhb', 'c', 'jxzon', 'mwtqjwbhgh', 'liguhuxudbnh', 'zxjegsyovdrmw', 'eziwkmg', 'mjfqwltvzk', 'xbpipyhh', 'vhsgzvwiixxaob', 'tutjdfnvhahxy', 'odjgdgzfmrazvnd', 'b', 'inpobubzbvstk', 'tyjmnhlfnrtz', 'yldwwgezlqur', 'vnrrzerz', 'zljmwt', 'zlteob', 'igfagitkrext', 'hwialkbjgzc', 'dtjrrkxro', 'nlzdhucvayrz', 'ooetjiz', 'iobioqm', 'topsuqomfjrd', 'iedzqswrsnfmnn', 'ajrcsfogh', 'zaqswwofedxj', 'ztlbggsuzctoc', 'jp', 'vhnqvi', 'bedrqfui', 'phiuvdv', 'jav', 'vfaimxrqnyiq', 'aljhrx', 'gvwxljbo', 'cjcywjkfvukvveq', 'fqmwciqtynca', 'svjgzk', 'dynaiukctgrzjx', 'zyiurxvf', 'qzyabzrco', 'mfccj', 'qwdmfpwvamisns', 'bvmuyarjwqpcoywa', 'ygjtyzleizme', 'krzolrglgn', 'nig', 'cpjesdzy', 'imqypqo', 'piwllpgnlpcnezqs', 'tcjup', 'rfkqyuqfjkx', 'endjvxjyghrveu', 'tyycsibbeaxn', 'isdbplotyak', 'kjwdqeg', 'jrxd', 'djpchowhwevbqvjj', 'akvmxzbaei', 'if', 'opajzeahv', 'jdgwjbztl', 'e', 'ybrhodjn', 'zihegt', 'euexyudhrioi', 'taqakgim', 'blbxhjsgcuoxmqft', 'chyicqibxdgkqtg', 'qbsqtipq', 'lugpktauixp', 'ysljsqminajfipds', 'sbphcejuylh', 'vbgjtbv', 'oqkijy', 'tpnwwiif', 'zngyodiqlchxyycx', 'kggdgpljfisylt', 'hfedli', 'cqnlvlzr', 'jbtvitkqn', 'tkzpzrscwbx', 'lcibpxkidmwexp', 'aqhlswbzievij', 'fjwrhjcrtbcytn', 'crcszmgplszwfn', 'jpyntsefxi', 'ufgmypupei', 'iehimvoymyjasin', 'vmoymbmytjvfcgt', 'h', 'dlazixtlxyvm', 'vewj', 'vjqpzkcfc', 'dzwwzaelmo', 'imqpzwmshlpj', 'islif', 'sjvmsbrcfwretbie', 'ihicd', 'swpksfdxicemjbf', 'rdkugsbdpawxi', 'kgaynkddbzllecd', 'fvnyqkzlheruxr', 'srfyjjumcbxole', 'xhhivxnutkx', 'ljhqsaneicvaerqx', 'vyeikgjdnml', 'fz', 'ybugjsblhzfravzn', 'x', 'pciulccqssaqgd', 'prtvoju', 'xhppcjnq', 'anhsyxli', 'snjniegvdvotu', 'iwpdklhum', 'tkkolzcfi', 'jszyeruwnupqgmy', 'zxqyhvizqmamj', 'l', 'hsrznlzrf', 'gijjy', 'objltu', 'zhift', 'fnsbijkeepyxry', 'cijyy', 'kbesuhquepj', 'wofwgjkykm', 'edkxjq', 'dwneyqisozq', 'wqtldwhjouas', 'earjrncmmkdel', 'zpsbhgokwtfcisj', 'ekfkuajjogbxhjii', 'fpbuiujlolnjl', 'xgtpdtkz', 'rjhykpadahbhj', 'ssebtpznwoytjefo', 'zveswrjevfz', 'wiw', 'cdvdpvjlagwmg', 's', 'vqythyvzxbcgrlbg', 'cwupzrts', 'cibpynkxg', 'vorxwgdtgjilgydq', 'bztvaal', 'lpprjjalchhhcmh', 'fzgyhvnwjcns', 'lzqrxl', 'igxprunj', 'aqufowbig', 'iaxakholawoydvch', 'ngiutnuqbzi', 'tltienw', 'xrbasbznvxas', 'fewjjscjrei', 'miwdn', 'iznorvonzjfea', 'bbufnxorixibbd', 'hqjtkqaqh', 'iizic', 'yrmooliaobbnlap', 'ppzaecvmx', 'gpucqwbihemixqmy', 'gwoxjicdkv', 'tzlyb'}


# expected_more = set(expected).difference(output)
# print('output_more', output_more)
# print('expected_more', expected_more)
# print(output == expected)




output = Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
expected = ["catsdogcats","dogcatsdog","ratcatdogcat"]

# output = [1, 2, 3]
# expected = [3, 4, 5]
# print('output', output)
# print('expected_more', expected_more)

# reduceAlldifference = list(set(output)^set(expected))
output_more = set(output).difference(expected)
# {'ovytgaufpjl', 'oadojxmvgqgdodw', 'ydgxlrjzucxyid', 'w', 'batvzmziq', 'hiyjlkxmeplnrvxg', 'spsqiu', 'hbrcewjxvcezi', 'mplirup', 'qrwfajnfahyqocdb', 'yybwsjmajbwtuhkk', 'kczvhsybloet', 'fbiguhsfuqo', 'rjfozvgmdakdhao', 'vumnwehj', 'mkgiwfvqfkotpdz', 'faz', 'uspujvqhydw', 'ljxl', 'dibmye', 'zksmx', 'poeugoqynkbfiv', 'gwsibcqahmyyeagk', 'janxk', 'wogwczlkyrde', 'rghzyz', 'pjzdkmoue', 'toxmxzimgfao', 'ngnpxjkxims', 'rgorfbjrofokggaf', 'ncvrjo', 'ypaotdzjxxrsc', 'qiaixdtbhqvlzd', 'sgenjcfxr', 'jvdrjkhxkq', 'vwtifcoqepqyzwya', 'fdgpouzjwbq', 'urxkwcypctjkabi', 'zkndgojnjnxqsoqi', 'wblxki', 'fhxbldylqqewdnj', 'ufzazyxtqxcu', 'astaiamnepwkya', 'lznfhbaokxvce', 'athltizloasimp', 'bljvkypcflsaqe', 'ldhlhqdyjcfhu', 'ipfvr', 'nmhskodmidaj', 'ifdegsyjtswselk', 'gkzrpc', 'nbuinl', 'zvu', 'vepcxhozpjxtreyn', 'yyifkin', 'poxcgnexmaajzuha', 'uz', 'hzkosvn', 'vgmkgjwle', 'gcdxstpz', 'igwb', 'lwhhjwsl', 'voibuvbhhjcdflvl', 'vtpieworwhyiucs', 'jrliuaifpp', 'nwhpiid', 'rlrstkcbtikklmh', 'ygeraoozbtt', 'iltaqzawhgu', 'ybaibmzonzqlnmd', 'nrwsjaxzwmh', 'klgohcmmbukz', 'jedyedimaa', 'zyesldujjlp', 'mnlpimduzgmwszc', 'khbzp', 'hqqevqjugi', 'dvwhbyumthkiktb', 'o', 'odjq', 'xazjarqgfm', 'rmajxis', 'ioajuppvqluhbdet', 'xweimxlnzoh', 'qujhd', 'f', 'jdkgfc', 'gjftyfehik', 'ffxviyvsktqrfa', 'mjewiyo', 'lbgihet', 'glvbtkegzjs', 'kcqjjwcwuhvzydm', 'eyavnz', 'a', 'nrzbllldgdmyrpgl', 'berbpmglbjipnuj', 'jtizpezjl', 'eiu', 'vzuszqvhlmapty', 'mfomgxjphcscuxj', 'zgxgodlhmix', 'ktrniqwoofoeenbz', 'dtttiixlhpikbv', 'bgihl', 'alsyxezjwtlwmxv', 'apzuhsbssaxj', 'lwstjkoxbczkj', 'zylbhoaac', 'ijeglxsvc', 'acnjx', 'yzwfor', 'evhyfnlohavrj', 'hzaplclkwl', 'oxbbemejgosgcynf', 'tvvimvroz', 'iephs', 'juffuguqepwnfh', 'dftdyelydzyummmt', 'dzfpfnwbfuj', 'micmun', 'jm', 'zjhudtpqsfc', 'bbqeonycaegxfj', 'oja', 'ivws', 'sqqyrxtjkcalswq', 'howbzhaoscgyk', 'bci', 'zcmukotirrxx', 'owijatklvjzscizr', 'upityz', 'fxwiaqqb', 'tffmjggrmyil', 'hvyimhe', 'jncxgviyu', 'vzemmxtklis', 'higfkfavgeemcgo', 'kkfj', 'updqikocrdyex', 'zxbshnrvbykjql', 'jpjxcjyi', 'ulicojzjfrc', 'bqajopjjlfthe', 'ivd', 'qgztvqdolf', 'msxphqdgz', 'schgwrrzt', 'upj', 'yfikp', 'crfhpxprbsshsjxd', 'cyhbsuxnlftmjc', 'rlzddjzcshvd', 'abinmy', 'zea', 'qthkcij', 'd', 'wjute', 'uip', 'ahqghzhoqprgkym', 'adzpbfudkklrw', 'tqthlftjblnpht', 'lqjnqzrwrmgt', 'wnqwqecyjyib', 'k', 'tdayz', 'iiygnzfov', 'iwh', 'drswybwlfyzph', 'sileeztxwjl', 'jvtfzddlgch', 'mqopusqktdthpvz', 'fmwevhwlezo', 'tpjidglpxqfxv', 'ujxcxck', 'wmqigymr', 'ovqzgdixrpddzp', 'kscfodjxg', 'ghzlgnfoas', 'czohpyewf', 'qplci', 'kxwldnmi', 'rxfcztzqopdi', 'vtdlzwpbhcsbvjno', 'cyvfiykmkllf', 'rzuqsyr', 'mshoj', 'hujdmcyxdqteqja', 'ipvqq', 'wrjxffzbjexsh', 'jtxytykkcku', 'ztzdjqmadthtdmv', 'wjkfvabn', 'y', 'xgaujnyclcjq', 'cnsmgmwmpbgjq', 'jonqwhkwezjvjgg', 'fbuujzxhln', 'zceuuwg', 'm', 'jfrfgznuaytvaegm', 'zd', 'mzuejrttefhdwqc', 'jlxnoixsy', 'zchpicyuawpovm', 'fnxwgqtvwztje', 'apwlmbzit', 'lbdlcumdgixjbcq', 'mflvioemycnphfjt', 'fapfvrmezbsjxs', 'uskihek', 'zjyagi', 'pzsupxoflq', 'ywdsjegd', 'xrrcfuusicc', 'zsmhylnjpktb', 'lvvgoifltzywueyp', 'cjl', 'rbbyklndcqdj', 'dxmzhoq', 'jxxvzdjlpyurxpj', 'iucrmmmjqtcey', 'oqxbypihdv', 'jvkmxhtmyznha', 'umofzhhowyftz', 'cqkrtbxgzg', 'ilfzpszgrgj', 'ijsnfkpfy', 'yeqfqojwtw', 'mowsjvpvhznbsi', 'sngqvoijxuv', 'bwfqqvjcukjbsg', 'tkbkoljyodlipof', 'pbozezeygljfftvy', 'wsdthzmlmbhjkm', 'xz', 'vhtonlampljgzyve', 'irzosjuncvh', 'qjwufmwresfsfaok', 'lim', 'eadosqafyxbmzgr', 'zjv', 'jyajrkcvysicisab', 'znrvjqeyqi', 'pmvfvyguqdi', 'ukjqsjbmp', 't', 'ktwtj', 'xrcorfygjxpi', 'id', 'zmg', 'wgzvqkxuqrsqxs', 'rmoybqjjgdyo', 'r', 'iqbqjlnpbf', 'byzhtvvpj', 'lkfrimprrhen', 'naiqyufxffdw', 'xkelind', 'onzgeyddkqwuhnim', 'fhdzsbiyjld', 'v', 'hllwnqozf', 'urtxsezrwz', 'dazwzwtdjoyuqeqj', 'wyvfpjyglzrmhfqp', 'qzjbrpljwuzpl', 'upgei', 'aajpfpyljt', 'zpmqfbmnr', 'ogwaxrssjxgvnka', 'rjzv', 'yqsj', 'oklsqebuzeziisw', 'bvazmzbndl', 'hstyopbvuiqc', 'jy', 'sebevsopjvciwljf', 'gznfnqydisn', 'p', 'iwbnzhybsx', 'il', 'mwdgxaigmxpy', 'oorbyyiigppuft', 'mbbhfli', 'azefobxutitrf', 'yaxzfbjbkrxi', 'zoolzslgd', 'rncplkeweoirje', 'lihdnvud', 'npitruijvyllsi', 'hbjnb', 'wglucmugwqi', 'qsmzc', 'yfqvnvtnqspyjbxr', 'wikfuxwjht', 'u', 'curkxfoimnw', 'tiq', 'oai', 'czqeevvbvcwh', 'pjxurgqbtldims', 'publurhztntgmimc', 'velbhj', 'cjbmsamjyqqrasz', 'fnlaozmff', 'yjutkeqakoarru', 'evcuanuujszitaoa', 'ihmfrj', 'suxteeitxtg', 'zechoc', 'ncsyjlzlxyyklc', 'hcnhhrajahitn', 'uvfmaicednym', 'mhrbdxjwi', 'dmzdzveslyjad', 'inx', 'hqoyefmugjvewhxu', 'iwbdvusywqlsc', 'swmalgbgpaplqgz', 'pvcz', 'zagpiuiia', 'iqebfibigljbc', 'gjykhz', 'qrsjchxp', 'jeobu', 'pzcejvxzeoybb', 'aozmixr', 'fbrpzlk', 'rcumyacqdapwczen', 'zbotrokaxaryxlk', 'tviihjwxdcz', 'nuqhmfj', 'lrfkraoheucsvpi', 'klaitgdphcspij', 'ixylxjmlfv', 'rexuhucxpi', 'biztkfomz', 'jf', 'zbphmgoxq', 'vnrtysfrzrmzl', 'zz', 'pzchrgef', 'zuufzphd', 'jxigaskpj', 'n', 'mlvyoshiktodnsjj', 'cdzcuunkrf', 'iizudxqjvfnky', 'q', 'hiwxrgftittd', 'eibcapetpmeaid', 'wzi', 'umzpnoiei', 'lzandlltowjpwsal', 'pnkeluekvelj', 'bwnkxnwpzeoohlx', 'cijcyrgmqirz', 'g', 'opwyfovdz', 'jqmdabmyu', 'mqhoggvrvjqrp', 'kvhhwkzvtvlhhb', 'c', 'jxzon', 'mwtqjwbhgh', 'liguhuxudbnh', 'zxjegsyovdrmw', 'eziwkmg', 'mjfqwltvzk', 'xbpipyhh', 'vhsgzvwiixxaob', 'tutjdfnvhahxy', 'odjgdgzfmrazvnd', 'b', 'inpobubzbvstk', 'tyjmnhlfnrtz', 'yldwwgezlqur', 'vnrrzerz', 'zljmwt', 'zlteob', 'igfagitkrext', 'hwialkbjgzc', 'dtjrrkxro', 'nlzdhucvayrz', 'ooetjiz', 'iobioqm', 'topsuqomfjrd', 'iedzqswrsnfmnn', 'ajrcsfogh', 'zaqswwofedxj', 'ztlbggsuzctoc', 'jp', 'vhnqvi', 'bedrqfui', 'phiuvdv', 'jav', 'vfaimxrqnyiq', 'aljhrx', 'gvwxljbo', 'cjcywjkfvukvveq', 'fqmwciqtynca', 'svjgzk', 'dynaiukctgrzjx', 'zyiurxvf', 'qzyabzrco', 'mfccj', 'qwdmfpwvamisns', 'bvmuyarjwqpcoywa', 'ygjtyzleizme', 'krzolrglgn', 'nig', 'cpjesdzy', 'imqypqo', 'piwllpgnlpcnezqs', 'tcjup', 'rfkqyuqfjkx', 'endjvxjyghrveu', 'tyycsibbeaxn', 'isdbplotyak', 'kjwdqeg', 'jrxd', 'djpchowhwevbqvjj', 'akvmxzbaei', 'if', 'opajzeahv', 'jdgwjbztl', 'e', 'ybrhodjn', 'zihegt', 'euexyudhrioi', 'taqakgim', 'blbxhjsgcuoxmqft', 'chyicqibxdgkqtg', 'qbsqtipq', 'lugpktauixp', 'ysljsqminajfipds', 'sbphcejuylh', 'vbgjtbv', 'oqkijy', 'tpnwwiif', 'zngyodiqlchxyycx', 'kggdgpljfisylt', 'hfedli', 'cqnlvlzr', 'jbtvitkqn', 'tkzpzrscwbx', 'lcibpxkidmwexp', 'aqhlswbzievij', 'fjwrhjcrtbcytn', 'crcszmgplszwfn', 'jpyntsefxi', 'ufgmypupei', 'iehimvoymyjasin', 'vmoymbmytjvfcgt', 'h', 'dlazixtlxyvm', 'vewj', 'vjqpzkcfc', 'dzwwzaelmo', 'imqpzwmshlpj', 'islif', 'sjvmsbrcfwretbie', 'ihicd', 'swpksfdxicemjbf', 'rdkugsbdpawxi', 'kgaynkddbzllecd', 'fvnyqkzlheruxr', 'srfyjjumcbxole', 'xhhivxnutkx', 'ljhqsaneicvaerqx', 'vyeikgjdnml', 'fz', 'ybugjsblhzfravzn', 'x', 'pciulccqssaqgd', 'prtvoju', 'xhppcjnq', 'anhsyxli', 'snjniegvdvotu', 'iwpdklhum', 'tkkolzcfi', 'jszyeruwnupqgmy', 'zxqyhvizqmamj', 'l', 'hsrznlzrf', 'gijjy', 'objltu', 'zhift', 'fnsbijkeepyxry', 'cijyy', 'kbesuhquepj', 'wofwgjkykm', 'edkxjq', 'dwneyqisozq', 'wqtldwhjouas', 'earjrncmmkdel', 'zpsbhgokwtfcisj', 'ekfkuajjogbxhjii', 'fpbuiujlolnjl', 'xgtpdtkz', 'rjhykpadahbhj', 'ssebtpznwoytjefo', 'zveswrjevfz', 'wiw', 'cdvdpvjlagwmg', 's', 'vqythyvzxbcgrlbg', 'cwupzrts', 'cibpynkxg', 'vorxwgdtgjilgydq', 'bztvaal', 'lpprjjalchhhcmh', 'fzgyhvnwjcns', 'lzqrxl', 'igxprunj', 'aqufowbig', 'iaxakholawoydvch', 'ngiutnuqbzi', 'tltienw', 'xrbasbznvxas', 'fewjjscjrei', 'miwdn', 'iznorvonzjfea', 'bbufnxorixibbd', 'hqjtkqaqh', 'iizic', 'yrmooliaobbnlap', 'ppzaecvmx', 'gpucqwbihemixqmy', 'gwoxjicdkv', 'tzlyb'}


expected_more = set(expected).difference(output)
print('output_more', output_more)
print('expected_more', expected_more)
print(output == expected)




```





