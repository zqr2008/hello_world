# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
df1=pd.read_excel(r"D:\TAAD_data\all_patients.xlsx",header=1)
df2=pd.read_excel(r"D:\TAAD_data\xinjiang_labresult.xlsx")


# %%
df3=pd.DataFrame({'record_id':df2['record_id'],
                 'abg_ph':df2['酸碱度(pH)-动脉血'],'abg_paco2':df2['二氧化碳分压(PaCO2)-动脉血'],
                 'abg_pao2':df2['氧分压(PaO2)-动脉血'],'abg_sao2':df2['氧饱和度(SaO2)-动脉血'],
                 'crp':df2['C-反应蛋白(CRP)-静脉血'],'alt':df2['丙氨酸氨基转移酶(ALT)-静脉血'],
                 'ldh':df2['乳酸脱氢酶(LDH)-静脉血'],'ast':df2['天门冬氨酸氨基转移酶(AST)-静脉血'],
                 'bun':df2['尿素氮(BUN)-静脉血'],'uric_acid':df2['尿酸(UA)-静脉血'],
                 'ctni':df2['心肌肌钙蛋白I(cTnI)-静脉血'],'ctnt':df2['心肌肌钙蛋白T(cTnT)-静脉血'],
                 'total_cholesterol':df2['总胆固醇(TC)-静脉血'],'tbil':df2['总胆红素(TBIL)-静脉血'],
                 'amylase':df2['淀粉酶(Amy)-静脉血'],'triglyceride':df2['甘油三酯(TG)-静脉血'],
                 'alb':df2['白蛋白(ALB)-静脉血'],'globulin':df2['球蛋白(GLO)-静脉血'],
                 'scr':df2['肌酐(Crea)-静脉血'],'ck':df2['肌酸激酶(CK)-静脉血'],
                 'ckmb_2':df2['肌酸激酶同工酶MB(CK-MB)-静脉血'],'ckmb':df2['肌酸激酶同工酶-静脉血'],
                 'd_dimer_mg_l':df2['D-二聚体(D-Dimer)-静脉血'],'pt':df2['凝血酶原时间(PT)-静脉血'],
                 'inr':df2['凝血酶原国际标准化比值(PT-INR)-静脉血'],'tt':df2['凝血酶时间(TT)-静脉血'],
                 'pta':df2['凝血酶原时间活动度(PTA)-静脉血'],'aptt':df2['活化部分凝血活酶时间(APTT)-静脉血'],
                 'fdp_mg_l':df2['纤维蛋白原降解产物(FDP)-静脉血'],'fib':df2['纤维蛋白原(Fbg)-静脉血'],
                 'neutrophli':df2['中性粒细胞计数(Neut#)-静脉血'],'lymphocyte':df2['淋巴细胞计数(Lymph#)-静脉血'],
                 'wbc':df2['白细胞计数(WBC#)-静脉血'],'plt':df2['血小板计数(PLT#)-静脉血'],
                 'hg':df2['血红蛋白(Hb)-静脉血'],'interleukin_6':df2['白细胞介素-6(IL-6)-静脉血'],
                 'hba1c':df2['糖化血红蛋白A1c(HbA1c)-静脉血'],'esr':df2['红细胞沉降率(ESR)-静脉血'],
                 'homocysteine':df2['同型半胱氨酸(HCY)-静脉血'],'abg_lac':df2['乳酸(Lact)-静脉血'],
                 'pct':df2['降钙素原(PCT)-静脉血'],'hs_crp':df2['超敏C反应蛋白(hs-CRP)-静脉血'],
                 'bnp2':df2['脑钠肽(BNP)-静脉血']
                  })


# %%
df3


# %%
df4=pd.merge(df1,df3,on='record_id',how='outer')
df4.head()


# %%
def function (x):
    global df4
    x_x=x+'_x'
    x_y=x+'_y'
    df4[x] = df4[x_x].fillna(df4[x_y])
    df4 = df4.drop([x_x, x_y], axis=1)
    return (df4)


