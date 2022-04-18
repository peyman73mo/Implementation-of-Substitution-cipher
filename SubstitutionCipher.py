import pandas as pd
import numpy as np
import string
from Decryption import dec
from Encryption import enc
from FastAttack import fast_attack
from GetPlainText import get_plain_text
from KeyGenerator import key_generator
from FindFrequency import find_frequency
from GuessKey import guess_key


# =========================================================================     
def show_key(key):
    for i,j in enumerate(key):
        print(i,chr(i+65),chr(j))
# =========================================================================     
def show_text(text):
    print(''.join(text))
    
# =========================================================================           
def d_score(a,b):
    return np.abs(a - b).sum()
# =========================================================================           
def swap_dimensions(x,i,j):
    x[:,[i,j]] = x[:,[j,i]]
    x[[i,j],:] = x[[j,i],:]
    return x
# =========================================================================
def fast_attack(s,guess,key):  
    score = d_score(s,guess)
    for _ in range(10):
        for i in range(1,26):
            for j in range(0,26-i):
                temp = swap_dimensions(np.copy(guess),j,j+i)
                if d_score(s,temp) < score:
                    guess = temp
                    score = d_score(s,temp)
                    key[j],key[j+i] = key[j+i],key[j]
    return key

# =========================================================================
def r(key,x):
    t = 0
    for i in range(26):
        if x[i] == key[i]:
            t +=1
    return (t/26)*100
