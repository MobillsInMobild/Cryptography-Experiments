import gmpy2

def basicBroadcastAttack(c1,c2,c3,n1,n2,n3):
    n=n1*n2*n3
    m_3=((((c1%n)*(c2%n))%n)*c3%n)%n
    return gmpy2.iroot(m_3, 3)

if __name__ == "__main__":
    e = 3
    N = [67332683067604526744997517492826779689357914237071889334799615320704145458655342972607084542375120497111572450281235412800125398354038403228449307899109231631264906467692879810054609210948730816122903276423105639132560967186266490394273589907495517023687418775233038143849486057886133335546642333997458504129, 81755609535548134938127487539387928831464869009510869333962606212881598663372900726790711068728346145938036285291773229073153826304676638382326867215902513103115633544896621709442589061591035029761494118990364900953582883335342261789166603530822911796675994377443644506042990228215107827438741804057366287581, 84538153658427573873159312306939108742136655463804516075904017295760921846090699930391663152695068570602927893163637661058337912897291115527607543144464899008038928441772211080234546518912305240098722501509866532217883727840856060109329117860966505810195884300851173200008362879576488778128865037242190968831, 129278275579652094110332186976032667085617217505804650942616252163759794815081788914870162070985361128216219914057950862606126570805139776025615653625635083074705720604990989824472163906223935814970351025871115709904324008535536285863442345162166582361477855003552648678919481547375335098101415493048140523271, 71832574253330592068237361254381795913163381665462989723938127466785095183431438875916931234051582591402468573330323939779469637431337653428275632112928933707477615628444296846539307753325526153364699993468757008650404342848349883715213323527495077487318119499800947612777291283437497346196785710255577051493]####################################################################################################
    C = [40993533772170905160154890122081951910717814526315553493697772501482685138820735340020440371107194162049566767249174190721977487208841734455667971225026841969309104238470177209807355795700392161075438489608007105877140190475851774152936930012513903087495048434054875958091110099763212972608058145029379846993, 56896179443510197275311907781950824627667766561721279372021785898305064884777501573496427058360790956542342709785656897822438599401043451050385017687051789021329705642961916628250183122614278940874325018746080602044835065322162826951962645339661578288629222710431033452470957858885227635392131071313515343724, 69649338968556844590637391352900331833769827753318728759796855387723679432906749352190262620046454239171350033137133864919461702721470575396242852466123769907649614893937866240832317965060925411024039854019389797279666354090012044625234667370991238735804036569052054961586088590925020338645924283243201964204, 70841482220390795469019877210699430420728581090686562624803021121908739096190567442929447433987609003965543231135630887291596832013804853347414996863359158143859471339774165007436904542266103599447714324147081030030507884027224934022213112215595366459583736566752034966816258789901232156053265071218303446061, 30234308510834308513153012442338845008033637856938639279240579834681065549178716386112133105136421735815907613044506137736245060780924779037121069801941643732553826220356449972393130157709540582940293812087393700864719894229818718997593165273915189244023687489700554544417952274719205014712837728566430374981]
    print(basicBroadcastAttack(C[0],C[1],C[2],N[0],N[1],N[2]))
    