function ('abg_ph')
function ('abg_paco2')
function ('abg_pao2')
function('abg_sao2')
function('crp')
function('alt')
function('ldh')
function('ast')
function('bun')
function('uric_acid')
function('ctni')
function('ctnt')
function('total_cholesterol')
function('tbil')
function('amylase')
function('triglyceride')
function('alb')
function('globulin')
function('scr')
function('ck')
function('ckmb_2')
function('ckmb')
function('d_dimer_mg_l')
function('pt')
function('inr')
function('tt')
function('pta')
function('aptt')
function('fdp_mg_l')
function('fib')
function('neutrophli')
function('lymphocyte')
function('wbc')
function('plt')
function('hg')
function('interleukin_6')
function('hba1c')
function('esr')
function('homocysteine')
function('abg_lac')
function('pct')
function('hs_crp')
function('bnp2')


# %%
df4.head()


# %%
file = open(r"D:\TAAD_data\all_patients_aftermatching.xlsx")
outputpath=r"D:\TAAD_data\all_patients_aftermatching.xlsx"
df4.to_excel(r"D:\TAAD_data\all_patients_aftermatching.xlsx", sheet_name='Sheet1', na_rep='',
 float_format=None, columns=None, header=True, index=True, 
 index_label=None, startrow=0, startcol=0, engine=None, 
 merge_cells=True, encoding=None, inf_rep='inf', verbose=True, 
 freeze_panes=None)


# %%
酸碱度(pH)-动脉血，abg_ph
二氧化碳分压(PaCO2)-动脉血，abg_paco2
氧分压(PaO2)-动脉血，abg_pao2
氧饱和度(SaO2)-动脉血，abg_sao2
C-反应蛋白(CRP)-静脉血，crp
丙氨酸氨基转移酶(ALT)-静脉血，alt
乳酸脱氢酶(LDH)-静脉血，ldh
天门冬氨酸氨基转移酶(AST)-静脉血，ast
尿素氮(BUN)-静脉血，bun
尿酸(UA)-静脉血，uric_acid
心肌肌钙蛋白I(cTnI)-静脉血，ctni
心肌肌钙蛋白T(cTnT)-静脉血，ctnt
总胆固醇(TC)-静脉血，total_cholesterol
总胆红素(TBIL)-静脉血，tbil
淀粉酶(Amy)-静脉血，amylase
甘油三酯(TG)-静脉血，triglyceride
白蛋白(ALB)-静脉血，alb
球蛋白(GLO)-静脉血，globulin
肌酐(Crea)-静脉血，scr
肌酸激酶(CK)-静脉血，ck
肌酸激酶同工酶MB(CK-MB)-静脉血，ckmb_2
肌酸激酶同工酶-静脉血，ckmb
D-二聚体(D-Dimer)-静脉血，d_dimer_mg_l
凝血酶原时间(PT)-静脉血，pt
凝血酶原国际标准化比值(PT-INR)-静脉血，inr
凝血酶时间(TT)-静脉血，tt
凝血酶原时间活动度(PTA)-静脉血，pta
活化部分凝血活酶时间(APTT)-静脉血，aptt
纤维蛋白原降解产物(FDP)-静脉血，fdp_mg_l
纤维蛋白原(Fbg)-静脉血，fib
中性粒细胞计数(Neut#)-静脉血，neutrophli
淋巴细胞计数(Lymph#)-静脉血，lymphocyte
白细胞计数(WBC#)-静脉血，wbc
血小板计数(PLT#)-静脉血，plt
血红蛋白(Hb)-静脉血，hg
白细胞介素-6(IL-6)-静脉血，interleukin_6
糖化血红蛋白A1c(HbA1c)-静脉血，hba1c
红细胞沉降率(ESR)-静脉血，esr
同型半胱氨酸(HCY)-静脉血，homocysteine
乳酸(Lact)-静脉血，abg_lac
降钙素原(PCT)-静脉血，pct
超敏C反应蛋白(hs-CRP)-静脉血，hs_crp
脑钠肽(BNP)-静脉血，bnp2


