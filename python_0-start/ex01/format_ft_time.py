import datetime as dt

now = dt.datetime.today()
ts = now.timestamp()
print(
    f"Seconds since January 1, 1970: {ts:,.4f} or {ts:.2e} "
    "in scientific notation"
)
now = dt.date.today()
print(now)
