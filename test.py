from quant.data import wind

table = wind.get_wind_table(
    table_name="AShareBalanceSheet",
    columns=[
        "ann_dt",
        "s_info_windcode",
        "report_period",
        "tot_assets",
        "tot_liab",
    ],
)
print(table)

table = wind.get_wind_table(
    table_name="AShareIncome",
    columns=["ann_dt", "s_info_windcode", "oper_rev", "statement_type"],
)
print(table)