# =========================================================================
def create_freq():
    s = "AA 0.003% BA 0.146% CA 0.538% DA 0.151% EA 0.688% FA 0.164% GA 0.148% HA 0.926% IA 0.286% JA 0.026% KA 0.017% LA 0.528% MA 0.565%  NA 0.347% OA 0.057% PA 0.324% QA 0.000% RA 0.686% SA 0.218% TA 0.530% UA 0.136% VA 0.140% WA 0.385% XA 0.030% YA 0.016% ZA 0.025% AB 0.230% BB 0.011% CB 0.001% DB 0.003% EB 0.027% FB 0.000% GB 0.000% HB 0.004% IB 0.099% JB 0.000% KB 0.001% LB 0.007% MB 0.090% NB 0.004% OB 0.097% PB 0.001% QB 0.000% RB 0.027% SB 0.008% TB 0.003% UB 0.089% VB 0.000% WB 0.001% XB 0.000% YB 0.004% ZB 0.000% AC 0.448% BC 0.002% CC 0.083% DC 0.003% EC 0.477% FC 0.001% GC 0.000% HC 0.001% IC 0.699% JC 0.000% KC 0.000% LC 0.012% MC 0.004% NC 0.416% OC 0.166% PC 0.001% QC 0.000% RC 0.121% SC 0.155% TC 0.026% UC 0.188% VC 0.000% WC 0.001% XC 0.026% YC 0.014% ZC 0.000% AD 0.368% BD 0.002% CD 0.002% DD 0.043% ED 1.168% FD 0.000% GD 0.003% HD 0.003% ID 0.296% JD 0.000% KD 0.001% LD 0.253% MD 0.001%  ND 1.352% OD 0.195% PD 0.001% QD 0.000% RD 0.189% SD 0.005% TD 0.001% UD 0.091% VD 0.000% WD 0.004% XD 0.000% YD 0.007% ZD 0.000% AE 0.012% BE 0.576% CE 0.651% DE 0.765% EE 0.378% FE 0.237% GE 0.385% HE 3.075% IE 0.385% JE 0.052% KE 0.214% LE 0.829% ME 0.793% NE 0.692% OE 0.039% PE 0.478% QE 0.000% RE 1.854% SE 0.932% TE 1.205% UE 0.147% VE 0.825% WE 0.361% XE 0.022% YE 0.093% ZE 0.050% AF 0.074% BF 0.000% CF 0.001% DF 0.003% EF 0.163% FF 0.146% GF 0.001% HF 0.002% IF 0.203% JF 0.000% KF 0.002% LF 0.053% MF 0.004% NF 0.067% OF 1.175% PF 0.001% QF 0.000% RF 0.032% SF 0.017% TF 0.006% UF 0.019% VF 0.000% WF 0.002% XF 0.002% YF 0.001% ZF 0.000% AG 0.205% BG 0.000% CG 0.001% DG 0.031% EG 0.120% FG 0.001% GG 0.025% HG 0.000% IG 0.255% JG 0.000% KG 0.003% LG 0.006% MG 0.001% NG 0.953% OG 0.094% PG 0.000% QG 0.000% RG 0.100% SG 0.002% TG 0.002% UG 0.128% VG 0.000% WG 0.000% XG 0.000% YG 0.003% ZG 0.000% AH 0.014% BH 0.001% CH 0.598% DH 0.005% EH 0.026% FH 0.000% GH 0.228% HH 0.001% IH 0.002% JH 0.000% KH 0.003% LH 0.002% MH 0.001%  NH 0.011% OH 0.021% PH 0.094% QH 0.000% RH 0.015% SH 0.315% TH 3.556% UH 0.001% VH 0.000% WH 0.379% XH 0.004% YH 0.001% ZH 0.001% AI 0.316% BI 0.107% CI 0.281% DI 0.493% EI 0.183% FI 0.285% GI 0.152% HI 0.763% II 0.023% JI 0.003% KI 0.098% LI 0.624% MI 0.318% NI 0.339% OI 0.088% PI 0.123% QI 0.000% RI 0.728% SI 0.550% TI 1.343% UI 0.101% VI 0.270% WI 0.374% XI 0.039% YI 0.029% ZI 0.012% AJ 0.012% BJ 0.023% CJ 0.000% DJ 0.005% EJ 0.005% FJ 0.000% GJ 0.000% HJ 0.000% IJ 0.001% JJ 0.000% KJ 0.000% LJ 0.000% MJ 0.000% NJ 0.011% OJ 0.007% PJ 0.000% QJ 0.000% RJ 0.001% SJ 0.000% TJ 0.000% UJ 0.001% VJ 0.000% WJ 0.000% XJ 0.000% YJ 0.000% ZJ 0.000% AK 0.105% BK 0.000% CK 0.118% DK 0.000% EK 0.016% FK 0.000% GK 0.000% HK 0.000% IK 0.043% JK 0.000% KK 0.000% LK 0.020% MK 0.000%  NK 0.052% OK 0.064% PK 0.001% QK 0.000% RK 0.097% SK 0.039% TK 0.000% UK 0.005% VK 0.000% WK 0.001% XK 0.000% YK 0.000% ZK 0.000% AL 1.087% BL 0.233% CL 0.149% DL 0.032% EL 0.530% FL 0.065% GL 0.061% HL 0.013% IL 0.432% JL 0.000% KL 0.011% LL 0.577% ML 0.005% NL 0.064% OL 0.365% PL 0.263% QL 0.000% RL 0.086% SL 0.056% TL 0.098% UL 0.346% VL 0.000% WL 0.015% XL 0.001% YL 0.015% ZL 0.001% AM 0.285% BM 0.003% CM 0.003% DM 0.018% EM 0.374% FM 0.001% GM 0.010% HM 0.013% IM 0.318% JM 0.000% KM 0.002% LM 0.023% MM 0.096% NM 0.028% OM 0.546% PM 0.016% QM 0.000% RM 0.175% SM 0.065% TM 0.026% UM 0.138% VM 0.000% WM 0.001% XM 0.000% YM 0.024% ZM 0.000% AN 1.985% BN 0.002% CN 0.001% DN 0.008% EN 1.454% FN 0.000% GN 0.066% HN 0.026% IN 2.433% JN 0.000% KN 0.051% LN 0.006% MN 0.009% NN 0.073% ON 1.758% PN 0.001% QN 0.000% RN 0.160% SN 0.009% TN 0.010% UN 0.394% VN 0.000% WN 0.079% XN 0.000% YN 0.013% ZN 0.000% AO 0.005% BO 0.195% CO 0.794% DO 0.188% EO 0.073% FO 0.488% GO 0.132% HO 0.485% IO 0.835% JO 0.054% KO 0.006% LO 0.387% MO 0.337% NO 0.465% OO 0.210% PO 0.361% QO 0.000% RO 0.727% SO 0.398% TO 1.041% UO 0.011% VO 0.071% WO 0.222% XO 0.003% YO 0.150% ZO 0.007% AP 0.203% BP 0.001% CP 0.001% DP 0.002% EP 0.172% FP 0.000% GP 0.000% HP 0.001% IP 0.089% JP 0.000% KP 0.001% LP 0.019% MP 0.239% NP 0.006% OP 0.224% PP 0.137% QP 0.000% RP 0.042% SP 0.191% TP 0.004% UP 0.136% VP 0.000% WP 0.001% XP 0.067% YP 0.025% ZP 0.000% AQ 0.002% BQ 0.000% CQ 0.005% DQ 0.001% EQ 0.057% FQ 0.000% GQ 0.000% HQ 0.000% IQ 0.011% JQ 0.000% KQ 0.000% LQ 0.000% MQ 0.000% NQ 0.006% OQ 0.001% PQ 0.000% QQ 0.000% RQ 0.001% SQ 0.007% TQ 0.000% UQ 0.000% VQ 0.000% WQ 0.000% XQ 0.000% YQ 0.000% ZQ 0.000% AR 1.075% BR 0.112% CR 0.149% DR 0.085% ER 2.048% FR 0.213% GR 0.197% HR 0.084% IR 0.315% JR 0.000% KR 0.003% LR 0.010% MR 0.003% NR 0.009% OR 1.277% PR 0.474% QR 0.000% RR 0.121% SR 0.006% TR 0.426% UR 0.543% VR 0.001% WR 0.031% XR 0.000% YR 0.008% ZR 0.000% AS 0.871% BS 0.046% CS 0.023% DS 0.126% ES 1.339% FS 0.006% GS 0.051% HS 0.015% IS 1.128% JS 0.000% KS 0.048% LS 0.142% MS 0.093% NS 0.509% OS 0.290% PS 0.055% QS 0.000% RS 0.397% SS 0.405% TS 0.337% US 0.454% VS 0.001% WS 0.035% XS 0.000% YS 0.097% ZS 0.000% AT 1.487% BT 0.017% CT 0.461% DT 0.003% ET 0.413% FT 0.082% GT 0.015% HT 0.130% IT 1.123% JT 0.000% KT 0.001% LT 0.124% MT 0.001% NT 1.041% OT 0.442% PT 0.106% QT 0.000% RT 0.362% ST 1.053% TT 0.171% UT 0.405% VT 0.000% WT 0.007% XT 0.047% YT 0.017% ZT 0.000% AU 0.119% BU 0.185% CU 0.163% DU 0.148% EU 0.031% FU 0.096% GU 0.086% HU 0.074% IU 0.017% JU 0.059% KU 0.003% LU 0.135% MU 0.115% NU 0.079% OU 0.870% PU 0.105% QU 0.148% RU 0.128% SU 0.311% TU 0.255% UU 0.001% VU 0.002% WU 0.001% XU 0.005% YU 0.001% ZU 0.002% AV 0.205% BV 0.004% CV 0.000% DV 0.019% EV 0.255% FV 0.000% GV 0.000% HV 0.000% IV 0.288% JV 0.000% KV 0.000% LV 0.035% MV 0.000% NV 0.052% OV 0.178% PV 0.000% QV 0.000% RV 0.069% SV 0.001% TV 0.001% UV 0.003% VV 0.000% WV 0.000% XV 0.002% YV 0.000% ZV 0.000% AW 0.060% BW 0.000% CW 0.000% DW 0.008% EW 0.117% FW 0.000% GW 0.001% HW 0.005% IW 0.001% JW 0.000% KW 0.002% LW 0.013% MW 0.001% NW 0.006% OW 0.330% PW 0.001% QW 0.000% RW 0.013% SW 0.024% TW 0.082% UW 0.000% VW 0.000% WW 0.000% XW 0.000% YW 0.003% ZW 0.000% AX 0.019% BX 0.000% CX 0.000% DX 0.000% EX 0.214% FX 0.000% GX 0.000% HX 0.000% IX 0.022% JX 0.000% KX 0.000% LX 0.000% MX 0.000% NX 0.003% OX 0.019% PX 0.000% QX 0.000% RX 0.001% SX 0.000% TX 0.000% UX 0.004% VX 0.000% WX 0.000% XX 0.003% YX 0.000% ZX 0.000% AY 0.217% BY 0.176% CY 0.042% DY 0.050% EY 0.144% FY 0.009% GY 0.026% HY 0.050% IY 0.000% JY 0.000% KY 0.006% LY 0.425% MY 0.062% NY 0.098% OY 0.036% PY 0.012% QY 0.000% RY 0.248% SY 0.057% TY 0.227% UY 0.005% VY 0.005% WY 0.002% XY 0.003% YY 0.000% ZY 0.002% AZ 0.012% BZ 0.000% CZ 0.001% DZ 0.000% EZ 0.005% FZ 0.000% GZ 0.000% HZ 0.000% IZ 0.064% JZ 0.000% KZ 0.000% LZ 0.000% MZ 0.000% NZ 0.004% OZ 0.003% PZ 0.000% QZ 0.000% RZ 0.001% SZ 0.000% TZ 0.004% UZ 0.002% VZ 0.000% WZ 0.000% XZ 0.000% YZ 0.002% ZZ 0.003%"
    s = s.replace('%','')
    s = s.split()
    for i,j in enumerate(s):
        if i%2 == 1:
            s[i] = float(s[i])
    for i in s:
        if type(i) == str:
            s.remove(i)
    
    s = [float(i) for i in s]
    s = np.array(s)
    s = s/100
    s = s.reshape(26,26)
    s = s.transpose()
    return s
# =========================================================================
frequency = [ord(i) for i in 'e t a o i n s r h l d c u m f p g w y b v k x j q z'.upper().split()]
alphabet = [ord(i) for i in string.ascii_uppercase]
# =========================================================================

print('insert data')
plain_text = get_plain_text()
cipher_text, key = enc(plain_text,key_generator())
print("cipher text : ",cipher_text)
print(" secret key : ",key)

guessKey = guess_key(alphabet,cipher_text,frequency)
print("Guess key : ",guessKey)
dec_txt = dec(guessKey,cipher_text)

frequency_guess = find_frequency(dec_txt)

s = create_freq()

accuracy = r(key,fast_attack(s,frequency_guess,guessKey))
print("accuracy : ",accuracy)


