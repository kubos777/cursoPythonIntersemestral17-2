# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:43:00 2017

@author: alan
"""

import pandas as pd
import numpy as np

s=pd.Series([1,2,4.5,np.nan,5+4j])
print(s)

fechas=pd.date_range('20171030',periods=6,freq="M")
print(fechas[0])


df=pd.DataFrame(np.random.randn(6,4),
                index=fechas,columns=list("ABCD"))
print(df)
print(df["A"][0])

df1=pd.DataFrame({
            "A":1,
            "B":pd.Timestamp('20171030'),
            "C":pd.Series(1,index=list(range(4))),
            "D":np.array([3]*4,dtype='int32')
})

print(df1)

print(df1.head(2))
print(df1.tail(2))

print(df1.columns)

print(df1.values)

print(df1.sort_index(axis=1,ascending=False))

print(df1.sort_index(axis=0,ascending=False))

print(df1.A)
print(df1[0:1])

df1.loc(fechas[0])

df1["D"]=0

print(df1)


