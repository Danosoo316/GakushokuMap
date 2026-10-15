from maps.GakushokuSample import GakushokuSample
from maps.k25061 import k25061

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(), k25061(), ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_summary())
    print()