from ....common.db.sql import VARCHAR, Numeric as NUMBER, DateTime as DATETIME, Column, BaseModel, CLOB, DATE
VARCHAR2 = VARCHAR


class CBondPlateWind(BaseModel):
    """
    4.121 中国Wind债券概念板块

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_info_industrycode: VARCHAR2(20)
        板块代码   
    s_info_industryname: VARCHAR2(100)
        板块名称   
    opdate: DATETIME
        opdate   
    opmode: VARCHAR(1)
        opmode   

    """
    __tablename__ = "CBondPlateWind"
    object_id = Column(VARCHAR2(100), primary_key=True)
    s_info_windcode = Column(VARCHAR2(40))
    s_info_industrycode = Column(VARCHAR2(20))
    s_info_industryname = Column(VARCHAR2(100))
    opdate = Column(DATETIME)
    opmode = Column(VARCHAR(1))
    
